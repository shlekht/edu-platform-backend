from repositories import history_repository
from sqlalchemy.orm import Session
from schemas.history import HistoryResponseSchema


def get_history_by_user_id(user_id: int, db: Session) -> list[HistoryResponseSchema]:

    records = history_repository.get_history_by_user_id(user_id=user_id, db = db)


    return [
        HistoryResponseSchema(
            course_id=record.course_id,
            title=record.course.title,
            authorName=record.course.author.full_name, 
            viewed_at=record.viewed_at,
        )
        for record in records
    ]