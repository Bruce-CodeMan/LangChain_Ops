"""
Date: 2023-05-16 14:26:53
Author: Bruce
Description: 
"""
import asyncio
from decouple import config
from bilibili_api import video, Credential


async def main() -> None:
    # Instantiate the objects
    c = Credential(
        sessdata=config("SESSDATA"),
        bili_jct=config("BILI_JCT"),
        buvid3=config("BUVID3"),
    )
    v = video.Video(bvid="BV1uv411q7Mv", credential=c)

    await v.like(True)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
