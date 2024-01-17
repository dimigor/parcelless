import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    """
    Default values for the configuration. To override
    any value, put it into a ".env" file or export it.
    """

    model_config: SettingsConfigDict = SettingsConfigDict(env_file=os.getenv("ENV_FILE"))

    OPENAPI_URL: str = ""

    # Sentry
    SENTRY_DSN: str = ""

    # Sendcloud App Configuration
    SENDCLOUD_API_KEY: str = ""
    SENDCLOUD_API_SECRET: str = ""


@lru_cache()
def get_config():
    app_config = AppConfig()
    return app_config


config = get_config()
