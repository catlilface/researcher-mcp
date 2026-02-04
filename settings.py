from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
import os


class Settings(BaseSettings):
    arxiv_base_url: Optional[str] = Field(
        default_factory=lambda: os.getenv("ARXIV_BASE_URL")
    )
    pubmed_base_url: Optional[str] = Field(
        default_factory=lambda: os.getenv("PUBMED_BASE_URL")
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


# Create a singleton instance
settings = Settings()


# Maintain backward compatibility
def get_settings() -> Settings:
    return settings
