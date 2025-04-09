#!/bin/bash

uv venv -p 3.12
uv pip install --upgrade syft-event
uv run main.py
