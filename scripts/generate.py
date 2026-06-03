#!/usr/bin/env python3
"""Python SDK emitter.

Language-neutral spec parsing, grouping, aliasing, and the operations docs table
live in the vendored `scripts/_sdkgen/core.py` (synced from the API repo). This
file only maps OpenAPI schemas to Python types and writes the Python artifacts:
`crawlora/operations.py` (runtime metadata) and `crawlora/client.pyi` (stubs).
"""
import json
import keyword
import os
import pprint
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _sdkgen import core  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPEC = ROOT / "openapi" / "public.json"
SPEC_PATH = Path(os.environ.get("CRAWLORA_OPENAPI_SPEC", DEFAULT_SPEC))

POLICY = core.NamingPolicy(
    case_fn=lambda parts: "_".join(parts) or "call",
    dedup_sep="_",
    keywords=frozenset(keyword.kwlist),
    tag_group_overrides={
        "AppStore": "app_store",
        "CoinGecko": "coin_gecko",
        "GooglePlay": "google_play",
        "ProductHunt": "product_hunt",
        "SimilarWeb": "similar_web",
        "SpotifyPodcasts": "spotify_podcasts",
        "TikTok": "tiktok",
        "YouTube": "youtube",
    },
)


def schema_type_name(value):
    return "Model" + core.type_name(value)


def schema_ref_name(schema):
    ref = (schema or {}).get("$ref", "")
    return ref.rsplit("/", 1)[-1] if ref else ""


def py_schema_type(schema):
    if not schema:
        return "Any"
    if "$ref" in schema:
        return schema_type_name(schema_ref_name(schema))
    if "allOf" in schema:
        parts = [py_schema_type(part) for part in schema.get("allOf", [])]
        concrete = [part for part in parts if part != "Any"]
        return concrete[0] if len(concrete) == 1 else "Any"
    enum_schema_values = schema.get("enum") or []
    if enum_schema_values:
        return "Literal[" + ", ".join(repr(str(value)) for value in enum_schema_values) + "]"
    typ = schema.get("type")
    if typ == "integer":
        return "int"
    if typ == "number":
        return "float"
    if typ == "boolean":
        return "bool"
    if typ == "string":
        return "str"
    if typ == "array":
        return f"list[{py_schema_type(schema.get('items', {'type': 'string'}))}]"
    if typ == "object":
        additional = schema.get("additionalProperties")
        if additional:
            value_type = py_schema_type(additional) if isinstance(additional, dict) else "Any"
            return f"dict[str, {value_type}]"
        return "dict[str, Any]"
    return "Any"


def py_type(param):
    enum_values = param.get("enum") or []
    if enum_values:
        return "Literal[" + ", ".join(repr(str(value)) for value in enum_values) + "]"
    typ = param.get("type")
    if typ == "integer":
        return "int"
    if typ == "number":
        return "float"
    if typ == "boolean":
        return "bool"
    if typ == "array":
        return f"list[{py_type(param.get('items', {'type': 'string'}))}]"
    if typ == "file":
        return "Any"
    return "str"


