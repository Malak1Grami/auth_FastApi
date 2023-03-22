from fastapi import FastAPI
from utils.config import settings
from fastapi.middleware.cors import CORSMiddleware


from users.model import *

from users import api as users
from auth import api as auth





app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(users.app, tags=["User"])
app.include_router(auth.app, tags=["auth"])