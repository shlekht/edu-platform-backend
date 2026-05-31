from datetime import datetime
from pydantic import BaseModel
from schemas.user import UserRead


# схема для создания комментария
class CommentCreateSchema(BaseModel):
    text: str


# схема для ответа при GET запросе комментариев
class CommentResponseSchema(BaseModel):
    id: int
    text: str
    user_id: int
    course_id: int
    created_at: datetime
    user: UserRead  # автор загрузится через joinedload

    class Config:
        from_attributes = True