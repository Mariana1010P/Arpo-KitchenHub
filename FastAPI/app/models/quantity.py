""" Quantity model """

from pydantic import BaseModel


class Quantity(BaseModel):
    """Model representing a quantity
    Attributes:
        id_quantity: int
        grammes: float
        liters: float
    """

    id_quantity: int
    grammes: float
    liters: float
