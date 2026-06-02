from __future__ import annotations

import argparse
from pathlib import Path

from .analysis import generate_research_notes, load_dataset, save_summary_outputs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analise exploratoria para projetos de artigo com dados agropecuarios."
    )
    parser.add_argument("--input", required=True, help="Caminho para o arquivo CSV de entrada.")
    parser.add_argument(
        "--output",
        default="outputs",
        help="Diretorio de saida para tabelas e figuras.",
    )
    parser.add_argument(
        "--target",
        default=None,
        help="Nome da variavel numerica principal do estudo.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    frame = load_dataset(args.input)
    save_summary_outputs(frame, args.output, args.target)

    notes = generate_research_notes(frame, args.target)
    notes_path = Path(args.output) / "research_notes.txt"
    notes_path.parent.mkdir(parents=True, exist_ok=True)
    notes_path.write_text("\n".join(notes), encoding="utf-8")

    print(f"Analise concluida. Resultados salvos em: {Path(args.output).resolve()}")
    print(f"Notas iniciais de pesquisa: {notes_path.resolve()}")


if __name__ == "__main__":
    main()