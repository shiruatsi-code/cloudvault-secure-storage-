from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CloudVault"
    app_env: str = "development"
    debug: bool = True

    database_url: str = (
        "postgresql://cloudvault_user:change_me@database:5432/cloudvault"
    )

    secret_key: str = "replace_with_a_long_random_secret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    aws_region: str = "us-east-1"
    aws_s3_bucket: str = "cloudvault-development"

    max_upload_size_mb: int = 25
    allowed_file_types: str = "pdf,jpg,jpeg,png,txt,csv,docx,xlsx"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
