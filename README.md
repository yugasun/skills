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
| Delivery | `html-to-pdf`, `s3` |
| Media | `aliyun-image-gen` |

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
