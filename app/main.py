# main.py

from fastapi import FastAPI
from .api import users

app = FastAPI()

# include the routers
app.include_router(users.router)

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}
