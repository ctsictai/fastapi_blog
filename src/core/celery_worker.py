from src.core.celery import celery_task

@celery_task.task
def divide(x,y):
    import time 
    time.sleep(5)
    return x/y