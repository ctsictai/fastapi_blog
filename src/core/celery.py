from celery import Celery

celery_task = Celery(
    "app",
    broker="redis://127.0.0.1:6379/0",
    include=['src.core.celery_worker'],
    result_backend="rpc://",
    accept_content=["json"],
    task_serializer="json",
    result_serializer="json",
    timezone="Asia/Seoul",
)

