from playwright.async_api import async_playwright

# headers to simulate a web browser
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) "
        "Gecko/20100101 Firefox/93.0"
    ),
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


async def fetch_page_html(url: str) -> str:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.set_extra_http_headers(HEADERS)
        await page.goto(url, timeout=15000, wait_until="networkidle")
        content: str = await page.content()
        await browser.close()
        return content
