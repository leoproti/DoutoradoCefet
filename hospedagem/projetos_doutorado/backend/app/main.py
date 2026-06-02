from __future__ import annotations

from fastapi import FastAPI

from app.api.routes.automata_routes import router as automata_router
from app.api.routes.health_routes import router as health_router


app = FastAPI(title="Doutorado API", version="1.0.0")

app.include_router(health_router)
app.include_router(automata_router, prefix="/api/v1")
