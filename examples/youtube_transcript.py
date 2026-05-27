import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from crawlora import CrawloraClient


def main() -> None:
    client = new_client()
    if client is None:
        return

    video_id = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("CRAWLORA_YOUTUBE_VIDEO_ID", "")
    if not video_id:
        print("set CRAWLORA_YOUTUBE_VIDEO_ID or pass a video id to run this live example", file=sys.stderr)
        return

    text = client.youtube.transcript(id=video_id, format="text", _response_type="text")
    print(text)


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
