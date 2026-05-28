from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import select
from exceptions.auth import AuthenticationError, UserAlreadyExistsError

from core.security import create_access_token, hash_password, verify_password
from models.user import User
from schemas.user import UserCreate
from repositories import users_repository
def register(user_in: UserCreate, db: Session):
    
    if users_repository.is_user_exist(user_in.email, db):
        raise UserAlreadyExistsError()
    
    new_user = User(
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password=hash_password(user_in.password),
        role=user_in.role
    )
    return users_repository.create_user(new_user, db)


def login(
        form_data:OAuth2PasswordRequestForm, 
        db: Session,
    ):
    # OAuth2PasswordRequestForm использует поле 'username' для логина (в нашем случае это email)
    user = users_repository.get_user_by_email(form_data.username, db)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise AuthenticationError()
    
    # Создаем токен, записывая ID пользователя в поле 'sub'
    access_token = create_access_token(subject=user.id)
    
    return {
        "access_token": access_token, 
        "token_type": "bearer"
    }