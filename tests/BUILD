load("//macros:pytest_macros.bzl", "custom_py_test")

package(default_visibility = ["//visibility:public"])

filegroup(
    name = "unittest_files",
    srcs = glob(
        include = ["unit/*_test.py"],
        allow_empty = True,
    ),
)

filegroup(
    name = "non_unittest_files",
    srcs = glob(
        include = ["**/*_test.py"],
        allow_empty = True,
        exclude = ["unit/**"],
    ),
)

filegroup(
    name = "test_files",
    srcs = [
        ":non_unittest_files",
        ":unittest_files",
    ],
)

custom_py_test(
    name = "unit_tests",
    srcs = [
        ":unittest_files",
        "//lib:libs",
    ],
    tags = ["unit"],
    deps = ["//:py_test_deps"],
)
