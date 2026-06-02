from __future__ import annotations

from app.dto.automata_dto import SimulationRequestDTO, SimulationResponseDTO
from app.models.automata_model import AutomataSimulationParams, AutomataSimulationResult


def normalize_initial_kind(initial_kind: str) -> str:
    return "Aleatorio" if initial_kind.lower().startswith("a") else "Central"


def request_dto_to_model(payload: SimulationRequestDTO) -> AutomataSimulationParams:
    return AutomataSimulationParams(
        rule=payload.rule,
        size=payload.size,
        steps=payload.steps,
        initial_kind=normalize_initial_kind(payload.initial_kind),
        density=payload.density,
        grouped=payload.grouped,
    )


def result_model_to_response_dto(result: AutomataSimulationResult) -> SimulationResponseDTO:
    return SimulationResponseDTO(
        rule=result.rule,
        size=result.size,
        steps=result.steps,
        initial_kind=result.initial_kind,
        density=result.density,
        grouped=result.grouped,
        evolution=result.evolution,
    )
