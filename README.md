# Crawlora Python SDK

Python client for the public Crawlora API. Use it to call Crawlora scraping,
search, social, developer, marketplace, datasets, reviews, travel, media, books,
maps, finance, prediction-market, brand, and usage endpoints
with generated type stubs for editor and type-checker support.

- Runtime: Python 3.10+
- Auth: `x-api-key`
- Default API base URL: `https://api.crawlora.net/api/v1`
- Reference: [operations](docs/operations.md) and [recipes](docs/recipes.md)

## Install

Published on [PyPI](https://pypi.org/project/crawlora/). The current release is a
prerelease (`1.18.0.dev1`), so install it with `--pre`:

```sh
pip install --pre crawlora
```

(Git installs from beta tags also work, e.g.
`pip install "git+https://github.com/Crawlora-org/crawlora-python-sdk.git@latest"`.)

## API Key

Create or sign in to your Crawlora account at [crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-python-sdk),
then create an API key in the dashboard.

```sh
read -r CRAWLORA_API_KEY
export CRAWLORA_API_KEY
```

## First Request

```python
import os
from crawlora import CrawloraClient

crawlora = CrawloraClient(api_key=os.environ["CRAWLORA_API_KEY"])

response = crawlora.bing.search(
    q="coffee shops",
    count=10,
)

print(response["data"]["results"][0])
```

Endpoint groups are generated from the public API contract, so common calls are
available as methods such as `crawlora.bing.search(...)`,
`crawlora.youtube.transcript(...)`, and `crawlora.google.map_search(...)`.

## Typed Dynamic Calls

You can also call by operation id. Literal operation ids are covered by the
generated `.pyi` stubs, so type checkers can infer the matching parameter and
response aliases:

```python
response = crawlora.request("bing-search", {
    "q": "coffee shops",
    "count": 10,
})
```

Generated stubs include operation ids, endpoint groups, keyword parameters,
enum values, response aliases, and reserved request options.

## Configuration

```python
crawlora = CrawloraClient(
    api_key=os.environ["CRAWLORA_API_KEY"],
    base_url="https://api.crawlora.net/api/v1",
    timeout=30,
    retries=2,
    retry_delay=0.25,
    headers={"x-client": "my-app"},
)
```

Per-request options are available through reserved keyword arguments. Header
names are matched case-insensitively, so request headers can override default
auth, user-agent, and content headers without duplicating variants such as
`x-api-key` and `X-API-KEY`:

```python
response = crawlora.bing.search(
    q="coffee shops",
    _timeout=10,
    _headers={"x-request-id": "search-001"},
)
```

## Text Responses

Most endpoints return JSON. `_response_type` must be `auto`, `json`, or
`text`. Endpoints that support alternate text output, such as YouTube
transcripts, can opt into text mode:

```python
transcript = crawlora.youtube.transcript(
    id="VIDEO_ID",
    format="text",
    _response_type="text",
)

print(transcript)
```

## Errors

Failed API calls raise `CrawloraError`:

```python
from crawlora import CrawloraError

try:
    crawlora.bing.search(q="coffee shops")
except CrawloraError as error:
    print(error.status, error.code, error.body)
    raise
```

The error includes `status`, optional API `code`, parsed `body`, `raw_body`,
response `headers`, and the underlying parser or transport exception as
`__cause__` when available. Retryable responses honor positive `Retry-After`
headers, capped at 30 seconds. Timeout-like transport failures use the
`Crawlora request timed out` SDK message.

`CrawloraError` has three subclasses for branching on the failure kind:
`CrawloraClientError` (4xx, request rejected), `CrawloraServerError` (5xx), and
`CrawloraNetworkError` (transport failure or timeout before a response).

## Async

`AsyncCrawloraClient` mirrors the synchronous client for asyncio applications:

```python
from crawlora import AsyncCrawloraClient

crawlora = AsyncCrawloraClient(api_key="YOUR_API_KEY")
result = await crawlora.bing.search(q="coffee shops")
```

It reuses the same validation, retries, and `Retry-After` handling, running each
request in a worker thread so the package stays dependency-free.

## Pagination

`client.paginate` yields successive pages, advancing the page/offset query
parameter and stopping when a page returns no data:

```python
for page in crawlora.paginate("ebay-seller-feedback", {"seller": "acme"}):
    for review in page["data"]:
        print(review)
```

`AsyncCrawloraClient.paginate` is the `async for` equivalent. Override detection
with `page_param`, `start`, `step`, and `max_pages`.

## Examples

Runnable examples live under `examples/` and skip cleanly when required
environment variables are missing:

```sh
python3 examples/bing_search.py
python3 examples/youtube_transcript.py
```

Set `CRAWLORA_BASE_URL` to point examples at a staging or local API.

## Package Notes

The import name is `crawlora`:

```python
from crawlora import CrawloraClient
```

The package is published on [PyPI](https://pypi.org/project/crawlora/) as
`crawlora` (a prerelease — `pip install --pre crawlora`). Git beta tags and the
moving `latest` tag also work, as shown above.
