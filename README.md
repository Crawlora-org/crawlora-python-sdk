# Crawlora Python SDK

Git-installable beta SDK for the public Crawlora API.

## Install

```sh
pip install "git+https://github.com/Crawlora-org/crawlora-python-sdk.git@v1.2.0-sdk.4"
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

Multipart upload endpoints accept bytes, file paths, or file-like objects:

```python
result = crawlora.google.lens(image=b"image-bytes")
```

API failures raise `CrawloraError` with `status`, optional API `code`, parsed
`body`, `raw_body`, and the underlying transport exception as `__cause__`.

## Versioning

This SDK is currently released as Git beta tags. Pin an explicit tag in
applications and upgrade intentionally.

## Regeneration

The committed `openapi/public.json` is the SDK contract source. Regenerate after
updating that file:

```sh
python3 scripts/generate.py
python3 -m unittest discover -s tests
```

## Optional Live Smoke Test

Default tests use a local mock server. For live API checks, set
`CRAWLORA_API_KEY` in your own environment and call a low-cost endpoint
manually. Live calls are not part of default CI.
