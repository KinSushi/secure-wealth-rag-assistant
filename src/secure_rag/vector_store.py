"""Local TF-IDF retrieval index for public RAG demo."""

from __future__ import annotations

from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from secure_rag.chunking import Chunk


@dataclass(frozen=True)
class RetrievalResult:
    """Retrieved chunk with score."""

    chunk: Chunk
    score: float


class LocalTfidfIndex:
    """Small local retrieval index without external services."""

    def __init__(self, chunks: list[Chunk]) -> None:
        if not chunks:
            raise ValueError("Cannot build index without chunks")
        self.chunks = chunks
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = self.vectorizer.fit_transform([chunk.text for chunk in chunks])

    def search(self, query: str, top_k: int = 3) -> list[RetrievalResult]:
        """Return top-k retrieved chunks."""

        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.matrix).ravel()
        order = similarities.argsort()[::-1][:top_k]
        return [RetrievalResult(self.chunks[index], float(similarities[index])) for index in order]
