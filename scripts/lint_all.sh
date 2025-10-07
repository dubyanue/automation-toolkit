#!/bin/bash
set -e

# For tests, we need to find the workspace root differently
if [[ -n "$TEST_WORKSPACE" ]]; then
    # Running as a test
    cd "$TEST_WORKSPACE"
elif [[ -n "$BUILD_WORKSPACE_DIRECTORY" ]]; then
    # Running as a binary
    cd "$BUILD_WORKSPACE_DIRECTORY"
fi

echo "Running standard linters (ruff, biome, etc.)..."
bazel run //:check

echo "Running format check..."
bazel run //:format.check

echo "Running pylint..."
bazel run //:pylint -- src/

echo "All linters completed successfully!"
