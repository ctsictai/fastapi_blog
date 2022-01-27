from fastapi import FastAPI
from .core.config import settings
from fastapi.openapi.utils import get_openapi


app = FastAPI(
    openapi_url=settings.openapi_url,
    title="fastapi start",
    description= "#############3",
    version= "0.1.0",    
)

app.openapi

@app.get("/")
async def root():
    return {"message": "Hello World"}