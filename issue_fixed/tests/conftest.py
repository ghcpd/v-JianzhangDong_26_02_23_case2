"""Pytest configuration for the issue_fixed test suite.

The upstream tests import the ``taskflow`` package directly. Since this kata is
executed from the workspace root, we need to ensure that the copied project
folder (``issue_fixed``) is on ``sys.path``.

This file does not change any test assertions; it only adjusts import paths.
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
