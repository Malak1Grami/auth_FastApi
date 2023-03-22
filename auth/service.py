from bson.objectid import ObjectId

from db import *


def get_user(email: str):
    return collection_user.find_one({"email": email})
    

def get_user_by_id(id: str):
    return collection_user.find_one({"_id": ObjectId(id)})

def hash_password(password: str):
    # Hash password using bcrypt or similar library
    return password

