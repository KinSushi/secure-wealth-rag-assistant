from pathlib import Path

from secure_rag.evaluation import run_evaluation


def test_run_evaluation(tmp_path: Path) -> None:
    report = run_evaluation(tmp_path / "eval.json")
    assert report["cases"] >= 1
    assert 0 <= report["hit_rate"] <= 1
