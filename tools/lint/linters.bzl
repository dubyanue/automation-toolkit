"""Linter configurations for the project.

This file declares linter aspects using the aspect rules_lint framework.
Source: https://github.com/aspect-build/rules_lint/blob/main/docs/linting.md
"""

load("@aspect_rules_lint//lint:ruff.bzl", "lint_ruff_aspect")

# Ruff linter configuration
# Uses pyproject.toml for configuration (ruff will automatically find it)
# Source: https://github.com/aspect-build/rules_lint/blob/main/example/tools/lint/linters.bzl
ruff = lint_ruff_aspect(
    binary = "@aspect_rules_lint//lint:ruff_bin",
    configs = [
        Label("//:pyproject.toml"),
    ],
    rule_kinds = [
        "py_binary",
        "py_library",
        "py_test",
    ],
)
