from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.ensemble import IsolationForest


def load_tabular_dataset(input_path: str | Path) -> pd.DataFrame:
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {path}")

    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    return pd.read_csv(path)


def build_duplicate_table(frame: pd.DataFrame, id_columns: list[str]) -> pd.DataFrame:
    if not id_columns:
        return pd.DataFrame()

    valid_columns = [column for column in id_columns if column in frame.columns]
    if not valid_columns:
        return pd.DataFrame()

    duplicated = frame[frame.duplicated(subset=valid_columns, keep=False)].copy()
    return duplicated.sort_values(valid_columns)


def build_outlier_table(frame: pd.DataFrame, numeric_columns: list[str]) -> pd.DataFrame:
    rows: list[pd.DataFrame] = []
    for column in numeric_columns:
        if column not in frame.columns:
            continue

        series = pd.to_numeric(frame[column], errors="coerce").dropna()
        if series.empty:
            continue

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        mask = pd.to_numeric(frame[column], errors="coerce").between(lower, upper, inclusive="both")
        outliers = frame[~mask.fillna(False)].copy()
        if outliers.empty:
            continue

        outliers.insert(0, "outlier_variable", column)
        outliers.insert(1, "lower_bound", lower)
        outliers.insert(2, "upper_bound", upper)
        rows.append(outliers)

    if not rows:
        return pd.DataFrame()
    return pd.concat(rows, ignore_index=True)


def build_entity_summary(frame: pd.DataFrame, entity_columns: list[str], numeric_columns: list[str]) -> pd.DataFrame:
    valid_entities = [column for column in entity_columns if column in frame.columns]
    valid_numeric = [column for column in numeric_columns if column in frame.columns]
    if not valid_entities:
        return pd.DataFrame()

    summaries: list[pd.DataFrame] = []
    for entity in valid_entities:
        grouped = frame.groupby(entity, dropna=False).size().rename("records").reset_index()
        grouped.insert(0, "entity_column", entity)

        for numeric in valid_numeric:
            series = pd.to_numeric(frame[numeric], errors="coerce")
            stats = frame.assign(**{numeric: series}).groupby(entity, dropna=False)[numeric].agg(["mean", "sum", "max"])
            stats = stats.reset_index().rename(
                columns={
                    "mean": f"{numeric}_mean",
                    "sum": f"{numeric}_sum",
                    "max": f"{numeric}_max",
                }
            )
            grouped = grouped.merge(stats, on=entity, how="left")

        summaries.append(grouped.sort_values("records", ascending=False).head(50))

    return pd.concat(summaries, ignore_index=True)


def build_temporal_flags(frame: pd.DataFrame, date_column: str | None) -> pd.DataFrame:
    if not date_column or date_column not in frame.columns:
        return pd.DataFrame()

    timestamps = pd.to_datetime(frame[date_column], errors="coerce")
    valid = frame.loc[timestamps.notna()].copy()
    if valid.empty:
        return pd.DataFrame()

    timestamps = timestamps.loc[timestamps.notna()]
    valid.insert(0, "emission_hour", timestamps.dt.hour.to_list())
    valid.insert(1, "weekday", timestamps.dt.day_name().to_list())
    valid.insert(2, "is_weekend", timestamps.dt.dayofweek.ge(5).to_list())
    valid.insert(3, "is_night", timestamps.dt.hour.isin([0, 1, 2, 3, 4, 5, 22, 23]).to_list())
    return valid[valid["is_weekend"] | valid["is_night"]].copy()


def build_model_matrix(frame: pd.DataFrame, numeric_columns: list[str], date_column: str | None) -> pd.DataFrame:
    model_frame = pd.DataFrame(index=frame.index)

    for column in numeric_columns:
        if column not in frame.columns:
            continue
        model_frame[column] = pd.to_numeric(frame[column], errors="coerce")

    if date_column and date_column in frame.columns:
        timestamps = pd.to_datetime(frame[date_column], errors="coerce")
        model_frame["emission_hour"] = timestamps.dt.hour
        model_frame["day_of_week"] = timestamps.dt.dayofweek
        model_frame["day_of_month"] = timestamps.dt.day

    model_frame = model_frame.dropna(axis=1, how="all")
    return model_frame.fillna(model_frame.median(numeric_only=True)).fillna(0)


def build_anomaly_scores(
    frame: pd.DataFrame,
    numeric_columns: list[str],
    date_column: str | None,
    contamination: float = 0.03,
) -> pd.DataFrame:
    model_matrix = build_model_matrix(frame, numeric_columns, date_column)
    if model_matrix.empty or len(model_matrix) < 10:
        return pd.DataFrame()

    model = IsolationForest(
        n_estimators=300,
        contamination=contamination,
        random_state=42,
    )
    labels = model.fit_predict(model_matrix)
    scores = model.decision_function(model_matrix)

    result = frame.copy()
    result.insert(0, "anomaly_label", labels)
    result.insert(1, "anomaly_score", scores)
    result.insert(2, "is_suspect", result["anomaly_label"].eq(-1))
    return result.sort_values(["is_suspect", "anomaly_score"], ascending=[False, True])


def save_fraud_outputs(
    frame: pd.DataFrame,
    output_dir: str | Path,
    id_columns: list[str],
    entity_columns: list[str],
    numeric_columns: list[str],
    date_column: str | None,
) -> list[str]:
    output_path = Path(output_dir)
    tables_dir = output_path / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)

    notes: list[str] = []

    duplicates = build_duplicate_table(frame, id_columns)
    duplicates.to_csv(tables_dir / "duplicate_records.csv", index=False)
    notes.append(f"Registros duplicados identificados: {len(duplicates)}.")

    outliers = build_outlier_table(frame, numeric_columns)
    outliers.to_csv(tables_dir / "numeric_outliers.csv", index=False)
    notes.append(f"Sinais de outlier numerico encontrados: {len(outliers)}.")

    entity_summary = build_entity_summary(frame, entity_columns, numeric_columns)
    entity_summary.to_csv(tables_dir / "entity_summary.csv", index=False)
    notes.append(f"Resumo por entidade gerado para {len(entity_summary)} linhas agregadas.")

    temporal_flags = build_temporal_flags(frame, date_column)
    temporal_flags.to_csv(tables_dir / "temporal_flags.csv", index=False)
    notes.append(f"Registros com padrao temporal incomum: {len(temporal_flags)}.")

    anomaly_scores = build_anomaly_scores(frame, numeric_columns, date_column)
    anomaly_scores.to_csv(tables_dir / "anomaly_scores.csv", index=False)
    suspects = int(anomaly_scores["is_suspect"].sum()) if not anomaly_scores.empty else 0
    notes.append(f"Registros priorizados como suspeitos pelo modelo: {suspects}.")

    return notes