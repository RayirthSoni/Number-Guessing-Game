# Makefile
.PHONY: local

# Set default values
difficulty ?= medium

local:
	@echo "Running Python script with variables..."
	DIFFICULTY=$(difficulty) python game.py
