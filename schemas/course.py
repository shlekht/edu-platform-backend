from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from schemas.user import UserRead

# схема для создания курса
class CourseCreateSchema(BaseModel):
    title: str
    description: str
    content: str  # markdown строка

# схема курса для главной страницы (без контента, чтобы не грузить много лишнего)
class CourseShortSchema(BaseModel):
    id: int
    title: str
    description: str
    author: str
    created_at: datetime

    class Config:
        from_attributes = True

# схема для детального просмотра курса
class CourseDetailSchema(BaseModel):
    id: int
    title: str
    description: str
    content: str
    author_id: int
    created_at: datetime
    author: UserRead  # автор загрузится через joinedload

    class Config:
        from_attributes = True