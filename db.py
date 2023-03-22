from fastapi import FastAPI
from utils.config import settings
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_STR}/openapi.json"
)

db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).projectName
collection_user = db_client.users
    


