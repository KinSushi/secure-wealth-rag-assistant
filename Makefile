.PHONY: install test lint ci demo evaluate clean

install:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

ci: lint test

demo:
	python -m secure_rag.app "What is the synthetic client's risk profile?"

evaluate:
	python -m secure_rag.evaluation

clean:
	rm -f reports/*.json reports/*.md
	rm -f output/*
