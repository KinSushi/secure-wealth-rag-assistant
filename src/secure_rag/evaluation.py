"""Retrieval evaluation for the secure RAG demo."""

from __future__ import annotations

import json
from pathlib import Path

from secure_rag.rag_pipeline import answer_question, build_index

EVAL_CASES = [
    {
        "question": "What is the synthetic client's risk profile?",
        "expected_source_contains": "portfolio_report_sample.md",
    },
    {
        "question": "What does the market note say about volatility?",
        "expected_source_contains": "market_note_sample.md",
    },
]


def run_evaluation(output_path: Path = Path("reports/retrieval_evaluation.json")) -> dict[str, object]:
    """Run simple retrieval evaluation."""

    index = build_index()
    results = []
    hits = 0
    for case in EVAL_CASES:
        answer = answer_question(case["question"], index=index)
        hit = any(case["expected_source_contains"] in citation for citation in answer.citations)
        hits += int(hit)
        results.append({"question": case["question"], "hit": hit, "citations": answer.citations})

    report = {"cases": len(EVAL_CASES), "hits": hits, "hit_rate": hits / len(EVAL_CASES), "results": results}
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def main() -> None:
    """CLI entry point."""

    print(json.dumps(run_evaluation(), indent=2))


if __name__ == "__main__":
    main()
