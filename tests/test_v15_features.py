import json
import threading
import time
import unittest

from crawlora import CrawloraClient, CrawloraServerError


def make_transport(responses=None, record=None):
    queue = responses or [(200, {"code": 200, "data": {}})]
    state = {"i": 0}

    def transport(request, timeout):
        if record is not None:
            record.append({
                "method": request.get_method(),
                "url": request.full_url,
                "headers": {k: v for k, v in request.header_items()},
            })
        status, body = queue[min(state["i"], len(queue) - 1)]
        state["i"] += 1
        payload = body if isinstance(body, (bytes, bytearray)) else json.dumps(body).encode()
        return type("R", (), {"status": status, "headers": {"content-type": "application/json"}, "body": payload})()

    return transport


class MiddlewareTest(unittest.TestCase):
    def test_before_request_injects_header(self):
        rec = []
        client = CrawloraClient(
            api_key="k", base_url="http://x/api/v1", transport=make_transport(record=rec),
            before_request=lambda ctx: ctx["headers"].__setitem__("X-Sig", "sig-" + ctx["operation"]),
        )
        client.bing.search(q="c")
        self.assertEqual(rec[0]["headers"].get("X-sig") or rec[0]["headers"].get("X-Sig"), "sig-bing-search")

    def test_after_response_transforms_body(self):
        client = CrawloraClient(
            api_key="k", base_url="http://x/api/v1", transport=make_transport(),
            after_response=lambda op, status, headers, body: {**body, "_op": op},
        )
        result = client.bing.search(q="c")
        self.assertEqual(result["_op"], "bing-search")


class IdempotencyTest(unittest.TestCase):
    def test_key_stable_across_retries_on_post(self):
        rec = []
        client = CrawloraClient(
            api_key="k", base_url="http://x/api/v1", retries=1, retry_delay=0, idempotency_keys=True,
            transport=make_transport([(503, {"code": 503}), (200, {"code": 200, "data": {}})], record=rec),
        )
        client.google.search(searchOption={"q": "c"})  # POST
        keys = [r["headers"].get("Idempotency-key") or r["headers"].get("Idempotency-Key") for r in rec]
        self.assertEqual(len(rec), 2)
        self.assertTrue(keys[0])
        self.assertEqual(keys[0], keys[1])

    def test_no_key_on_get(self):
        rec = []
        client = CrawloraClient(api_key="k", base_url="http://x/api/v1", idempotency_keys=True, transport=make_transport(record=rec))
        client.bing.search(q="c")  # GET
        self.assertIsNone(rec[0]["headers"].get("Idempotency-key") or rec[0]["headers"].get("Idempotency-Key"))


class PerRequestRetryTest(unittest.TestCase):
    def test_per_request_retries_override(self):
        rec = []
        client = CrawloraClient(
            api_key="k", base_url="http://x/api/v1", retries=5, retry_delay=0,
            transport=make_transport([(503, {"code": 503})], record=rec),
        )
        with self.assertRaises(CrawloraServerError):
            client.request("bing-search", {"q": "c"}, retries=0)
        self.assertEqual(len(rec), 1)  # override to 0 retries


class TypedRuntimeTest(unittest.TestCase):
    def test_unknown_kwarg_raises(self):
        client = CrawloraClient(api_key="k", base_url="http://x/api/v1", transport=make_transport())
        with self.assertRaisesRegex(TypeError, "unexpected parameter"):
            client.bing.search(q="c", bogus_param="x")

    def test_known_kwargs_ok(self):
        client = CrawloraClient(api_key="k", base_url="http://x/api/v1", transport=make_transport())
        client.bing.search(q="c", count=3, _timeout=5)  # valid params + option


class RateLimitTest(unittest.TestCase):
    def test_max_concurrency_caps_in_flight(self):
        active = {"n": 0, "max": 0}
        lock = threading.Lock()

        def transport(request, timeout):
            with lock:
                active["n"] += 1
                active["max"] = max(active["max"], active["n"])
            time.sleep(0.02)
            with lock:
                active["n"] -= 1
            return type("R", (), {"status": 200, "headers": {"content-type": "application/json"}, "body": b'{"code":200,"data":{}}'})()

        client = CrawloraClient(api_key="k", base_url="http://x/api/v1", transport=transport, max_concurrency=2)
        threads = [threading.Thread(target=lambda: client.bing.search(q="c")) for _ in range(6)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertLessEqual(active["max"], 2)


if __name__ == "__main__":
    unittest.main()
