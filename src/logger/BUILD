load("@rules_python//python:defs.bzl", "py_library")

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
