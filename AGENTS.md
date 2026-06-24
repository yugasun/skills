# AGENTS.md

This repository publishes reusable agent skills. Most changes should stay local to one skill package under [skills/](skills).

## Repository Focus

- Published skills live in [skills/](skills).
- The skill catalog lives in [docs/available-skills.md](docs/available-skills.md).
- The minimal new-skill template is [template/SKILL.md](template/SKILL.md).
- The spec pointer is [spec/agent-skills-spec.md](spec/agent-skills-spec.md).
- Human contributor guidance is in [CONTRIBUTING.md](CONTRIBUTING.md).

## Working Model

- Treat each folder under [skills/](skills) as a self-contained package.
- Keep changes scoped to the target skill unless you are intentionally updating shared docs.
- Prefer linking to existing docs over duplicating long guidance into `SKILL.md`.
- Put executable helpers in `scripts/`, long-form supporting docs in `references/`, and verification in `tests/` when a skill ships non-trivial code.

## When Adding Or Updating A Skill

1. Create or update `skills/<name>/SKILL.md` under [skills/](skills).
2. Keep the frontmatter valid:
   - `name`: hyphen-case only, max 64 chars.
   - `description`: explicit trigger guidance, usually starting with `Use when...`.
   - Allowed top-level keys are limited by the validator; do not invent extra frontmatter fields.
3. Keep `SKILL.md` concise. Put reference material in `references/` and link to it.
4. If the skill has scripts or behavior worth regression coverage, add or update tests inside that skill folder.
5. Update [docs/available-skills.md](docs/available-skills.md) when a skill is added, removed, or its positioning materially changes.
6. Leave [README.md](README.md) and [README.zh-CN.md](README.zh-CN.md) alone unless project-level positioning, installation, or top-level navigation changed.

## Validation Commands

Run from the repo root:

```bash
pip install -r requirements-dev.txt
python skills/skill-creator/scripts/quick_validate.py skills/<skill-name>
python skills/skill-creator/scripts/validate_all.py
python skills/skill-creator/scripts/package_skill.py skills/<skill-name> ./dist
```

If the target skill includes tests, run the narrowest relevant test command as well, for example:

```bash
python skills/skill-creator/scripts/run_skill_tests.py
```

## Useful Local Examples

- [skills/ai-news-collector/SKILL.md](skills/ai-news-collector/SKILL.md): minimal instruction-only skill.
- [skills/dev-web/SKILL.md](skills/dev-web/SKILL.md): skill with linked references and metadata.
- [skills/aliyun-image-gen/SKILL.md](skills/aliyun-image-gen/SKILL.md): skill with scripts and tests.
- [skills/brainstorming/SKILL.md](skills/brainstorming/SKILL.md): workflow-heavy skill with bundled scripts.

## Pitfalls To Avoid

- Do not add extra documentation files inside a skill when `SKILL.md`, `references/`, or existing docs already cover the need.
- Do not move shared project guidance into individual skills.
- Do not update the catalog for internal script-only refactors unless the skill's public positioning changed.
- Do not hardcode secrets in scripts or examples; use environment variables and document them in the skill.
