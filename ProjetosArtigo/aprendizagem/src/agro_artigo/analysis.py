from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def load_dataset(input_path: str | Path) -> pd.DataFrame:
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {path}")
    return pd.read_csv(path)


def numeric_columns(frame: pd.DataFrame) -> list[str]:
    return frame.select_dtypes(include=["number"]).columns.tolist()


def build_summary_table(frame: pd.DataFrame) -> pd.DataFrame:
    summary = frame.describe(include="all").transpose().reset_index()
    return summary.rename(columns={"index": "variable"})


def build_missing_table(frame: pd.DataFrame) -> pd.DataFrame:
    missing = frame.isna().sum().rename("missing_values").reset_index()
    missing.columns = ["variable", "missing_values"]
    missing["missing_rate"] = missing["missing_values"] / len(frame)
    return missing.sort_values("missing_values", ascending=False)


def build_correlation_table(frame: pd.DataFrame, target: str) -> pd.DataFrame:
    columns = numeric_columns(frame)
    if target not in columns:
        raise ValueError(f"A variavel alvo '{target}' precisa ser numerica.")

    correlation = (
        frame[columns]
        .corr(numeric_only=True)[target]
        .dropna()
        .sort_values(ascending=False)
        .reset_index()
    )
    correlation.columns = ["variable", "correlation_with_target"]
    return correlation


def save_summary_outputs(frame: pd.DataFrame, output_dir: str | Path, target: str | None = None) -> None:
    output_path = Path(output_dir)
    tables_dir = output_path / "tables"
    figures_dir = output_path / "figures"
    tables_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    build_summary_table(frame).to_csv(tables_dir / "summary.csv", index=False)
    build_missing_table(frame).to_csv(tables_dir / "missing.csv", index=False)

    numeric = numeric_columns(frame)
    if numeric:
        corr = frame[numeric].corr(numeric_only=True)
        corr.to_csv(tables_dir / "correlation_matrix.csv")

        plt.figure(figsize=(10, 7))
        sns.heatmap(corr, cmap="YlGn", annot=False)
        plt.title("Matriz de correlacao")
        plt.tight_layout()
        plt.savefig(figures_dir / "correlation_heatmap.png", dpi=200)
        plt.close()

    if target and target in numeric:
        correlation = build_correlation_table(frame, target)
        correlation.to_csv(tables_dir / "target_correlation.csv", index=False)

        top_variables = correlation.head(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(data=top_variables, x="correlation_with_target", y="variable", palette="crest")
        plt.title(f"Correlacao com {target}")
        plt.xlabel("Coeficiente de correlacao")
        plt.ylabel("Variavel")
        plt.tight_layout()
        plt.savefig(figures_dir / "target_correlation.png", dpi=200)
        plt.close()


def generate_research_notes(frame: pd.DataFrame, target: str | None = None) -> list[str]:
    notes: list[str] = []
    notes.append(f"A base contem {len(frame)} registros e {len(frame.columns)} variaveis.")

    numeric = numeric_columns(frame)
    notes.append(f"Foram identificadas {len(numeric)} variaveis numericas potencialmente utilizaveis em modelos.")

    missing = build_missing_table(frame)
    top_missing = missing.head(5)
    for _, row in top_missing.iterrows():
        if int(row["missing_values"]) > 0:
            notes.append(
                f"A variavel {row['variable']} possui {int(row['missing_values'])} valores ausentes "
                f"({row['missing_rate']:.1%} da base)."
            )

    if target and target in numeric:
        correlation = build_correlation_table(frame, target)
        for _, row in correlation.head(5).iterrows():
            notes.append(
                f"A variavel {row['variable']} apresentou correlacao de "
                f"{row['correlation_with_target']:.3f} com {target}."
            )

    return notes