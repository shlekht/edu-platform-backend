from datetime import datetime, timedelta, timezone
import hashlib
from typing import Any, Union, Optional
import bcrypt
from jose import jwt
# from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from .config import settings


# tokenUrl — это путь, по которому Swagger будет отправлять логин/пароль для получения токена
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    pwd_encoded = hashlib.sha256(password.encode('utf-8')).hexdigest().encode('utf-8')
    return bcrypt.hashpw(pwd_encoded, bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    pwd_encoded = hashlib.sha256(plain_password.encode('utf-8')).hexdigest().encode('utf-8')
    return bcrypt.checkpw(pwd_encoded, hashed_password.encode('utf-8'))

def create_access_token(subject: Union[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    
    to_encode = {"exp": expire, "sub": str(subject)}
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)