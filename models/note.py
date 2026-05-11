from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .user import User

class Note(Base):
    __tablename__ = "note"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    text: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), 
        onupdate=func.now()
    )

    # Relationships
    user: Mapped["User"] = relationship(back_populates="notes")