from fastapi import FastAPI
from src.core.config import settings
from fastapi.openapi.utils import get_openapi
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter
from src.schemas.foo import FooItem
from src.core.celery_worker import divide

from .routers import api


app = FastAPI(
    openapi_url=settings.openapi_url,
    title="fastapi start",
    description="api documentaion at swagger",
    version="0.1.0",
)


app.include_router(api.router)
# CRUD generator example
app.include_router(CRUDRouter(schema=FooItem))


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/work")
async def work(a:int, b:int, task_id:str):
    divide.apply_async([a, b], task_id=task_id)
    return {"message": "celery start"}

@app.get("/work_result")
async def work_result(task_id: str):
    result = divide.AsyncResult(task_id)
    return {"message": result.info}