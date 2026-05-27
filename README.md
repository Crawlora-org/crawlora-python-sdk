# Crawlora Python SDK

Git-only beta SDK for the public Crawlora API.

## Install

```sh
pip install "git+https://github.com/Crawlora-org/crawlora-python-sdk.git@v1.2.0-sdk.3"
```

## Usage

```python
from crawlora import CrawloraClient

crawlora = CrawloraClient(api_key="...")
result = crawlora.bing.search(q="coffee shops", count=10)
```

Generated type stubs cover endpoint groups, keyword parameters, enum values,
request options, and response aliases for editors and type checkers.

## Configuration

```python
import os
from crawlora import CrawloraClient

crawlora = CrawloraClient(
    api_key=os.environ["CRAWLORA_API_KEY"],
    base_url="https://api.crawlora.net/api/v1",
    retries=2,
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