def stub_declarations(model):
    lines = [
        "from __future__ import annotations",
        "",
        "import sys",
        "from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload",
        "",
        "if sys.version_info >= (3, 11):",
        "    from typing import NotRequired, Required, TypedDict, Unpack",
        "else:",
        "    from typing_extensions import NotRequired, Required, TypedDict, Unpack",
        "",
        'ResponseType = Literal["auto", "json", "text", "stream"]',
        "",
        "class CrawloraError(Exception):",
        "    status: int",
        "    code: int | None",
        "    body: Any",
        "    raw_body: str",
        "    headers: Mapping[str, str]",
        "    request_id: str | None",
        "    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...",
        "",
        "class CrawloraClientError(CrawloraError): ...",
        "class CrawloraServerError(CrawloraError): ...",
        "class CrawloraNetworkError(CrawloraError): ...",
        "",
        "class _RequestOptions(TypedDict, total=False):",
        "    _response_type: ResponseType",
        "    _timeout: float",
        "    _headers: Mapping[str, str]",
        "",
    ]
    for schema_name, schema in model.definitions.items():
        model_name = schema_type_name(schema_name)
        if schema.get("type") == "object" and schema.get("properties"):
            required = set(schema.get("required") or [])
            lines.append(f"{model_name} = TypedDict({model_name!r}, {{")
            for prop_name, prop_schema in sorted(schema.get("properties", {}).items()):
                wrapper = "Required" if prop_name in required else "NotRequired"
                lines.append(f"    {prop_name!r}: {wrapper}[{py_schema_type(prop_schema)}],")
            lines.append("}, total=False)")
            lines.append("")
            continue
        lines.append(f"{model_name} = {py_schema_type(schema)}")
        lines.append("")
    for operation_id, meta in model.meta.items():
        base = meta["type_base"]
        body_type = py_schema_type(meta["body_schema"])
        if body_type != "Any":
            lines.append(f"{base}Body = {body_type}")
        lines.append(f"{base}Response = {py_schema_type(meta['response_schema'])}")
        fields = {
            "_response_type": "NotRequired[ResponseType]",
            "_timeout": "NotRequired[float]",
            "_headers": "NotRequired[Mapping[str, str]]",
        }
        for param in meta["params"]:
            wrapper = "Required" if param.get("required") else "NotRequired"
            typ = f"{base}Body" if param.get("in") == "body" else py_type(param)
            fields[param["name"]] = f"{wrapper}[{typ}]"
        lines.append(f"{base}Params = TypedDict({(base + 'Params')!r}, {{")
        for key, typ in fields.items():
            lines.append(f"    {key!r}: {typ},")
        lines.append("}, total=False)")
        lines.append("")
    for group_name, methods in model.groups.items():
        lines.append(f"class {core.type_name(group_name, 'group')}:")
        if not methods:
            lines.append("    pass")
        for method_name, operation_id in methods.items():
            base = model.meta[operation_id]["type_base"]
            lines.append(f"    def {method_name}(self, **params: Unpack[{base}Params]) -> {base}Response: ...")
        lines.append("")
    operation_ids = list(model.meta.keys())
    lines.append("OperationId = Literal[")
    for operation_id in operation_ids:
        lines.append(f"    {operation_id!r},")
    lines.append("]")
    lines.append("")
    lines.append("class CrawloraClient:")
    for group_name in model.groups:
        lines.append(f"    {group_name}: {core.type_name(group_name, 'group')}")
    lines.extend(
        [
            "    api_key: str",
            "    jwt_token: str",
            "    base_url: str",
            "    timeout: float",
            "    retries: int",
            "    retry_delay: float",
            "    max_retry_delay: float",
            "    retry_statuses: frozenset[int] | None",
            "    retry_predicate: Callable[[int, BaseException | None], bool] | None",
            "    on_retry: Callable[[int, BaseException, float], None] | None",
            "    request_id: bool",
            "    idempotency_keys: bool",
            "    rate_limit: float | None",
            "    max_concurrency: int | None",
            "    logger: Callable[[Mapping[str, Any]], None] | None",
            "    before_request: list[Callable[[dict[str, Any]], None]]",
            "    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]",
            "    headers: dict[str, str]",
            "    user_agent: str",
            "    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...",
            "    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...",
            "    def _log(self, event: Mapping[str, Any]) -> None: ...",
            "    def __init__(",
            "        self,",
            "        *,",
            "        api_key: str | None = ...,",
            "        jwt_token: str | None = ...,",
            "        base_url: str | None = ...,",
            "        timeout: float = ...,",
            "        retries: int = ...,",
            "        retry_delay: float = ...,",
            "        max_retry_delay: float = ...,",
            "        retry_statuses: Iterable[int] | None = ...,",
            "        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,",
            "        on_retry: Callable[[int, BaseException, float], None] | None = ...,",
            "        request_id: bool = ...,",
            "        idempotency_keys: bool = ...,",
            "        rate_limit: float | None = ...,",
            "        max_concurrency: int | None = ...,",
            "        logger: Callable[[Mapping[str, Any]], None] | None = ...,",
            "        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,",
            "        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,",
            "        headers: Mapping[str, str] | None = ...,",
            "        user_agent: str | None = ...,",
            "        transport: Callable[..., Any] | None = ...,",
            "    ) -> None: ...",
            "    def close(self) -> None: ...",
            "    def __enter__(self) -> CrawloraClient: ...",
            "    def __exit__(self, *exc: Any) -> None: ...",
            "    def paginate(",
            "        self,",
            "        operation_id: str,",
            "        params: Mapping[str, Any] | None = ...,",
            "        *,",
            "        page_param: str | None = ...,",
            "        cursor_param: str | None = ...,",
            "        next_cursor: Callable[[Any], Any] | None = ...,",
            "        start: Any = ...,",
            "        step: int = ...,",
            "        max_pages: int | None = ...,",
            "        response_type: ResponseType = ...,",
            "        timeout: float | None = ...,",
            "        headers: Mapping[str, str] | None = ...,",
            "    ) -> Iterator[Any]: ...",
            "    def paginate_items(",
            "        self,",
            "        operation_id: str,",
            "        params: Mapping[str, Any] | None = ...,",
            "        *,",
            "        items: Callable[[Any], Any] | None = ...,",
            "        page_param: str | None = ...,",
            "        cursor_param: str | None = ...,",
            "        next_cursor: Callable[[Any], Any] | None = ...,",
            "        start: Any = ...,",
            "        step: int = ...,",
            "        max_pages: int | None = ...,",
            "        response_type: ResponseType = ...,",
            "        timeout: float | None = ...,",
            "        headers: Mapping[str, str] | None = ...,",
            "    ) -> Iterator[Any]: ...",
        ]
    )
    for method_name in ("operation", "request"):
        for operation_id in operation_ids:
            base = model.meta[operation_id]["type_base"]
            params_default = " = ..." if not model.meta[operation_id]["has_required_params"] else ""
            lines.extend(
                [
                    "    @overload",
                    f"    def {method_name}(",
                    "        self,",
                    f"        operation_id: Literal[{operation_id!r}],",
                    f"        params: {base}Params{params_default},",
                    "        *,",
                    "        response_type: ResponseType = ...,",
                    "        timeout: float | None = ...,",
                    "        headers: Mapping[str, str] | None = ...,",
                    "        retries: int | None = ...,",
                    "        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,",
                    f"    ) -> {base}Response: ...",
                ]
            )
        lines.extend(
            [
                "    @overload",
                f"    def {method_name}(",
                "        self,",
                "        operation_id: str,",
                "        params: Mapping[str, Any] | None = ...,",
                "        *,",
                "        response_type: ResponseType = ...,",
                "        timeout: float | None = ...,",
                "        headers: Mapping[str, str] | None = ...,",
                "        retries: int | None = ...,",
                "        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,",
                "    ) -> Any: ...",
            ]
        )
    lines.extend(
        [
            "",
            "VERSION: str",
            "",
            "# Internal helpers reused by the async client; not part of the public API.",
            "def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...",
            "def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...",
            "def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...",
            "def _ensure_request_id(headers: dict[str, str]) -> str: ...",
            "def _header_value(headers: Mapping[str, str], name: str) -> str: ...",
            "def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...",
            "def _validate_response_type(response_type: str) -> ResponseType: ...",
            "def _api_error_class(status: int) -> type[CrawloraError]: ...",
            "def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...",
            "def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...",
            "def _allowed_params(operation_id: str) -> set[str]: ...",
        ]
    )
    return "\n".join(lines) + "\n"


