

from .model import *

from time import sleep

from db import *


#existed user 
async def find_exist_user(email):
    document = await collection_user.find_one({"email":email},{"_id","email","username"})
    
    return (document)

# Create new user
async def save_user(user):
    document = user
    result = await collection_user.insert_one(document)
    # if result:
    #     query=await collection_user.update_one(
    #         {"email":user['email']}
    #         # , {"$set":{"otp_code":otp_code}}
    #     )
        
    return result

def expired_otp_code(otp_code):
    sleep(300)
    doc= collection_user.update_one({"otp_code":otp_code},{"$unset":{"otp_code":""}})
    if doc :
        return True
    else:
        False

