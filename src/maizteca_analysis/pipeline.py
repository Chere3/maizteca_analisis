from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(slots=True)
class AnalysisMetrics:
    rows: int
    columns: int
    null_cells: int


def load_dataset(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path)


def validate_dataset(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Dataset is empty")
    if len(df.columns) < 2:
        raise ValueError("Dataset must contain at least two columns")


def summarize(df: pd.DataFrame) -> AnalysisMetrics:
    return AnalysisMetrics(
        rows=len(df),
        columns=len(df.columns),
        null_cells=int(df.isna().sum().sum()),
    )


def write_report(metrics: AnalysisMetrics, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "\n".join(
            [
                "# Maizteca Analysis Report",
                "",
                "## Dataset health",
                f"- Rows: {metrics.rows}",
                f"- Columns: {metrics.columns}",
                f"- Null cells: {metrics.null_cells}",
            ]
        ),
        encoding="utf-8",
    )


def run(data_path: Path, output_path: Path) -> AnalysisMetrics:
    df = load_dataset(data_path)
    validate_dataset(df)
    metrics = summarize(df)
    write_report(metrics, output_path)
    return metrics
