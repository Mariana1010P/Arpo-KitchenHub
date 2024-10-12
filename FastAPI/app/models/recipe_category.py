"""RecipeCategory model"""

from pydantic import BaseModel


class RecipeCategory(BaseModel):
    """Model representing a recipe category
    Attributes:
        id_recipe: int
        id_category: int
    """

    id_recipe: int
    id_category: int
