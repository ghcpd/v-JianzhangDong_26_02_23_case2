#!/usr/bin/env python
"""Automated test runner that logs results to logs/test_run.log"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path


def run_tests():
    """Run pytest and log the results to logs/test_run.log.
    
    Returns:
        int: The exit code from pytest (0 for success, non-zero for failure).
    """
    # Ensure logs directory exists
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / "test_run.log"
    
    # Prepare log header
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"\n{'='*70}\nTest Run: {timestamp}\n{'='*70}\n\n"
    
    # Run pytest and capture output
    print(f"Running tests... (logging to {log_file})")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-v", "--tb=short"],
        capture_output=True,
        text=True
    )
    
    # Combine stdout and stderr
    output = result.stdout + result.stderr
    
    # Write to log file
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(header)
        f.write(output)
        f.write(f"\n\nExit Code: {result.returncode}\n")
        if result.returncode == 0:
            f.write("Status: ALL TESTS PASSED ✓\n")
        else:
            f.write("Status: SOME TESTS FAILED ✗\n")
    
    # Print summary to console
    print(f"\nTest results written to: {log_file}")
    print(f"Exit code: {result.returncode}")
    
    if result.returncode == 0:
        print("✓ All tests passed!")
    else:
        print("✗ Some tests failed. Check the log for details.")
    
    # Also print the output to console
    print("\nTest Output:")
    print(output)
    
    return result.returncode


if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)
