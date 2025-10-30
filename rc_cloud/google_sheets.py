"""Google Sheets integration for RcCloud.

Provides a thin wrapper to append rows to a worksheet using a service
account `credentials.json`. Errors are logged but do not crash the app.
"""

from __future__ import annotations

import os
from datetime import date, datetime
from typing import Iterable, List, Sequence

from .config import settings

try:
    import gspread  # type: ignore
    from google.oauth2.service_account import Credentials  # type: ignore
except Exception:  # pragma: no cover - optional import in tooling contexts
    gspread = None  # type: ignore
    Credentials = None  # type: ignore


_CLIENT = None


def _ensure_client():
    global _CLIENT
    if _CLIENT is not None:
        return _CLIENT
    if gspread is None or Credentials is None:
        return None

    creds_path = os.path.join(os.path.dirname(__file__), "credentials.json")
    if not os.path.exists(creds_path):
        # Also try CWD (Render Secret File may mount differently)
        alt = os.path.join(os.getcwd(), "credentials.json")
        creds_path = alt if os.path.exists(alt) else creds_path

    try:
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(creds_path, scopes=scopes)
        _CLIENT = gspread.authorize(creds)
        return _CLIENT
    except Exception:
        return None


def _normalize_cell(value):
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if value is None:
        return ""
    return str(value)


def _normalize_rows(values: Iterable[Sequence]) -> List[List[str]]:
    rows: List[List[str]] = []
    for row in values:
        # Accept dict_values or any iterable
        if not isinstance(row, (list, tuple)):
            try:
                row = list(row)  # type: ignore
            except Exception:
                row = [row]  # type: ignore
        rows.append([_normalize_cell(v) for v in row])
    return rows


def update_sheet(sheet_name: str, values: Iterable[Sequence]) -> bool:
    """Append rows to the given worksheet name.

    Returns True on success, False if skipped or failed.
    """
    try:
        if not settings.google_sheet_id:
            return False
        client = _ensure_client()
        if client is None:
            return False

        sheet = client.open_by_key(settings.google_sheet_id)
        ws = sheet.worksheet(sheet_name)
        rows = _normalize_rows(values)
        if not rows:
            return False
        ws.append_rows(rows)
        return True
    except Exception:
        # Intentionally swallow to avoid impacting primary flow
        return False


