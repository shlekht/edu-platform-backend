from sqlalchemy.orm import Session
from models.note import Note


def get_all_notes(user_id: int, db: Session):
    return db.query(Note).filter(Note.user_id == user_id).all()


def get_note_by_id(note_id: int, db: Session) -> Note | None:
        return db.query(Note).filter(Note.id == note_id).first()

def create_note(note_obj: Note, db: Session) -> Note:
    db.add(note_obj)      
    db.commit()         
    db.refresh(note_obj)  
    return note_obj


def update_note(note_obj: Note, db: Session) -> Note:
    db.commit()
    db.refresh(note_obj)
    return note_obj


def delete_note(note: Note, db: Session) -> None:
    db.delete(note)
    db.commit()