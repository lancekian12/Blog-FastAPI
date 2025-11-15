from fastapi import FastAPI
from schemas import Blog

app = FastAPI()


@app.post('/blog')
def create_blog(blog: Blog):
    return blog

