from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from .database import engine
from .database import get_db

from .models import Base

from .schemas import UserCreate
from .schemas import UserLogin

from .crud import create_user
from .crud import get_user_by_username

from .security import verify_password

from .jwt_handler import create_access_token

from .auth import get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():

    return {
        "message": "Auth Service Running"
    }


@app.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_username(
        db,
        user.username
    )

    if existing_user:

        raise HTTPException(
            status_code=409,
            detail="Username already exists"
        )

    create_user(
        db,
        user.username,
        user.email,
        user.password
    )

    return {
        "message": "User created"
    }


@app.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = get_user_by_username(
        db,
        user.username
    )

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {
            "sub": db_user.username
        }
    )

    return {
        "access_token": access_token
    }


@app.get("/profile")
def profile(
    current_user: str = Depends(
        get_current_user
    )
):

    return {
        "username": current_user
    }