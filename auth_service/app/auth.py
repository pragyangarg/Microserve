from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from .jwt_handler import verify_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    username = verify_token(token)

    if not username:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return username