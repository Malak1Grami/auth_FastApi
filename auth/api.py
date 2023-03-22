
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from users.service import *
from utils.security import *

from utils.token import *

from auth.model import *

from auth.service import *


app = APIRouter()



@app.post("/auth/login")
async def login(request: OAuth2PasswordRequestForm = Depends() ):
    
        #check user existed
    user = await get_user(request.username)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    #verified password

    userpwd = UserPWD(**user)
    is_valid = verify_password(request.password, userpwd.password)
    if not is_valid:
        raise HTTPException(status_code=404, detail="Incorrect username or password")
    #create token
    userauth=User(**user)
    return create_token(userauth)
    # return json.loads(json_util.dumps(user))



@app.post("/refresh_token")
async def token_refresh(request: TokenRefreshRequest):
    return await refresh_token(request.refresh_token)
