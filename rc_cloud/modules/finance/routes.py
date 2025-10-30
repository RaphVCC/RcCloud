"""API routes for Finance."""

from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .models import Expense
from .schemas import ExpenseCreate
from rc_cloud.core.helpers import safe_model_dump
from rc_cloud.database import get_db
from rc_cloud.google_sheets import update_sheet


router = APIRouter(prefix="/finance", tags=["Finance"])


@router.post("/expense")
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(**safe_model_dump(expense))
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    update_sheet("Despesas", [safe_model_dump(expense).values()])
    return {"status": "ok", "message": "Expense added", "id": new_expense.id}


