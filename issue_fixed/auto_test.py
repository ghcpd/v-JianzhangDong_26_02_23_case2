"""Run pytest suite and log results to ``logs/test_run.log``.

Usage:
    python auto_test.py
"""
from __future__ import annotations

import datetime as _dt
import pathlib
import subprocess
import sys
from typing import List


def run_pytest(argv: List[str] | None = None) -> int:
    """Execute pytest and write both console and log output.

    Parameters
    ----------
    argv:
        Optional extra arguments to pass to pytest. If ``None``, defaults to
        ``['-q']`` for quiet output.

    Returns
    -------
    int
        The pytest exit code.
    """

    argv = argv or ["-q"]
    root = pathlib.Path(__file__).resolve().parent
    log_dir = root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "test_run.log"

    cmd = [sys.executable, "-m", "pytest", *argv]

    timestamp = _dt.datetime.now().isoformat(sep=" ", timespec="seconds")
    header = f"\n=== Pytest run @ {timestamp} ===\nCommand: {' '.join(cmd)}\n"

    result = subprocess.run(cmd, cwd=root, text=True, capture_output=True)

    # Echo to console
    sys.stdout.write(header)
    sys.stdout.write(result.stdout)
    if result.stderr:
        sys.stderr.write(result.stderr)

    # Append to log file
    with log_file.open("a", encoding="utf-8") as fh:
        fh.write(header)
        fh.write(result.stdout)
        if result.stderr:
            fh.write("\n[stderr]\n")
            fh.write(result.stderr)

    return result.returncode


def main() -> None:
    exit_code = run_pytest()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