def main():
    if not SPEC_PATH.exists():
        raise SystemExit(f"public OpenAPI spec not found: {SPEC_PATH}")
    spec = json.loads(SPEC_PATH.read_text())
    (ROOT / "openapi").mkdir(exist_ok=True)
    target_spec = ROOT / "openapi" / "public.json"
    if SPEC_PATH.resolve() != target_spec.resolve():
        shutil.copyfile(SPEC_PATH, target_spec)

    model = core.build_model(spec, POLICY)

    # SCREAMING_SNAKE_CASE aliases for every operation id, exposed as a class so
    # editors autocomplete them: client.request(OperationId.BING_SEARCH, {...}).
    const_lines = ["class OperationId:"]
    used_consts = set()
    for operation_id, meta in sorted(model.meta.items(), key=lambda item: item[1]["type_base"]):
        const = "_".join(core.words(meta["type_base"])).upper() or "OPERATION"
        base = const
        i = 2
        while const in used_consts:
            const = f"{base}_{i}"
            i += 1
        used_consts.add(const)
        const_lines.append(f"    {const} = {operation_id!r}")
    content = (
        "# Generated by scripts/generate.py. Do not edit manually.\n"
        f"OPERATIONS = {pprint.pformat(model.operations, sort_dicts=True, width=120)}\n\n"
        f"GROUPS = {pprint.pformat(model.groups, sort_dicts=True, width=120)}\n\n"
        f"OPERATION_COUNT = {model.operation_count}\n\n"
        + "\n".join(const_lines)
        + "\n"
    )
    (ROOT / "crawlora" / "operations.py").write_text(content)
    (ROOT / "crawlora" / "client.pyi").write_text(stub_declarations(model))
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs" / "operations.md").write_text(
        core.operation_docs(model, title="Crawlora Python SDK Operations", type_render=py_type)
    )


if __name__ == "__main__":
    main()
