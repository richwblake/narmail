from datetime import datetime
from typing import Optional
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from narmail.extensions import db
from narmail.utils import nm_datetime

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
