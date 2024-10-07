""" User model """

from pydantic import BaseModel


class User(BaseModel):
    """Model representing an user
    Attributes:
        id_user: int
        username: str
        name: str
        lastname: str
        email: str
        password: str
        profile_picture: str
        type_user: str
    """

    id_user: int
    username: str
    name: str
    lastname: str
    email: str
    password: str
    profile_picture: str
    type_user: str
