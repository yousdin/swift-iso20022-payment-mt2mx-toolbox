# Makefile for SWIFT ISO20022 Toolbox

.PHONY: help install run lint test clean

help:
	@echo "Available targets:"
	@echo "  install   Install all Python dependencies."
	@echo "  run       Launch the Streamlit GUI."
	@echo "  lint      Run flake8 on all Python files."
	@echo "  test      Run all tests (if any)."
	@echo "  clean     Remove Python cache and temporary files."

install:
	pip install -r requirements.txt

run:
	streamlit run iso20022_toolbox.py

lint:
	flake8 .

test:
	pytest

clean:
	rm -rf __pycache__ .pytest_cache *.pyc *.pyo */__pycache__
