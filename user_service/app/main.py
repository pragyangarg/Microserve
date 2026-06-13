from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.auth import get_current_user
from fastapi import Depends

from app.cache import redis_client
import json


Base.metadata.create_all(
    bind=engine
)

app = FastAPI()


@app.get("/")
def root():

    return {
        "service": "User Service Running"
    }



@app.get("/me")
def me(
    current_user: str = Depends(
        get_current_user
    )
):

    cached_user = redis_client.get(
        current_user
    )

    if cached_user:

        print("CACHE HIT")

        return json.loads(
            cached_user
        )

    print("CACHE MISS")

    user_data = {
        "username": current_user,
        "service": "user-service"
    }

    redis_client.set(
        current_user,
        json.dumps(user_data),
        ex=60
    )

    return user_data