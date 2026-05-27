# Crawlora Python SDK

Git-installable beta SDK for the public Crawlora API.

## Install

```sh
pip install "git+https://github.com/Crawlora-org/crawlora-python-sdk.git@latest"
```

For reproducible builds, pin the current beta release tag:

```sh
pip install "git+https://github.com/Crawlora-org/crawlora-python-sdk.git@v1.2.0-sdk.8"
```

## Usage

```python
import os
from crawlora import CrawloraClient

crawlora = CrawloraClient(api_key=os.environ["CRAWLORA_API_KEY"])
result = crawlora.bing.search(q="coffee shops", count=10)
print(result)
```

Generated type stubs cover endpoint groups, keyword parameters, enum values,
request options, and response aliases for editors and type checkers.

## Configuration

```python
crawlora = CrawloraClient(
    api_key=os.environ["CRAWLORA_API_KEY"],
    base_url="https://api.crawlora.net/api/v1",
    retries=2,
    retry_delay=0.25,
    headers={"x-client": "example"},
)
```

Per-request options are available through reserved keyword arguments:

```python
text = crawlora.youtube.transcript(
    id="VIDEO_ID",
    format="text",
    _response_type="text",
    _timeout=10,
)
```

API failures raise `CrawloraError` with `status`, optional API `code`, parsed
`body`, `raw_body`, and the underlying transport exception as `__cause__`.

## Examples

Runnable examples live under `examples/`:

```sh
CRAWLORA_API_KEY=... python3 examples/bing_search.py
CRAWLORA_API_KEY=... CRAWLORA_YOUTUBE_VIDEO_ID=... python3 examples/youtube_transcript.py
```

Each example also accepts `CRAWLORA_BASE_URL` for staging or local API testing.
The examples exit without making a request when the required live environment
variables are not set.

## Versioning

This SDK is currently released as Git beta tags. The moving `latest` tag tracks
the current promoted beta, while explicit tags such as `v1.2.0-sdk.8` remain
available for reproducible builds. Pin an explicit tag in production
applications and upgrade intentionally.

## Registry Readiness

The future PyPI package target is `crawlora`, matching the import name:

```sh
pip install crawlora
```

Registry publication is not enabled yet. Until then, install from an explicit
Git beta tag or the moving `latest` tag as shown above.

## Regeneration

The committed `openapi/public.json` is the SDK contract source. Regenerate after
updating that file:

```sh
python3 scripts/generate.py
python3 -m unittest discover -s tests
```

## Optional Live Smoke Test

Default tests use a local mock server. The programs under `examples/` can be
used as optional live smoke tests when `CRAWLORA_API_KEY` is available. Live
calls are not part of default CI.
