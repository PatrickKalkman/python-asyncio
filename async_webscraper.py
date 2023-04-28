import asyncio
import httpx
from bs4 import BeautifulSoup


async def fetch_content(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            title = soup.title.string if soup.title else "No title found"
            print(f"Title of {url}: {title}")
        else:
            print(f"Failed to fetch from {url} status: {resp.status_code}")


async def main():
    urls = [
        "https://www.google.com/",
        "https://github.com/",
        "https://www.formula1.com/",
    ]
    tasks = [fetch_content(url) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
