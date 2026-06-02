from __future__ import annotations

import argparse
from pathlib import Path

from .fraud import load_tabular_dataset, save_fraud_outputs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analise inicial de fraude e anomalias em GTAs."
    )
    parser.add_argument("--input", required=True, help="Caminho para o arquivo CSV ou Excel de entrada.")
    parser.add_argument("--output", default="outputs/fraud", help="Diretorio de saida das tabelas de fraude.")
    parser.add_argument(
        "--date-column",
        default=None,
        help="Nome da coluna de data ou data-hora de emissao.",
    )
    parser.add_argument(
        "--id-columns",
        nargs="*",
        default=[],
        help="Colunas de identificacao documental para checagem de duplicidade.",
    )
    parser.add_argument(
        "--entity-columns",
        nargs="*",
        default=[],
        help="Colunas como emitente, produtor, propriedade, municipio ou destino.",
    )
    parser.add_argument(
        "--numeric-columns",
        nargs="*",
        default=[],
        help="Colunas numericas como quantidade, distancia, valor ou peso.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    frame = load_tabular_dataset(args.input)
    notes = save_fraud_outputs(
        frame=frame,
        output_dir=args.output,
        id_columns=args.id_columns,
        entity_columns=args.entity_columns,
        numeric_columns=args.numeric_columns,
        date_column=args.date_column,
    )

    notes_path = Path(args.output) / "fraud_notes.txt"
    notes_path.parent.mkdir(parents=True, exist_ok=True)
    notes_path.write_text("\n".join(notes), encoding="utf-8")

    print(f"Analise de fraude concluida. Resultados salvos em: {Path(args.output).resolve()}")
    print(f"Resumo inicial: {notes_path.resolve()}")


if __name__ == "__main__":
    main()