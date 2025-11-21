from fastapi import APIRouter, Depends, HTTPException, status
from ..schemas import schemas
from ..database.database import get_db
from ..models import models
from sqlalchemy.orm import Session
from ..utils import security

router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    if not security.Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    # generate a jwt token and return it
    return user
