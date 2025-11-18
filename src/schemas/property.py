import datetime
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl, field_serializer

from src.models.enums import SourceEnum


class PropertyCreate(BaseModel):
    url: HttpUrl = Field(..., description="Url to property")
    title: str = Field(..., description="Listing title")
    price: float = Field(..., description="Price of the property in PLN")
    area_m2: Optional[float] = Field(
        None, description="Area of the property in square metres"
    )
    rooms: Optional[float] = Field(None, description="Number of rooms of the property")
    description: Optional[str] = Field(None, description="Description of the property")
    is_active: bool = Field(
        ..., description="Whether the property listing is currently active"
    )
    province: Optional[str] = Field(None, description="Listing province")
    city: Optional[str] = Field(None, description="City where the property is located")
    district: Optional[str] = Field(None, description="District within the city")
    address: Optional[str] = Field(None, description="Street address of the property")
    source: Optional[SourceEnum] = Field(
        SourceEnum.OTODOM, description="Listing source"
    )

    @field_serializer("url")
    def serialize_url(self, url: HttpUrl, _info):
        return str(url)

    class Config:
        json_schema_extra = {
            "example": {
                "url": "http://example.com/listing/123",
                "title": "Mieszkanie 3 pokoje Katowice",
                "price": 250000,
                "area_m2": 68,
                "rooms": 3,
                "is_active": True,
                "city": "Katowice",
                "district": "Śródmieście",
                "address": "ul. Przykładowa 1",
                "source": "otodom",
            }
        }


class PropertyRead(BaseModel):
    id: int = Field(..., description="Id of the property")
    url: str = Field(..., description="Url to property")
    title: str = Field(..., description="Listing title")
    price: float = Field(..., description="Price of the property in PLN")
    area_m2: Optional[float] = Field(
        None, description="Area of the property in square metres"
    )
    rooms: Optional[float] = Field(None, description="Number of rooms of the property")
    description: Optional[str] = Field(None, description="Description of the property")
    scraped_at: datetime.datetime
    first_seen: datetime.datetime
    last_seen: datetime.datetime
    is_active: bool
    city: Optional[str] = Field(None, description="City where the property is located")
    district: Optional[str] = Field(None, description="District within the city")
    address: Optional[str] = Field(None, description="Street address of the property")
    source: SourceEnum = Field(..., description="Listing source")

    class Config:
        from_attributes = True
