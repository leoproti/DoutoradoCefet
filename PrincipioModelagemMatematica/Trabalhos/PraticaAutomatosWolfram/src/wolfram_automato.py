import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def rule_to_lookup(rule: int) -> np.ndarray:
    if rule < 0 or rule > 255:
        raise ValueError("rule must be in [0, 255]")
    bits = np.array([(rule >> i) & 1 for i in range(8)], dtype=np.uint8)
    # Map neighborhood 111..000 to outputs. Index is binary value of neighborhood.
    # For neighborhood n (0..7), output is bit n from rule representation.
    return bits


def initial_state(width: int, mode: str, density: float, grouped: bool, seed: int | None) -> np.ndarray:
    if width <= 0:
        raise ValueError("width must be > 0")
    if not (0.0 <= density <= 1.0):
        raise ValueError("density must be in [0, 1]")

    state = np.zeros(width, dtype=np.uint8)
    rng = np.random.default_rng(seed)

    if mode == "single":
        state[width // 2] = 1
        return state

    if grouped:
        n_occ = int(round(density * width))
        n_occ = max(0, min(width, n_occ))
        if n_occ > 0:
            start = (width - n_occ) // 2
            state[start : start + n_occ] = 1
    else:
        state = (rng.random(width) < density).astype(np.uint8)

    return state


def evolve(rule: int, init: np.ndarray, steps: int) -> np.ndarray:
    if steps <= 0:
        raise ValueError("steps must be > 0")

    lookup = rule_to_lookup(rule)
    width = init.size
    grid = np.zeros((steps, width), dtype=np.uint8)
    grid[0] = init

    for t in range(1, steps):
        left = np.roll(grid[t - 1], 1)
        center = grid[t - 1]
        right = np.roll(grid[t - 1], -1)
        neighborhood = (left << 2) | (center << 1) | right
        grid[t] = lookup[neighborhood]

    return grid


def plot_grid(grid: np.ndarray, rule: int, show: bool, save_fig: Path | None) -> None:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(grid, cmap="binary", interpolation="nearest", aspect="auto")
    ax.set_title(f"Automato de Wolfram - Regra {rule}")
    ax.set_xlabel("Sitio")
    ax.set_ylabel("Tempo")
    plt.tight_layout()

    if save_fig is not None:
        save_fig.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_fig, dpi=150)

    if show:
        plt.show()
    else:
        plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Automatos celulares elementares de Wolfram")
    parser.add_argument("--rule", type=int, required=True, help="Regra de Wolfram (0..255)")
    parser.add_argument("--width", type=int, default=151, help="Numero de sitios")
    parser.add_argument("--steps", type=int, default=120, help="Numero de passos temporais")
    parser.add_argument(
        "--initial",
        choices=["single", "random"],
        default="single",
        help="Estado inicial: single (um sitio ocupado) ou random",
    )
    parser.add_argument(
        "--density",
        type=float,
        default=0.5,
        help="Densidade inicial de sitios ocupados para modo random",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--grouped", action="store_true", help="Sitios ocupados agrupados")
    group.add_argument("--spread", action="store_true", help="Sitios ocupados espalhados")
    parser.add_argument("--seed", type=int, default=None, help="Semente aleatoria")
    parser.add_argument("--save-fig", type=Path, default=None, help="Caminho para salvar figura")
    parser.add_argument("--save-grid", type=Path, default=None, help="Caminho para salvar matriz (csv)")
    parser.add_argument("--no-show", action="store_true", help="Nao abre janela do grafico")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    grouped = True
    if args.spread:
        grouped = False

    init = initial_state(
        width=args.width,
        mode=args.initial,
        density=args.density,
        grouped=grouped,
        seed=args.seed,
    )
    grid = evolve(rule=args.rule, init=init, steps=args.steps)

    if args.save_grid is not None:
        args.save_grid.parent.mkdir(parents=True, exist_ok=True)
        np.savetxt(args.save_grid, grid, fmt="%d", delimiter=",")

    plot_grid(grid=grid, rule=args.rule, show=not args.no_show, save_fig=args.save_fig)


if __name__ == "__main__":
    main()
