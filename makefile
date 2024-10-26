# Makefile
.PHONY: local

# Set default values
difficulty ?= medium
guesses ?= 100

local:
	@echo "Running Python script with variables..."
	DIFFICULTY=$(difficulty) GUESSES=$(guesses) python game.py
