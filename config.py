from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App
    APP_TITLE:   str = "E-Commerce API"
    APP_VERSION: str = "1.0.0"
    DEBUG:       bool = True

    # Database
    DATABASE_URL: str = "sqlite:///./ecommerce.db"

    # JWT
    SECRET_KEY:                  str = "change-this-key"
    ALGORITHM:                   str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # CORS
    ALLOWED_ORIGINS: str = "*"

    # First admin (optional)
    FIRST_ADMIN_EMAIL:    str = "admin@example.com"
    FIRST_ADMIN_PASSWORD: str = "admin123"
    FIRST_ADMIN_NAME:     str = "Admin"

    class Config:
        env_file = ".env"          # reads from .env automatically
        env_file_encoding = "utf-8"

settings = Settings()
