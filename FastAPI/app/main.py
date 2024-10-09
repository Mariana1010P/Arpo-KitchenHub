"""Main module."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse
from helpers.api_key_auth import get_api_key
from routes.user_route import user_router
from config.database import database as connection


@asynccontextmanager
async def manage_lifespan(_app: FastAPI):
    """
    Manage the lifespan of the FastAPI application.

    Args:
        _app (FastAPI): The FastAPI application.

    Yields:
        None
    """
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        await connection.is_closed()
        connection.close()


app = FastAPI(
    title="Arpo's KitchenHub",
    version="1.0",
    contact={
        "url": "https://github.com/Mariana1010P/Arpo-KitchenHub",
    },
    description="""
    Arpo's KitchenHub API

    ## Contactos:

    - **Mariana Portela Escobar**
    - **Sebastian Arce Pareja**
    - **Juan Felipe Giraldo Rodriguez**
    """,
    lifespan=manage_lifespan,
)


@app.get("/", include_in_schema=False)
def read_root():
    """
    Redirects to the Swagger UI documentation.
    """
    return RedirectResponse(url="/docs")


app.include_router(
    user_router,
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_api_key)],
)
