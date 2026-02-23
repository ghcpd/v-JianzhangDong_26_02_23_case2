"""Utility to run the package's test suite and log output.

This script adjusts ``sys.path`` so that the local ``issue`` package is
importable, then invokes ``pytest`` and writes both stdout and stderr to
``logs/test_run.log``.  The script exits with the same return code as the
pytest invocation so it can be used in CI or shell scripts.
"""

import logging
import os
import subprocess
import sys


def main():
    # ensure logs directory exists
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/test_run.log",
        level=logging.INFO,
        format="%(asctime)s %(message)s",
    )

    # Add local package to path
    root = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(root, "issue"))

    # run pytest
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=root,
        capture_output=True,
        text=True,
    )

    logging.info(result.stdout)
    logging.info(result.stderr)

    # mirror output to console as well
    print(result.stdout)
    print(result.stderr, file=sys.stderr)

    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
