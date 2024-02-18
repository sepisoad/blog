.PHONY: build
build:
	python -m src.frozen

live:
	DEBUG_FROZEN=1 python -m src.frozen