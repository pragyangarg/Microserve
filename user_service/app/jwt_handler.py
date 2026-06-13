from jose import jwt
from jose import JWTError

SECRET_KEY = "super-secret-key"

ALGORITHM = "HS256"


def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        return username

    except JWTError:

        return None