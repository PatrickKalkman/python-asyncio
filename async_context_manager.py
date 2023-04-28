import aiohttp
import asyncio


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://example.com"
    content = await fetch(url)
    print(content[:100])


asyncio.run(main())
