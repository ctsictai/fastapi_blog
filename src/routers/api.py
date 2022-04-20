# ENDPOINT
from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.post("/item/",)
async def create_item():
    return {"message" : "create_router"}

@router.get("/item/",)
async def search_item():
    return {"message" : "selecst_router"}