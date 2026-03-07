#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import pandas as pd

DATASET_PATH = Path("data/maizteca.csv")
OUTPUT_PATH = Path("reports/executive-summary.md")


def top(series: pd.Series, count: int = 3):
    return series.value_counts(dropna=True).head(count)


def main() -> int:
    if not DATASET_PATH.exists():
        raise SystemExit(f"Dataset not found: {DATASET_PATH}")

    df = pd.read_csv(DATASET_PATH)
    df = df.rename(columns=lambda c: str(c).strip())
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    likes = df["gusto elote"].astype(str).str.lower().str.contains("si|sí", regex=True, na=False).sum()
    total = len(df)

    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        f.write("# Resumen Ejecutivo - Maizteca\n\n")
        f.write(f"- **Muestra analizada:** {total} respuestas\n")
        f.write(f"- **Interés declarado por elote:** {likes} ({(likes/total)*100:.1f}%)\n\n")

        f.write("## Top preferencias\n\n")
        f.write("### Rango de precio\n")
        for label, value in top(df["precio"]).items():
            f.write(f"- {label}: {value}\n")

        f.write("\n### Formato de presentación\n")
        for label, value in top(df["formato presentacion"]).items():
            f.write(f"- {label}: {value}\n")

        f.write("\n### Condimentos favoritos\n")
        for label, value in top(df["condimentos favoritos"]).items():
            f.write(f"- {label}: {value}\n")

        f.write("\n## Recomendación inicial\n\n")
        f.write(
            "Priorizar un menú base con los condimentos más frecuentes y validar precios del top 2 en una prueba piloto de 2 semanas.\n"
        )

    print(f"Summary written to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
