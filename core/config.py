import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus
from pydantic_settings import BaseSettings

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    # Database

    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # JWT
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("JWT_TOKEN_EXPIRE_MINUTES")


def get_settings() -> Settings:
    return Settings()
