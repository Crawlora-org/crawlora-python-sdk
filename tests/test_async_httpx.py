import asyncio
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from crawlora import AsyncCrawloraClient, CrawloraServerError

try:
    import httpx  # noqa: F401

    HAS_HTTPX = True
except ImportError:
    HAS_HTTPX = False


class Handler(BaseHTTPRequestHandler):
    fail_first = False
    state = {"n": 0}

    def do_GET(self):
        self.state["n"] += 1
        if self.fail_first and self.state["n"] == 1:
            self.send_response(503)
            self.send_header("content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"code":503,"msg":"down"}')
            return
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        page = self.path.split("page=")[-1].split("&")[0] if "page=" in self.path else "1"
        data = [{"p": int(page)}] if int(page) < 3 else []
        self.wfile.write(json.dumps({"code": 200, "msg": "OK", "data": data}).encode())

    def log_message(self, *_a):
        return


@unittest.skipUnless(HAS_HTTPX, "httpx not installed (pip install crawlora[async])")
class AsyncHttpxTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}/api/v1"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def setUp(self):
        Handler.fail_first = False
        Handler.state = {"n": 0}

    def test_async_request_uses_httpx(self):
        async def run():
            async with AsyncCrawloraClient(api_key="k", base_url=self.base_url) as client:
                self.assertTrue(client.uses_httpx)
                result = await client.bing.search(q="coffee")
                self.assertEqual(result["data"], [{"p": 1}])

        asyncio.run(run())

    def test_async_retry(self):
        Handler.fail_first = True

        async def run():
            async with AsyncCrawloraClient(api_key="k", base_url=self.base_url, retries=1, retry_delay=0) as client:
                result = await client.bing.search(q="coffee")
                self.assertEqual(result["data"], [{"p": 1}])

        asyncio.run(run())

    def test_async_paginate_items(self):
        async def run():
            async with AsyncCrawloraClient(api_key="k", base_url=self.base_url) as client:
                items = [item async for item in client.paginate_items("ebay-seller-feedback", {"seller": "a"})]
                self.assertEqual(items, [{"p": 1}, {"p": 2}])

        asyncio.run(run())

    def test_async_error_classification(self):
        Handler.fail_first = True

        async def run():
            async with AsyncCrawloraClient(api_key="k", base_url=self.base_url, retries=0) as client:
                with self.assertRaises(CrawloraServerError):
                    await client.bing.search(q="coffee")

        asyncio.run(run())


if __name__ == "__main__":
    unittest.main()
