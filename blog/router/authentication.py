from fastapi import APIRouter, Depends, HTTPException, status
from ..schemas import schemas
from ..database.database import get_db
from ..models import models
from sqlalchemy.orm import Session
from ..utils import security
from datetime import timedelta
from ..utils.token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

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
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
