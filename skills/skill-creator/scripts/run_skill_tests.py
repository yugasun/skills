#!/usr/bin/env python3
"""Discover and run unittest suites under skills/*/tests/."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


def discover_skill_tests(skills_dir: Path) -> unittest.TestSuite:
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    for tests_dir in sorted(skills_dir.glob("*/tests")):
        if tests_dir.is_dir():
            suite.addTests(loader.discover(str(tests_dir), pattern="test_*.py"))

    return suite


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    skills_dir = repo_root / "skills"
    if not skills_dir.is_dir():
        raise SystemExit(f"Skills directory not found: {skills_dir}")

    suite = discover_skill_tests(skills_dir)
    if suite.countTestCases() == 0:
        print("No skill tests found.")
        return

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
