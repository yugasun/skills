# Yuga Sun's Agent Skills

[English](README.md) | [简体中文](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CI](https://github.com/yugasun/skills/actions/workflows/ci.yml/badge.svg)](https://github.com/yugasun/skills/actions/workflows/ci.yml)

一组面向 AI Agent 的 [Agent Skills](https://agentskills.io) 集合，用于统一现代全栈开发与工作自动化的执行方式。

这些技能适用于支持 Skills 机制的 Agent 环境，例如 Cursor、Claude Code、Windsurf 或自定义 Agent。仓库重点不是堆砌提示词，而是沉淀可复用的工作流、参考资料、脚本和最佳实践。

## 安装

```bash
npx skills add yugasun/skills
```

全局安装：

```bash
npx skills add yugasun/skills -g
```

CLI 用法见 [vercel-labs/skills](https://github.com/vercel-labs/skills)。

## 为什么用这个仓库

- 为常见开发场景提供可复用的 Agent 工作流，而不是每次从零提示
- 把脚本、参考文档和约定放进同一个 skill 包里，便于长期维护
- 将 web、server、研究、发布、工具等能力拆成独立技能，方便按需组合

## 技能清单

完整列表见 [docs/available-skills.md](docs/available-skills.md)。

| 分类 | 技能 |
| --- | --- |
| 开发 | `dev-web`、`dev-server`、`file-refactor`、`skill-creator` |
| 规划 | `brainstorming` |
| 研究 | `ai-news-collector`、`tavily` |
| 交付 | `html-to-pdf`、**`nice-lark-doc`**、`s3` |
| 媒体 | `aliyun-image-gen` |

## 精选技能：`nice-lark-doc`

> [!TIP]
> **把朴素的飞书文档变成专业、易读的成品。** `nice-lark-doc` 对内容做 5 维度评分，匹配 **6 种风格配方（Recipe）**，再用画板（SVG / Mermaid）、表格、Callout、Checkbox 渲染出结构清晰的飞书文档，并通过视觉节奏规则确保「文字墙」不会出现。

核心亮点：

- **6 种风格配方，按意图匹配** —— 素雅编辑、技术严谨、产品叙事、行动导向、数据密集、演示风格。
- **画板优先**：架构 / 流程 / 关系 → SVG 画板；时序 / 类图 / 饼图 / 甘特图 → Mermaid；画板会解析为可编辑的飞书节点。
- **反文字墙规则**：连续纯文本不超过 3 段，各配方视觉元素占比 20%–60%，配色遵循对比度铁律。
- **美化现有文档**：直接给飞书文档 URL，自动诊断 → 重新匹配配方 → 渲染，不删减原文信息。
- 基于飞书 CLI（`lark-doc` / `lark-whiteboard` / `lark-drive`）；首次使用运行 `bash scripts/setup.sh`。

入口：[`skills/nice-lark-doc/SKILL.md`](skills/nice-lark-doc/SKILL.md)

## 仓库结构

```text
.
├── skills/              # 对外发布的 skill 包
├── docs/                # 技能清单与补充文档
├── spec/                # 格式规范与约束说明
├── template/            # 新 skill 模板
├── CONTRIBUTING.md      # 贡献者指南
├── AGENTS.md            # Agent 维护规则
└── .github/workflows/   # CI 校验
```

## 快速导航

- 技能清单：[docs/available-skills.md](docs/available-skills.md)
- 技能实现：[skills/](skills)
- 技能格式规范：[spec/agent-skills-spec.md](spec/agent-skills-spec.md)
- 贡献指南：[CONTRIBUTING.md](CONTRIBUTING.md)

## 典型用途

安装后，Agent 可以直接引用这些 skills 来：

1. 脚手架新项目，并沿用统一技术栈与目录约定。
2. 在实现功能时复用已有工作流、参考资料和脚本。
3. 为研究、发布、内容交付等任务提供稳定执行路径。

## 贡献

欢迎提交 Issue 和 Pull Request。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

面向 Agent 的维护规则见 [AGENTS.md](AGENTS.md)。

## 许可证

MIT © [Yuga Sun](https://github.com/yugasun)
