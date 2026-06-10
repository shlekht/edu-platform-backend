from sqlalchemy.orm import Session
from exceptions.course import CourseNotFoundError
from exceptions.auth import AuthenticationError
from models.course import Course
from repositories import courses_repository
from repositories import history_repository
from schemas.course import CourseCreateSchema


def get_all_courses(db: Session):
        return courses_repository.get_all_courses(db)

def get_course_by_id(course_id: int, user_id: int, db: Session):
    course = courses_repository.get_course_by_id(course_id, db)
    if not course:
        raise CourseNotFoundError(f"Course with id {course_id} not found")
    
    # пользователь открыл курс = пишем/обновляем историю
    history_repository.upsert_view_history(user_id, course_id, db)
    
    return course

def create_course(course_data: CourseCreateSchema, author_id: int, db: Session):

    course_to_create = Course(
        **course_data.model_dump(),
        author_id=author_id
    )
    
    return courses_repository.create_course(course_to_create, db)

def delete_course(course_id: int, user_id: int, db: Session):
    course = courses_repository.get_course_by_id(course_id, db)
    if not course:
        raise CourseNotFoundError(f"Course with id {course_id} not found")
    
    if course.author_id != user_id:
        raise AuthenticationError(f"User with id {user_id} is not the author of course with id {course_id}")
    
    courses_repository.delete_course(course, db)