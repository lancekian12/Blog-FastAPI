from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

class ShowBloG(BaseModel):
    title: str
    class Config():
        from_attributes = True
        
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

    class Config:
         from_attributes = True