from pydantic import BaseModel, EmailStr
from models.user import UserRole

class UserBase(BaseModel):
    email: EmailStr
    full_name: str



# схема при создании пользователя, включает password, role, email, full_name
class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.user # по умолчанию роль user



# схема при прочтении основных данных пользователя
class UserRead(UserBase):
    id: int
    role: UserRole

    class Config:
        from_attributes = True


# схема для ответа при GET запросе /users/me, включает id, email, full_name, role
class UserMeResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: UserRole
    

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str