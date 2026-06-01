import io
import json
import os
import unittest
from unittest import mock

from crawlora import CrawloraClient, CrawloraError, CrawloraServerError


def transport_for(responses):
    """Build a transport that returns queued (status, body) responses, recording calls."""
    calls = []
    state = {"i": 0}

    def transport(request, timeout):
        calls.append(request.full_url)
        status, body = responses[min(state["i"], len(responses) - 1)]
        state["i"] += 1
        payload = body if isinstance(body, (bytes, bytearray)) else json.dumps(body).encode()
        return type("R", (), {"status": status, "headers": {"content-type": "application/json"}, "body": payload})()

    transport.calls = calls
    return transport


class RetryCustomizationTest(unittest.TestCase):
    def test_retry_predicate_supersedes_status_set(self):
        seen = []
        tx = transport_for([(500, {"code": 500, "msg": "x"}), (200, {"code": 200, "data": {"ok": True}})])
        client = CrawloraClient(
            api_key="k", base_url="http://x/api/v1", retries=2, retry_delay=0, transport=tx,
            retry_predicate=lambda status, err: (seen.append(status), status == 500)[1],
        )
        self.assertTrue(client.bing.search(q="c")["data"]["ok"])
        self.assertEqual(len(tx.calls), 2)
        self.assertIn(500, seen)

    def test_retry_statuses_override(self):
        tx = transport_for([(404, {"code": 404, "msg": "nf"})])
        # 404 not in default retry set; make it retryable, but cap attempts so it still raises.
        client = CrawloraClient(api_key="k", base_url="http://x/api/v1", retries=1, retry_delay=0, transport=tx, retry_statuses=[404])
        with self.assertRaises(CrawloraError):
            client.bing.search(q="c")
        self.assertEqual(len(tx.calls), 2)  # one retry happened

    def test_on_retry_hook(self):
        events = []
        tx = transport_for([(503, {"code": 503, "msg": "x"}), (200, {"code": 200, "data": {"ok": True}})])
        client = CrawloraClient(
            api_key="k", base_url="http://x/api/v1", retries=1, retry_delay=0, transport=tx,
            on_retry=lambda attempt, err, delay: events.append((attempt, err.status)),
        )
        client.bing.search(q="c")
        self.assertEqual(events, [(1, 503)])

    def test_request_id_generated_and_on_error(self):
        captured = {}

        def tx(request, timeout):
            captured["rid"] = request.get_header("X-request-id")
            return type("R", (), {"status": 500, "headers": {"content-type": "application/json"}, "body": b'{"code":500,"msg":"x"}'})()

        client = CrawloraClient(api_key="k", base_url="http://x/api/v1", transport=tx, request_id=True)
        with self.assertRaises(CrawloraServerError) as raised:
            client.bing.search(q="c")
        self.assertTrue(captured["rid"])
        self.assertEqual(raised.exception.request_id, captured["rid"])

    def test_logger_receives_events(self):
        logs = []
        tx = transport_for([(503, {"code": 503}), (200, {"code": 200, "data": {}})])
        client = CrawloraClient(api_key="k", base_url="http://x/api/v1", retries=1, retry_delay=0, transport=tx, logger=logs.append)
        client.bing.search(q="c")
        self.assertEqual(logs[0]["event"], "request")
        self.assertTrue(any(e["event"] == "retry" for e in logs))


class PaginationTest(unittest.TestCase):
    def test_cursor_pagination(self):
        def tx(request, timeout):
            from urllib.parse import urlparse, parse_qs
            cur = parse_qs(urlparse(request.full_url).query).get("cursor", [""])[0]
            nxt = {"": "a", "a": "b", "b": ""}[cur]
            return type("R", (), {"status": 200, "headers": {"content-type": "application/json"}, "body": json.dumps({"code": 200, "data": [cur or "start"], "next": nxt}).encode()})()

        client = CrawloraClient(api_key="k", base_url="http://x/api/v1", transport=tx)
        pages = list(client.paginate("producthunt-leaderboard", cursor_param="cursor", next_cursor=lambda p: p.get("next")))
        self.assertEqual(len(pages), 3)

    def test_cursor_requires_both(self):
        client = CrawloraClient(api_key="k", base_url="http://x/api/v1")
        with self.assertRaisesRegex(ValueError, "requires both"):
            list(client.paginate("producthunt-leaderboard", cursor_param="cursor"))

    def test_cursor_param_must_be_query_param(self):
        client = CrawloraClient(api_key="k", base_url="http://x/api/v1")
        with self.assertRaisesRegex(ValueError, "not a query parameter"):
            list(client.paginate("producthunt-leaderboard", cursor_param="bogus", next_cursor=lambda p: None))

    def test_paginate_items(self):
        def tx(request, timeout):
            from urllib.parse import urlparse, parse_qs
            p = int(parse_qs(urlparse(request.full_url).query).get("page", ["1"])[0])
            data = [{"n": p}] if p < 3 else []
            return type("R", (), {"status": 200, "headers": {"content-type": "application/json"}, "body": json.dumps({"code": 200, "data": data}).encode()})()

        client = CrawloraClient(api_key="k", base_url="http://x/api/v1", transport=tx)
        items = list(client.paginate_items("ebay-seller-feedback", {"seller": "a"}))
        self.assertEqual(items, [{"n": 1}, {"n": 2}])


class StreamingTest(unittest.TestCase):
    def test_stream_returns_file_like(self):
        tx = transport_for([(200, b"chunkdata")])
        client = CrawloraClient(api_key="k", base_url="http://x/api/v1", transport=tx)
        stream = client.request("bing-search", {"q": "c"}, response_type="stream")
        self.assertIsInstance(stream, io.BytesIO)
        self.assertEqual(stream.read(), b"chunkdata")

    def test_stream_error_still_raises(self):
        tx = transport_for([(500, {"code": 500, "msg": "boom"})])
        client = CrawloraClient(api_key="k", base_url="http://x/api/v1", transport=tx)
        with self.assertRaises(CrawloraServerError):
            client.request("bing-search", {"q": "c"}, response_type="stream")


class EnvConfigTest(unittest.TestCase):
    def test_env_var_fallback(self):
        with mock.patch.dict(os.environ, {"CRAWLORA_API_KEY": "env_key", "CRAWLORA_BASE_URL": "http://env/api/v1"}):
            client = CrawloraClient()
        self.assertEqual(client.api_key, "env_key")
        self.assertEqual(client.base_url, "http://env/api/v1")

    def test_explicit_overrides_env(self):
        with mock.patch.dict(os.environ, {"CRAWLORA_API_KEY": "env_key"}):
            client = CrawloraClient(api_key="explicit")
        self.assertEqual(client.api_key, "explicit")


if __name__ == "__main__":
    unittest.main()
