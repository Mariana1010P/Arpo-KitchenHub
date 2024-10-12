"""Group model"""

from pydantic import BaseModel


class Group(BaseModel):
    """Model representing a group
    Attributes:
        id_group: int
        name: str
    """

    id_group: int
    name: str
