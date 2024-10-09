"""
This module contains the definition of the User class,
which represents an user schema using Pydantic.

The User class includes attributes such as id_user, username,
name, lastname, email, password, profile_picture, and type_user.
"""

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
