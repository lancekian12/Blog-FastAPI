from typing import List
from fastapi import APIRouter, Depends, Response, status, HTTPException
from blog.schemas import schemas
from ..schemas import schemas
from ..models import models
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/blog', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowAllBlogs], tags=['blogs'] )
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBloG, tags=['blogs'])
def show(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(
        models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not found")
    return blog


@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def delete(id: int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id ==
                                 id).delete(synchronize_session=False)
    db.commit()
    return 'done'


@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED , tags=['blogs'])
def update(id: int, blog: schemas.Blog, db: Session = Depends(get_db)):
    updated_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not updated_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not found")
    updated_blog.update({'title': blog.title, 'body': blog.body})
    db.commit()
    return 'updated'