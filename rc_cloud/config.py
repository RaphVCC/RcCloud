"""Configuration module for RcCloud.

Loads environment variables and provides centralized settings.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

try:
    # Load from a local .env if present (useful for local dev)
    from dotenv import load_dotenv  # type: ignore

    load_dotenv()
except Exception:
    # dotenv is optional in production on Render where env vars are provided
    pass


@dataclass(frozen=True)
class Settings:
    database_url: str
    api_key: Optional[str]
    google_sheet_id: Optional[str]
    log_level: str

    @staticmethod
    def from_env() -> "Settings":
        database_url = os.getenv("DATABASE_URL", "")
        if not database_url:
            # Intentionally allow empty to enable import in tools; runtime should provide it
            pass

        return Settings(
            database_url=database_url,
            api_key=os.getenv("API_KEY"),
            google_sheet_id=os.getenv("GOOGLE_SHEET_ID"),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
        )


settings = Settings.from_env()


