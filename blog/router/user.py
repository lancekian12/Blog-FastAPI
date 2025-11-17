from fastapi import Depends, status, HTTPException, APIRouter, Response
from sqlalchemy.orm import Session

from ..schemas import schemas
from ..models import models
from ..database import get_db
from ..utils.security import Hash

router = APIRouter()

@router.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=['users'])
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=Hash.bcrypt_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser, tags=['users'])
def show_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not found")
    return user