from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Real Estate Monitor"
    debug: bool = True
    database_url: str = "postgresql://appuser:secretpassword@db:5432/realestate"

    class Config:
        env_file = ".env"


settings = Settings()
