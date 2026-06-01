# Changelog

## v1.3.0-sdk.1

- Added `AsyncCrawloraClient` for asyncio applications: `await
  client.bing.search(q="coffee")`. It reuses the synchronous client's validation,
  retries, and `Retry-After` handling, running each request in a worker thread so
  the package stays dependency-free.
- Added `CrawloraClientError`, `CrawloraServerError`, and `CrawloraNetworkError`
  subclasses of `CrawloraError` for branching on 4xx vs 5xx vs transport failures.
- Added `client.paginate(operation_id, params)` (and the async equivalent) to
  iterate page/offset endpoints, stopping on an empty page.
- Added the generated `OperationId` constants for typo-safe dynamic operation ids,
  e.g. `client.request(OperationId.BING_SEARCH, {"q": "coffee"})`.
- The generator now shares a single language-neutral core with the Go and
  TypeScript SDKs; generated output is unchanged.

## v1.2.0-sdk.19

- Regenerated the public SDK contract with the promoted Shopify endpoint family.
- Added the generated `shopify` group with 11 active Shopify operations.
- Updated the generated operation reference to 330 public SDK operations.

## v1.2.0-sdk.16

- Documented response headers on `CrawloraError`, case-insensitive header
  overrides, strict response modes, `Retry-After` retries, and timeout wrapping.
- Added docs coverage checks for the release-polish behavior.
- Kept the generated operation contract unchanged.

## v1.2.0-sdk.15

- Added case-insensitive request header overrides across auth, user-agent, and
  content headers.
- Added strict response mode validation, response headers on SDK errors, and
  `Retry-After` aware retry delays capped at 30 seconds.
- Clarified timeout transport wrapping while preserving retry behavior for
  transport failures.

## v1.2.0-sdk.14

- Aligned the promoted SDK beta tag with the JavaScript and Go SDKs.
- Added explicit coverage for request-level header overrides.

## v1.2.0-sdk.12

- Added generated public operation reference docs and usage recipes.
- Included docs in source distributions for easier offline reference.

## v1.2.0-sdk.11

- Added generated `OperationId` literals and overloads so type checkers infer
  dynamic `request` and `operation` responses from literal operation ids.
- Added mypy-backed type-usage coverage for typed dynamic calls.

## v1.2.0-sdk.10

- Generated OpenAPI schema model `TypedDict` definitions and aliases for
  endpoint responses and body parameters.
- Updated typed endpoint stubs to return concrete response aliases while
  keeping runtime call shapes unchanged.

## v1.2.0-sdk.9

- Added fail-fast enum validation for generated query and form parameters.
- Wrapped malformed JSON responses in `CrawloraError` with response status,
  raw body, and parser cause details.

## v1.2.0-sdk.8

- Regenerated from the SDK spec that excludes deprecated endpoints.
- Removed the deprecated Google Lens example and generated SDK surface.

## v1.2.0-sdk.7

- Added fail-fast validation for required query, form, and body parameters.
- Normalized negative retry settings and made JWT auth scheme detection
  case-insensitive.

## v1.2.0-sdk.6

- Added runnable Bing search, YouTube transcript, and Google Lens upload
  examples.
- Documented optional live smoke-test commands without requiring live API
  credentials in default tests.

## v1.2.0-sdk.5

- Prepared the SDK metadata and documentation for future PyPI publishing as
  `crawlora`.
- Kept the import name unchanged and refreshed beta install references.

## v1.2.0-sdk.4

- Added release-readiness files, CI, license, fuller README guidance, and Python
  package metadata.
- Corrected package metadata to Python 3.10+ and kept stubs included in wheels.
- Kept endpoint behavior and generated operation contract unchanged.

## v1.2.0-sdk.3

- Added generated Python type stubs for endpoint groups, keyword parameters,
  enum values, request options, and response aliases.

## v1.2.0-sdk.2

- Improved retries, request options, user agent handling, multipart support,
  response parsing, and SDK error details.

## v1.2.0-sdk.1

- Cleaned public SDK docs to avoid maintainer-only generation details.

## Initial SDK

- Added the first Git-installable Crawlora Python SDK generated from the public
  API contract.
