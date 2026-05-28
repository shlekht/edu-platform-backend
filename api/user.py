# api/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_session
from api.deps import get_current_user
from models import User
from schemas.user import UserMeResponse
from services import user_service

router = APIRouter(prefix="/user", tags=["Users"])

@router.get("/me", response_model=UserMeResponse) 
def get_me(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)  
):
    user_profile = user_service.get_current_user_profile(current_user.id, db)
    return user_profile