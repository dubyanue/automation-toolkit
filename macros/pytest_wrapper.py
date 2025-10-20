import os
import sys

import pytest

# if using 'bazel test ...'
if __name__ == "__main__":
    # Expand environment variables in arguments
    args = []
    for arg in sys.argv[1:]:
        if "$TEST_UNDECLARED_OUTPUTS_DIR" in arg:
            # Replace $$TEST_UNDECLARED_OUTPUTS_DIR with actual env var value
            test_outputs_dir = os.environ.get("TEST_UNDECLARED_OUTPUTS_DIR", "")
            expanded_arg = arg.replace("$TEST_UNDECLARED_OUTPUTS_DIR", test_outputs_dir)
            args.append(expanded_arg)
        else:
            args.append(arg)

    sys.exit(pytest.main(args))
