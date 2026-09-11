from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    db_connection: str
    secret_key: str
    algorithm: str
    expire_time: int

settings = Settings()