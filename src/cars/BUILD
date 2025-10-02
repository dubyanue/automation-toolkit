
load("@rules_python//python:defs.bzl", "py_library", "py_binary")

package(default_visibility = ["//visibility:public"])

py_library(
    
)

py_library(
    name = "cars_lib",
    srcs = glob(
        include=["*.py"],
        exclude=[
            "*_test.py",
            "main.py"
            ]
    ),
    deps = []
)

py_binary(
    name = "cars_app",
    srcs = ["main.py"],
    main = "main.py",
    deps = [
        ":cars_lib",
    ]
)
