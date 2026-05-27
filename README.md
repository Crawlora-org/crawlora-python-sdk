# Crawlora Python SDK

Git-only beta SDK for the public Crawlora API.

## Install

```sh
pip install "git+https://github.com/crawlora/crawlora-python-sdk.git@v1.2.0-sdk.1"
```

## Usage

```python
from crawlora import CrawloraClient

crawlora = CrawloraClient(api_key="...")
result = crawlora.bing.search(q="coffee shops", count=10)
```

Run `python3 scripts/generate.py` after updating `../webscraping-api/dist/openapi.public.json`.
