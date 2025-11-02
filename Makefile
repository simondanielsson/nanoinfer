#!/usr/bin/make

## help: Print help.
.PHONY: help
help:
	@echo Possible commands:
	@cat Makefile | grep '##' | grep -v "Makefile" | sed -e 's/^##/  -/'

## install: Install dependencies.
.PHONY: install
install:
	uv pip install -e .

## install_dev: Install dependencies for development.
.PHONY: install_dev
install_dev: install
	uv pip install -e . --group dev --group test
	# Installs the pre-commit hook.
	pre-commit install
