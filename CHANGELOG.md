# Changelog

## v1.10.0-sdk.1

- Regenerated from the public API contract (525 to 529 operations). Adds the
  **Airbnb Markets dataset** (4 endpoints): aggregate short-term-rental market
  statistics -- listing supply, Superhost share, ratings, and nightly-price bands
  -- rolled up by country, metro, and geo cell (search, item lookup, facets, and
  nearby density). Aggregate-only: no individual listings or hosts.

## v1.9.0-sdk.1

- Regenerated from the public API contract (499 to 525 operations). Adds four
  platforms/families to the client:
  - **GitHub** (16 endpoints): organizations, repositories (contributors,
    forks, languages, releases, stargazers), user profiles/events/pinned/repos,
    repository and user search, and trending repositories/developers.
  - **GitHub Users dataset** (4): search, facets, nearby, and item lookup.
  - **X** (3): post, profile, and profile posts.
  - **Apps datasets** (3): apps, apps-charts, and apps-reviews search.
  - **Creators dataset** (1): TikTok creators search.
- Removes the retired tiktok popular-trend/creator operation.

## v1.8.0-sdk.2

- Regenerated from the public API contract (499 operations, unchanged). Enriches
  the Web `antibot-check` diagnostic response with additional fields:
  `block_reason`, `block_detail`, `auth_required`, `captcha_type`,
  `captcha_types`, `captcha_mode`, `confidence_score`, `custom_vm`, and
  `vm_vendor`.
- Clarified the `google-search` and datasets `google-map-businesses/search`
  endpoint descriptions (wording only; no behavior change).

## v1.8.0-sdk.1

- Added two new platforms, regenerated from the public API contract (now 499
  operations): **Redfin** (real-estate `search`, `property`, `estimate`,
  `region-trends`, `similar`) and **Web** (generic `web-scrape`, `contact`, and
  the `antibot-check` diagnostic).
- Refreshed response schemas: `contact` gains `crawl_status`, `web-scrape` gains
  `cache_state`/`cached_at`/`max_age`, and the Spotify country-hub responses gain
  `partialErrors`.

## v1.7.0-sdk.1

- Added six new platforms, regenerated from the public API contract (now 491
  operations): **Polymarket**, **Kalshi**, and **Metaculus** (prediction
  markets); **IMDb**, **Rotten Tomatoes**, and **Box Office Mojo** (film/TV).
- Expanded **Reddit**: subreddit about/comments, multi-subreddit posts,
  domain posts, user posts/comments, and trends.

## v1.6.0-sdk.1

- Added the **Reddit** platform (`reddit.search`, `reddit.post`,
  `reddit.comments`, `reddit.subreddit_posts`) and the **Brand** platform
  (`brand.retrieve`), plus Yahoo Finance `yahoo_finance.lookup`. Regenerated from
  the public API contract.

## v1.5.0-sdk.1

- Added `before_request`/`after_response` middleware hooks (sync + async).
- Added opt-in `idempotency_keys` (stable `Idempotency-Key` on POST/PATCH, reused
  across retries) and per-request `retries`/`retry_predicate` overrides.
- Added client-side `rate_limit` (requests/sec) and `max_concurrency` throttling
  (sync + async).
- The sync client now uses a keep-alive connection pool by default and is a
  context manager (`with CrawloraClient(...) as client:` / `close()`).
- Grouped operation calls (`client.bing.search(...)`) now raise `TypeError` on
  unknown keyword arguments instead of silently dropping them.

## v1.4.0-sdk.1

- True async transport: `pip install crawlora[async]` makes `AsyncCrawloraClient`
  use `httpx.AsyncClient`; without it, it falls back to the thread-based path.
  Added `aclose()` and async context-manager support.
- Configurable retries: `max_retry_delay`, `retry_statuses`, and a
  `retry_predicate`; added an `on_retry` hook, opt-in `request_id` (x-request-id,
  also on `error.request_id`), and a `logger` event sink.
- Pagination: cursor/token mode (`cursor_param` + `next_cursor`) and a
  `paginate_items` per-item iterator (sync + async); operation metadata now
  exposes `paginatable` and `cursorParams`.
- Streaming: `response_type="stream"` returns a file-like body.
- Config: `CRAWLORA_API_KEY` / `CRAWLORA_BASE_URL` environment fallback.

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
