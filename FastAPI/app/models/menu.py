"""Menu model"""

from pydantic import BaseModel


class Menu(BaseModel):
    """Model representing a menu
    Attributes:
        id_menu: int
        name: str
        id_typeMenu: int
    """

    id_menu: int
    name: str
    id_typeMenu: int
