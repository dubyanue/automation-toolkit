"""Macros for bazel pytest
"""

load("@rules_python//python:defs.bzl", "py_test")

def custom_py_test(name, srcs, deps = [], args = [], data = [], aspect_hints = [], **kwargs):
    common_args = [
        # "--mypy",
        # "--ruff",
        # "--ruff-format",
        "--tb=long",
        "--verbose",
        "--junit-xml=$$XML_OUTPUT_FILE",
        "--html=$$TEST_UNDECLARED_OUTPUTS_DIR/report.html",
        "--self-contained-html",
        "--cov",
        "--cov-config=.coveragerc",
        "--cov-report=xml:$$TEST_UNDECLARED_OUTPUTS_DIR/coverage.xml",
        "--cov-report=html:$$TEST_UNDECLARED_OUTPUTS_DIR/coverage_html",
        "-rfExP",
    ]

    py_test(
        name = name,
        main = "//macros:pytest_wrapper.py",
        srcs = srcs + ["//macros:pytest_wrapper.py"],
        aspect_hints = aspect_hints + [
            "@aspect_rules_lint//lint:ruff_bin",
        ],
        deps = deps + ["//:py_test_deps"],
        data = data + [
            "//:config_files",
            "//:.coveragerc",
        ],
        args = common_args + args,  # Allows extra args if needed
        **kwargs
    )
