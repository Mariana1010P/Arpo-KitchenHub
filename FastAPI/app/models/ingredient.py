""""Ingredient model"""

from datetime import datetime
from pydantic import BaseModel


class Ingredient(BaseModel):
    """Model representing an ingredient
    Attributes:
        id_ingredient: int
        name: str
        expiration_date: datetime
        id_nutrition_info: int
    """

    id_ingredient: int
    name: str
    expiration_date: datetime
    id_nutrition_info: int
