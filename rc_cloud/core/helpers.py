"""Helper utilities for RcCloud."""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Dict, List


def safe_model_dump(model: Any) -> Dict[str, Any]:
    """Support Pydantic v1 (.dict) and v2 (.model_dump)."""
    if hasattr(model, "model_dump"):
        return model.model_dump()  # type: ignore[attr-defined]
    if hasattr(model, "dict"):
        return model.dict()  # type: ignore[attr-defined]
    raise TypeError("Unsupported model type for dump")


def to_values_row(data: Dict[str, Any]) -> List[str]:
    def _fmt(v: Any) -> str:
        if isinstance(v, (date, datetime)):
            return v.isoformat()
        if v is None:
            return ""
        return str(v)

    return [_fmt(v) for v in data.values()]


