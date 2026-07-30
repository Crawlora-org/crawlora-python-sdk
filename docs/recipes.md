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
post_with_metrics = crawlora.reddit.post(id="1v8hy3q", include_metrics=True)
comments_with_metrics = crawlora.reddit.comments(id="1v8hy3q", include_metrics=True, limit=25)
brand = crawlora.brand.retrieve(domain="stripe.com")
```

Omit `include_metrics` for the 1-credit feed mode. Set it to `True` for the
3-credit anonymous HTML mode with public post and comment engagement metrics.

## Company Job Searches

Search public job listings directly from employer career sites:

```python
amazon = crawlora.amazon_jobs.search(q="software engineer", country="US")
apple = crawlora.apple_jobs.search(q="machine learning", location="United States")
google = crawlora.google_jobs.search(q="data scientist", location="Singapore")
meta = crawlora.meta_jobs.search(q="product manager", is_remote_only=True)
tesla = crawlora.tesla_jobs.list(query="manufacturing", location="Texas")
```

## Threads Public Lookups

```python
profile = crawlora.threads.profile(username="zuck")
post = crawlora.threads.post(username="zuck", code="DakyAavlKLZ")
results = crawlora.threads.search(q="openai")
posts = crawlora.threads.profile_posts(username="zuck")
replies = crawlora.threads.post_replies(username="zuck", code="DakyAavlKLZ")
```

## Box Office Mojo Dataset

Search theatrical box-office records, fetch one title, and facet the same filter set.

```python
titles = crawlora.datasets.boxofficemojo_search(q="avatar", sort="worldwide_desc")
avatar = crawlora.datasets.boxofficemojo_item(title_id="tt0499549")
years = crawlora.datasets.boxofficemojo_facets(facet="years_active", gross_band="over_1b")
```

## Software, Reviews, And Market Datasets

Build a Chrome extension competitive-intelligence view without downloading the
whole catalog: create a high-adoption shortlist, load chart-ready market
metrics, watch movers, and audit permission changes or one item's history.

```python
extensions = crawlora.datasets.chrome_extensions_search(q="productivity", min_users=10000, sort="users_desc", page_size=20)
metrics = crawlora.datasets.chrome_extensions_metrics(days=30, limit=10)
movers = crawlora.datasets.chrome_extensions_trending(item_type="extension", page_size=20)
permission_changes = crawlora.datasets.chrome_extensions_changes(change_type="permissions", limit=25)
history = crawlora.datasets.chrome_extensions_history(id="fjgncogppolhfdpijihbpfmeohpaadpc", limit=90)

cities = crawlora.datasets.numbeo_cities_search(country="Portugal", sort="quality_of_life_desc")
software = crawlora.capterra.search(q="project management")
games = crawlora.metacritic.browse(type="game", sort="score")
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
