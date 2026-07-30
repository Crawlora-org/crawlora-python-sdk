from __future__ import annotations

import io
import json
import mimetypes
import os
import random
import socket
import threading
import time
import uuid
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Mapping, Literal
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen

from ._pagination import default_items, default_start, detect_page_param, page_is_empty
from ._transport_sync import KeepAliveTransport
from .operations import GROUPS, OPERATIONS

DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1"
VERSION = "1.27.0-sdk.1"
DEFAULT_USER_AGENT = f"crawlora-python-sdk/{VERSION}"
DEFAULT_MAX_RETRY_DELAY = 30.0
DEFAULT_RETRY_STATUSES = (408, 409, 425, 429)
ResponseType = Literal["auto", "json", "text", "stream"]
RetryPredicate = Callable[[int, "BaseException | None"], bool]
RetryHook = Callable[[int, "BaseException", float], None]
Logger = Callable[[Mapping[str, Any]], None]
# before_request receives a mutable context dict {operation, method, url, headers};
# mutating "headers"/"url" rewrites the outgoing request. after_response receives
# (operation_id, status, headers, body) and may return a replacement body.
BeforeRequest = Callable[[dict], None]
AfterResponse = Callable[[str, int, Mapping[str, str], Any], Any]


def _as_hook_list(value: Any) -> list:
    if value is None:
        return []
    if callable(value):
        return [value]
    return list(value)


def _run_before_request(hooks: list, ctx: dict) -> None:
    for hook in hooks:
        hook(ctx)


def _run_after_response(hooks: list, operation_id: str, status: int, headers: Mapping[str, str], body: Any) -> Any:
    for hook in hooks:
        result = hook(operation_id, status, headers, body)
        if result is not None:
            body = result
    return body


class CrawloraError(Exception):
    def __init__(
        self,
        message: str,
        *,
        status: int = 0,
        code: int | None = None,
        body: Any = None,
        raw_body: str = "",
        headers: Mapping[str, str] | None = None,
        request_id: str | None = None,
        cause: BaseException | None = None,
    ):
        super().__init__(message)
        self.status = status
        self.code = code
        self.body = body
        self.raw_body = raw_body
        self.headers = dict(headers or {})
        self.request_id = request_id
        self.__cause__ = cause


class CrawloraClientError(CrawloraError):
    """Raised for 4xx API responses: the request was rejected by the API."""


class CrawloraServerError(CrawloraError):
    """Raised for 5xx API responses: the API failed to handle a valid request."""


class CrawloraNetworkError(CrawloraError):
    """Raised for transport failures and timeouts before a response arrived."""


def _api_error_class(status: int) -> type[CrawloraError]:
    if 400 <= status < 500:
        return CrawloraClientError
    if status >= 500:
        return CrawloraServerError
    return CrawloraError


@dataclass(frozen=True)
class _Response:
    status: int
    headers: Mapping[str, str]
    body: bytes


class _RateLimiter:
    """Optional client-side throttle: caps concurrency and spaces requests to a
    maximum rate (requests per second)."""

    def __init__(self, rps: float | None, concurrency: int | None) -> None:
        self._interval = (1.0 / rps) if rps and rps > 0 else 0.0
        self._sem = threading.Semaphore(concurrency) if concurrency and concurrency > 0 else None
        self._lock = threading.Lock()
        self._next = 0.0

    def __enter__(self) -> "_RateLimiter":
        if self._sem is not None:
            self._sem.acquire()
        if self._interval:
            with self._lock:
                now = time.monotonic()
                wait = max(0.0, self._next - now)
                self._next = max(now, self._next) + self._interval
            if wait > 0:
                time.sleep(wait)
        return self

    def __exit__(self, *_exc: Any) -> None:
        if self._sem is not None:
            self._sem.release()


