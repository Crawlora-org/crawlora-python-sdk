"""Shared pagination helpers used by the sync and async clients.

This module deliberately has no `.pyi` stub so type checkers read its inline
annotations directly (the `client.pyi` stub shadows `client.py`).
"""

from __future__ import annotations

from typing import Any, Mapping

PAGE_PARAM_NAMES = ("page", "offset")


def detect_page_param(operation: Mapping[str, Any]) -> str | None:
    names = {parameter["name"] for parameter in operation.get("queryParams", [])}
    for candidate in PAGE_PARAM_NAMES:
        if candidate in names:
            return candidate
    return None


def page_is_empty(response: Any) -> bool:
    data = response
    if isinstance(response, Mapping) and "data" in response:
        data = response["data"]
    if data is None:
        return True
    if isinstance(data, (list, tuple, dict, str)):
        return len(data) == 0
    return not data


def default_start(page_param: str) -> int:
    return 0 if page_param == "offset" else 1
