import pathlib
from pydantic import BaseSettings
from typing import Optional


# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    QSBI_DB_URL: Optional[str] = "sqlite:///example.db"
    QSBI_DB_URL_ASYNC: Optional[str] = "sqlite+aiosqlite:///example.db"

    class Config:
        case_sensitive = True


settings = Settings()
