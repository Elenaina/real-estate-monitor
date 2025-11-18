import asyncio

from src.scrapers.fetcher import fetch_page_html


async def main():
    url = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/slaskie/katowice?page=1"  # TEMP hardcoded for tests
    html = await fetch_page_html(url)
    print(html[:500])


if __name__ == "__main__":
    asyncio.run(main())
