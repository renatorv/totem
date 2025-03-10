from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    DATA_BASE: str
    SECRET_KEY: str
    REFRESH_SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

config = Config()
