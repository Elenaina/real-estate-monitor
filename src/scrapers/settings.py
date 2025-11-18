SOURCES = {
    "otodom": {
        "base_url": "https://www.otodom.pl",
        "list_url_template": "https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/{province}/{city}?page={page}",
        "listing_selector": 'div[data-sentry-element="ContentContainer"]',
        "link_selector": 'a[data-cy="listing-item-link"]',
        "title_selector": '[data-cy="listing-item-title"]',
        "price_selector": 'span[data-sentry-element="MainPrice"]',
    }
}
