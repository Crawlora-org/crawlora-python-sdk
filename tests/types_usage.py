from crawlora import CrawloraClient
from crawlora.client import BingSearchResponse, GoogleSearchBody, GoogleSearchResponse

client = CrawloraClient(api_key="api_test")

search_response: BingSearchResponse = client.request("bing-search", {"q": "coffee"})
search_response["data"]["results"][0]["title"].upper()

search_body: GoogleSearchBody = {
    "country": "us",
    "keyword": "coffee",
    "language": "en",
}

google_response: GoogleSearchResponse = client.operation("google-search", {"searchOption": search_body})
google_response["data"]["result"][0]["title"].upper()
