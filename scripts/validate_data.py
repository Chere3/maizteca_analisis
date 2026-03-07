#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

DATASET_PATH = Path("data/maizteca.csv")
REQUIRED_COLUMNS = [
    "Marca temporal",
    "sexo",
    "edad",
    "gusto elote",
    "condimentos favoritos",
    "precio",
    "formato presentacion",
    "intolerante lactosa",
    "grado de coccion",
]


def main() -> int:
    if not DATASET_PATH.exists():
        raise SystemExit(f"Dataset not found: {DATASET_PATH}")

    df = pd.read_csv(DATASET_PATH)
    df = df.rename(columns=lambda c: str(c).strip())
    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]

    if missing:
        print(f"Missing required columns: {', '.join(missing)}")
        return 1

    report = {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "missing_values": {column: int(df[column].isna().sum()) for column in REQUIRED_COLUMNS},
    }

    print(json.dumps(report, ensure_ascii=False, indent=2))

    # Basic quality gate: no required field should have more than 20% missing values.
    threshold = max(1, int(len(df) * 0.2))
    noisy_columns = [name for name, count in report["missing_values"].items() if count > threshold]
    if noisy_columns:
        print(f"Columns above missing-value threshold ({threshold}): {', '.join(noisy_columns)}")
        return 1

    print("Dataset validation passed ✅")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
