from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from passlib.context import CryptContext

from db import collection_user as bd
from users.model import *
from auth.model import *
from utils.config import settings



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

def create_access_token(user:User, expires_delta: Optional[timedelta] = None):
    user_dict = {"username": user.username, "email": user.email}
    to_encode = user_dict.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "sub": str(user.email)})  # Add a "sub" claim with the user ID
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def create_refresh_token(data):
    if isinstance(data, User):
        data = data.dict()
    expire = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, settings.JWT_REFRESH_SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

