---
name: template-skill
description: Use when you need a placeholder description. Replace with what the skill does and when an agent should trigger it.
---

# Template Skill

Replace this file with the skill instructions.

## Recommended Layout

```text
skills/<name>/
├── SKILL.md
├── scripts/       # optional executable helpers
├── references/    # optional long-form docs
└── tests/         # optional regression tests
```

## Authoring Notes

- Keep `SKILL.md` concise; move long references into `references/`.
- Write `description` as explicit trigger guidance for skill routing.
- Validate with `python skills/skill-creator/scripts/quick_validate.py skills/<name>`.
