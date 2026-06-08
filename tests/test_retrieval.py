from pathlib import Path

from secure_rag.chunking import chunk_documents
from secure_rag.ingest_documents import load_documents
from secure_rag.vector_store import LocalTfidfIndex


def test_local_retrieval_returns_results() -> None:
    chunks = chunk_documents(load_documents(Path("docs_sample")))
    index = LocalTfidfIndex(chunks)
    results = index.search("risk profile", top_k=2)

    assert len(results) == 2
    assert results[0].score >= 0
