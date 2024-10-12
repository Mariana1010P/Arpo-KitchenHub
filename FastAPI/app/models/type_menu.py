""" TypeMenu model """

from pydantic import BaseModel


class TypeMenu(BaseModel):
    """Model representing a type menu
    Attributes:
        id_typeMenu: int
        name: str
        type: str
    """

    id_typeMenu: int
    name: str
    type: str
