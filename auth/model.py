from uuid import UUID
from pydantic import BaseModel

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    
    
class TokenPayload(BaseModel):
    sub: UUID = None
    exp: int = None
class TokenRefreshRequest(BaseModel):
    refresh_token: str
class UserPWD (BaseModel):
    
    password:str

class User(BaseModel):
    
    username:str
    email:str
class UserLogin (BaseModel):
    username:str
    password:str