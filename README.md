# maizteca_analisis

Análisis de datos del proyecto Maizteca con flujo reproducible (notebook + pipeline CLI).

## Qué incluye

- Notebook exploratorio (`main.ipynb`)
- Pipeline de análisis reutilizable (`src/maizteca_analysis`)
- Reporte ejecutivo generado automáticamente (`reports/executive-summary.md`)
- Tests de calidad de datos y flujo base

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
maizteca-analyze --data data/maizteca.csv --output reports/executive-summary.md
pytest -q
```

## Estructura

```
data/
main.ipynb
src/maizteca_analysis/
tests/
reports/
```

## Roadmap

Ver [ROADMAP.md](./ROADMAP.md).
