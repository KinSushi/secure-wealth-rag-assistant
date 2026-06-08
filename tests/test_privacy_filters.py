from secure_rag.guardrails import contains_pii, enforce_non_advice_boundary


def test_contains_pii_email() -> None:
    assert contains_pii("contact test@example.com")


def test_non_advice_boundary() -> None:
    assert enforce_non_advice_boundary("Should I invest in this product?")
