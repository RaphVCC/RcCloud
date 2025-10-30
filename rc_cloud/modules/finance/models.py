"""SQLAlchemy models for Finance."""

from __future__ import annotations

from datetime import date
from sqlalchemy import Column, Integer, String, Float, Date, Text

from database import Base


class Expense(Base):
    __tablename__ = "finance_expenses"

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=date.today)
    description = Column(String)
    category = Column(String)
    value = Column(Float)
    source = Column(String)
    notes = Column(Text)


