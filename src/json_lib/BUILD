load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "json_lib",
    srcs = glob(
        include = ["*.py"],
        exclude = [
            "*_test.py",
            "main.py",
        ],
    ),
    deps = [
        "//:misc_deps",
        "//src/file_factory:file_lib",
    ],
)
