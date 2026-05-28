# Crawlora Python SDK

Python client for the public Crawlora API. Use it to call Crawlora scraping,
search, marketplace, media, maps, finance, and usage endpoints with generated
type stubs for editor and type-checker support.

- Runtime: Python 3.10+
- Auth: `x-api-key`
- Default API base URL: `https://api.crawlora.net/api/v1`
- Reference: [operations](docs/operations.md) and [recipes](docs/recipes.md)

## Install

The Python SDK is currently distributed from Git beta tags:

```sh
pip install "git+https://github.com/Crawlora-org/crawlora-python-sdk.git@latest"
```

For reproducible builds, pin a released tag:

```sh
pip install "git+https://github.com/Crawlora-org/crawlora-python-sdk.git@TAG"
```

## API Key

Create or sign in to your Crawlora account at [crawlora.net](https://crawlora.net),
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

The future PyPI package target is also `crawlora`, but registry publication is
not enabled yet. Until then, install from an explicit Git beta tag or the
moving `latest` tag as shown above.
