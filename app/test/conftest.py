import asyncio
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from app.core.config import Settings, get_settings
from main import app
from models import Users

from tortoise.contrib.test import finalizer, initializer


def get_settings_override():
    return Settings(db_url="sqlite:///:memory:")


app.dependency_overrides[get_settings] = get_settings_override


@pytest.fixture(scope="module")
def client() -> Generator:
    initializer(["models"])
    with TestClient(app) as cl:
        yield cl
    finalizer()


@pytest.fixture(scope="module")
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()


# TODO: move this test to other file


def test_create_user(client: TestClient, event_loop: asyncio.AbstractEventLoop):  # nosec
    response = client.post("/users", json={"username": "admin"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["username"] == "admin"
    assert "id" in data
    user_id = data["id"]

    async def get_user_by_db():
        user = await Users.get(id=user_id)
        return user

    user_obj = event_loop.run_until_complete(get_user_by_db())
    assert user_obj.id == user_id
