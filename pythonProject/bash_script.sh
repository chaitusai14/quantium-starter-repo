#!/bin/bash

# Activate the virtual environment
source pythonProject/venv/bin/activate

# Run the test suite with pytest
pytest pythonProject/tests/test_app.py

# Check the exit code from pytest
if [ $? -eq 0 ]; then
  echo "All tests passed!"
  exit 0  # Success
else
  echo "Some tests failed."
  exit 1  # Failure
fi
