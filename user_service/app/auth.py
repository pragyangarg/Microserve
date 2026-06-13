from fastapi import HTTPException
from fastapi import Depends

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from .jwt_handler import verify_token

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    username = verify_token(token)

    if not username:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return username
