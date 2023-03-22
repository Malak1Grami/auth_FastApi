from typing import List

from decouple import config
from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_STR: str = "/api"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 100
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        
    ]
    PROJECT_NAME: str = "name of project"
    
    # Database
    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)
    
    class Config:
        case_sensitive = True
        
settings = Settings()