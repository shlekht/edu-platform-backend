from pydantic import BaseModel, EmailStr
from models.user import UserRole

class UserBase(BaseModel):
    email: EmailStr
    full_name: str




class UserCreate(UserBase):
    password: str
    # По умолчанию регистрируем как обычного пользователя
    role: UserRole = UserRole.user




class UserRead(UserBase):
    id: int
    role: UserRole

    class Config:
        from_attributes = True




class Token(BaseModel):
    access_token: str
    token_type: str