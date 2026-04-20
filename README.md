# Yuga Sun's Agent Skills

一组面向 AI Agent 的高质量、强偏好技能集合，用来统一现代全栈开发与工作自动化的执行方式。

这些技能适用于支持 Skills 机制的 Agent 环境，比如 Moltbot、Clawdbot、Cursor、Windsurf 或自定义 Agent。仓库重点不是堆砌提示词，而是沉淀可复用的工作流、参考资料、脚本和最佳实践。

## Installation

```bash
npx skills add yugasun/skills
```

全局安装：

```bash
npx skills add yugasun/skills -g
```

CLI 用法见 [vercel-labs/skills](https://github.com/vercel-labs/skills)。

## Why This Repo

- 为常见开发场景提供可复用的 Agent 工作流，而不是每次从零提示。
- 把脚本、参考文档和约定放进同一个 skill 包里，便于长期维护。
- 将 web、server、slides、部署、研究、内容生产等能力拆成独立技能，方便按需组合。

## Skill Catalog

完整技能列表单独维护在 [docs/available-skills.md](docs/available-skills.md)。

## Quick Navigation

- 技能目录： [docs/available-skills.md](docs/available-skills.md)
- 技能实现： [skills/](skills)
- 技能格式规范： [spec/agent-skills-spec.md](spec/agent-skills-spec.md)

## Repository Layout

```text
.
├── skills/          # 实际对外提供的 skills
├── docs/            # 补充文档、设计稿、规划材料
├── spec/            # skill 格式与约束规范
├── template/        # 新 skill 模板
└── AGENTS.md        # 生成与维护规则
```

## Typical Uses

安装后，Agent 可以直接引用这些 skills 来：

1. 脚手架新项目，并沿用统一技术栈与目录约定。
2. 在实现功能时复用已有工作流、参考资料和脚本。
3. 为内容生成、搜索研究、部署发布等任务提供稳定执行路径。

## Contributing

如果你要新增或维护技能，优先阅读 [AGENTS.md](AGENTS.md) 和 [template/SKILL.md](template/SKILL.md)。

常规维护建议：

1. 技能内容更新放在对应的 `skills/<name>/`。
2. 技能增删优先同步到 [docs/available-skills.md](docs/available-skills.md)。
3. 只有在项目定位、安装方式或导航结构变化时再修改 README。

## License

MIT © [Yuga Sun](https://github.com/yugasun)
