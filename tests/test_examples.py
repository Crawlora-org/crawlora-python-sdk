import os
import subprocess
import sys
import unittest
from pathlib import Path


class ExamplesTest(unittest.TestCase):
    def test_examples_skip_cleanly_without_live_credentials(self):
        root = Path(__file__).resolve().parents[1]
        for example in [
            "examples/bing_search.py",
            "examples/youtube_transcript.py",
        ]:
            with self.subTest(example=example):
                result = subprocess.run(
                    [sys.executable, example],
                    cwd=root,
                    env=scrub_live_env(),
                    text=True,
                    capture_output=True,
                    check=False,
                )

                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("CRAWLORA_", result.stderr)


def scrub_live_env():
    env = dict(os.environ)
    for key in (
        "CRAWLORA_API_KEY",
        "CRAWLORA_BASE_URL",
        "CRAWLORA_YOUTUBE_VIDEO_ID",
    ):
        env.pop(key, None)
    return env
