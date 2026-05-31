from sqlalchemy.orm import Session, joinedload
from models import Comment



def get_all_comments_by_course_id(course_id: int, db: Session) -> list[Comment]:
        
        return (
            db.query(Comment)
            .options(joinedload(Comment.user)) # загружаем автора комментария динамически
            .filter(Comment.course_id == course_id)
            .order_by(Comment.created_at.desc()) 
            .all()
        )

def create_comment(comment_obj: Comment, db: Session) -> Comment:
        db.add(comment_obj)
        db.commit()
        db.refresh(comment_obj)
        return comment_obj