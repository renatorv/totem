from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_401_UNAUTHORIZED

from src.core.database import GetDBDep

from src.services.auth import authenticate_user, create_access_token
from src.core import models

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login_for_access_token(
    db: GetDBDep,
    form_data: OAuth2PasswordRequestForm = Depends(),
):

    user: models.User | None = authenticate_user(email=form_data.username, password=form_data.password, db=db)

    if not user:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Incorrect email or password!!")

    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}

