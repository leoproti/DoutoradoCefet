from __future__ import annotations

from pydantic import BaseModel, Field


class SimulationRequestDTO(BaseModel):
    rule: int = Field(default=30, ge=0, le=255)
    size: int = Field(default=101, ge=21, le=401)
    steps: int = Field(default=100, ge=1, le=1000)
    initial_kind: str = Field(default="Central")
    density: float = Field(default=0.5, ge=0.0, le=1.0)
    grouped: bool = Field(default=False)


class SimulationResponseDTO(BaseModel):
    rule: int
    size: int
    steps: int
    initial_kind: str
    density: float
    grouped: bool
    evolution: list[list[int]]
