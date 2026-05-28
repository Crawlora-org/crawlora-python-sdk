# Crawlora Python SDK Recipes

## Authentication

```python
crawlora = CrawloraClient(api_key=os.environ["CRAWLORA_API_KEY"])
```

Self-service account endpoints can use JWT auth:

```python
crawlora = CrawloraClient(jwt_token=os.environ["CRAWLORA_JWT_TOKEN"])
```

## Typed Endpoint Stubs

```python
result = crawlora.bing.search(q="coffee shops", count=10)
result["data"]["results"][0]["title"]
```

## Typed Dynamic Operations

```python
result = crawlora.request("bing-search", {"q": "coffee shops"})
result["data"]["results"][0]["title"]
```

Literal operation ids infer response aliases in type checkers. Use grouped
endpoint methods for ordinary app code and dynamic operation calls when your app
stores operation ids in configuration, queues, or jobs.

## Retries, Timeouts, And Headers

```python
crawlora = CrawloraClient(
    api_key=os.environ["CRAWLORA_API_KEY"],
    retries=2,
    retry_delay=0.25,
    headers={"x-client": "example"},
)

result = crawlora.bing.search(q="coffee shops", _timeout=10)
```

## Text Responses

```python
text = crawlora.youtube.transcript(
    id="VIDEO_ID",
    format="text",
    _response_type="text",
)
```

## Errors

```python
try:
    crawlora.bing.search(q="coffee shops")
except CrawloraError as error:
    print(error.status, error.code, error.raw_body)
```

## Optional Live Smoke Tests

```sh
CRAWLORA_API_KEY=... python3 examples/bing_search.py
CRAWLORA_API_KEY=... CRAWLORA_YOUTUBE_VIDEO_ID=... python3 examples/youtube_transcript.py
```
