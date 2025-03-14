# tasks.py
from app.dependencies.celery_service import celery_app

@celery_app.task
def add(x, y):
    print('add is calling')
    return x + y
