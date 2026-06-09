# Validation

## Purpose

This file documents the local and CI validation path for this repository.

## Static validation

```powershell
python -m compileall -q src tests
python -m pytest -q --maxfail=1
python -m ruff check .
```

## RAG execution checks

```powershell
python -m secure_rag.app "What is the synthetic client's risk profile?"
python -m secure_rag.evaluation
```

The project uses synthetic documents only and local retrieval. No external LLM or private document ingestion is required for V1.

## Public-safety validation

```powershell
Get-ChildItem -Recurse -File |
  Where-Object { $_.FullName -notmatch "\\.git\\" -and $_.FullName -notmatch "\\.venv\\" } |
  Select-String -Pattern "BEGIN .*PRIVATE KEY","gho_","api_key","secret","token","password"
```

Expected review notes:

- Documentation may contain safety words such as `secret`, `token`, or `password`.
- Real credentials must never appear.
- Real client, banking, insurance, health, employer or private documents must never appear.

## Portfolio rule

This repository is public technical evidence. It must not contain CVs, cover letters, salary targets, private school documents, real client data, employer data, credentials or production decisioning claims.
