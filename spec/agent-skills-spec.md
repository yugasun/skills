# Agent Skills Spec

This repository follows the upstream Agent Skills specification.

- Canonical spec: <https://agentskills.io/specification>
- Local validation: `python skills/skill-creator/scripts/quick_validate.py skills/<skill-name>`

Required `SKILL.md` frontmatter in this repo:

| Field | Rule |
| --- | --- |
| `name` | Required. Hyphen-case, max 64 characters. |
| `description` | Required. Plain text trigger guidance, max 1024 characters. |
| `license` | Optional. |
| `allowed-tools` | Optional. |
| `metadata` | Optional. Nested key/value metadata. |

Do not add unsupported top-level frontmatter keys; CI validation will fail.
