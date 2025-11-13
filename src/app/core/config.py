from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Real Estate Monitor"
    debug: bool = True

    # Database settings
    postgres_user: str = Field(default="appuser")
    postgres_password: str = Field(default="secretpassword")
    postgres_db: str = Field(default="realestate")
    postgres_host: str = Field(default="db")
    postgres_port: int = Field(default=5432)

    # Redis settings
    redis_host: str = Field(default="redis")
    redis_port: int = Field(default=6379)

    # Backend settings
    backend_port: int = Field(default=8000)

    # PgAdmin (opcjonalne)
    pgadmin_default_email: str = Field(default="admin@example.com")
    pgadmin_default_password: str = Field(default="admin123")

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    @property
    def database_url(self) -> str:
        """Konstruuje async URL do bazy danych PostgreSQL (dla FastAPI)"""
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    @property
    def async_database_url(self) -> str:
        """Alias dla database_url - dla kompatybilności z db.py"""
        return self.database_url

    @property
    def sync_db_url(self) -> str:
        """Konstruuje synchroniczny URL do bazy danych PostgreSQL (dla Alembic)"""
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


settings = Settings()
