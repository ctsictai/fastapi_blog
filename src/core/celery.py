from celery import Celery

# cloudAMQP broker and redis
celery_task = Celery(
    "app",
    # broker="amqps://ffddrbcd:yaGlPDnUCh6wc3aYyDQE7qCtCsFTu8fN@dingo.rmq.cloudamqp.com/ffddrbcd",
    broker="redis://127.0.0.1:6379/0",
    include=['src.core.celery_worker'],
    result_backend="rpc://",
    accept_content=["json"],
    task_serializer="json",
    result_serializer="json",
    timezone="Asia/Seoul",
)

