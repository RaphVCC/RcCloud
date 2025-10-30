"""Business logic for Fitness.

Placeholder for future macro/kcal calculations and validations.
"""

from __future__ import annotations

from typing import Dict


def summarize_meal(meal: Dict[str, float]) -> Dict[str, float]:
    """Return a simple summary. Extend in the future as needed."""
    return {
        "kcal": float(meal.get("kcal", 0.0)),
        "protein": float(meal.get("protein", 0.0)),
        "carbs": float(meal.get("carbs", 0.0)),
        "fat": float(meal.get("fat", 0.0)),
    }


