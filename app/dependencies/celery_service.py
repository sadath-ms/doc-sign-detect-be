# celery.py
from celery import Celery
import os

# Initialize Celery with Redis as the broker
celery_app = Celery(
    "worker",
    broker="redis://redis:6379/0",  # Use 'redis' as the hostname
    backend="redis://redis:6379/0"
)

# Configure Celery to discover tasks from the FastAPI app
celery_app.conf.update(
    task_routes={
        'app.tasks.*': {'queue': 'default'},
    },
)
