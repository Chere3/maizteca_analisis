.PHONY: install test build-report validate

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .

test:
	pytest -q

build-report:
	python scripts/build_report.py

validate: test build-report
	@test -s reports/market-summary.md
	@echo "✓ Validation completed"
