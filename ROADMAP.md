# ROADMAP

## Quick wins (1-2 weeks)

- [x] Pin and validate dependencies (`requirements.txt` + package metadata)
- [x] Add reproducible CLI pipeline (`maizteca-analyze`)
- [x] Add data-quality smoke tests for baseline reliability

## Medium improvements (2-4 weeks)

- [ ] Add outlier + anomaly detection report section
- [ ] Export charts as PNG artifacts for non-technical stakeholders
- [ ] Add CI workflow for notebook + pipeline tests

## Big bets (1-2 months)

- [ ] Build feature store for recurring Maizteca analyses
- [ ] Introduce interactive dashboard (Plotly/Streamlit)
- [ ] Add experiment tracking for scenario comparisons

## Strategic rewrites

- [ ] Migrate notebook-heavy flow to layered data app architecture (ingest/transform/present)
- [ ] Add declarative config for analysis scenarios
- [ ] Integrate scheduled runs + artifact publishing
