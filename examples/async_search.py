import asyncio
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from crawlora import AsyncCrawloraClient


async def main() -> None:
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        print("set CRAWLORA_API_KEY to run this live example", file=sys.stderr)
        return

    async with AsyncCrawloraClient(
        api_key=api_key,
        base_url=os.environ.get("CRAWLORA_BASE_URL", "https://api.crawlora.net/api/v1"),
    ) as client:
        result = await client.bing.search(q="coffee shops", count=5)
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
