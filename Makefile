.PHONY: help build dev 

PYTHON := python3
PIP := pip3 

SRC := src
MAIN := main.py

help:
	@echo "Available commands:"
	@echo "make build"
	@echo "make dev"

build:
	@echo "code"
	@$(PYTHON) -m py_compile $(SRC)/*.py $(MAIN) 2>&1/dev/null
	@(PYTHON) -m py_compile $(MAIN)

dev:
	@echo "chạy chương trình"
	@$(PYTHON) $(MAIN)
