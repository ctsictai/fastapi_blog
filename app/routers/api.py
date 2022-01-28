# ENDPOINT
from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.post("/item/",)
async def create_item():
    return {"message" : "create_router"}