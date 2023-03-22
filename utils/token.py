from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError


from auth.service import get_user
from db import collection_user as db
from auth.model import User
from utils.config import settings
from users.service import find_exist_user
from utils.security import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_user_from_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id =  payload['email']
        
        # print(user_id)
        user_data  =await find_exist_user(user_id)
        if user_data is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        # user=UserAuth(**user_data )
        # print("||||||||||||||||||||||||||||||||||||")
        # print(user_data)
        return user_data
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials"
        )

def create_token(user: UserAuth):
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return {"access_token": access_token, "refresh_token": refresh_token}

async def refresh_token(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, settings.JWT_REFRESH_SECRET_KEY, algorithms=[settings.ALGORITHM])
        
        
        user_id = payload['email']
        
        # print(user_id)
        user_data  = await get_user(user_id)
        if user_data  is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )
        user=User(**user_data )
        new_token = create_access_token(user)
        return {"access_token": new_token}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials"
        )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = await get_user_from_token(token)
    
    
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user["disabled"]:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
