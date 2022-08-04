from api.routers.base import api_router
from core.config import settings
from db.database import Base, engine
from fastapi import FastAPI


def include_router(app):
    """Include all routers"""
    app.include_router(api_router)


def create_app():
    """Create the app"""
    app = FastAPI(
        title="FastAPI + Tortoise ORM + Template",
    )
    include_router(app)
    # TODO: add fastapi tortoise register

    @app.get("/")
    def _root():  # noqa: WPS430 because this is a small test code
        """Root route"""
        return {"Ping": "Pong"}

    return app


app = create_app()
