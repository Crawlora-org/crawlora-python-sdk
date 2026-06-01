"""Asyncio client for the Crawlora API.

Two transports:

* When ``httpx`` is installed (``pip install crawlora[async]``) the client uses
  ``httpx.AsyncClient`` for true non-blocking I/O with connection pooling.
* Otherwise it falls back to running the synchronous client in a worker thread
  via :func:`asyncio.to_thread`, keeping the base package dependency-free.

Both paths reuse the synchronous client's request building, validation, retry,
``Retry-After`` handling, error classification, and observability options, so
behavior stays aligned with :class:`CrawloraClient`.

    client = AsyncCrawloraClient(api_key="...")
    result = await client.bing.search(q="coffee")
    async for item in client.paginate_items("ebay-seller-feedback", {"seller": "acme"}):
        ...
    await client.aclose()
"""

from __future__ import annotations

import asyncio
import io
from typing import Any, AsyncIterator, Callable, Mapping

from ._pagination import default_items, default_start, detect_page_param, page_is_empty
from .client import (
    CrawloraClient,
    CrawloraNetworkError,
    ResponseType,
    _api_error_class,
    _auth_headers,
    _build_request,
    _ensure_request_id,
    _header_value,
    _merge_headers,
    _parse_response,
    _validate_response_type,
)
from .operations import GROUPS, OPERATIONS

try:  # optional dependency: pip install crawlora[async]
    import httpx
except ImportError:  # pragma: no cover - exercised only without httpx
    httpx = None


