from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .course import Course

class UserCourseHistory(Base):
    __tablename__ = "user_course_history"
    __table_args__ = (
        UniqueConstraint("user_id", "course_id", name="uq_user_course_history"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"))
    viewed_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), 
        onupdate=func.now()
    )

    # Relationships
    user: Mapped["User"] = relationship(back_populates="history")
    course: Mapped["Course"] = relationship(back_populates="history")