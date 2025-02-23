from typing import Annotated

from fastapi import Depends, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from src.core import models
from src.core.database import GetDBDep
from src.services.auth import oauth2_scheme, verify_token


def get_current_user(
    db: GetDBDep, token: Annotated[str, Depends(oauth2_scheme)]
):
    email = verify_token(token)

    if not email:
        raise HTTPException(HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        raise HTTPException(HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return user

