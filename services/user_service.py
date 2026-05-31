



from sqlalchemy.orm import Session

from models.user import User
from repositories import users_repository


def get_current_user_profile(user_id: int, db: Session) -> User | None:
    return users_repository.get_user_by_id(user_id, db)
