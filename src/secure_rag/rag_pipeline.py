"""Citation-grounded answer builder for local RAG demo."""

from __future__ import annotations

from dataclasses import dataclass

from secure_rag.chunking import chunk_documents
from secure_rag.guardrails import detect_prompt_injection, enforce_non_advice_boundary
from secure_rag.ingest_documents import load_documents
from secure_rag.vector_store import LocalTfidfIndex, RetrievalResult


@dataclass(frozen=True)
class RagAnswer:
    """Answer with retrieved evidence."""

    answer: str
    citations: list[str]
    blocked: bool = False
    reason: str | None = None


def build_index() -> LocalTfidfIndex:
    """Build local index from sample docs."""

    return LocalTfidfIndex(chunk_documents(load_documents()))


def answer_question(question: str, index: LocalTfidfIndex | None = None, top_k: int = 3) -> RagAnswer:
    """Return a conservative citation-grounded answer."""

    if detect_prompt_injection(question):
        return RagAnswer(
            answer="Request blocked by prompt-injection guardrail.",
            citations=[],
            blocked=True,
            reason="prompt_injection_detected",
        )
    if enforce_non_advice_boundary(question):
        return RagAnswer(
            answer="I cannot provide investment, medical or legal advice. I can summarize retrieved synthetic context only.",
            citations=[],
            blocked=True,
            reason="advice_boundary",
        )

    retrieval_index = index or build_index()
    results: list[RetrievalResult] = retrieval_index.search(question, top_k=top_k)
    useful = [result for result in results if result.score > 0]
    if not useful:
        return RagAnswer(
            answer="Insufficient retrieved synthetic context to answer safely.",
            citations=[],
            blocked=False,
            reason="insufficient_context",
        )

    snippets = " ".join(result.chunk.text for result in useful)
    citations = [result.chunk.chunk_id for result in useful]
    answer = (
        "Based on the retrieved synthetic context, "
        + snippets[:450]
        + ("..." if len(snippets) > 450 else "")
    )
    return RagAnswer(answer=answer, citations=citations)
