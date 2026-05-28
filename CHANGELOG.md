# Changelog

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
