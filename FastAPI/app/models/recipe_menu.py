""" """

from pydantic import BaseModel


class RecipeMenu(BaseModel):
    """Model representing a recipe menu
    Attributes:
        id_recipe: int
        id_menu: int
    """

    id_recipe: int
    id_menu: int
