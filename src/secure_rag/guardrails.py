"""Guardrails and privacy checks for synthetic RAG demo."""

from __future__ import annotations

import re

PROMPT_INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"reveal hidden",
    r"system prompt",
    r"developer message",
    r"private key",
    r"api key",
]

PII_PATTERNS = [
    r"\b\d{3}-\d{2}-\d{4}\b",
    r"\b[A-Z]{2}\d{2}[A-Z0-9]{1,30}\b",
    r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
]


def detect_prompt_injection(text: str) -> bool:
    """Detect simple prompt-injection patterns."""

    lowered = text.lower()
    return any(re.search(pattern, lowered) for pattern in PROMPT_INJECTION_PATTERNS)


def contains_pii(text: str) -> bool:
    """Detect simple PII-like patterns."""

    return any(re.search(pattern, text) for pattern in PII_PATTERNS)


def enforce_non_advice_boundary(question: str) -> bool:
    """Return True if query appears to ask for advice-like output."""

    lowered = question.lower()
    advice_terms = ["should i invest", "buy", "sell", "medical advice", "legal advice"]
    return any(term in lowered for term in advice_terms)
