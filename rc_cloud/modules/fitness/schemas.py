"""Pydantic schemas for Fitness."""

from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel


class MealCreate(BaseModel):
    date: date
    meal: str
    kcal: float
    protein: float
    carbs: float
    fat: float
    notes: Optional[str] = None


class WorkoutCreate(BaseModel):
    date: date
    exercise: str
    sets: int
    reps: int
    weight: float
    notes: Optional[str] = None


class WeightCreate(BaseModel):
    date: date
    weight: float


