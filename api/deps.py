from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from jose import jwt, JWTError

from core.config import settings
from core.security import oauth2_scheme
from models.user import User, UserRole
from db.database import get_session
from schemas.comment import CommentCreateSchema 
from services import comment_service


def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_session)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    
    user = db.execute(select(User).where(User.id == int(user_id))).scalar_one_or_none()
    
    if user is None:
        raise credentials_exception
    return user

def check_teacher_role(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role != UserRole.teacher:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have enough permissions (Teacher role required)"
        )
    return current_user


def moderate_comment(comment: CommentCreateSchema):
    print("moderate comment")
    text_to_check = comment.text
    comment_is_safe = comment_service.moderate_comment(text_to_check)
    if not comment_is_safe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "Comment is potentially harmful."
        )
    return comment
    
    
    