from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_session
from api.deps import get_current_user
from models import User
from schemas.history import HistoryResponseSchema
from services import history_service

router = APIRouter(prefix="/history", tags=["History"])

@router.get("/", response_model=list[HistoryResponseSchema]) 
def get_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)  
):
    try:
        return history_service.get_history_by_user_id(user_id=current_user.id, db=db)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error when getting history"
        )