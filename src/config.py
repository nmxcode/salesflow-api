from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# پیدا کردن مسیر ریشه پروژه
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    DATABASE_URL: str
    APP_NAME: str = "SalesFlow API"
    DEBUG: bool = True


settings = Settings()