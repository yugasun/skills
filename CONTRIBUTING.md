# Contributing

Thanks for helping improve this repository. Contributions are welcome as issues, documentation fixes, and pull requests that add or refine skills.

## Before You Start

1. Read [README.md](README.md) (or [README.zh-CN.md](README.zh-CN.md)) for project scope and installation.
2. Browse the catalog in [docs/available-skills.md](docs/available-skills.md).
3. For agent-oriented maintenance rules, see [AGENTS.md](AGENTS.md).
4. Follow the upstream skill format at [agentskills.io/specification](https://agentskills.io/specification).

## Development Setup

```bash
git clone https://github.com/yugasun/skills.git
cd skills
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

Validate one skill:

```bash
python skills/skill-creator/scripts/quick_validate.py skills/<skill-name>
```

Validate every published skill:

```bash
python skills/skill-creator/scripts/validate_all.py
```

Package a skill for distribution:

```bash
python skills/skill-creator/scripts/package_skill.py skills/<skill-name> ./dist
```

Run skill tests:

```bash
python skills/skill-creator/scripts/run_skill_tests.py
```

## Adding Or Updating A Skill

1. Create or edit `skills/<name>/SKILL.md`.
2. Keep each skill self-contained:
   - `scripts/` for executable helpers
   - `references/` for long-form docs loaded on demand
   - `tests/` for regression coverage when scripts are non-trivial
3. Use valid frontmatter:
   - `name`: hyphen-case, max 64 characters
   - `description`: explicit trigger guidance, usually starting with `Use when...`
4. Update [docs/available-skills.md](docs/available-skills.md) when the public catalog changes.
5. Do not commit secrets. Use environment variables and document them in the skill.

Scaffold a new skill with:

```bash
python skills/skill-creator/scripts/init_skill.py <skill-name>
```

Use [template/SKILL.md](template/SKILL.md) as the minimal starting point.

## Pull Request Guidelines

- Keep changes focused. Prefer one skill or one docs area per PR.
- Run validation locally before opening the PR.
- Fill out the PR checklist in [.github/pull_request_template.md](.github/pull_request_template.md).
- Avoid unrelated README edits unless project positioning or installation changed.

## Code Of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). By participating, you agree to uphold it.

## Questions

Open a [GitHub issue](https://github.com/yugasun/skills/issues) for bugs, skill requests, or maintenance questions.
