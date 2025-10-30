"""RcCloud FastAPI backend entrypoint."""

from __future__ import annotations

from fastapi import FastAPI

from rc_cloud.core.logger import configure_logging
from rc_cloud.core.security import verify_token
from rc_cloud.database import Base, engine
from rc_cloud.modules.fitness import routes as fitness_routes
from rc_cloud.modules.finance import routes as finance_routes
from rc_cloud.modules.automations import router as automations_router


configure_logging()

app = FastAPI(title="RcCloud")


# Auth middleware
app.middleware("http")(verify_token)


# Routers
app.include_router(fitness_routes.router)
app.include_router(finance_routes.router)
app.include_router(automations_router)


@app.on_event("startup")
def on_startup():
    # Simple bootstrap: create tables if not present
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "ok"}


