"""NutritionInfo model"""

from pydantic import BaseModel


class NutritionInfo(BaseModel):
    """Model representing a Nutrition info
    Attributes:
        id_nutrition_info: int
        sugar: float
        calories: float
        protein: float
        fat: float
        carbohydrates: float
    """

    id_nutrition_info: int
    sugar: float
    calories: float
    protein: float
    fat: float
    carbohydrates: float
