from __future__ import annotations

import numpy as np

from app.models.automata_model import AutomataSimulationParams, AutomataSimulationResult


class AutomataService:
    def _rule_to_binary(self, rule: int) -> np.ndarray:
        return np.array([int(bit) for bit in f"{rule:08b}"])

    def _initial_state(
        self,
        size: int,
        kind: str = "Central",
        density: float = 0.5,
        grouped: bool = False,
    ) -> np.ndarray:
        state = np.zeros(size, dtype=int)
        if kind == "Central":
            state[size // 2] = 1
        elif kind == "Aleatorio":
            k = int(density * size)
            if k <= 0:
                return state
            if grouped:
                start = np.random.randint(0, size - k + 1)
                state[start:start + k] = 1
            else:
                occupied = np.random.choice(size, k, replace=False)
                state[occupied] = 1
        return state

    def _apply_rule(self, state: np.ndarray, rule_binary: np.ndarray) -> np.ndarray:
        size = len(state)
        new_state = np.zeros(size, dtype=int)
        for i in range(size):
            left = state[(i - 1) % size]
            center = state[i]
            right = state[(i + 1) % size]
            pattern = (left << 2) | (center << 1) | right
            new_state[i] = rule_binary[7 - pattern]
        return new_state

    def simulate(self, params: AutomataSimulationParams) -> AutomataSimulationResult:
        rule_binary = self._rule_to_binary(params.rule)
        state = self._initial_state(
            size=params.size,
            kind=params.initial_kind,
            density=params.density,
            grouped=params.grouped,
        )

        evolution = [state.copy()]
        for _ in range(params.steps):
            state = self._apply_rule(state, rule_binary)
            evolution.append(state.copy())

        return AutomataSimulationResult(
            rule=params.rule,
            size=params.size,
            steps=params.steps,
            initial_kind=params.initial_kind,
            density=params.density,
            grouped=params.grouped,
            evolution=np.array(evolution).astype(int).tolist(),
        )
