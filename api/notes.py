from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session


from db.database import get_session 
from api.deps import get_current_user
from schemas.note import NoteCreateSchema, NoteSchema
from services import notes_service

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.get("/", response_model=list[NoteSchema])
def get_all_notes(current_user = Depends(get_current_user), db: Session = Depends(get_session)  ):
    try:
        return notes_service.get_all_notes(user_id = current_user.id, db = db)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Ошибка при получении заметок"
    )

@router.post("/", response_model=NoteSchema, status_code=status.HTTP_201_CREATED)
def create_note(
    note_data: NoteCreateSchema, 
    current_user = Depends(get_current_user), 
    db: Session = Depends(get_session)
):
    
    return notes_service.create_note(
        user_id=current_user.id, 
        note_data=note_data, 
        db=db
    )

    