from __future__ import annotations

from app.dto.automata_dto import SimulationRequestDTO, SimulationResponseDTO
from app.mappers.automata_mapper import request_dto_to_model, result_model_to_response_dto
from app.services.automata_service import AutomataService


class AutomataController:
    def __init__(self, service: AutomataService | None = None) -> None:
        self.service = service or AutomataService()

    def simulate(self, payload: SimulationRequestDTO) -> SimulationResponseDTO:
        params = request_dto_to_model(payload)
        result = self.service.simulate(params)
        return result_model_to_response_dto(result)