class CrawloraClient:
    """Synchronous client for the Crawlora API.

    Call operations via grouped helpers (``client.bing.search(q="...")``) or
    dynamically (``client.request("bing-search", {"q": "..."})``). Supports
    configurable retries, an ``on_retry`` hook, opt-in ``request_id`` and
    ``idempotency_keys``, ``before_request``/``after_response`` middleware,
    client-side ``rate_limit``/``max_concurrency``, pagination
    (``paginate``/``paginate_items``), and ``response_type="stream"``. Uses a
    keep-alive connection pool by default; use it as a context manager (or call
    ``close()``) to release pooled connections. See ``AsyncCrawloraClient`` for
    an asyncio client.
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        jwt_token: str | None = None,
        base_url: str | None = None,
        timeout: float = 30,
        retries: int = 0,
        retry_delay: float = 0.25,
        max_retry_delay: float = DEFAULT_MAX_RETRY_DELAY,
        retry_statuses: Iterable[int] | None = None,
        retry_predicate: RetryPredicate | None = None,
        on_retry: RetryHook | None = None,
        request_id: bool = False,
        idempotency_keys: bool = False,
        rate_limit: float | None = None,
        max_concurrency: int | None = None,
        logger: Logger | None = None,
        before_request: BeforeRequest | Iterable[BeforeRequest] | None = None,
        after_response: AfterResponse | Iterable[AfterResponse] | None = None,
        headers: Mapping[str, str] | None = None,
        user_agent: str | None = DEFAULT_USER_AGENT,
        transport: Callable[[Request, float], _Response] | None = None,
    ) -> None:
        # Precedence: explicit argument > environment variable > default.
        self.api_key = api_key or os.environ.get("CRAWLORA_API_KEY", "")
        self.jwt_token = jwt_token or ""
        self.base_url = (base_url or os.environ.get("CRAWLORA_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout
        self.retries = max(0, int(retries))
        self.retry_delay = max(0.0, float(retry_delay))
        self.max_retry_delay = max(0.0, float(max_retry_delay))
        self.retry_statuses = frozenset(retry_statuses) if retry_statuses is not None else None
        self.retry_predicate = retry_predicate
        self.on_retry = on_retry
        self.request_id = request_id
        self.idempotency_keys = idempotency_keys
        self.rate_limit = rate_limit
        self.max_concurrency = max_concurrency
        self._rate_limiter = _RateLimiter(rate_limit, max_concurrency) if (rate_limit or max_concurrency) else None
        self.logger = logger
        self.before_request = _as_hook_list(before_request)
        self.after_response = _as_hook_list(after_response)
        self.headers = dict(headers or {})
        self.user_agent = user_agent or ""
        # Default to a keep-alive pool (connection reuse); an injected transport
        # (e.g. tests) is used as-is.
        self._transport = transport or KeepAliveTransport()

        for group_name, operations in GROUPS.items():
            setattr(self, group_name, _OperationGroup(self, operations))

    def close(self) -> None:
        """Close pooled keep-alive connections, if any."""
        closer = getattr(self._transport, "close", None)
        if callable(closer):
            closer()

    def __enter__(self) -> "CrawloraClient":
        return self

    def __exit__(self, *_exc: Any) -> None:
        self.close()

    def _is_retryable(self, status: int, exc: BaseException | None) -> bool:
        if self.retry_predicate is not None:
            return bool(self.retry_predicate(status, exc))
        if self.retry_statuses is not None:
            # Network failures (status 0) stay retryable unless a predicate decides.
            return status == 0 or status in self.retry_statuses
        return _should_retry(status)

    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float:
        retry_after = _retry_after_delay(headers, self.max_retry_delay)
        if retry_after is not None:
            return retry_after
        if self.retry_delay <= 0:
            return 0.0
        delay = self.retry_delay * (2 ** max(0, attempt - 1))
        jitter = random.uniform(0, self.retry_delay / 2)
        return delay + jitter

    def _log(self, event: Mapping[str, Any]) -> None:
        if self.logger is not None:
            self.logger(event)

    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = None,
        *,
        response_type: ResponseType = "auto",
        timeout: float | None = None,
        headers: Mapping[str, str] | None = None,
        retries: int | None = None,
        retry_predicate: RetryPredicate | None = None,
    ) -> Any:
        return self.request(
            operation_id, params, response_type=response_type, timeout=timeout, headers=headers,
            retries=retries, retry_predicate=retry_predicate,
        )

    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = None,
        *,
        response_type: ResponseType = "auto",
        timeout: float | None = None,
        headers: Mapping[str, str] | None = None,
        retries: int | None = None,
        retry_predicate: RetryPredicate | None = None,
    ) -> Any:
        operation = OPERATIONS.get(operation_id)
        if operation is None:
            raise ValueError(f"unknown Crawlora operation: {operation_id}")
        response_type = _validate_response_type(response_type)
        self._log({"event": "request", "operation": operation_id})
        max_retries = self.retries if retries is None else max(0, int(retries))
        idempotency_key = uuid.uuid4().hex if self.idempotency_keys and operation["method"] in ("POST", "PATCH") else None

        attempt = 0
        while True:
            try:
                return self._send(operation, dict(params or {}), response_type=response_type, timeout=timeout, headers=headers, idempotency_key=idempotency_key)
            except CrawloraError as exc:
                retryable = retry_predicate(exc.status, exc) if retry_predicate is not None else self._is_retryable(exc.status, exc)
                if attempt >= max_retries or not retryable:
                    raise
                attempt += 1
                delay = self._compute_retry_delay(attempt, exc.headers)
                self._log({"event": "retry", "operation": operation_id, "attempt": attempt, "status": exc.status, "delay": delay})
                if self.on_retry is not None:
                    self.on_retry(attempt, exc, delay)
                if delay > 0:
                    time.sleep(delay)

    def _send(
        self,
        operation: Mapping[str, Any],
        params: dict[str, Any],
        *,
        response_type: ResponseType,
        timeout: float | None,
        headers: Mapping[str, str] | None,
        idempotency_key: str | None = None,
    ) -> Any:
        url, body, body_headers = _build_request(self.base_url, operation, params)
        request_headers = _merge_headers(
            self.headers,
            _auth_headers(operation.get("security", []), self.api_key, self.jwt_token),
            {"User-Agent": self.user_agent} if self.user_agent else {},
            body_headers,
            headers or {},
        )
        req_id = _ensure_request_id(request_headers) if self.request_id else _header_value(request_headers, "x-request-id") or None
        if idempotency_key and not _header_value(request_headers, "idempotency-key"):
            request_headers["Idempotency-Key"] = idempotency_key
        if self.before_request:
            ctx = {"operation": operation.get("id"), "method": operation["method"], "url": url, "headers": request_headers}
            _run_before_request(self.before_request, ctx)
            url, request_headers = ctx["url"], ctx["headers"]
        request = Request(url, data=body, headers=request_headers, method=operation["method"])
        request_timeout = timeout if timeout is not None else self.timeout
        try:
            if self._rate_limiter is not None:
                with self._rate_limiter:
                    response = self._transport(request, request_timeout)
            else:
                response = self._transport(request, request_timeout)
        except Exception as exc:
            message = "Crawlora request timed out" if _is_timeout_error(exc) else "Crawlora transport error"
            raise CrawloraNetworkError(message, request_id=req_id, cause=exc) from exc
        raw_body = response.body.decode(errors="replace")
        is_error = response.status < 200 or response.status >= 300
        if response_type == "stream" and not is_error:
            # Caller reads the file-like body; truly incremental streaming is
            # available on AsyncCrawloraClient (httpx).
            return io.BytesIO(response.body)
        parse_mode = "auto" if response_type == "stream" else response_type
        try:
            parsed = _parse_response(response.body, _header_value(response.headers, "content-type"), parse_mode)
        except json.JSONDecodeError as exc:
            raise CrawloraError(
                "Crawlora JSON parse error",
                status=response.status,
                raw_body=raw_body,
                headers=response.headers,
                request_id=req_id,
                cause=exc,
            ) from exc
        if response.status < 200 or response.status >= 300:
            code = parsed.get("code") if isinstance(parsed, dict) else None
            message = parsed.get("msg") if isinstance(parsed, dict) and parsed.get("msg") else f"HTTP {response.status}"
            error_class = _api_error_class(response.status)
            raise error_class(message, status=response.status, code=code, body=parsed, raw_body=raw_body, headers=response.headers, request_id=req_id)
        if self.after_response:
            parsed = _run_after_response(self.after_response, operation.get("id"), response.status, response.headers, parsed)
        return parsed

    def paginate(
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
    ):
        """Yield successive pages of a paginated operation.

        Numeric mode (default) advances the ``page``/``offset`` query parameter
        and stops on an empty page. Cursor mode (pass both ``cursor_param`` and a
        ``next_cursor`` extractor) sends the cursor parameter and stops when
        ``next_cursor`` returns a falsy value.
        """
        operation = OPERATIONS.get(operation_id)
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
                response = self.request(operation_id, page_params, response_type=response_type, timeout=timeout, headers=headers)
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
            response = self.request(operation_id, page_params, response_type=response_type, timeout=timeout, headers=headers)
            yield response
            fetched += 1
            if page_is_empty(response):
                break
            page_value += step

    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = None,
        *,
        items: Callable[[Any], Any] | None = None,
        **kwargs: Any,
    ):
        """Yield individual items across pages. ``items`` extracts the list from
        a page (default: the Crawlora ``data`` array)."""
        extract = items or default_items
        for page in self.paginate(operation_id, params, **kwargs):
            for item in extract(page):
                yield item

    @staticmethod
    def _urlopen_transport(request: Request, timeout: float) -> _Response:
        try:
            with urlopen(request, timeout=timeout) as response:
                return _Response(response.status, dict(response.headers.items()), response.read())
        except HTTPError as exc:
            return _Response(exc.code, dict(exc.headers.items()), exc.read())
        except URLError:
            raise


def _allowed_params(operation_id: str) -> set[str]:
    operation = OPERATIONS.get(operation_id) or {}
    allowed = set(operation.get("pathParams", []))
    allowed |= {p["name"] for p in operation.get("queryParams", [])}
    allowed |= {p["name"] for p in operation.get("formParams", [])}
    if operation.get("bodyParam"):
        allowed.add(operation["bodyParam"])
    allowed.add("body")
    return allowed


_REQUEST_OPTION_KWARGS = ("_response_type", "_timeout", "_headers")


class _OperationGroup:
    def __init__(self, client: CrawloraClient, operations: Mapping[str, str]) -> None:
        self._client = client
        self._operations = operations

    def __getattr__(self, name: str) -> Callable[..., Any]:
        operation_id = self._operations.get(name)
        if operation_id is None:
            raise AttributeError(name)
        allowed = _allowed_params(operation_id)

        def call(**params: Any) -> Any:
            response_type = params.pop("_response_type", "auto")
            timeout = params.pop("_timeout", None)
            headers = params.pop("_headers", None)
            unknown = set(params) - allowed
            if unknown:
                raise TypeError(f"unexpected parameter(s) for {operation_id}: {', '.join(sorted(unknown))}")
            return self._client.request(operation_id, params, response_type=response_type, timeout=timeout, headers=headers)

        return call


def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[str, bytes | None, dict[str, str]]:
    _validate_required_params(operation, params)
    _validate_enum_params(operation, params)
    path = operation["path"]
    for name in operation.get("pathParams", []):
        value = params.get(name)
        if value in (None, ""):
            raise ValueError(f"missing required path parameter: {name}")
        path = path.replace("{" + name + "}", quote(str(value), safe=""))

    query: list[tuple[str, Any]] = []
    for parameter in operation.get("queryParams", []):
        name = parameter["name"]
        value = params.get(name)
        if value in (None, ""):
            continue
        if isinstance(value, (list, tuple)):
            query.extend((name, _stringify_param(item)) for item in value)
        else:
            query.append((name, _stringify_param(value)))
    url = base_url + path
    if query:
        url += "?" + urlencode(query, doseq=True)

    if operation.get("formParams"):
        return url, *_multipart_body(operation["formParams"], params)

    body_param = operation.get("bodyParam")
    if body_param:
        value = params.get(body_param, params.get("body"))
        if value is not None:
            return url, json.dumps(value).encode(), {"content-type": "application/json"}

    return url, None, {}


def _validate_required_params(operation: Mapping[str, Any], params: Mapping[str, Any]) -> None:
    for name in operation.get("pathParams", []):
        if _is_missing(params.get(name)):
            raise ValueError(f"missing required path parameter: {name}")
    for location in ("queryParams", "formParams"):
        for parameter in operation.get(location, []):
            if parameter.get("required") and _is_missing(params.get(parameter["name"])):
                param_location = parameter.get("in", "request")
                raise ValueError(f"missing required {param_location} parameter: {parameter['name']}")
    if operation.get("bodyRequired"):
        body_param = operation.get("bodyParam")
        if _is_missing(params.get(body_param)) and _is_missing(params.get("body")):
            raise ValueError(f"missing required body parameter: {body_param}")


def _validate_enum_params(operation: Mapping[str, Any], params: Mapping[str, Any]) -> None:
    for location in ("queryParams", "formParams"):
        for parameter in operation.get(location, []):
            enum_values = parameter.get("enum") or []
            value = params.get(parameter["name"])
            if not enum_values or _is_missing(value):
                continue
            values = value if isinstance(value, (list, tuple)) else [value]
            for item in values:
                if _stringify_param(item) not in enum_values:
                    param_location = parameter.get("in", "request")
                    expected = ", ".join(enum_values)
                    raise ValueError(f"invalid {param_location} parameter {parameter['name']}: expected one of {expected}")


def _is_missing(value: Any) -> bool:
    return value is None or value == "" or (isinstance(value, (list, tuple)) and len(value) == 0)


def _multipart_body(form_params: list[Mapping[str, Any]], params: Mapping[str, Any]) -> tuple[bytes, dict[str, str]]:
    boundary = f"crawlora-{uuid.uuid4().hex}"
    chunks: list[bytes] = []
    for parameter in form_params:
        name = parameter["name"]
        if name not in params or params[name] is None:
            continue
        value = params[name]
        chunks.append(f"--{boundary}\r\n".encode())
        if parameter.get("type") == "file":
            filename, data = _read_file_value(value)
            content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
            chunks.append(
                f'Content-Disposition: form-data; name="{name}"; filename="{filename}"\r\n'
                f"Content-Type: {content_type}\r\n\r\n".encode()
            )
            chunks.append(data)
            chunks.append(b"\r\n")
        else:
            chunks.append(f'Content-Disposition: form-data; name="{name}"\r\n\r\n{value}\r\n'.encode())
    chunks.append(f"--{boundary}--\r\n".encode())
    return b"".join(chunks), {"content-type": f"multipart/form-data; boundary={boundary}"}


def _read_file_value(value: Any) -> tuple[str, bytes]:
    if isinstance(value, (bytes, bytearray)):
        return "upload.bin", bytes(value)
    if isinstance(value, os.PathLike) or isinstance(value, str):
        path = os.fspath(value)
        with open(path, "rb") as file:
            return os.path.basename(path), file.read()
    name = os.path.basename(getattr(value, "name", "upload.bin"))
    return name, value.read()


def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]:
    headers: dict[str, str] = {}
    if "ApiKeyAuth" in security and api_key:
        headers["x-api-key"] = api_key
    if "JWTAuth" in security and jwt_token:
        headers["Authorization"] = jwt_token if jwt_token.lower().startswith(("token ", "bearer ")) else f"Token {jwt_token}"
    return headers


def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]:
    headers: dict[str, str] = {}
    names: dict[str, str] = {}
    for source in sources:
        for name, value in source.items():
            lower = name.lower()
            existing = names.get(lower)
            if existing and existing != name:
                headers.pop(existing, None)
            headers[name] = str(value)
            names[lower] = name
    return headers


def _validate_response_type(response_type: str) -> ResponseType:
    if response_type in ("auto", "json", "text", "stream"):
        return response_type  # type: ignore[return-value]
    raise ValueError("invalid response_type: expected one of auto, json, text, stream")


def _parse_response(body: bytes, content_type: str, response_type: str) -> Any:
    if response_type == "text":
        return body.decode()
    if response_type == "json" or "application/json" in content_type.lower():
        return json.loads(body.decode()) if body else None
    return body.decode()


def _stringify_param(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _should_retry(status: int) -> bool:
    return status == 0 or status in DEFAULT_RETRY_STATUSES or status >= 500


def _ensure_request_id(headers: dict[str, str]) -> str:
    existing = _header_value(headers, "x-request-id")
    if existing:
        return existing
    request_id = uuid.uuid4().hex
    headers["x-request-id"] = request_id
    return request_id


def _retry_after_delay(headers: Mapping[str, str], cap: float) -> float | None:
    value = _header_value(headers, "retry-after")
    if not value:
        return None
    try:
        seconds = float(value)
    except ValueError:
        seconds = None
    if seconds is not None and seconds > 0:
        return min(seconds, cap)
    try:
        from email.utils import parsedate_to_datetime

        target = parsedate_to_datetime(value)
        delay = target.timestamp() - time.time()
    except (TypeError, ValueError, OverflowError):
        return None
    if delay > 0:
        return min(delay, cap)
    return None


def _header_value(headers: Mapping[str, str], name: str) -> str:
    for key, value in headers.items():
        if key.lower() == name.lower():
            return value
    return ""


def _is_timeout_error(exc: BaseException) -> bool:
    if isinstance(exc, (TimeoutError, socket.timeout)):
        return True
    if isinstance(exc, URLError):
        reason = exc.reason
        if isinstance(reason, (TimeoutError, socket.timeout)):
            return True
        return "timed out" in str(reason).lower()
    return "timed out" in str(exc).lower()
