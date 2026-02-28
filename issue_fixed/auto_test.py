#!/usr/bin/env python3
"""Automated test runner with logging to file."""

import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime


def run_tests():
    """Run pytest and log results to logs/test_run.log."""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    log_file = logs_dir / "test_run.log"
    
    # Change to the script's directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Prepare pytest command to run in current venv
    cmd = [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"]
    
    with open(log_file, "w") as f:
        f.write(f"Test Run: {datetime.now().isoformat()}\n")
        f.write(f"Command: {' '.join(cmd)}\n")
        f.write(f"Python: {sys.executable}\n")
        f.write("=" * 70 + "\n\n")
        
        # Run pytest
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Write output
        f.write(result.stdout)
        if result.stderr:
            f.write("\nSTDERR:\n")
            f.write(result.stderr)
        
        f.write("\n" + "=" * 70 + "\n")
        f.write(f"Exit Code: {result.returncode}\n")
        f.write(f"Status: {'PASSED' if result.returncode == 0 else 'FAILED'}\n")
    
    # Also print to console
    print(f"Test results logged to {log_file}")
    print(f"\n{result.stdout}")
    
    return result.returncode


if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)
