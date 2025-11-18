from pydantic import BaseModel, HttpUrl


class ParsedProperty(BaseModel):
    """
    Minimalny obiekt zwracany przez scraper.
    Nie jest to model z bazy danych — tylko struktura wyciągnięta z HTML.
    """

    url: HttpUrl
    title: str
    price: float | None = None
