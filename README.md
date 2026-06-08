# secure-wealth-rag-assistant

<div align="center">

<img src="assets/secure-rag-banner.svg" alt="secure-wealth-rag-assistant banner" width="100%"/>

<br/>

**Secure RAG / LLMOps starter for sensitive-document workflows using synthetic documents only**

RAG Â· Local Retrieval Â· Evaluation Â· Privacy Controls Â· Prompt-Injection Tests Â· Human Review Â· AI Governance

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-Document%20Retrieval-6F42C1?style=flat)
![Privacy](https://img.shields.io/badge/Privacy-PII%20Controls-2EA043?style=flat)
![Evaluation](https://img.shields.io/badge/Evaluation-Retrieval%20%2F%20Grounding-1F6FEB?style=flat)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![Public Safety](https://img.shields.io/badge/Documents-Synthetic%20Only-24292F?style=flat)

</div>

---

## Executive summary

`secure-wealth-rag-assistant` is a public LLMOps / RAG portfolio project demonstrating safe document ingestion, local retrieval, citation-grounded answering, privacy controls, prompt-injection testing and human-review governance using synthetic documents only.

```text
synthetic docs -> chunking -> local index -> retrieval -> grounded answer -> evaluation -> privacy / injection tests -> governance docs
```

The project is designed for regulated and data-intensive environments: private banking, insurance, health data, pharma/medtech, consulting, research and big-tech AI/data platforms.

No real client, banking, insurance, health, employer or private documents belong here.

---

## Target roles

| Role family | Why this project helps |
|---|---|
| Junior AI Engineer | retrieval, grounded outputs and evaluation |
| LLMOps Engineer Junior | prompt-injection tests, privacy controls and governance docs |
| AI Platform Engineer Junior | safe workflow design and public technical evidence |
| Risk / Compliance Analytics | sensitive-document workflow boundaries and human review |
| Big-tech AI/data systems | testable retrieval, no external dependency, reproducible evaluation |

---

## Architecture

```mermaid
flowchart LR
    A[Synthetic documents] --> B[Document loader]
    B --> C[Chunking]
    C --> D[Local TF-IDF index]
    E[User question] --> F[Retrieval]
    D --> F
    F --> G[Grounded answer builder]
    G --> H[Citations]
    G --> I[Evaluation]
    G --> J[Guardrails]
    J --> K[Human review policy]
```

---

## Quickstart

```bash
make install
make test
make lint
make demo
```

Run CLI demo:

```bash
python -m secure_rag.app "What is the synthetic client's risk profile?"
```

Run evaluation:

```bash
make evaluate
```

---

## Public-safety rules

- synthetic documents only;
- no real client profiles;
- no real bank, insurance or health documents;
- no private PDFs, contracts or identity documents;
- no financial, medical, legal or insurance advice;
- no production decisioning claims;
- no employer-specific application content;
- no secrets or API keys.

---

## Non-goals

This project is not a production RAG platform, not a financial adviser, not a medical adviser, not a legal adviser, and not an application dossier.
---

## Portfolio layer

This repository is part of the KinSushi public technical portfolio.

| Layer | Evidence |
|---|---|
| LLMOps / RAG | synthetic documents, retrieval evaluation, prompt-injection tests, privacy controls |

Detailed cross-repository context: [docs/PORTFOLIO_LAYER.md](docs/PORTFOLIO_LAYER.md)

