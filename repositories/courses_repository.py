from sqlalchemy.orm import Session, joinedload


from models.course import Course



def get_all_courses(db: Session) -> list[Course]:
    return db.query(Course).options(joinedload(Course.author)).all() # загружаем авторов вместе с курсами


def get_course_by_id(course_id: int, db: Session) -> Course | None:
        
        return (
            db.query(Course)
            .options(joinedload(Course.author)) # загружаем автора вместе с курсом
            .filter(Course.id == course_id)
            .first()
        )

def create_course(course_obj: Course, db: Session) -> Course:
        db.add(course_obj)
        db.commit()
        db.refresh(course_obj)
        return course_obj

def delete_course(course: Course, db: Session) -> None:
        db.delete(course)
        db.commit()