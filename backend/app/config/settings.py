from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool

    # Server
    HOST: str
    PORT: int

    # Database
    DATABASE_URL: str

    # JWT Authentication
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()