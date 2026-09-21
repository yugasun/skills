# Yuga Sun's Agent Skills

[English](README.md) | [简体中文](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/yugasun/skills/actions/workflows/ci.yml/badge.svg)](https://github.com/yugasun/skills/actions/workflows/ci.yml)

Reusable [Agent Skills](https://agentskills.io) for modern full-stack development and workflow automation.

These skills work in agent environments that support the Skills format, such as Cursor, Claude Code, Windsurf, and custom agents. The repository focuses on durable workflows, references, scripts, and conventions—not one-off prompts.

## Installation

```bash
npx skills add yugasun/skills
```

Global install:

```bash
npx skills add yugasun/skills -g
```

See [vercel-labs/skills](https://github.com/vercel-labs/skills) for CLI usage.

## Why This Repo

- Reusable agent workflows for common development tasks
- Scripts, references, and conventions packaged per skill
- Independent skills for web, server, research, publishing, and utilities

## Skill Catalog

The full list lives in [docs/available-skills.md](docs/available-skills.md).

| Area | Skills |
| --- | --- |
| Development | `dev-web`, `dev-server`, `file-refactor`, `skill-creator` |
| Planning | `brainstorming` |
| Research | `ai-news-collector`, `tavily` |
| Delivery | `html-to-pdf`, **`nice-lark-doc`**, `s3` |
| Media | `aliyun-image-gen` |

## Featured Skill: `nice-lark-doc`

> [!TIP]
> **Turn plain Lark (Feishu) docs into professional, readable documents.** `nice-lark-doc` scores your content across 5 dimensions, matches one of **6 style recipes**, and renders structured Lark docs with whiteboards (SVG / Mermaid), tables, callouts, and checkboxes — enforcing visual rhythm so a wall of text never ships.

Highlights:

- **6 style recipes matched to intent** — 素雅编辑 (editorial), 技术严谨 (technical), 产品叙事 (product narrative), 行动导向 (action-oriented), 数据密集 (data-dense), 演示风格 (presentation).
- **Whiteboard-first**: architecture / flow / relationships → SVG whiteboards; sequence / class / pie / gantt → Mermaid; every whiteboard is parsed into editable Lark nodes.
- **Anti-text-wall rules**: at most 3 consecutive text paragraphs, a per-recipe visual ratio (20%–60%), and a contrast-safe color system.
- **Beautifies existing docs**: point it at a Lark URL and it diagnoses, re-matches a recipe, and re-renders without dropping source information.
- Built on the Lark CLI (`lark-doc` / `lark-whiteboard` / `lark-drive`). First run: `bash scripts/setup.sh`.

Entry: [`skills/nice-lark-doc/SKILL.md`](skills/nice-lark-doc/SKILL.md)

## Repository Layout

```text
.
├── skills/              # Published skill packages
├── docs/                # Catalog and supporting docs
├── spec/                # Format pointers and constraints
├── template/            # Minimal new-skill template
├── CONTRIBUTING.md      # Human contributor guide
├── AGENTS.md            # Agent maintenance guide
└── .github/workflows/   # CI validation
```

## Quick Navigation

- Skill catalog: [docs/available-skills.md](docs/available-skills.md)
- Skill packages: [skills/](skills)
- Skill format spec: [spec/agent-skills-spec.md](spec/agent-skills-spec.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)

## Typical Uses

After installation, agents can use these skills to:

1. Scaffold projects with consistent stacks and folder conventions.
2. Reuse workflows, references, and scripts during implementation.
3. Run stable paths for research, publishing, and content delivery tasks.

## Contributing

Issues and pull requests are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md).

For agent-oriented maintenance rules, see [AGENTS.md](AGENTS.md).

## License

MIT © [Yuga Sun](https://github.com/yugasun)
