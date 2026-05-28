from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from jose import jwt, JWTError

from core.config import settings
from core.security import oauth2_scheme
from models.user import User, UserRole
from db.database import get_session 

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
            detail="У вас недостаточно прав (требуется роль Teacher)"
        )
    return current_user