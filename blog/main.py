from fastapi import FastAPI, Response, Depends, status, HTTPException

from .schemas import schemas
from .models import models
from .database.database import engine, Sessionlocal, get_db
from .utils.security import Hash
from sqlalchemy.orm import Session
from typing import List
from pwdlib import PasswordHash
from .router import blog, user

app = FastAPI()

models.Base.metadata.create_all(engine)

get_db = get_db

app.include_router(blog.router)
app.include_router(user.router)


