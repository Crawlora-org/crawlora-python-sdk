"""Asyncio-friendly wrapper around the synchronous :class:`CrawloraClient`.

The core client is built on the standard library only, so the async client runs
each request in a worker thread via :func:`asyncio.to_thread`. This keeps the
package dependency-free while giving ``await``-able ergonomics that integrate
with asyncio applications:

    client = AsyncCrawloraClient(api_key="...")
    result = await client.bing.search(q="coffee")
    async for page in client.paginate("ebay-seller-feedback", {"seller": "acme"}):
        ...
"""

from __future__ import annotations

import asyncio
from typing import Any, AsyncIterator, Callable, Mapping

from ._pagination import default_start, detect_page_param, page_is_empty
from .client import CrawloraClient, ResponseType
from .operations import GROUPS, OPERATIONS


class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None:
        self._client = CrawloraClient(**kwargs)
        for group_name, operations in GROUPS.items():
            setattr(self, group_name, _AsyncOperationGroup(self, operations))

    @property
    def sync_client(self) -> CrawloraClient:
        """The underlying synchronous client."""
        return self._client

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
        return await asyncio.to_thread(
            self._client.request,
            operation_id,
            params,
            response_type=response_type,
            timeout=timeout,
            headers=headers,
        )

    async def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = None,
        *,
        page_param: str | None = None,
        start: int | None = None,
        step: int = 1,
        max_pages: int | None = None,
        response_type: ResponseType = "auto",
        timeout: float | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Async iterator over pages of a paginated operation.

        Mirrors :meth:`CrawloraClient.paginate`, awaiting each page request.
        """
        operation: Any = OPERATIONS.get(operation_id)
        if operation is None:
            raise ValueError(f"unknown Crawlora operation: {operation_id}")
        page_param = page_param or detect_page_param(operation)
        if not page_param:
            raise ValueError(f"operation {operation_id} has no page or offset query parameter to paginate")
        if start is None:
            start = default_start(page_param)
        base_params = dict(params or {})
        page_value = start
        fetched = 0
        while max_pages is None or fetched < max_pages:
            page_params = {**base_params, page_param: page_value}
            response = await self.request(
                operation_id, page_params, response_type=response_type, timeout=timeout, headers=headers
            )
            yield response
            fetched += 1
            if page_is_empty(response):
                break
            page_value += step


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
