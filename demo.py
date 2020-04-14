import os
from typing import List

from fastapi import FastAPI, Request, APIRouter
from fastapi_sqlalchemy import db
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

from db import SQLAlchemySessionMiddleware
from fastapi_demo import models, schema
from fastapi_demo.api import api_router

SECRET_KEY = os.getenv("SECRET_KEY", "secret-key")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@db:5432")


middleware = [
    Middleware(SessionMiddleware, secret_key=SECRET_KEY),
    Middleware(SQLAlchemySessionMiddleware, db_url=DATABASE_URL, session_args=dict(autocommit=True)),
]

app = FastAPI(middleware=middleware)
app.include_router(api_router, prefix='/api')


#
# Use request.session
#


@app.get("/")
async def root(request: Request):
    n = request.session.get("cnt", 0)
    request.session["cnt"] = n + 1
    return {"message": "Hello World", "cnt": n}


#
# Use db.session directly
#

@app.post("/user/", response_model=schema.User)
async def create_user(user: schema.User):
    db_user = models.User(
        first_name=user.first_name, last_name=user.last_name, age=user.age
    )
    db.session.add(db_user)
    db.session.flush()
    return db_user


@app.get("/users/", response_model=List[schema.User])
def get_users(skip: int = 0, limit: int = 100):
    return list(db.session.query(models.User).all()[skip:limit])
