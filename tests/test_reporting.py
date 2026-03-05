from pathlib import Path

from maizteca.reporting import compute_metrics, render_markdown


def test_compute_metrics_and_render(tmp_path: Path):
    csv = tmp_path / "sample.csv"
    csv.write_text(
        "precio,formato presentacion,condimentos favoritos\n"
        "20-30,Vaso,Chile\n"
        "20-30,Vaso,Queso\n"
        "30-40,Palito,Chile\n",
        encoding="utf-8",
    )

    metrics = compute_metrics(csv)
    assert metrics.total_responses == 3
    assert metrics.top_price_segment == "20-30"
    assert metrics.top_presentation_format == "Vaso"

    report = render_markdown(metrics)
    assert "Resumen Ejecutivo Maizteca" in report
    assert "Respuestas totales" in report
