from __future__ import annotations

from fastapi import APIRouter

from app.controllers.automata_controller import AutomataController
from app.dto.automata_dto import SimulationRequestDTO, SimulationResponseDTO


router = APIRouter(prefix="/automata", tags=["automata"])
controller = AutomataController()


@router.post("/simulate", response_model=SimulationResponseDTO)
def simulate(payload: SimulationRequestDTO) -> SimulationResponseDTO:
    return controller.simulate(payload)
