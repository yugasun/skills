# Yuga Sun's Agent Skills

A collection of high-quality, opinionated agent skills for modern full-stack development. These skills are designed to be used with AI agents (like Cursor, Windsurf, or custom agents) to standardize project creation and maintenance.

## Installation

```bash
# Using pnpm
pnpx skills add yugasun/skills
```

or to install it globally:

```bash
# Using pnpm
pnpx skills add yugasun/skills -g
```

Learn more about the CLI usage at [skills](https://github.com/vercel-labs/skills).


## Available Skills

### 🌐 Web (`web`)
A modern, high-performance frontend stack.
- **Runtime**: [Bun](https://bun.sh)
- **Framework**: React 19 + Vite
- **Language**: TypeScript 5 (Strict Mode)
- **Styling**: Tailwind CSS 4 + shadcn/ui 3
- **State**: TanStack Query & Router

### 🖥️ Server (`server`)
A robust, async Python backend stack.
- **Manager**: [uv](https://github.com/astral-sh/uv)
- **Framework**: FastAPI (Python 3.12+)
- **Database**: Async SQLAlchemy + Alembic
- **AI**: LiteLLM (OpenAI/Aliyun) + Docling

### 📊 Slides (`slides`)
An interactive, single-file HTML presentation generator.
- **Theme**: "Cyberpunk Professional" / Dark Tech
- **Format**: Single HTML file with embedded CSS/JS
- **Features**: Mobile responsiveness, navigation controls, animations

## Usage

Once installed, your AI agent will have access to these skills and can reference them to:
1.  Scaffold new projects with the correct directory structure and configuration.
2.  Implement features following best practices.
3.  Ensure consistency across your distinct "web" and "server" workspaces.

## License

MIT © [Yuga Sun](https://github.com/yugasun)
