"""UserGroup model"""

from pydantic import BaseModel


class UserGroup(BaseModel):
    """Model representing an user group
    Attributes:
        id_user: int
        id_group: int
    """

    id_user: int
    id_group: int
