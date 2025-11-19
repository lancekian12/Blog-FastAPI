from fastapi import Depends, status, HTTPException, APIRouter, Response
from sqlalchemy.orm import Session
from ..schemas import schemas
from ..models import models
from ..database.database import get_db
from ..utils.security import Hash
from ..repository.user import create_user_repo, get_user_repo

router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return create_user_repo(user, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    return get_user_repo(id, db)
