"""Category model"""

from pydantic import BaseModel


class Category(BaseModel):
    """Model representing a category
    Attributes:
        id_category: int
        name: str
        description: str
    """

    id_category: int
    name: str
    description: str
