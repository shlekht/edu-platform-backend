from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Text, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .course import Course

class Comment(Base):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Relationships
    user: Mapped["User"] = relationship(back_populates="comments")
    course: Mapped["Course"] = relationship(back_populates="comments")