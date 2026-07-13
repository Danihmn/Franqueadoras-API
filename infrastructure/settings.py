from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: str = "dev"
    database_url: str
    environment: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
