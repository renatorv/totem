from typing import Annotated

from fastapi import Depends, HTTPException, Header
from starlette.status import HTTP_401_UNAUTHORIZED

from src.api.admin.services.auth import oauth2_scheme, verify_access_token
from src.core import models
from src.core.database import GetDBDep


def get_current_user(
    db: GetDBDep, token: Annotated[str, Depends(oauth2_scheme)]
):
    email = verify_access_token(token)

    if not email:
        raise HTTPException(HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        raise HTTPException(HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return user


def get_optional_user(db: GetDBDep, authorizatio: Annotated[str | None, Header()] = None):
    token = authorizatio
    if not token:
        return  None

    try:
        token_type, _, token_value = token.partition(" ")
        if token_type.lower() != "bearer" or not token_value:
            return None

        # TODO: Verificar conversão para bytes
        return get_current_user(token_value, db)
    except Exception as e:
        print(e)
        return None

GetCurrentUserDep = Annotated[models.User, Depends(get_current_user)]
GetOptionalUserDeb = Annotated[models.User | None, Depends(get_optional_user)]