.PHONY: install validate summary check

install:
	python -m pip install -r requirements.txt

validate:
	python scripts/validate_data.py

summary:
	python scripts/generate_summary.py

check: validate summary
