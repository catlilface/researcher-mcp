import os
from typing import Optional


class Settings:
    def __init__(self):
        self.arxiv_base_url: Optional[str] = os.getenv("ARXIV_BASE_URL")
        self.pubmed_base_url: Optional[str] = os.getenv("PUBMED_BASE_URL")

    @classmethod
    def get_settings(cls) -> "Settings":
        return cls()
