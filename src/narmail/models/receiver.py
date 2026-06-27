from __future__ import annotations
from datetime import datetime
from typing import Optional
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from narmail.extensions import db
from narmail.utils import nm_datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from narmail.models.message import Message


class Receiver(db.Model):
    __tablename__ = "receivers"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(DateTime, default=nm_datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=nm_datetime.utcnow, onupdate=nm_datetime.utcnow, nullable=False)

    messages: Mapped[list[Message]] = relationship(back_populates="receiver")