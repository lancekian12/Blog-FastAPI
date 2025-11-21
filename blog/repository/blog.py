from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create_blog(db: Session, blog):
    new_blog = models.Blog(title=blog.title, 
                           body=blog.body, user_id=1
                           )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show_blog(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not found")
    return blog

def delete_blog(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update_blog(db: Session, id: int, blog):
    updated_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not updated_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not found")
    updated_blog.update({'title': blog.title, 'body': blog.body})
    db.commit()
    return 'updated'