#!/usr/bin/env python3
"""Validate every skill package under skills/."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from quick_validate import validate_skill


def find_default_skills_dir() -> Path:
    current = SCRIPT_DIR
    while current != current.parent:
        candidate = current / "skills"
        if candidate.is_dir() and any(
            (child / "SKILL.md").exists()
            for child in candidate.iterdir()
            if child.is_dir()
        ):
            return candidate
        current = current.parent
    raise SystemExit("Could not find a skills/ directory with skill packages")


def resolve_skills_dir(arg: str | None) -> Path:
    if arg:
        path = Path(arg).resolve()
        if path.name == "skills":
            return path
        if (path / "SKILL.md").exists():
            return path.parent
        nested = path / "skills"
        if nested.is_dir():
            return nested
        raise SystemExit(f"Could not resolve skills directory from: {path}")

    return find_default_skills_dir()


def main() -> None:
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    skills_dir = resolve_skills_dir(arg)

    skill_dirs = sorted(
        path
        for path in skills_dir.iterdir()
        if path.is_dir() and (path / "SKILL.md").exists()
    )

    if not skill_dirs:
        raise SystemExit(f"No skills found in {skills_dir}")

    failed: list[str] = []
    for skill_dir in skill_dirs:
        valid, message = validate_skill(skill_dir)
        status = "OK" if valid else "FAIL"
        print(f"[{status}] {skill_dir.name}: {message}")
        if not valid:
            failed.append(skill_dir.name)

    if failed:
        print(f"\n{len(failed)} skill(s) failed validation: {', '.join(failed)}")
        raise SystemExit(1)

    print(f"\nAll {len(skill_dirs)} skill(s) passed validation.")


if __name__ == "__main__":
    main()
