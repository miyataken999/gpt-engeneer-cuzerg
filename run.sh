#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the main script
python src/main.py

# Run the tests
pytest tests/
