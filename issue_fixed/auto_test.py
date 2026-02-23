"""Utility script to run the project's test suite.

This script is intended for quick local verification. It runs ``pytest`` against
``issue_fixed/tests`` and stores the full output in ``issue_fixed/logs/test_run.log``.

Usage:
    .venv/Scripts/python.exe issue_fixed/auto_test.py
"""

from __future__ import annotations

import pathlib
import subprocess
import sys
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parent
LOG_DIR = ROOT / "logs"
LOG_FILE = LOG_DIR / "test_run.log"


def main() -> int:
    """Run pytest and write results to the log file."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    cmd = [sys.executable, "-m", "pytest", str(ROOT / "tests")]  # noqa: S603,S607
    start_time = datetime.utcnow().isoformat() + "Z"

    process = subprocess.run(
        cmd,
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )

    output = (
        f"=== Test run at {start_time} ===\n"
        f"Command: {' '.join(cmd)}\n\n"
        f"STDOUT:\n{process.stdout}\n\n"
        f"STDERR:\n{process.stderr}\n\n"
        f"Exit code: {process.returncode}\n"
        f"=== End test run ===\n\n"
    )

    LOG_FILE.write_text(output, encoding="utf-8")

    # Also print to console for quick feedback.
    print(output)
    return process.returncode


if __name__ == "__main__":
    raise SystemExit(main())
