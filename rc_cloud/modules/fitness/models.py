"""SQLAlchemy models for Fitness."""

from __future__ import annotations

from datetime import date
from sqlalchemy import Column, Integer, String, Float, Date, Text

from database import Base


class Meal(Base):
    __tablename__ = "fitness_meals"

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=date.today)
    meal = Column(String)
    kcal = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fat = Column(Float)
    notes = Column(Text)


class Workout(Base):
    __tablename__ = "fitness_workouts"

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=date.today)
    exercise = Column(String)
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float)
    notes = Column(Text)


class Weight(Base):
    __tablename__ = "fitness_weights"

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=date.today)
    weight = Column(Float)


