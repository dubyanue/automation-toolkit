load("//macros:pytest_macros.bzl", "custom_py_test")

custom_py_test(
    name = "unit_tests",
    srcs = glob(
        ["unit/*_test.py"],
    ),
    tags = [
        "unit",
    ],
    deps = [
        "//:py_test_deps",
        "//lib/file_libs:file_lib",
    ],
)
