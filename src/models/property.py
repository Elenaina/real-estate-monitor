import datetime
from typing import Optional

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Property(Base):
    __tablename__ = "properties"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    url: Mapped[str] = mapped_column(String, unique=True)
    title: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    area: Mapped[Optional[float]] = mapped_column(Float)
    rooms: Mapped[Optional[int]] = mapped_column(Float)
    description: Mapped[Optional[str]] = mapped_column(String)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
