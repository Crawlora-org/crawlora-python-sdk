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

    image_path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("CRAWLORA_LENS_IMAGE", "")
    if not image_path:
        print("set CRAWLORA_LENS_IMAGE or pass an image path to run this live example", file=sys.stderr)
        return

    path = Path(image_path)
    if not path.is_file():
        raise SystemExit(f"image file not found: {path}")

    result = client.google.lens(image=path)
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
