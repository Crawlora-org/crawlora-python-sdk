import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from crawlora import CrawloraClient


class Handler(BaseHTTPRequestHandler):
    calls = []
    response_body = {"code": 200, "msg": "OK", "data": {"ok": True}}
    content_type = "application/json"

    def do_GET(self):
        self.__class__.calls.append({"path": self.path, "headers": dict(self.headers)})
        body = self.response_body
        if isinstance(body, str):
            payload = body.encode()
        else:
            payload = json.dumps(body).encode()
        self.send_response(200)
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
        Handler.content_type = "application/json"

    def test_api_key_auth_and_query_params(self):
        client = CrawloraClient(api_key="api_test", base_url=self.base_url)
        response = client.bing.search(q="coffee", count=3)

        self.assertTrue(response["data"]["ok"])
        self.assertEqual(Handler.calls[0]["path"], "/api/v1/bing/search?q=coffee&count=3")
        self.assertEqual(Handler.calls[0]["headers"]["X-Api-Key"], "api_test")

    def test_jwt_auth(self):
        client = CrawloraClient(jwt_token="jwt_test", base_url=self.base_url)
        client.user.me()

        self.assertEqual(Handler.calls[0]["headers"]["Authorization"], "Token jwt_test")

    def test_text_response(self):
        Handler.response_body = "hello"
        Handler.content_type = "text/plain"
        client = CrawloraClient(api_key="api_test", base_url=self.base_url)

        self.assertEqual(client.youtube.transcript(id="abc123", format="text"), "hello")


if __name__ == "__main__":
    unittest.main()
