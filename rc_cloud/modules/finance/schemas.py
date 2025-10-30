"""Pydantic schemas for Finance."""

from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel


class ExpenseCreate(BaseModel):
    date: date
    description: str
    category: str
    value: float
    source: str
    notes: Optional[str] = None


