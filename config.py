from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URL: str
    MONGO_DB_NAME: str
    MONGO_MAX_POOL_SIZE: int = 50
    MONGO_MIN_POOL_SIZE: int = 5

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()