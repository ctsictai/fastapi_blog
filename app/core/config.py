from pydantic import BaseSettings

class Settings(BaseSettings):
    openapi_url:str = "/openapi.json"
    
settings = Settings()