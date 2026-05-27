from __future__ import annotations

import json
import mimetypes
import os
import uuid
from dataclasses import dataclass
from typing import Any, Callable, Mapping
from urllib.error import HTTPError
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen

from .operations import GROUPS, OPERATIONS

DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1"


class CrawloraError(Exception):
    def __init__(self, message: str, *, status: int, code: int | None = None, body: Any = None):
        super().__init__(message)
        self.status = status
        self.code = code
        self.body = body


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
        headers: Mapping[str, str] | None = None,
        transport: Callable[[Request, float], _Response] | None = None,
    ) -> None:
        self.api_key = api_key or ""
        self.jwt_token = jwt_token or ""
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retries = retries
        self.headers = dict(headers or {})
        self._transport = transport or self._urlopen_transport

        for group_name, operations in GROUPS.items():
            setattr(self, group_name, _OperationGroup(self, operations))

    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = None,
        *,
        response_type: str = "auto",
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return self.request(operation_id, params, response_type=response_type, headers=headers)

    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = None,
        *,
        response_type: str = "auto",
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        operation = OPERATIONS.get(operation_id)
        if operation is None:
            raise ValueError(f"unknown Crawlora operation: {operation_id}")

        attempt = 0
        while True:
            try:
                return self._send(operation, dict(params or {}), response_type=response_type, headers=headers)
            except CrawloraError as exc:
                if attempt >= self.retries or not _should_retry(exc.status):
                    raise
                attempt += 1

    def _send(
        self,
        operation: Mapping[str, Any],
        params: dict[str, Any],
        *,
        response_type: str,
        headers: Mapping[str, str] | None,
    ) -> Any:
        url, body, body_headers = _build_request(self.base_url, operation, params)
        request_headers = {
            **self.headers,
            **_auth_headers(operation.get("security", []), self.api_key, self.jwt_token),
            **body_headers,
            **dict(headers or {}),
        }
        request = Request(url, data=body, headers=request_headers, method=operation["method"])
        response = self._transport(request, self.timeout)
        parsed = _parse_response(response.body, response.headers.get("content-type", ""), response_type)
        if response.status < 200 or response.status >= 300:
            code = parsed.get("code") if isinstance(parsed, dict) else None
            message = parsed.get("msg") if isinstance(parsed, dict) and parsed.get("msg") else f"HTTP {response.status}"
            raise CrawloraError(message, status=response.status, code=code, body=parsed)
        return parsed

    @staticmethod
    def _urlopen_transport(request: Request, timeout: float) -> _Response:
        try:
            with urlopen(request, timeout=timeout) as response:
                return _Response(response.status, dict(response.headers.items()), response.read())
        except HTTPError as exc:
            return _Response(exc.code, dict(exc.headers.items()), exc.read())


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
            headers = params.pop("_headers", None)
            return self._client.request(operation_id, params, response_type=response_type, headers=headers)

        return call


def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[str, bytes | None, dict[str, str]]:
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
            query.extend((name, item) for item in value)
        else:
            query.append((name, value))
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
        headers["Authorization"] = jwt_token if jwt_token.startswith(("Token ", "Bearer ")) else f"Token {jwt_token}"
    return headers


def _parse_response(body: bytes, content_type: str, response_type: str) -> Any:
    if response_type == "text":
        return body.decode()
    if response_type == "json" or "application/json" in content_type:
        return json.loads(body.decode()) if body else None
    return body.decode()


def _should_retry(status: int) -> bool:
    return status in {408, 409, 425, 429} or status >= 500
