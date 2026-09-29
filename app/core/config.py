
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "E-Commerce RAG AI Service"

    APP_ENV: str = "development"

    DEBUG: bool = False

    CHROMA_PERSIST_DIR: str = "./storage/chroma"

    CHROMA_COLLECTION_NAME: str = "ecommerce_products"

    EMBEDDING_MODEL: str = (
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    LLM_API_KEY: str = ""

    LLM_MODEL: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
