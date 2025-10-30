"""API routes for Automations."""

from __future__ import annotations

from fastapi import APIRouter


router = APIRouter(prefix="/automations", tags=["Automations"])


@router.get("/")
def list_automations():
    return {"automations": []}


