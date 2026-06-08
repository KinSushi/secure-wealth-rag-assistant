"""Document loading utilities for synthetic docs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Document:
    """Loaded synthetic document."""

    source: str
    text: str


def load_documents(directory: Path = Path("docs_sample")) -> list[Document]:
    """Load markdown and JSON sample documents."""

    documents: list[Document] = []
    for path in sorted(directory.glob("*")):
        if path.suffix.lower() in {".md", ".json", ".txt"}:
            documents.append(Document(source=path.name, text=path.read_text(encoding="utf-8")))
    if not documents:
        raise FileNotFoundError(f"No synthetic documents found in {directory}")
    return documents
