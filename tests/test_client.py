import json
import threading
import unittest
from pathlib import Path
from urllib.error import URLError
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from crawlora import OPERATION_COUNT, CrawloraClient, CrawloraError


class Handler(BaseHTTPRequestHandler):
    calls = []
    response_body = {"code": 200, "msg": "OK", "data": {"ok": True}}
    content_type = "application/json"

    def do_GET(self):
        self.__class__.calls.append({"path": self.path, "headers": dict(self.headers)})
        self._write_response()

    def do_POST(self):
        body = self.rfile.read(int(self.headers.get("content-length", "0") or "0"))
        self.__class__.calls.append({"path": self.path, "headers": dict(self.headers), "body": body})
        self._write_response()

    def _write_response(self):
        body = self.response_body
        if isinstance(body, str):
            payload = body.encode()
        else:
            payload = json.dumps(body).encode()
        status = getattr(self, "response_status", 200)
        self.send_response(status)
        self.send_header("content-type", self.content_type)
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, *_args):
        return


class CrawloraClientTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}/api/v1"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.thread.join(timeout=2)

    def setUp(self):
        Handler.calls = []
        Handler.response_body = {"code": 200, "msg": "OK", "data": {"ok": True}}
        Handler.response_status = 200
        Handler.content_type = "application/json"

    def test_api_key_auth_and_query_params(self):
        client = CrawloraClient(api_key="api_test", base_url=self.base_url)
        response = client.bing.search(q="coffee", count=3)

        self.assertTrue(response["data"]["ok"])
        self.assertEqual(Handler.calls[0]["path"], "/api/v1/bing/search?q=coffee&count=3")
        self.assertEqual(Handler.calls[0]["headers"]["X-Api-Key"], "api_test")
        self.assertTrue(Handler.calls[0]["headers"]["User-Agent"].startswith("crawlora-python-sdk/"))

    def test_jwt_auth(self):
        client = CrawloraClient(jwt_token="jwt_test", base_url=self.base_url)
        client.user.me()

        self.assertEqual(Handler.calls[0]["headers"]["Authorization"], "Token jwt_test")

    def test_text_response(self):
        Handler.response_body = "hello"
        Handler.content_type = "text/plain"
        client = CrawloraClient(api_key="api_test", base_url=self.base_url)

        self.assertEqual(client.youtube.transcript(id="abc123", format="text"), "hello")

    def test_custom_headers_false_zero_and_arrays(self):
        client = CrawloraClient(api_key="api_test", base_url=self.base_url)
        client.request(
            "datasets-google-map-businesses-search",
            {"q": "coffee", "page": 0, "has_website": False},
            headers={"x-test": "yes"},
        )

        self.assertIn("page=0", Handler.calls[0]["path"])
        self.assertIn("has_website=false", Handler.calls[0]["path"])
        self.assertEqual(Handler.calls[0]["headers"]["X-Test"], "yes")

        client.request("tripadvisor-search", {"q": "hotel", "amenities": [1, 2], "online_options": ["3", "4"]})
        self.assertIn("amenities=1", Handler.calls[1]["path"])
        self.assertIn("amenities=2", Handler.calls[1]["path"])
        self.assertIn("online_options=3", Handler.calls[1]["path"])
        self.assertIn("online_options=4", Handler.calls[1]["path"])

    def test_json_body(self):
        client = CrawloraClient(api_key="api_test", base_url=self.base_url)
        client.google.search(searchOption={"q": "coffee"})

        self.assertEqual(Handler.calls[0]["body"], b'{"q": "coffee"}')
        self.assertEqual(Handler.calls[0]["headers"]["Content-Type"], "application/json")

    def test_multipart_upload(self):
        client = CrawloraClient(api_key="api_test", base_url=self.base_url)
        client.google.lens(image=b"image-bytes")

        self.assertIn("multipart/form-data", Handler.calls[0]["headers"]["Content-Type"])
        self.assertIn(b"image-bytes", Handler.calls[0]["body"])

    def test_api_error(self):
        Handler.response_status = 429
        Handler.response_body = {"code": 429, "msg": "rate limited"}
        client = CrawloraClient(api_key="api_test", base_url=self.base_url)

        with self.assertRaises(CrawloraError) as raised:
            client.bing.search(q="coffee")

        self.assertEqual(raised.exception.status, 429)
        self.assertEqual(raised.exception.code, 429)
        self.assertEqual(str(raised.exception), "rate limited")
        self.assertIn("rate limited", raised.exception.raw_body)

    def test_retries_retryable_status(self):
        calls = {"count": 0}

        def transport(request, timeout):
            calls["count"] += 1
            if calls["count"] == 1:
                return type("Response", (), {
                    "status": 503,
                    "headers": {"content-type": "application/json"},
                    "body": b'{"code":503,"msg":"try again"}',
                })()
            return type("Response", (), {
                "status": 200,
                "headers": {"content-type": "application/json"},
                "body": b'{"code":200,"msg":"OK","data":{"ok":true}}',
            })()

        client = CrawloraClient(api_key="api_test", base_url=self.base_url, retries=1, retry_delay=0, transport=transport)
        self.assertTrue(client.bing.search(q="coffee")["data"]["ok"])
        self.assertEqual(calls["count"], 2)

    def test_transport_error_is_wrapped(self):
        cause = URLError("socket closed")

        def transport(_request, _timeout):
            raise cause

        client = CrawloraClient(api_key="api_test", base_url=self.base_url, transport=transport)

        with self.assertRaises(CrawloraError) as raised:
            client.bing.search(q="coffee")

        self.assertEqual(raised.exception.status, 0)
        self.assertIs(raised.exception.__cause__, cause)

    def test_operation_metadata_count(self):
        self.assertEqual(OPERATION_COUNT, 318)

    def test_generated_stub_includes_typed_endpoint_groups(self):
        stub = Path(__file__).resolve().parents[1].joinpath("crawlora", "client.pyi").read_text()
        self.assertIn("BingSearchParams = TypedDict", stub)
        self.assertIn("'q': Required[str]", stub)
        self.assertIn("'count': NotRequired[int]", stub)
        self.assertIn("GoogleSearchBody = dict[str, Any]", stub)
        self.assertIn("def search(self, **params: Unpack[BingSearchParams]) -> BingSearchResponse: ...", stub)
        self.assertIn("class CrawloraClient:", stub)


if __name__ == "__main__":
    unittest.main()
