from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from models.user import User


def is_user_exist(email: str, db: Session) -> bool:
    query = select(User).where(User.email == email)
    existing_user = db.execute(query).scalar_one_or_none()
    if existing_user:
        return True
    return False


def create_user(user_obj: User, db: Session) -> User:
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


def get_user_by_email(email: str, db: Session) -> User | None:
    query = select(User).where(User.email == email)
    return db.execute(query).scalar_one_or_none()


def get_user_by_id(user_id: int, db: Session) -> User | None:
    query = (
        select(User)
        .where(User.id == user_id)
    )
    return db.execute(query).scalar_one_or_none()