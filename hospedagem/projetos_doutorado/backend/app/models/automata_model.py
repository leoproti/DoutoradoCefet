from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AutomataSimulationParams:
    rule: int
    size: int
    steps: int
    initial_kind: str
    density: float
    grouped: bool


@dataclass(frozen=True)
class AutomataSimulationResult:
    rule: int
    size: int
    steps: int
    initial_kind: str
    density: float
    grouped: bool
    evolution: list[list[int]]
