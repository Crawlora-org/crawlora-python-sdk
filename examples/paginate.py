import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from crawlora import CrawloraClient


def main() -> None:
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        print("set CRAWLORA_API_KEY to run this live example", file=sys.stderr)
        return

    with CrawloraClient(
        api_key=api_key,
        base_url=os.environ.get("CRAWLORA_BASE_URL", "https://api.crawlora.net/api/v1"),
    ) as client:
        seller = os.environ.get("CRAWLORA_EBAY_SELLER", "garlandcomputer")
        count = 0
        for item in client.paginate_items("ebay-seller-feedback", {"seller": seller}, max_pages=3):
            count += 1
        print(f"collected {count} feedback items across up to 3 pages")


if __name__ == "__main__":
    main()
