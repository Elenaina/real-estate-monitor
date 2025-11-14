import datetime
from typing import Optional

from sqlalchemy import DateTime, Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.models.enums import SourceEnum, StatusEnum


class ScrapingJob(Base):
    __tablename__ = "scraping_jobs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    source: Mapped[SourceEnum] = mapped_column(
        Enum(SourceEnum, name="source_enum"), primary_key=True, index=True
    )

    status: Mapped[StatusEnum] = mapped_column(
        Enum(StatusEnum, name="status_enum"), primary_key=True, index=True
    )
    started_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now()
    )
    finished_at: Mapped[Optional[datetime.datetime]] = mapped_column(nullable=True)

    properties_found: Mapped[int] = mapped_column(Integer, default=0)
    error_msg: Mapped[Optional[str]] = mapped_column(String)
