#!/bin/bash
set -e

# Load the Bazel runfiles library
# shellcheck source=/dev/null
source "${RUNFILES_DIR:-/dev/null}/bazel_tools/tools/bash/runfiles/runfiles.bash" || \
# source "$(grep -sm1 "^bazel_tools/tools/bash/runfiles/runfiles.bash " "${RUNFILES_MANIFEST_FILE:-/dev/null}" | cut -f2- -d' ')" 2>/dev/null || \
# source "$0.runfiles/bazel_tools/tools/bash/runfiles/runfiles.bash"

# Find workspace root for test context
if [[ -n "$TEST_SRCDIR" ]]; then
    cd "$TEST_SRCDIR/_main"
fi

echo "Running ALL linters as test (using rlocation)..."

echo "Running biome..."
biome_bin="$(rlocation "biome/file/downloaded")"
if [[ -x "$biome_bin" ]]; then
    "$biome_bin" ci --colors=off --linter-enabled=true --formatter-enabled=true --assist-enabled=false
else
    echo "ERROR: Could not find biome binary at: $biome_bin"
    exit 1
fi

echo "Running taplo..."
taplo_bin="$(rlocation "my_deps_312_taplo/bin/taplo")"
if [[ -x "$taplo_bin" ]]; then
    "$taplo_bin" lint --verbose #--default-schema-catalogs --cache-path=./
else
    echo "ERROR: Could not find taplo binary at: $taplo_bin"
    exit 1
fi

echo "Running yamllint..."
./yamllint --strict --format=github ./

echo "Running mypy..."
./mypy --strict \
    --pretty \
    -p lib \
    -p tests

echo "Running pylint (no cache for sandbox)..."
./pylint --persistent=no ./

echo "Running ruff check..."
ruff_bin="$(rlocation "my_deps_312_ruff/bin/ruff")"
if [[ -x "$ruff_bin" ]]; then
    "$ruff_bin" check --preview --no-fix --respect-gitignore --force-exclude --verbose
else
    echo "ERROR: Could not find ruff binary at: $ruff_bin"
    exit 1
fi

echo "All linters passed!"
