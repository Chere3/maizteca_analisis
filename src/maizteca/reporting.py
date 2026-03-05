from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass
class SurveyMetrics:
    total_responses: int
    top_price_segment: str
    top_presentation_format: str
    top_condiment: str


def compute_metrics(csv_path: Path) -> SurveyMetrics:
    df = pd.read_csv(csv_path)

    def mode_for(column: str) -> str:
        values = df[column].dropna().astype(str).str.strip()
        return values.mode().iloc[0] if not values.empty else "N/A"

    return SurveyMetrics(
        total_responses=len(df),
        top_price_segment=mode_for("precio"),
        top_presentation_format=mode_for("formato presentacion"),
        top_condiment=mode_for("condimentos favoritos"),
    )


def render_markdown(metrics: SurveyMetrics) -> str:
    return f"""# Resumen Ejecutivo Maizteca\n\n## Métricas clave\n- Respuestas totales: **{metrics.total_responses}**\n- Segmento de precio más frecuente: **{metrics.top_price_segment}**\n- Formato de presentación más frecuente: **{metrics.top_presentation_format}**\n- Condimento más frecuente: **{metrics.top_condiment}**\n\n## Próximas acciones recomendadas\n1. Diseñar oferta inicial alineada al segmento de precio dominante.\n2. Priorizar punto de venta según preferencia observada.\n3. Crear menú base con el condimento más demandado y variantes de prueba.\n"""
