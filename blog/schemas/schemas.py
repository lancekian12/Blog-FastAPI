from typing import List, Optional
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class ShowAllBlogs(BaseModel):
    title: str
    body: str

    class Config():
        from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[ShowAllBlogs] = []

    class Config():
        from_attributes = True


class ShowBloG(BaseModel):
    title: str
    body: str
    owner: ShowUser


class Config():
    from_attributes = True

class Login(BaseModel):
    email: str
    password: str