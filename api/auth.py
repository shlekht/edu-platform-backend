from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import get_session
from exceptions.auth import AuthenticationError, UserAlreadyExistsError
from schemas.user import UserCreate, UserRead, Token
import services.auth as auth_service

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(
    user_in: UserCreate,
    db: Session = Depends(get_session)
):
    try:
        return auth_service.register(user_in, db)
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=400,
            detail="User with this email already exists"
    )
    


@router.post("/token", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_session)
):
    try:
        return auth_service.login(form_data, db)
    except AuthenticationError:
         raise HTTPException(
             status_code=status.HTTP_401_UNAUTHORIZED,
             detail="Invalid email or password",
             headers={"WWW-Authenticate": "Bearer"},
         )