class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None:
        self._client = CrawloraClient(**kwargs)
        self._httpx = httpx.AsyncClient() if httpx is not None else None
        for group_name, operations in GROUPS.items():
            setattr(self, group_name, _AsyncOperationGroup(self, operations))

    @property
    def sync_client(self) -> CrawloraClient:
        """The underlying synchronous client (holds the shared configuration)."""
        return self._client

    @property
    def uses_httpx(self) -> bool:
        return self._httpx is not None

    async def aclose(self) -> None:
        if self._httpx is not None:
            await self._httpx.aclose()

    async def __aenter__(self) -> "AsyncCrawloraClient":
        return self

    async def __aexit__(self, *_exc: Any) -> None:
        await self.aclose()

    async def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = None,
        *,
        response_type: ResponseType = "auto",
        timeout: float | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return await self.request(operation_id, params, response_type=response_type, timeout=timeout, headers=headers)

    async def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = None,
        *,
        response_type: ResponseType = "auto",
        timeout: float | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        if self._httpx is None:
            return await asyncio.to_thread(
                self._client.request, operation_id, params,
                response_type=response_type, timeout=timeout, headers=headers,
            )

        operation = OPERATIONS.get(operation_id)
        if operation is None:
            raise ValueError(f"unknown Crawlora operation: {operation_id}")
        response_type = _validate_response_type(response_type)
        c = self._client
        c._log({"event": "request", "operation": operation_id})

        attempt = 0
        while True:
            try:
                return await self._send(operation, dict(params or {}), response_type, timeout, headers)
            except Exception as exc:  # noqa: BLE001 - re-raised unless retryable
                from .client import CrawloraError

                if not isinstance(exc, CrawloraError) or attempt >= c.retries or not c._is_retryable(exc.status, exc):
                    raise
                attempt += 1
                delay = c._compute_retry_delay(attempt, exc.headers)
                c._log({"event": "retry", "operation": operation_id, "attempt": attempt, "status": exc.status, "delay": delay})
                if c.on_retry is not None:
                    c.on_retry(attempt, exc, delay)
                if delay > 0:
                    await asyncio.sleep(delay)

    async def _send(
        self,
        operation: Mapping[str, Any],
        params: dict[str, Any],
        response_type: ResponseType,
        timeout: float | None,
        headers: Mapping[str, str] | None,
    ) -> Any:
        c = self._client
        url, body, body_headers = _build_request(c.base_url, operation, params)
        request_headers = _merge_headers(
            c.headers,
            _auth_headers(operation.get("security", []), c.api_key, c.jwt_token),
            {"User-Agent": c.user_agent} if c.user_agent else {},
            body_headers,
            headers or {},
        )
        req_id = _ensure_request_id(request_headers) if c.request_id else _header_value(request_headers, "x-request-id") or None
        try:
            response = await self._httpx.request(
                operation["method"], url, content=body, headers=request_headers,
                timeout=timeout if timeout is not None else c.timeout,
            )
        except httpx.TimeoutException as exc:
            raise CrawloraNetworkError("Crawlora request timed out", request_id=req_id, cause=exc) from exc
        except httpx.HTTPError as exc:
            raise CrawloraNetworkError("Crawlora transport error", request_id=req_id, cause=exc) from exc

        raw = bytes(response.content)
        status = response.status_code
        resp_headers = dict(response.headers)
        is_error = status < 200 or status >= 300
        if response_type == "stream" and not is_error:
            return io.BytesIO(raw)
        parse_mode = "auto" if response_type == "stream" else response_type
        import json

        raw_body = raw.decode(errors="replace")
        try:
            parsed = _parse_response(raw, _header_value(resp_headers, "content-type"), parse_mode)
        except json.JSONDecodeError as exc:
            from .client import CrawloraError

            raise CrawloraError("Crawlora JSON parse error", status=status, raw_body=raw_body, headers=resp_headers, request_id=req_id, cause=exc) from exc
        if is_error:
            code = parsed.get("code") if isinstance(parsed, dict) else None
            message = parsed.get("msg") if isinstance(parsed, dict) and parsed.get("msg") else f"HTTP {status}"
            error_class = _api_error_class(status)
            raise error_class(message, status=status, code=code, body=parsed, raw_body=raw_body, headers=resp_headers, request_id=req_id)
        return parsed

    async def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = None,
        *,
        page_param: str | None = None,
        cursor_param: str | None = None,
        next_cursor: Callable[[Any], Any] | None = None,
        start: Any = None,
        step: int = 1,
        max_pages: int | None = None,
        response_type: ResponseType = "auto",
        timeout: float | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Async iterator over pages. Mirrors :meth:`CrawloraClient.paginate`."""
        operation: Any = OPERATIONS.get(operation_id)
        if operation is None:
            raise ValueError(f"unknown Crawlora operation: {operation_id}")
        base_params = dict(params or {})

        if cursor_param or next_cursor:
            if not (cursor_param and next_cursor):
                raise ValueError("cursor pagination requires both cursor_param and next_cursor")
            if cursor_param not in {p["name"] for p in operation.get("queryParams", [])}:
                raise ValueError(f"cursor_param {cursor_param!r} is not a query parameter of operation {operation_id}")
            cursor = start
            fetched = 0
            while max_pages is None or fetched < max_pages:
                page_params = dict(base_params)
                if cursor is not None:
                    page_params[cursor_param] = cursor
                response = await self.request(operation_id, page_params, response_type=response_type, timeout=timeout, headers=headers)
                yield response
                fetched += 1
                cursor = next_cursor(response)
                if not cursor:
                    break
            return

        page_param = page_param or detect_page_param(operation)
        if not page_param:
            raise ValueError(f"operation {operation_id} has no page or offset query parameter to paginate")
        page_value = default_start(page_param) if start is None else start
        fetched = 0
        while max_pages is None or fetched < max_pages:
            page_params = {**base_params, page_param: page_value}
            response = await self.request(operation_id, page_params, response_type=response_type, timeout=timeout, headers=headers)
            yield response
            fetched += 1
            if page_is_empty(response):
                break
            page_value += step

    async def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = None,
        *,
        items: Callable[[Any], Any] | None = None,
        **kwargs: Any,
    ) -> AsyncIterator[Any]:
        """Async iterator over individual items across pages."""
        extract = items or default_items
        async for page in self.paginate(operation_id, params, **kwargs):
            for item in extract(page):
                yield item


class _AsyncOperationGroup:
    def __init__(self, client: AsyncCrawloraClient, operations: Mapping[str, str]) -> None:
        self._client = client
        self._operations = operations

    def __getattr__(self, name: str) -> Callable[..., Any]:
        operation_id = self._operations.get(name)
        if operation_id is None:
            raise AttributeError(name)

        async def call(**params: Any) -> Any:
            response_type = params.pop("_response_type", "auto")
            timeout = params.pop("_timeout", None)
            headers = params.pop("_headers", None)
            return await self._client.request(
                operation_id, params, response_type=response_type, timeout=timeout, headers=headers
            )

        return call
