from pydantic_settings import BaseSettings
from typing import ClassVar

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY : ClassVar[str] = "wefregbhtn"

    class Config:
        env_file = ".env"
        extra = 'ignore'

settings = Settings()