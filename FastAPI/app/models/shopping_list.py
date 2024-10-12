"""ShoppingList model"""

from datetime import datetime
from pydantic import BaseModel


class ShoppingList(BaseModel):
    """Model representing a shopping list
    id_shopping_list: int
    status: bool
    total_items: int
    creation_date: datetime
    id_user: int
    id_quantity: int
    id_ingredient: int
    """

    id_shopping_list: int
    status: bool
    total_items: int
    creation_date: datetime
    id_user: int
    id_quantity: int
    id_ingredient: int
