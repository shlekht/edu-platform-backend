from sqlalchemy.orm import Session
from exceptions.auth import AuthenticationError
from exceptions.note import NoteNotFoundError
from models.note import Note
from repositories import notes_repository
from schemas.note import NoteCreateSchema, NoteUpdateSchema


def get_all_notes(user_id: int, db: Session) -> list[Note]:
    return notes_repository.get_all_notes(user_id=user_id, db=db)


def create_note(user_id: int, note_data: NoteCreateSchema, db: Session) -> Note:

    note_to_create = Note(**note_data.model_dump(), user_id=user_id)

    return notes_repository.create_note(note_obj=note_to_create, db=db)


def update_note(
    note_id: int, user_id: int, note_data: NoteUpdateSchema, db: Session
) -> Note:
    note = notes_repository.get_note_by_id(note_id=note_id, db=db)

    if not note:
        raise NoteNotFoundError("Заметка не найдена")

    if note.user_id != user_id:
        raise AuthenticationError("Нет прав на редактирование этой заметки")

    note.title = note_data.title
    note.text = note_data.text
    return notes_repository.update_note(note_obj=note, db=db)


def delete_note(note_id: int, user_id: int, db: Session) -> None:
    note = notes_repository.get_note_by_id(note_id=note_id, db=db)

    if not note:
        raise NoteNotFoundError("Заметка не найдена")

    if note.user_id != user_id:
        raise AuthenticationError("Нет прав на удаление этой заметки")

    notes_repository.delete_note(note=note, db=db)
