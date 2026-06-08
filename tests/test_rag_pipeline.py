from secure_rag.rag_pipeline import answer_question


def test_answer_question_returns_citations() -> None:
    answer = answer_question("What is the synthetic client's risk profile?")
    assert answer.answer
    assert answer.citations
