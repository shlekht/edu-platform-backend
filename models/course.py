from datetime import datetime
from typing import List, TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .comment import Comment
    from .history import UserCourseHistory

class Course(Base):
    __tablename__ = "course"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(500))
    content: Mapped[str] = mapped_column(Text)  # Markdown
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # Relationships
    author: Mapped["User"] = relationship(back_populates="authored_courses")
    comments: Mapped[List["Comment"]] = relationship(back_populates="course", cascade="all, delete-orphan")
    history: Mapped[List["UserCourseHistory"]] = relationship(back_populates="course", cascade="all, delete-orphan")