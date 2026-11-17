from crawlora import CrawloraClient
from crawlora.client import BingSearchResponse, WebEmailVerifyBody, WebEmailVerifyResponse

client = CrawloraClient(api_key="api_test")

search_response: BingSearchResponse = client.request("bing-search", {"q": "coffee"})
assert "data" in search_response
assert "results" in search_response["data"]
assert "title" in search_response["data"]["results"][0]
search_response["data"]["results"][0]["title"].upper()

email_verify_body: WebEmailVerifyBody = {
    "emails": ["jane@example.com"],
}

email_verify_response: WebEmailVerifyResponse = client.operation("email-verify", {"option": email_verify_body})
assert "data" in email_verify_response
assert "results" in email_verify_response["data"]
assert "address" in email_verify_response["data"]["results"][0]
email_verify_response["data"]["results"][0]["address"].upper()
