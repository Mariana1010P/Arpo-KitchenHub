"""Notification model"""

from datetime import datetime
from pydantic import BaseModel


class Notification(BaseModel):
    """Model representing a notification
    Attributes:
        id_notification: int
        message: str
        shopping_date: datetime
        id_user: int
    """

    id_notification: int
    message: str
    shopping_date: datetime
    id_user: int
