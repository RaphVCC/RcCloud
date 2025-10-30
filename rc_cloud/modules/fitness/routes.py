"""API routes for Fitness."""

from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .models import Meal, Workout, Weight
from .schemas import MealCreate, WorkoutCreate, WeightCreate
from rc_cloud.core.helpers import safe_model_dump
from rc_cloud.database import get_db
from rc_cloud.google_sheets import update_sheet


router = APIRouter(prefix="/fitness", tags=["Fitness"])


@router.post("/meal")
def add_meal(meal: MealCreate, db: Session = Depends(get_db)):
    new_meal = Meal(**safe_model_dump(meal))
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    update_sheet("Refeições", [safe_model_dump(meal).values()])
    return {"status": "ok", "message": "Meal added", "id": new_meal.id}


@router.post("/workout")
def add_workout(workout: WorkoutCreate, db: Session = Depends(get_db)):
    new_workout = Workout(**safe_model_dump(workout))
    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)
    update_sheet("Treinos", [safe_model_dump(workout).values()])
    return {"status": "ok", "message": "Workout added", "id": new_workout.id}


@router.post("/weight")
def add_weight(weight: WeightCreate, db: Session = Depends(get_db)):
    new_weight = Weight(**safe_model_dump(weight))
    db.add(new_weight)
    db.commit()
    db.refresh(new_weight)
    update_sheet("Pesagens", [safe_model_dump(weight).values()])
    return {"status": "ok", "message": "Weight added", "id": new_weight.id}


