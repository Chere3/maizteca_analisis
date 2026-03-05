from pathlib import Path

import pandas as pd
import pytest

from maizteca_analysis.pipeline import run, summarize, validate_dataset


def test_validate_dataset_rejects_empty() -> None:
    with pytest.raises(ValueError):
        validate_dataset(pd.DataFrame())


def test_summarize_counts_null_cells() -> None:
    df = pd.DataFrame({"a": [1, None], "b": [2, 3]})
    metrics = summarize(df)
    assert metrics.rows == 2
    assert metrics.columns == 2
    assert metrics.null_cells == 1


def test_run_generates_report(tmp_path: Path) -> None:
    data = tmp_path / "data.csv"
    data.write_text("a,b\n1,2\n3,4\n", encoding="utf-8")
    out = tmp_path / "report.md"

    metrics = run(data, out)

    assert metrics.rows == 2
    assert out.exists()
