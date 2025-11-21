from typing import List
from fastapi import APIRouter, Depends, Response, status, HTTPException
from ..schemas import schemas
from ..database.database import get_db
from sqlalchemy.orm import Session
from ..repository import blog as repository_blog
from blog.utils.oauth2password import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowAllBlogs])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return repository_blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return repository_blog.create_blog(db, blog)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBloG)
def show(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return repository_blog.show_blog(db, id)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return repository_blog.delete_blog(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, blog: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return repository_blog.update_blog(db, id, blog)
