from pydantic import BaseModel, Field


class NoteSchema(BaseModel):
    id: int
    title: str
    text: str

    class Config:
        from_attributes = True  


class NoteCreateSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    text: str