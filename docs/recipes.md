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

## Reddit And Brand

Newer platforms are grouped like every other endpoint:

```python
posts = crawlora.reddit.search(q="python", subreddit="programming")
brand = crawlora.brand.retrieve(domain="stripe.com")
```

## Airbnb Host Profiles

Look up a public Airbnb host, then page through their listings and guest reviews.

```python
host = crawlora.airbnb.host(id="65056940")
listings = crawlora.airbnb.host_listings(id="65056940", page=1)
reviews = crawlora.airbnb.host_reviews(id="65056940", page=1)
```



## Airbnb Markets Dataset

Aggregate Airbnb short-term-rental market data — listing supply, ratings and nightly-price bands rolled up by country, metro and geo cell. Aggregate-only.

```python
markets = crawlora.datasets.airbnb_markets_search(group_by="country", sort="listings_desc")
fr = crawlora.datasets.airbnb_markets_item(country="FR")
density = crawlora.datasets.airbnb_markets_nearby(lat=48.86, lon=2.35, radius_m=5000)
```

## Airbnb Markets Dataset

Aggregate Airbnb short-term-rental market data — listing supply, ratings and nightly-price bands rolled up by country, metro and geo cell. Aggregate-only.

```python
markets = crawlora.datasets.airbnb_markets_search(group_by="country", sort="listings_desc")
fr = crawlora.datasets.airbnb_markets_item(country="FR")
density = crawlora.datasets.airbnb_markets_nearby(lat=48.86, lon=2.35, radius_m=5000)
```

## TrustMRR Verified Startup Revenues

Browse verified startup revenues and the acquisition marketplace on TrustMRR: the marketplace snapshot, the revenue leaderboard, startup detail, and categories.

```python
deals = client.trust_mrr.trustmrr_marketplace()
board = client.trust_mrr.trustmrr_leaderboard(metric="mrr")
startup = client.trust_mrr.trustmrr_startup(slug="stan")
cats = client.trust_mrr.trustmrr_categories()
saas = client.trust_mrr.trustmrr_category(slug="saas")
```

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

Request headers override default auth, user-agent, and content headers
case-insensitively. Retryable API responses honor positive `Retry-After`
headers, capped at 30 seconds.

## Text Responses

`_response_type` must be `auto`, `json`, or `text`.

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
    print(error.status, error.code, error.raw_body, error.headers)
```

## Custom Retries And Observability

```python
crawlora = CrawloraClient(
    retries=3,
    max_retry_delay=10.0,
    retry_statuses=[429, 503],                          # or:
    retry_predicate=lambda status, error: status >= 500,
    on_retry=lambda attempt, error, delay: print("retry", attempt, error.status),
    request_id=True,                                    # sets x-request-id; available as error.request_id
    logger=lambda event: print(event),
)
```

Branch on `CrawloraClientError` (4xx), `CrawloraServerError` (5xx), and
`CrawloraNetworkError` (transport).

## Async

```python
from crawlora import AsyncCrawloraClient  # pip install crawlora[async] for true async

async with AsyncCrawloraClient(api_key="...") as crawlora:
    result = await crawlora.bing.search(q="coffee")
    async for item in crawlora.paginate_items("ebay-seller-feedback", {"seller": "acme"}):
        ...
```

## Pagination

```python
# page/offset (auto-detected)
for page in crawlora.paginate("ebay-seller-feedback", {"seller": "acme"}):
    ...

# per-item iteration
for item in crawlora.paginate_items("ebay-seller-feedback", {"seller": "acme"}):
    ...

# cursor/token pagination
for page in crawlora.paginate("producthunt-leaderboard", cursor_param="cursor", next_cursor=lambda p: p.get("next_cursor")):
    ...
```

## Streaming Responses

```python
stream = crawlora.request("bing-search", {"q": "coffee"}, response_type="stream")
data = stream.read()  # file-like; AsyncCrawloraClient with httpx streams incrementally
```

## Environment Variables

`CRAWLORA_API_KEY` and `CRAWLORA_BASE_URL` are used when not set explicitly
(precedence: argument > env > default).

## Middleware

```python
crawlora = CrawloraClient(
    before_request=lambda ctx: ctx["headers"].__setitem__("x-signature", sign(ctx)),
    after_response=lambda op, status, headers, body: body,  # return a value to transform
)
```

## Idempotency And Per-Request Retries

```python
crawlora = CrawloraClient(idempotency_keys=True)  # stable key on POST/PATCH retries

crawlora.request("bing-search", {"q": "coffee"}, retries=5, retry_predicate=lambda status, err: status >= 500)
```

## Rate Limiting And Pooling

```python
# <= 10 requests/sec, <= 4 in flight; keep-alive pool by default
with CrawloraClient(rate_limit=10, max_concurrency=4) as crawlora:
    crawlora.bing.search(q="coffee")
```

## Optional Live Smoke Tests

```sh
CRAWLORA_API_KEY=... python3 examples/bing_search.py
CRAWLORA_API_KEY=... CRAWLORA_YOUTUBE_VIDEO_ID=... python3 examples/youtube_transcript.py
```
