"""
user_route.py
This module contains the routes for user management.
"""

from fastapi import APIRouter, Body, HTTPException, status
from models.user import User
from services.user_service import UserService

user_router = APIRouter()


@user_router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(user: User = Body(...)):
    """
    Create a new user.

    Args:
        user (User): The user object.

    Returns:
        User: The created user object.

    Raises:
        HTTPException: If the user already exists.
    """
    try:
        return UserService.create_user(user)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@user_router.get("/users")
async def get_all_users():
    """
    Get all users.

    Returns:
        list[User]: A list of user objects.
    """
    return UserService.get_all_users()


@user_router.get("/user/{id_user}")
async def get_user_by_id(id_user: int):
    """
    Get a user by its ID.

    Args:
        id_user (int): The ID of the user.

    Returns:
        User: The user object.

    Raises:
        HTTPException: If the user does not exist.
    """
    try:
        return UserService.get_user_by_id(id_user)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@user_router.delete("/user/{id_user}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id_user: int):
    """
    Delete a user.

    Args:
        id_user (int): The ID of the user.

    Raises:
        HTTPException: If the user does not exist.
    """
    try:
        UserService.delete_user(id_user)
        return None
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@user_router.put("/user/{id_user}")
async def update_user(id_user: int, user: User = Body(...)):
    """
    Update a user.

    Args:
        id_user (int): The ID of the user.
        user (User): The updated user object.

    Returns:
        User: The updated user object.

    Raises:
        HTTPException: If the user does not exist.
    """
    try:
        user.id_user = id_user
        updated_user = UserService.update_user(user)
        return updated_user
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
