from typing import list
from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    server_host: str
    server_port: int
    base_url: AnyHttpUrl
    db_url: str
    backend_cors_origins: list[AnyHttpUrl]

    class Config(BaseSettings.Config):  # noqa: WPS431
        env_file = ".env"


def get_settings():
    return Settings()
