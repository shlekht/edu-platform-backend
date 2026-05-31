


from sqlalchemy.orm import Session
from models.note import Note
from repositories import notes_repository
from schemas.note import NoteCreateSchema


def get_all_notes(user_id: int, db: Session) -> list[Note]:
    return notes_repository.get_all_notes(user_id=user_id, db=db)


def create_note(user_id: int, note_data: NoteCreateSchema, db: Session) -> Note:
    
    note_to_create = Note(
        **note_data.model_dump(),
        user_id=user_id
    )

    return notes_repository.create_note(
        note_obj=note_to_create, 
        db=db
    )