from __future__ import annotations

import json
import mimetypes
import os
import random
import socket
import time
import uuid
from dataclasses import dataclass
from typing import Any, Callable, Mapping, Literal
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen

from .operations import GROUPS, OPERATIONS

DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1"
VERSION = "1.2.0-sdk.16"
DEFAULT_USER_AGENT = f"crawlora-python-sdk/{VERSION}"
ResponseType = Literal["auto", "json", "text"]


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
        cause: BaseException | None = None,
    ):
        super().__init__(message)
        self.status = status
        self.code = code
        self.body = body
        self.raw_body = raw_body
        self.headers = dict(headers or {})
        self.__cause__ = cause


@dataclass(frozen=True)
class _Response:
    status: int
    headers: Mapping[str, str]
    body: bytes


class CrawloraClient:
    def __init__(
        self,
        *,
        api_key: str | None = None,
        jwt_token: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30,
        retries: int = 0,
        retry_delay: float = 0.25,
        headers: Mapping[str, str] | None = None,
        user_agent: str | None = DEFAULT_USER_AGENT,
        transport: Callable[[Request, float], _Response] | None = None,
    ) -> None:
        self.api_key = api_key or ""
        self.jwt_token = jwt_token or ""
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retries = max(0, int(retries))
        self.retry_delay = max(0.0, float(retry_delay))
        self.headers = dict(headers or {})
        self.user_agent = user_agent or ""
        self._transport = transport or self._urlopen_transport

        for group_name, operations in GROUPS.items():
            setattr(self, group_name, _OperationGroup(self, operations))

    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = None,
        *,
        response_type: ResponseType = "auto",
        timeout: float | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return self.request(operation_id, params, response_type=response_type, timeout=timeout, headers=headers)

    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = None,
        *,
        response_type: ResponseType = "auto",
        timeout: float | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        operation = OPERATIONS.get(operation_id)
        if operation is None:
            raise ValueError(f"unknown Crawlora operation: {operation_id}")
        response_type = _validate_response_type(response_type)

        attempt = 0
        while True:
            try:
                return self._send(operation, dict(params or {}), response_type=response_type, timeout=timeout, headers=headers)
            except CrawloraError as exc:
                if attempt >= self.retries or not _should_retry(exc.status):
                    raise
                attempt += 1
                _sleep_before_retry(self.retry_delay, attempt, exc.headers)

    def _send(
        self,
        operation: Mapping[str, Any],
        params: dict[str, Any],
        *,
        response_type: ResponseType,
        timeout: float | None,
        headers: Mapping[str, str] | None,
    ) -> Any:
        url, body, body_headers = _build_request(self.base_url, operation, params)
        request_headers = _merge_headers(
            self.headers,
            _auth_headers(operation.get("security", []), self.api_key, self.jwt_token),
            {"User-Agent": self.user_agent} if self.user_agent else {},
            body_headers,
            headers or {},
        )
        request = Request(url, data=body, headers=request_headers, method=operation["method"])
        try:
            response = self._transport(request, timeout if timeout is not None else self.timeout)
        except Exception as exc:
            message = "Crawlora request timed out" if _is_timeout_error(exc) else "Crawlora transport error"
            raise CrawloraError(message, cause=exc) from exc
        raw_body = response.body.decode(errors="replace")
        try:
            parsed = _parse_response(response.body, _header_value(response.headers, "content-type"), response_type)
        except json.JSONDecodeError as exc:
            raise CrawloraError(
                "Crawlora JSON parse error",
                status=response.status,
                raw_body=raw_body,
                headers=response.headers,
                cause=exc,
            ) from exc
        if response.status < 200 or response.status >= 300:
            code = parsed.get("code") if isinstance(parsed, dict) else None
            message = parsed.get("msg") if isinstance(parsed, dict) and parsed.get("msg") else f"HTTP {response.status}"
            raise CrawloraError(message, status=response.status, code=code, body=parsed, raw_body=raw_body, headers=response.headers)
        return parsed

    @staticmethod
    def _urlopen_transport(request: Request, timeout: float) -> _Response:
        try:
            with urlopen(request, timeout=timeout) as response:
                return _Response(response.status, dict(response.headers.items()), response.read())
        except HTTPError as exc:
            return _Response(exc.code, dict(exc.headers.items()), exc.read())
        except URLError:
            raise


class _OperationGroup:
    def __init__(self, client: CrawloraClient, operations: Mapping[str, str]) -> None:
        self._client = client
        self._operations = operations

    def __getattr__(self, name: str) -> Callable[..., Any]:
        operation_id = self._operations.get(name)
        if operation_id is None:
            raise AttributeError(name)

        def call(**params: Any) -> Any:
            response_type = params.pop("_response_type", "auto")
            timeout = params.pop("_timeout", None)
            headers = params.pop("_headers", None)
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
    if response_type in ("auto", "json", "text"):
        return response_type  # type: ignore[return-value]
    raise ValueError("invalid response_type: expected one of auto, json, text")


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
    return status == 0 or status in {408, 409, 425, 429} or status >= 500


def _sleep_before_retry(base_delay: float, attempt: int, headers: Mapping[str, str]) -> None:
    retry_after = _retry_after_delay(headers)
    if retry_after is not None:
        time.sleep(retry_after)
        return
    if base_delay <= 0:
        return
    delay = base_delay * (2 ** max(0, attempt - 1))
    jitter = random.uniform(0, base_delay / 2)
    time.sleep(delay + jitter)


def _retry_after_delay(headers: Mapping[str, str]) -> float | None:
    value = _header_value(headers, "retry-after")
    if not value:
        return None
    try:
        seconds = float(value)
    except ValueError:
        seconds = None
    if seconds is not None and seconds > 0:
        return min(seconds, 30.0)
    try:
        from email.utils import parsedate_to_datetime

        target = parsedate_to_datetime(value)
        delay = target.timestamp() - time.time()
    except (TypeError, ValueError, OverflowError):
        return None
    if delay > 0:
        return min(delay, 30.0)
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
