#!/usr/bin/env python3
import json
import keyword
import os
import pprint
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPEC = ROOT / "openapi" / "public.json"
SPEC_PATH = Path(os.environ.get("CRAWLORA_OPENAPI_SPEC", DEFAULT_SPEC))
TAG_GROUP_OVERRIDES = {
    "AppStore": "app_store",
    "CoinGecko": "coin_gecko",
    "GooglePlay": "google_play",
    "ProductHunt": "product_hunt",
    "SimilarWeb": "similar_web",
    "SpotifyPodcasts": "spotify_podcasts",
    "TikTok": "tiktok",
    "YouTube": "youtube",
}
TAG_PREFIX_OVERRIDES = {
    "AppStore": "appstore",
    "CoinGecko": "coingecko",
    "GooglePlay": "googleplay",
    "ProductHunt": "producthunt",
    "SimilarWeb": "similarweb",
    "SpotifyPodcasts": "spotify-podcasts",
    "TikTok": "tiktok",
    "YouTube": "youtube",
}


def words(value):
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", value)
    return [part for part in re.split(r"[^A-Za-z0-9]+", value.lower()) if part]


def snake(parts):
    return "_".join(parts) or "call"


def alias(operation_id, tag, used):
    op_words = words(operation_id)
    tag_words = words(TAG_PREFIX_OVERRIDES.get(tag, tag))
    if op_words[: len(tag_words)] == tag_words:
        op_words = op_words[len(tag_words) :]
    name = snake(op_words)
    if not name or name in used:
        name = snake(words(operation_id))
    if keyword.iskeyword(name):
        name += "_"
    base = name
    i = 2
    while name in used:
        name = f"{base}_{i}"
        i += 1
    used.add(name)
    return name


def definition(operation_id, method, path, operation):
    params = operation.get("parameters", [])
    security = []
    for requirement in operation.get("security", []):
        security.extend(requirement.keys())
    return {
        "id": operation_id,
        "method": method.upper(),
        "path": path,
        "pathParams": [p["name"] for p in params if p.get("in") == "path"],
        "queryParams": [
            {
                "name": p["name"],
                "in": "query",
                **({"collectionFormat": p["collectionFormat"]} if "collectionFormat" in p else {}),
                **({"type": p["type"]} if "type" in p else {}),
                **({"required": True} if p.get("required") else {}),
                **({"enum": enum_values(p)} if enum_values(p) else {}),
            }
            for p in params
            if p.get("in") == "query"
        ],
        "formParams": [
            {
                "name": p["name"],
                "in": "formData",
                **({"type": p["type"]} if "type" in p else {}),
                **({"required": True} if p.get("required") else {}),
                **({"enum": enum_values(p)} if enum_values(p) else {}),
            }
            for p in params
            if p.get("in") == "formData"
        ],
        "bodyParam": next((p["name"] for p in params if p.get("in") == "body"), None),
        "bodyRequired": any(p.get("in") == "body" and p.get("required") for p in params),
        "consumes": operation.get("consumes", []),
        "produces": operation.get("produces", []),
        "security": security,
    }


def enum_values(param):
    return [str(value) for value in (param.get("enum") or param.get("items", {}).get("enum") or [])]


def type_name(*parts):
    return "".join(part[:1].upper() + part[1:] for part in words("-".join(parts))) or "Operation"


def schema_type_name(value):
    return "Model" + type_name(value)


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


