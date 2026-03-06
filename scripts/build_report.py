from __future__ import annotations

from pathlib import Path

from maizteca.reporting import compute_metrics, render_markdown

DATA_PATH = Path("data/maizteca.csv")
OUT_PATH = Path("reports/market-summary.md")


def main() -> int:
    if not DATA_PATH.exists():
        print(f"[ERROR] Missing dataset: {DATA_PATH}")
        return 1

    metrics = compute_metrics(DATA_PATH)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(render_markdown(metrics), encoding="utf-8")
    print(f"[OK] Report generated at {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
