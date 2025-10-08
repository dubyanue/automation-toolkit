"""Macros for bazel pytest
"""

load("@rules_python//python:defs.bzl", "py_test")

def custom_py_test(name, srcs, deps = [], args = [], data = [], aspect_hints = [], **kwargs):
    common_args = [
        "--mypy",
        "--ruff",
        "--ruff-format",
        # "--capture=no",
        # "-n logical",
        "--tb=long",
        "--verbose",
        "--junit-xml=$$XML_OUTPUT_FILE",
        # "--html=$$TEST_UNDECLARED_OUTPUTS_DIR/report.html",
        # "--self-contained-html",
        # "--cov",
        # "--cov-report=xml:$$TEST_UNDECLARED_OUTPUTS_DIR/coverage.xml",
        # "--cov-report=html:coverage_html",
        # "-s",
        "-rfExP",
        "-vv",
        # "--capture=no",
    ]

    py_test(
        name = name,
        main = "//macros:pytest_wrapper.py",
        srcs = srcs + ["//macros:pytest_wrapper.py"],
        aspect_hints = aspect_hints + [
            "@aspect_rules_lint//lint:ruff_bin",
        ],
        deps = deps,
        data = data + ["//:config_files"],
        args = common_args + args,  # Allows extra args if needed
        **kwargs
    )
