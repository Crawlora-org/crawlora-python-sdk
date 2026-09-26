from crawlora import CrawloraClient
from crawlora.client import BingSearchResponse, WebEmailVerifyBody, WebEmailVerifyResponse

client = CrawloraClient(api_key="api_test")

search_response: BingSearchResponse = client.request("bing-search", {"q": "coffee"})
search_response["data"]["results"][0]["title"].upper()

email_verify_body: WebEmailVerifyBody = {
    "emails": ["jane@example.com"],
}

email_verify_response: WebEmailVerifyResponse = client.operation("email-verify", {"option": email_verify_body})
email_verify_response["data"]["results"][0]["email"].upper()
