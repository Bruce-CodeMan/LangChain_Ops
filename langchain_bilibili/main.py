'''
Date: 2023-05-16 14:26:53
Author: Bruce
Description: 
'''
import asyncio
from bilibili_api import video

async def main() -> None:
    # Instaniate an object
    v = video.Video(bvid="BV1uv411q7Mv")
    # Get the info
    info = await v.get_info()
    # Print the information
    print(info)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())