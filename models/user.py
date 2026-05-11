import enum
from typing import List, TYPE_CHECKING
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .course import Course
    from .note import Note
    from .comment import Comment
    from .history import UserCourseHistory

class UserRole(enum.Enum):
    user = "user"
    teacher = "teacher"

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[str] = mapped_column(String(255))
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.user)

    # Relationships
    authored_courses: Mapped[List["Course"]] = relationship(back_populates="author")
    notes: Mapped[List["Note"]] = relationship(back_populates="user")
    comments: Mapped[List["Comment"]] = relationship(back_populates="user")
    history: Mapped[List["UserCourseHistory"]] = relationship(back_populates="user")