from __future__ import annotations

import argparse
from pathlib import Path

from .pipeline import run


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Maizteca analysis pipeline")
    parser.add_argument("--data", default="data/maizteca.csv")
    parser.add_argument("--output", default="reports/executive-summary.md")
    args = parser.parse_args()

    metrics = run(Path(args.data), Path(args.output))
    print(f"Report generated: rows={metrics.rows}, cols={metrics.columns}, nulls={metrics.null_cells}")


if __name__ == "__main__":
    main()
