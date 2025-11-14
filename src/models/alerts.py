import datetime
from typing import Optional

from sqlalchemy import Boolean, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class UserAlert(Base):
    """
    Represents a User Alert entity in the database.

    Contains information about user preferences for specific alerts such as
    location, price range, area range, and other relevant properties. This
    class is used to persist alert preferences and manage notifications
    accordingly.

    :ivar id: Unique identifier for the user alert.
    :type id: int
    :ivar user_email: Email of the user associated with the alert.
    :type user_email: str
    :ivar city: Name of the city associated with the alert. Optional.
    :type city: Optional[str]
    :ivar district: Name of the district associated with the alert. Optional.
    :type district: Optional[str]
    :ivar max_price: Maximum price defined in the alert. Optional.
    :type max_price: Optional[float]
    :ivar min_area: Minimum area defined in the alert. Optional.
    :type min_area: Optional[float]
    :ivar max_area: Maximum area defined in the alert. Optional.
    :type max_area: Optional[float]
    :ivar is_active: Boolean flag indicating whether the alert is active.
    :type is_active: bool
    :ivar created_at: Timestamp indicating when the alert was created.
    :type created_at: datetime.datetime
    """

    __tablename__ = "user_alert"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_email: Mapped[str] = mapped_column(String)
    city: Mapped[Optional[str]] = mapped_column(String)
    district: Mapped[Optional[str]] = mapped_column(String)

    max_price: Mapped[Optional[float]] = mapped_column(Float)
    min_area: Mapped[Optional[float]] = mapped_column(Float)
    max_area: Mapped[Optional[float]] = mapped_column(Float)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
