import asyncio
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from crawlora import (
    AsyncCrawloraClient,
    CrawloraClient,
    CrawloraClientError,
    CrawloraError,
    CrawloraNetworkError,
    CrawloraServerError,
    OperationId,
)


class Handler(BaseHTTPRequestHandler):
    calls = []
    status = 200
    body = {"code": 200, "msg": "OK", "data": {"ok": True}}

    def do_GET(self):
        self.__class__.calls.append(self.path)
        payload = self.body if isinstance(self.body, str) else json.dumps(self.body)
        self.send_response(self.status)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(payload.encode())

    do_POST = do_GET

    def log_message(self, *_args):
        return


class W2FeaturesTest(unittest.TestCase):
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
        Handler.status = 200
        Handler.body = {"code": 200, "msg": "OK", "data": {"ok": True}}

    def client(self):
        return CrawloraClient(api_key="api_test", base_url=self.base_url)

    def test_operation_id_constants(self):
        self.assertEqual(OperationId.BING_SEARCH, "bing-search")
        self.assertEqual(OperationId.SHOPIFY_STORE, "shopify-store")

    def test_client_error_for_4xx(self):
        Handler.status = 404
        Handler.body = {"code": 404, "msg": "not found"}
        with self.assertRaises(CrawloraClientError) as raised:
            self.client().bing.search(q="coffee")
        self.assertIsInstance(raised.exception, CrawloraError)
        self.assertEqual(raised.exception.status, 404)

    def test_server_error_for_5xx(self):
        Handler.status = 503
        Handler.body = {"code": 503, "msg": "down"}
        with self.assertRaises(CrawloraServerError) as raised:
            self.client().bing.search(q="coffee")
        self.assertEqual(raised.exception.status, 503)

    def test_network_error_on_transport_failure(self):
        def transport(_request, _timeout):
            raise OSError("socket closed")

        client = CrawloraClient(api_key="api_test", base_url=self.base_url, transport=transport)
        with self.assertRaises(CrawloraNetworkError):
            client.bing.search(q="coffee")

    def test_paginate_advances_and_stops_on_empty(self):
        pages_seen = []

        def transport(request, _timeout):
            from urllib.parse import urlparse, parse_qs

            page = int(parse_qs(urlparse(request.full_url).query).get("page", ["1"])[0])
            pages_seen.append(page)
            data = [{"id": page}] if page < 3 else []
            return type("R", (), {"status": 200, "headers": {"content-type": "application/json"}, "body": json.dumps({"code": 200, "msg": "OK", "data": data}).encode()})()

        client = CrawloraClient(api_key="api_test", base_url=self.base_url, transport=transport)
        pages = list(client.paginate("ebay-seller-feedback", {"seller": "acme"}))
        self.assertEqual(pages_seen, [1, 2, 3])
        self.assertEqual(len(pages), 3)
        self.assertEqual(pages[-1]["data"], [])

    def test_paginate_requires_page_param(self):
        with self.assertRaisesRegex(ValueError, "no page or offset query parameter"):
            list(self.client().paginate("user-me"))

    def test_async_client_request(self):
        async def run():
            client = AsyncCrawloraClient(api_key="api_test", base_url=self.base_url)
            result = await client.bing.search(q="coffee")
            self.assertTrue(result["data"]["ok"])
            via_request = await client.request("bing-search", {"q": "tea"})
            self.assertTrue(via_request["data"]["ok"])

        asyncio.run(run())

    def test_async_paginate(self):
        def transport(request, _timeout):
            from urllib.parse import urlparse, parse_qs

            page = int(parse_qs(urlparse(request.full_url).query).get("page", ["1"])[0])
            data = [{"id": page}] if page < 2 else []
            return type("R", (), {"status": 200, "headers": {"content-type": "application/json"}, "body": json.dumps({"code": 200, "msg": "OK", "data": data}).encode()})()

        async def run():
            client = AsyncCrawloraClient(api_key="api_test", base_url=self.base_url, transport=transport)
            pages = [page async for page in client.paginate("ebay-seller-feedback", {"seller": "acme"})]
            self.assertEqual(len(pages), 2)

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
