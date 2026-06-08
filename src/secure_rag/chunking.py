"""Simple deterministic text chunking."""

from __future__ import annotations

from dataclasses import dataclass

from secure_rag.ingest_documents import Document


@dataclass(frozen=True)
class Chunk:
    """A chunk of a source document."""

    chunk_id: str
    source: str
    text: str


def chunk_documents(documents: list[Document], max_words: int = 80) -> list[Chunk]:
    """Split documents into word-based chunks."""

    chunks: list[Chunk] = []
    for document in documents:
        words = document.text.split()
        for index in range(0, len(words), max_words):
            text = " ".join(words[index : index + max_words])
            if text.strip():
                chunks.append(
                    Chunk(
                        chunk_id=f"{document.source}:{index // max_words + 1}",
                        source=document.source,
                        text=text,
                    )
                )
    return chunks
