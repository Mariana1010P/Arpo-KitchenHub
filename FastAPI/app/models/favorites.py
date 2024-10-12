"""Favorites model"""

from pydantic import BaseModel


class Favorites(BaseModel):
    """Model representing a favorite
    Attributes:
        id_favorites: int
        id_user: int
        id_recipe: int
    """

    id_favorites: int
    id_user: int
    id_recipe: int
