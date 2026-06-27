from __future__ import annotations
from datetime import datetime
from typing import Optional
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from narmail.extensions import db
from narmail.utils import nm_datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from narmail.models.receiver import Receiver

class Message(db.Model):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    receiver_id: Mapped[int] = mapped_column(ForeignKey("receivers.id"), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=nm_datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=nm_datetime.utcnow, onupdate=nm_datetime.utcnow, nullable=False)

    receiver: Mapped[Receiver] = relationship(back_populates="messages")