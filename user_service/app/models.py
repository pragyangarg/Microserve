from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from .database import Base


class UserProfile(Base):

    __tablename__ = "user_profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True
    )

    full_name = Column(String)

    bio = Column(String)

    city = Column(String)