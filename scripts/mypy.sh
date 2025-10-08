#!/bin/bash
#   set -e

# Go to repo root
cd "$(dirname "$0")/../.."

# Find all .py files excluding the directories you specified
find . -name "*.py" \
    -not -path "./.venv/*" \
    -not -path "./bazel-*/*" \
    -not -path "./*cache*/*" \
    -not -path "./.*cache*/*" \
    | xargs python -m mypy --strict
