import datetime
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl, field_serializer


class PropertyCreate(BaseModel):
    url: HttpUrl = Field(..., description="Url to property")
    title: str = Field(..., description="Listng title")
    price: float = Field(..., description="Price of the property in PLN")
    area: Optional[float] = Field(
        None, description="Area of the property in square metres"
    )
    rooms: Optional[int] = Field(None, description="Number of rooms of the property")
    description: Optional[str] = Field(None, description="Description of the property")

    @field_serializer("url")
    def serialize_url(self, url: HttpUrl, _info):
        return str(url)

    class Config:
        json_schema_extra = {
            "example": {
                "url": "http://127.0.0.1:8000/properties",
                "title": "Mieszkanie 3 pokoje Katowice",
                "price": 250000,
                "area": 68,
                "rooms": 3,
            }
        }


class PropertyRead(BaseModel):
    id: int = Field(..., description="Id of the property")
    url: str = Field(..., description="Url to property")
    title: str = Field(..., description="Listing title")
    price: float = Field(..., description="Price of the property in PLN")
    area: Optional[float] = Field(
        None, description="Area of the property in square metres"
    )
    rooms: Optional[int] = Field(None, description="Number of rooms of the property")
    description: Optional[str] = Field(None, description="Description of the property")
    created_at: datetime.datetime

    class Config:
        from_attributes = True
