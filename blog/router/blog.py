from typing import List
from fastapi import APIRouter, Depends, Response, status, HTTPException
from blog.schemas import schemas
from ..schemas import schemas
from ..models import models
from ..database.database import get_db
from sqlalchemy.orm import Session
from ..repository import blog as repository_blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowAllBlogs])
def all(db: Session = Depends(get_db)):
    return repository_blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    return repository_blog.create_blog(db, blog)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBloG)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    return repository_blog.show_blog(db, id)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    return repository_blog.delete_blog(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, blog: schemas.Blog, db: Session = Depends(get_db)):
    return repository_blog.update_blog(db, id, blog)
