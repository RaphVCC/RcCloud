"""Security middleware for RcCloud.

Simple bearer token check. Skips public endpoints.
"""

from __future__ import annotations

from fastapi import Request
from fastapi.responses import JSONResponse

from ..config import settings


PUBLIC_PATHS = {"/", "/health", "/docs", "/openapi.json"}


async def verify_token(request: Request, call_next):
    if request.url.path in PUBLIC_PATHS:
        return await call_next(request)

    token = request.headers.get("Authorization")
    expected = f"Bearer {settings.api_key}" if settings.api_key else None
    if not expected or token != expected:
        return JSONResponse(status_code=401, content={"error": "Unauthorized"})

    return await call_next(request)


