from pathlib import Path

from secure_rag.chunking import chunk_documents
from secure_rag.ingest_documents import load_documents


def test_load_documents() -> None:
    documents = load_documents(Path("docs_sample"))
    assert len(documents) >= 2


def test_chunk_documents() -> None:
    documents = load_documents(Path("docs_sample"))
    chunks = chunk_documents(documents, max_words=20)
    assert chunks
    assert all(chunk.source for chunk in chunks)