def stub_declarations(groups, operation_meta):
    lines = [
        "from __future__ import annotations",
        "",
        "import sys",
        "from typing import Any, Callable, Literal, Mapping",
        "",
        "if sys.version_info >= (3, 11):",
        "    from typing import NotRequired, Required, TypedDict, Unpack",
        "else:",
        "    from typing_extensions import NotRequired, Required, TypedDict, Unpack",
        "",
        'ResponseType = Literal["auto", "json", "text"]',
        "",
        "class CrawloraError(Exception):",
        "    status: int",
        "    code: int | None",
        "    body: Any",
        "    raw_body: str",
        "",
        "class _RequestOptions(TypedDict, total=False):",
        "    _response_type: ResponseType",
        "    _timeout: float",
        "    _headers: Mapping[str, str]",
        "",
    ]
    for schema_name, schema in operation_meta["definitions"].items():
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
    for operation_id, meta in operation_meta.items():
        if operation_id == "definitions":
            continue
        base = meta["typeBase"]
        if meta["bodyType"] != "Any":
            lines.append(f"{base}Body = {meta['bodyType']}")
        lines.append(f"{base}Response = {meta['responseType']}")
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
    for group_name, methods in groups.items():
        lines.append(f"class {type_name(group_name, 'group')}:")
        if not methods:
            lines.append("    pass")
        for method_name, operation_id in methods.items():
            base = operation_meta[operation_id]["typeBase"]
            lines.append(f"    def {method_name}(self, **params: Unpack[{base}Params]) -> {base}Response: ...")
        lines.append("")
    lines.append("class CrawloraClient:")
    for group_name in groups:
        lines.append(f"    {group_name}: {type_name(group_name, 'group')}")
    lines.extend(
        [
            "    def __init__(",
            "        self,",
            "        *,",
            "        api_key: str | None = ...,",
            "        jwt_token: str | None = ...,",
            "        base_url: str = ...,",
            "        timeout: float = ...,",
            "        retries: int = ...,",
            "        retry_delay: float = ...,",
            "        headers: Mapping[str, str] | None = ...,",
            "        user_agent: str | None = ...,",
            "        transport: Callable[..., Any] | None = ...,",
            "    ) -> None: ...",
            "    def operation(",
            "        self,",
            "        operation_id: str,",
            "        params: Mapping[str, Any] | None = ...,",
            "        *,",
            "        response_type: ResponseType = ...,",
            "        timeout: float | None = ...,",
            "        headers: Mapping[str, str] | None = ...,",
            "    ) -> Any: ...",
            "    def request(",
            "        self,",
            "        operation_id: str,",
            "        params: Mapping[str, Any] | None = ...,",
            "        *,",
            "        response_type: ResponseType = ...,",
            "        timeout: float | None = ...,",
            "        headers: Mapping[str, str] | None = ...,",
            "    ) -> Any: ...",
            "",
            "VERSION: str",
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

    operations = {}
    groups = {}
    operation_meta = {}
    used_by_group = {}
    for path, methods in sorted(spec["paths"].items()):
        for method, operation in sorted(methods.items()):
            operation_id = operation["operationId"]
            tag = (operation.get("tags") or ["default"])[0]
            group_name = TAG_GROUP_OVERRIDES.get(tag, snake(words(tag)))
            groups.setdefault(group_name, {})
            used_by_group.setdefault(group_name, set())
            method_name = alias(operation_id, tag, used_by_group[group_name])
            groups[group_name][method_name] = operation_id
            operations[operation_id] = definition(operation_id, method, path, operation)
            params = operation.get("parameters", [])
            body_schema = next((p.get("schema") for p in params if p.get("in") == "body"), None)
            response_schema = operation.get("responses", {}).get("200", {}).get("schema")
            operation_meta[operation_id] = {
                "typeBase": type_name(group_name, method_name),
                "params": [p for p in params if p.get("in") in {"path", "query", "formData", "body"}],
                "bodyType": py_schema_type(body_schema),
                "responseType": py_schema_type(response_schema),
            }
    operation_meta["definitions"] = spec.get("definitions", {})

    content = (
        "# Generated by scripts/generate.py. Do not edit manually.\n"
        f"OPERATIONS = {pprint.pformat(operations, sort_dicts=True, width=120)}\n\n"
        f"GROUPS = {pprint.pformat(groups, sort_dicts=True, width=120)}\n\n"
        f"OPERATION_COUNT = {sum(len(methods) for methods in spec['paths'].values())}\n"
    )
    (ROOT / "crawlora" / "operations.py").write_text(content)
    (ROOT / "crawlora" / "client.pyi").write_text(stub_declarations(groups, operation_meta))


if __name__ == "__main__":
    main()
