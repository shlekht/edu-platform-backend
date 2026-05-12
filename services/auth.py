from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import select
from exceptions.auth import AuthenticationError, UserAlreadyExistsError

from core.security import create_access_token, hash_password, verify_password
from models.user import User
from schemas.user import UserCreate


def register(user_in: UserCreate, db: Session):
    
    query = select(User).where(User.email == user_in.email)
    existing_user = db.execute(query).scalar_one_or_none()
    
    if existing_user:
        raise UserAlreadyExistsError()
    
    
    new_user = User(
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password=hash_password(user_in.password),
        role=user_in.role
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login(
        form_data:OAuth2PasswordRequestForm, 
        db: Session,
    ):
    # OAuth2PasswordRequestForm использует поле 'username' для логина (в нашем случае это email)
    query = select(User).where(User.email == form_data.username)
    user = db.execute(query).scalar_one_or_none()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise AuthenticationError()
    
    # Создаем токен, записывая ID пользователя в поле 'sub'
    access_token = create_access_token(subject=user.id)
    
    return {
        "access_token": access_token, 
        "token_type": "bearer"
    }