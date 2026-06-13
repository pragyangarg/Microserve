from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.auth import get_current_user
from fastapi import Depends

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

    return {
        "username": current_user,
        "service": "user-service"
    }   