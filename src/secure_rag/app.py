"""CLI app for local RAG demonstration."""

from __future__ import annotations

import argparse

from secure_rag.rag_pipeline import answer_question


def parse_args() -> argparse.Namespace:
    """Parse CLI args."""

    parser = argparse.ArgumentParser(description="Ask a question against synthetic documents.")
    parser.add_argument("question")
    return parser.parse_args()


def main() -> None:
    """CLI entry point."""

    args = parse_args()
    response = answer_question(args.question)
    print(response.answer)
    if response.citations:
        print("\nCitations:")
        for citation in response.citations:
            print(f"- {citation}")


if __name__ == "__main__":
    main()
