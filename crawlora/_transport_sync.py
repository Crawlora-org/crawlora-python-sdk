"""Keep-alive HTTP transport for the synchronous client (standard library only).

Maintains a small pool of reusable connections per ``(scheme, host, port)`` so
the sync client avoids a fresh TCP + TLS handshake on every request. Each
request checks out its own connection, so the transport is safe to use from
multiple threads (e.g. under ``max_concurrency``). This module is stub-free so
type checkers read its inline annotations directly.

The transport returns a lightweight response object exposing ``status``,
``headers`` (a dict), and ``body`` (bytes) — the only fields the client reads.
"""

from __future__ import annotations

import http.client
import threading
from dataclasses import dataclass
from typing import Any, Mapping
from urllib.parse import urlsplit
from urllib.request import Request


def _title_case(name: str) -> str:
    return "-".join(part.capitalize() for part in name.split("-"))


@dataclass(frozen=True)
class _PooledResponse:
    status: int
    headers: Mapping[str, str]
    body: bytes


class KeepAliveTransport:
    """Connection-pooling transport. Drop-in for the urlopen transport: callable
    as ``transport(request, timeout) -> response``."""

    def __init__(self, max_per_host: int = 8) -> None:
        self._lock = threading.Lock()
        self._pools: dict[tuple, list[http.client.HTTPConnection]] = {}
        self._max_per_host = max_per_host

    def __call__(self, request: Request, timeout: float) -> _PooledResponse:
        parts = urlsplit(request.full_url)
        key = (parts.scheme, parts.hostname, parts.port)
        path = parts.path or "/"
        if parts.query:
            path = f"{path}?{parts.query}"
        method = request.get_method()
        # Send canonical HTTP title-case header names (matching the urlopen
        # transport's behavior), so receivers see e.g. "X-Api-Key".
        headers = {_title_case(name): value for name, value in request.header_items()}
        body = request.data

        last_exc: Exception | None = None
        for attempt in range(2):
            conn = self._checkout(key, parts, timeout)
            try:
                conn.request(method, path, body=body, headers=headers)
                response = conn.getresponse()
                data = response.read()
                result = _PooledResponse(response.status, dict(response.getheaders()), data)
            except (http.client.HTTPException, ConnectionError, OSError) as exc:
                # Likely a stale pooled connection the server already closed;
                # discard it and retry once on a fresh connection.
                last_exc = exc
                self._close(conn)
                if attempt == 1:
                    raise
                continue
            if response.will_close:
                self._close(conn)
            else:
                self._checkin(key, conn)
            return result
        raise last_exc if last_exc else RuntimeError("keep-alive transport failed")

    def close(self) -> None:
        with self._lock:
            pools = list(self._pools.values())
            self._pools.clear()
        for pool in pools:
            for conn in pool:
                self._close(conn)

    def _checkout(self, key: tuple, parts: Any, timeout: float) -> http.client.HTTPConnection:
        with self._lock:
            pool = self._pools.get(key)
            if pool:
                conn = pool.pop()
                conn.timeout = timeout
                return conn
        return self._new(parts, timeout)

    def _checkin(self, key: tuple, conn: http.client.HTTPConnection) -> None:
        with self._lock:
            pool = self._pools.setdefault(key, [])
            if len(pool) < self._max_per_host:
                pool.append(conn)
                return
        self._close(conn)

    @staticmethod
    def _new(parts: Any, timeout: float) -> http.client.HTTPConnection:
        if parts.scheme == "https":
            return http.client.HTTPSConnection(parts.hostname, parts.port or 443, timeout=timeout)
        return http.client.HTTPConnection(parts.hostname, parts.port or 80, timeout=timeout)

    @staticmethod
    def _close(conn: http.client.HTTPConnection) -> None:
        try:
            conn.close()
        except Exception:
            pass
