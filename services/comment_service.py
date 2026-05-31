from repositories import comments_repository
from repositories import courses_repository
from schemas.comment import CommentCreateSchema
from sqlalchemy.orm import Session
from models.comment import Comment
from exceptions.course import CourseNotFoundError


def get_comments_for_course(course_id: int, db: Session):
    
    if not courses_repository.get_course_by_id(course_id, db):
        raise CourseNotFoundError(f"Course with id {course_id} not found")
    return comments_repository.get_all_comments_by_course_id(course_id, db)



def add_comment(course_id: int, user_id: int, comment_data: CommentCreateSchema, db: Session):
    
    if not courses_repository.get_course_by_id(course_id, db):
        raise CourseNotFoundError(f"Course with id {course_id} not found")
        
    comment_to_create = Comment(
        **comment_data.model_dump(),
        user_id=user_id,
        course_id=course_id
    )

    return comments_repository.create_comment(comment_to_create, db)