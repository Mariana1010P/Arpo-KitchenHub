"""
This module configures and manages the database connection using Peewee ORM.
"""

import os
from dotenv import load_dotenv
from peewee import Model, MySQLDatabase, AutoField, CharField  # type: ignore
from config.settings import DATABASE

# Load environment variables from a .env file
load_dotenv()

print(DATABASE)

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)


# pylint: disable=too-few-public-methods
class UserModel(Model):
    """
    UserModel class for representing the 'user' table in the database.

    Attributes:
        id_user (AutoField): The unique identifier for the user.
        username (CharField): The username of the user.
        name (CharField): The name of the user.
        lastname (CharField): The lastname of the user.
        email (CharField): The email address of the user.
        password (CharField): The password of the user.
        profile_picture (CharField): The profile picture of the user.
        type_user (CharField): The type of user (admin or user).

    """

    id_user = AutoField(primary_key=True)
    username = CharField(max_length=50, unique=True)
    name = CharField(max_length=80)
    lastname = CharField(max_length=80)
    email = CharField(max_length=255)
    password = CharField(max_length=50)
    profile_picture = CharField(max_length=255, null=True)
    type_user = CharField(max_length=80)

    class Meta:
        """
        Meta class for the 'user' table in the database.

        Attributes:
            database (MySQLDatabase): The database connection used by the model.
            table_name (str): The name of the table in the database.
        """

        database = database
        table_name = "user"
