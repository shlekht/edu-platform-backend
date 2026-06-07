from pydantic import BaseModel

class MessageInSchema(BaseModel):
    text: str

class MessageOutSchema(BaseModel):
    text: str