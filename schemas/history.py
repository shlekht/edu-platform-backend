from pydantic import BaseModel
from datetime import datetime


# Схема ответа GET/history
class HistoryResponseSchema(BaseModel):
    course_id: int
    title: str
    authorName: str 
    viewed_at: datetime

    class Config:
        from_attributes = True