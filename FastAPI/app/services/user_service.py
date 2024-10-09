"""
Module for user service class and methods for user management.
"""

from peewee import DoesNotExist
from config.database import UserModel


class UserService:
    """
    Service class for handling user-related operations.

    Methods:
        create_user(user: UserModel): Create a new user in the database.
        get_user_by_id(id_user: int): Get a user by its ID.
        get_all_users(): Get all users from the database.
        update_user(user: UserModel): Update a user in the database.
        delete_user(user: UserModel): Delete a user from the database.

    Raises:
        ValueError: If the user already exists.
        DoesNotExist: If the user does not exist.
    """

    @staticmethod
    def create_user(user_data: UserModel) -> UserModel:
        """
        Create a new user in the database.

        Args:
            user_data (UserModel): The user object to be created.

        Returns:
            UserModel: The created user object.

        Raises:
            ValueError: If the user already exists.
        """
        if UserModel.select().where(UserModel.username == user_data.username).exists():
            raise ValueError("User already exists")

        new_user = UserModel(
            username=user_data.username,
            name=user_data.name,
            lastname=user_data.lastname,
            email=user_data.email,
            password=user_data.password,
            profile_picture=user_data.profile_picture,
            type_user=user_data.type_user,
        )
        new_user.save()
        return new_user

    @staticmethod
    def get_user_by_id(id_user: int) -> UserModel:
        """
        Get a user by its ID.

        Args:
            id_user (int): The ID of the user.

        Returns:
            UserModel: The user object.

        Raises:
            DoesNotExist: If the user does not exist.
        """
        try:
            return UserModel.get(UserModel.id_user == id_user)
        except DoesNotExist as exc:
            raise ValueError("User does not exist") from exc

    @staticmethod
    def get_all_users() -> list[UserModel]:
        """
        Get all users from the database.

        Returns:
            list[UserModel]: A list of user objects.
        """
        return list(UserModel.select())

    @staticmethod
    def update_user(user_data: UserModel) -> UserModel:
        """
        Update a user in the database.

        Args:
            user_data (UserModel): The user object to be updated.

        Returns:
            UserModel: The updated user object.

        Raises:
            DoesNotExist: If the user does not exist.
        """
        try:
            existing_user = UserModel.get(UserModel.id_user == user_data.id_user)
            existing_user.username = user_data.username
            existing_user.name = user_data.name
            existing_user.lastname = user_data.lastname
            existing_user.email = user_data.email
            existing_user.password = user_data.password
            existing_user.profile_picture = user_data.profile_picture
            existing_user.type_user = user_data.type_user
            existing_user.save()
            return existing_user
        except DoesNotExist as exc:
            raise ValueError("User does not exist") from exc

    @staticmethod
    def delete_user(id_user: int) -> None:
        """
        Delete a user from the database.

        Args:
            user (UserModel): The user object to be deleted.

        Raises:
            DoesNotExist: If the user does not exist.
        """
        try:
            user = UserModel.get(UserModel.id_user == id_user)
            user.delete_instance()
            return True
        except DoesNotExist as exc:
            raise ValueError("User does not exist") from exc
