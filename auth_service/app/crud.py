from sqlalchemy.orm import Session

from .models import User
from .security import hash_password


def create_user(
    db: Session,
    username: str,
    email: str,
    password: str
):
    hashed_password = hash_password(password)

    user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def get_user_by_username(
    db: Session,
    username: str
):
    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )