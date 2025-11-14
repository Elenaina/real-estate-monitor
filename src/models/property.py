import datetime
from typing import List, Optional

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.models.enums import SourceEnum


class Property(Base):
    """
    Represents a property with its associated details and relationships.

    The Property class is designed for real estate listings, storing details such
    as pricing, location, and other related attributes. This class accommodates
    relevant data for tracking changes over time, including price history and
    activity status.

    :ivar id: Unique identifier for the property.
    :type id: int
    :ivar url: Unique URL where the property is listed.
    :type url: str
    :ivar title: Title or name of the property listing.
    :type title: str
    :ivar price: Current price of the property.
    :type price: float
    :ivar area_m2: Area of the property in square meters.
    :type area_m2: Optional[float]
    :ivar rooms: Number of rooms in the property.
    :type rooms: Optional[int]
    :ivar description: A textual description of the property.
    :type description: Optional[str]
    :ivar scraped_at: Timestamp indicating when the property details were last
        scraped.
    :type scraped_at: datetime.datetime
    :ivar first_seen: Timestamp indicating when the property was first seen.
    :type first_seen: datetime.datetime
    :ivar last_seen: Timestamp indicating when the property was last seen.
    :type last_seen: datetime.datetime
    :ivar is_active: Indicates whether the property is currently active or not.
    :type is_active: bool
    :ivar city: City where the property is located.
    :type city: Optional[str]
    :ivar district: District where the property is located.
    :type district: Optional[str]
    :ivar address: Specific address of the property.
    :type address: Optional[str]
    :ivar price_history: List of price history objects related to the property.
    :type price_history: List[PriceHistory]
    """

    __tablename__ = "properties"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    url: Mapped[str] = mapped_column(String, unique=True, index=True)
    title: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)

    area_m2: Mapped[Optional[float]] = mapped_column(Float)
    rooms: Mapped[Optional[int]] = mapped_column(Float)
    description: Mapped[Optional[str]] = mapped_column(String)

    scraped_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
    first_seen: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
    last_seen: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
    is_active: Mapped[bool] = mapped_column(Boolean)

    city: Mapped[Optional[str]] = mapped_column(String, index=True)
    district: Mapped[Optional[str]] = mapped_column(String, index=True)
    address: Mapped[Optional[str]] = mapped_column(String)

    # Source of the listing (e.g., otodom)
    source: Mapped[SourceEnum] = mapped_column(
        Enum(SourceEnum, name="source_enum"),
        default=SourceEnum.OTODOM,
        index=True,
    )

    price_history: Mapped[List["PriceHistory"]] = relationship(
        "PriceHistory",
        back_populates="property",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        Index("idx_city_price", "city", "price"),
        Index("idx_city_area", "city", "area_m2"),
        Index("idx_is_active_city", "city", "is_active"),
    )


class PriceHistory(Base):
    """
    Represents the history of property prices.

    This class is used to maintain records of property price changes over time. It
    associates a property with a specific price at a given timestamp. The purpose of
    this class is to track historical data for analysis, reporting, and other
    computational tasks related to property values.

    :ivar id: Unique identifier for the price history record.
    :ivar property_id: Foreign key referencing the associated property.
    :ivar price: Recorded price of the property at a specific timestamp.
    :ivar checked_at: Timestamp indicating when the price was checked or recorded.
    :ivar property: Relationship to the associated Property object.
    """

    __tablename__ = "price_history"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    property_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("properties.id"), index=True
    )
    price: Mapped[float] = mapped_column(Float, nullable=False)
    checked_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )

    property: Mapped["Property"] = relationship(
        "Property",
        back_populates="price_history",
    )
