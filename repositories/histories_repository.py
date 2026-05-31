from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
from models.history import UserCourseHistory


def upsert_view_history(user_id: int, course_id: int, db: Session) -> None:
    """
    Добавляет запись в историю или обновляет last_viewed_at,
    если пара user_id и course_id уже существует.
    """
    
    
    # ON CONFLICT DO UPDATE
    stmt = insert(UserCourseHistory).values(
        user_id=user_id,
        course_id=course_id,
        
    )
    
    stmt = stmt.on_conflict_do_update(
        index_elements=['user_id', 'course_id'],  # UniqueConstraint в БД
        set_=dict(viewed_at=func.now())
    )
    
    db.execute(stmt)
    db.commit()