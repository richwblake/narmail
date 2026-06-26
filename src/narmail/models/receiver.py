from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from narmail.extensions import db

class Receiver(db.Model):
    __tablename__ = "receivers"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )