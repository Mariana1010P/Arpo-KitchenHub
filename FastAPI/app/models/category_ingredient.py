"""CategoryIngredient model"""

from pydantic import BaseModel


class CategoryIngredient(BaseModel):
    """Model representing a category ingredient
    Attributes:
        id_category_ingredient: int
        id_ingredient: int
        id_category: int
    """

    id_category_ingredient: int
    id_ingredient: int
    id_category: int
