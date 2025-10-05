load("@rules_python//python:defs.bzl", "py_library")
load("//tools/lint:linters.bzl", "ruff_test")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "logger_lib",
    srcs = glob(
        include = ["*.py"],
        exclude = [
            "*_test.py",
        ],
    ),
)

ruff_test(
    name = "lint",
    srcs = [
        ":logger_lib",
    ],
)
