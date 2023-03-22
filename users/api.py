from fastapi import APIRouter, HTTPException

from fastapi import Depends,BackgroundTasks


from utils.token import get_current_user
from .service import *
import json
from bson import json_util
from utils.otpUtil import *
from utils.cruptutil import *
from utils.emailUtil import *



app = APIRouter()

@app.post("/auth/register")
async def register(user: UserAuth):
    result = await find_exist_user(user.email)
    if result:
        raise HTTPException(status_code=404, detail="User already registered!")
    

        # Create new user
    user.password = hash_password(user.password)
    #await save_user(user.dict())
    # otp_code=random(6)
    
    await save_user(user.dict())
    # Sending email
    # subject = "OTP Code"
    # recipient = user.email
    # message = """
    #         <!DOCTYPE html>
    #         <html>
    #         <title>Créer mon compte</title>
    #         <body>
    #         <div style="width:100%;font-family: monospace;">
    #         <p>Bonjour,

    #         Vous avez initié une demande de création de compte. 
    #         Afin de confirmer votre identité,
    #         veuillez entrer le code suivant :</p>
    #             <h1>{0:}</h1>
    #         </div>
    #         </body>
    #         </html>
    #         """.format(otp_code)

    # await send_email(subject, recipient, message)
    if save_user:
    #     background_tasks.add_task(expired_otp_code,otp_code)

        return   {**user.dict() ,
        "code": 200,
    #         "message": "We've sent a code in email"
    }



@app.get("/profile/me")
async def get_user_profile(current_user:UserAuth=Depends(get_current_user)):
    response = current_user
    if response:
        return json.loads(json_util.dumps(response))
    raise HTTPException(400, "Something went wrong")
    

    