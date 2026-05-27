import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from crawlora import CrawloraClient


def main() -> None:
    client = new_client()
    if client is None:
        return

    result = client.bing.search(q="coffee shops", count=5)
    print(json.dumps(result, indent=2))


def new_client() -> CrawloraClient | None:
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        print("set CRAWLORA_API_KEY to run this live example", file=sys.stderr)
        return None
    return CrawloraClient(
        api_key=api_key,
        base_url=os.environ.get("CRAWLORA_BASE_URL", "https://api.crawlora.net/api/v1"),
    )


if __name__ == "__main__":
    main()
