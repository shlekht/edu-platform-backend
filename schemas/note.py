from pydantic import BaseModel


class NoteShortSchema(BaseModel):
    id: int
    title: str
    text: str

    class Config:
        from_attributes = True  