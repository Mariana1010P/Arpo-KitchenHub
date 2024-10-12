"""Rol model"""

from pydantic import BaseModel


class Rol(BaseModel):
    """Model representing a rol
    Attributes:
        id_rol: int
        name: str
    """

    id_rol: int
    name: str
