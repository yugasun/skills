---
name: blog-writer
description: Write long-form Chinese technical blog posts about AI architecture, agent frameworks, tools, protocols, and implementation tradeoffs. Use when the user wants a deep article, architecture analysis, tool deep dive, or blog draft that should combine judgment, examples, Mermaid diagrams, tables, source links, and optional article illustrations.
metadata:
  hermes:
    tags: [blog-writing, technical-article, ai-architecture]
---

# Blog Writer

## Overview

Write long-form, judgment-heavy technical blog posts. Start from one real question, make one defensible thesis, and use diagrams, tables, code, prompts, and illustrations only when they improve understanding.

For this blog repository, default to a personal technical-blog voice with clear author judgment. The article should feel like an engineer thinking something through in public, not a neutral lecture note, SEO article, or polished "standard answer".

Default expectations:

- Use Chinese unless the user asks otherwise.
- Deliver a complete article, not a loose outline, unless the user explicitly asks for a brief.
- Explain why a design or tool matters, not just what it is.
- Preserve source links when external material is used.

## When to Use

- AI or Agent framework architecture analysis
- Tool, protocol, runtime, or workflow deep dives
- Architecture commentary with tradeoff analysis
- Implementation articles that need code, prompts, Mermaid, or tables
- Blog drafts that may need cover or section illustrations tied to the article thesis

Do not use this skill for:

- Short announcements or release notes
- Marketing copy or hype-driven landing page text
- Pure API reference extraction with no editorial judgment

## Deliverables

Every finished article should include:

1. A one-sentence core thesis that is captured in working notes and fully reflected in the article's introduction and conclusion
2. A structure matched to the article mode
3. Supporting material only where it adds clarity: Mermaid, tables, code, prompts, or images
4. A closing judgment with scope, tradeoffs, or recommendations
5. A `## 参考资料` section when external sources were used
6. A completed illustration decision in the workflow, if relevant to the article

Publishable blog Markdown should not include workflow-only scaffolding such as `- core_thesis:` or `## Illustration Decision` unless the user explicitly asks to keep those blocks in the final article.

## Final Delivery Format

The final publishable blog post must contain only reader-facing content:

- frontmatter
- optional image embeds that are meant to appear in the article
- body sections and subsections
- Mermaid diagrams, tables, code blocks, and quotes that are part of the article itself
- a `## 参考资料` section when sources are used

The final publishable blog post must not contain workflow artifacts such as:

- `- core_thesis:` bullets
- `## Illustration Decision`
- illustration briefs or generation plans
- self-review checklists
- “deliverables”, “workflow”, or other meta process notes
- any instruction text aimed at the agent rather than the reader

## Final Output Checklist

Before handing off a publishable article, verify these four rules:

- final Markdown contains only reader-facing content
- thesis is expressed in prose, not as a standalone `- core_thesis:` bullet
- illustration decisions, briefs, and checklists are removed from the publishable article
- article ends with real closing judgment and `## 参考资料` when sources were used

## Smoke Cases

Use the regression notes in `tmp-smoke/20260422-publishable-output/` when you need a quick pressure test after changing this skill. The two minimum cases are:

- a plain publishable article with no illustration workflow leakage
- a `cover-only` article that keeps the cover embed but removes illustration decision logs and briefs from the final Markdown

## Core Workflow

1. Read the relevant material first: source code, docs, release notes, demos, or prior articles.
2. Reduce the topic to one core question and one thesis.
3. Choose the article mode before drafting.
4. Outline around this default spine: why now, problem, mechanism, practice, tradeoffs, conclusion.
5. Write a complete long-form article.
6. Run the illustration review. If the decision is not `none`, follow [the illustration workflow](references/illustration-workflow.md).
7. Strip workflow-only scaffolding from the publishable article while preserving the actual editorial judgment in prose.
8. Run the self-review checklist before delivery.
9. Verify the final output matches the Final Delivery Format section above.

## Article Modes

| Mode       | Use When                           | Preferred Support              |
| ---------- | ---------------------------------- | ------------------------------ |
| 架构解读型 | 分析框架、协议、运行时、上下文机制 | Mermaid 架构图、机制图、对比表 |
| 工具介绍型 | 介绍工具、插件、协议集成、上手流程 | 命令示例、配置片段、操作步骤   |
| 方案实践型 | 讲真实项目如何落地某个能力或模式   | 代码片段、Prompt、流程图       |
| 对比分析型 | 做框架、协议、方案、实现路径取舍   | 对比表、差异清单、选型建议     |

## Style Calibration For This Blog

- Write like an engineer explaining why something matters now, not like a training handout exhaustively covering a topic.
- State the article's judgment early. The introduction should quickly move from topic setup to a clear stance or tension.
- Prefer direct causal claims and concrete tradeoffs over balanced-but-generic summaries.
- Keep an identifiable author voice. The article should sound like someone who has a view, not like a system compiling background material.
- Let paragraphs vary in rhythm. Short emphatic paragraphs are fine when they sharpen the point.
- Section titles should read like real blog headings, not slide bullets, FAQ placeholders, or report headings.

## Voice And Language Texture

Write in a warm, direct, slightly opinionated Chinese technical-blog voice. The prose should have a human pulse: some sentences can be short, some can carry a longer chain of reasoning, and the author is allowed to say "我倾向于", "我不太相信", "这里真正麻烦的是", "这也是我更看重它的原因" when that makes the judgment clearer.

Avoid stiff connective tissue that makes the article sound generated or overly academic. In particular, do not lean on phrases such as:

- "自然是", "自然地", "自然的"
- "显而易见", "毋庸置疑", "不可否认"
- "值得注意的是", "需要指出的是", "从某种意义上说"
- "综上所述", "总而言之", "由此可见"
- "本文将从三个方面", "接下来我们将", "在当今时代背景下"

Replace them with concrete judgment, cause, or scene-setting:

| Stiff                                          | Better                                                         |
| ---------------------------------------------- | -------------------------------------------------------------- |
| "这自然是 Agent 发展的关键一步。"              | "这一步关键，是因为它把经验从一次性上下文里拎了出来。"         |
| "值得注意的是，记忆系统并不等同于向量数据库。" | "这里最容易误判的一点是：记忆系统不是换个名字的向量数据库。"   |
| "综上所述，微调和记忆各有优势。"               | "真正的取舍不在于谁更先进，而在于你要沉淀的是能力，还是经验。" |
| "本文将从架构、实践和风险三个方面展开。"       | "我会先把问题拆开，再看这些系统到底把经验放在了哪里。"         |

Prefer sentences that answer "why this matters" over sentences that merely connect sections. If a transition can be deleted without losing meaning, delete it.

Avoid these patterns unless they are genuinely needed:

- overly symmetrical three-part or four-part breakdowns just because they sound complete
- recap-heavy transitions that restate what the reader already understood
- generic "标准答案腔" phrasing such as abstract summaries that could fit any article with minimal edits
- repetitive sentence scaffolds like "第一/第二/第三" when the section is not inherently list-shaped
- definitions that arrive too late and merely restate what the previous paragraphs already established
- conclusions that only summarize sections instead of sharpening the final judgment
- decorative certainty words such as "自然", "显然", "无疑", "毋庸置疑" when they do not add evidence
- polite filler transitions such as "值得注意的是", "需要指出的是", "综上所述" when a sharper claim would work better

## Readability And Jargon Control

Keep the article technically deep, but do not make readers pay an unnecessary terminology tax. When a paragraph contains multiple English terms, framework labels, or research phrases, slow down and translate the important ones into plain Chinese before moving on.

Default rule: if a reader can understand the idea without the English term, use Chinese. If the English term is useful for search or citation, keep it once in parentheses after a clear Chinese explanation, then use the Chinese phrase afterwards.

Prefer concrete scenes and actions over abstract labels:

| Hard To Read                                     | Clearer                                                        |
| ------------------------------------------------ | -------------------------------------------------------------- |
| "失败只留在 transcript 里，下一次要靠检索碰运气" | "失败只躺在聊天记录里，下次能不能想起来就要看运气"             |
| "test-time learning"                             | "运行时学习，也就是部署以后在同一个任务里越做越好"             |
| "temporal context graph"                         | "带时间的关系图：事实什么时候开始有效、什么时候被新事实覆盖"   |
| "episode provenance"                             | "这条记忆最早来自哪段原始记录"                                 |
| "canonical memory"                               | "被确认过、可以长期使用的可信记忆"                             |
| "embedding cache、reranker、memory backend"      | "检索索引、结果排序、记忆后端；除非机制本身是重点，否则少展开" |

Use examples to lower the reading threshold. A technical claim becomes easier to follow when it is tied to a small scene:

- Instead of only saying "程序性记忆会改写 Agent 行为", add a concrete case such as "这个仓库跑端到端测试前要先启动模拟服务".
- Instead of only saying "上下文窗口缺少治理语义", explain that it cannot decide which fact expired, which preference is temporary, and which rule has been reviewed by a human.
- Instead of only saying "记忆需要可审计", say what should be auditable: source, scope, reviewer, effective time, and deletion path.

Before final delivery, sweep the article for dense terms such as `transcript`, `benchmark`, `workspace id`, `prompt`, `fine-tuning`, `test-time learning`, `temporal context graph`, `validity window`, `episode`, `supersede`, `embedding`, `reranker`, `canonical`, `profile`, `review queue`, `memory backend`, and `agentic configuration`. Translate, explain, or remove each one unless it is truly needed for source accuracy.

## Writing Rules

- Start with why this topic is worth writing now before defining terms.
- Move to the core judgment early; do not spend too long circling the topic before saying what the article actually thinks.
- Define the central concept early in plain language, then keep reconnecting later sections to it.
- Make each major section explain at least two of: the problem, the design reason, the benefit or cost.
- Prefer question-driven or explanation-driven section titles.
- Prefer titles that sound like a human blog writer's framing, not a textbook chapter heading.
- Treat code and prompts as evidence; always explain what they prove.
- Prefer assertive prose over over-buffered phrasing. If a point is clear, say it cleanly.
- Cut any sentence that only exists to make the article sound more "complete" without adding meaning.
- Avoid the rhythm of "raise concept -> define concept -> summarize concept" unless the topic truly needs that pacing.
- Avoid introducing a key phrase repeatedly without explaining how it connects to the article's main question.
- Avoid hype language such as “终极指南”, “颠覆式”, “革命性”.
- End with a synthesized judgment, not a flat recap.
- When tempted to write "自然是/显然/值得注意的是", replace it with the concrete reason, failure mode, or tradeoff behind the claim.
- When a sentence only makes sense to readers who already know the English term, rewrite it around a concrete Chinese explanation or example.

## Depth Standard

- Default to a long-form article unless the user asks for a shorter format.
- The introduction should normally contain at least two substantive paragraphs.
- Those opening paragraphs should establish both the problem and the author's stance, not just background and taxonomy.
- The body should normally contain at least three developed top-level sections.
- Prefer deeper reasoning over adding more headings.
- Avoid list-only sections except for comparisons, checklists, or final recommendations.

## Structure and Material Selection

### Diagrams and Tables

Use Mermaid when the reader needs to see structure, flow, or state.

| Need               | Preferred Format         |
| ------------------ | ------------------------ |
| 系统全景或模块关系 | `graph TB`               |
| 执行流程或调用链   | `graph LR` or `graph TD` |
| 状态变化           | `stateDiagram-v2`        |
| 类或接口关系       | `classDiagram`           |

Prefer tables for comparisons, tradeoffs, evolution, capability matrices, and selection guidance.

Do not add Mermaid just for form. If a simple comparison can be expressed in a table, use the table.

### Code and Prompt Usage

- Only include the key excerpt that supports the argument.
- Explain the mechanism or tradeoff after every excerpt.
- Prefer a small, representative snippet over a large dump.

### Reusable Assets

- Use [the article scaffold](references/article-template.md) when starting from zero.
- Use [the illustration workflow](references/illustration-workflow.md) when images are required.
- For article covers, prefer a horizontal tech-blog banner direction instead of a generic conceptual poster.
- Use `scripts/aliyun_image_gen.py` for image generation. When OSS environment variables are already available in the shell, prefer its built-in `--upload-to-oss` flow so generation, upload, and remote URL collection happen in one command.
- Use `scripts/upload_to_s3.py` as a manual fallback when images already exist locally and only the upload step needs to be rerun.
- Use [the image API reference](references/aliyun-image-gen-api-reference.md) only when low-level image generation details are needed.

## Illustration Review

Before delivery, always make an illustration decision in your workflow notes:

```markdown
## Illustration Decision

- decision: none | cover-only | cover-and-sections
- rationale: [why this article does or does not need images]
```

This block is a workflow artifact. Do not insert it into the final publishable blog Markdown unless the user explicitly requests the decision log to remain visible.

Use `none` when Mermaid and tables already carry the information or when extra images would be decorative noise.

Use `cover-only` when the article is long or abstract enough to benefit from a single thesis-aligned cover image.

For `cover-only`, default to a clean tech-blog banner treatment rather than an open-ended illustration: strong editorial composition, restrained abstract tech motifs, high contrast, no embedded text, and a warm orange accent close to `#ef7070` when it fits the topic.

Use `cover-and-sections` only when the article is long and has multiple strong conceptual transitions that benefit from visual pacing.

If the decision is not `none`:

1. Produce a full brief and generation plan from [the illustration workflow](references/illustration-workflow.md).
2. Generate the images.
3. If OSS upload is configured and upload succeeds, rewrite Markdown with the returned public URLs; otherwise use local `/static/...` paths.
4. If generation or upload fails, record the real blocker.

Do not claim the article is fully illustrated if image generation failed, assets were not saved, or Markdown references were not inserted.

## Source and Accuracy Rules

- Keep original source links in a `## 参考资料` section.
- Verify every cited link resolves to the material actually referenced.
- Prefer stable original URLs over search pages, redirectors, or tracking links.
- If a source is versioned or fast-moving, state the relevant version, date, or context.
- Do not remove sources just to make the article look cleaner.

## Repo-Specific Publishing Conventions

- Use the frontmatter `title` as the article title. Do not add a duplicate H1 in the body.
- Keep Markdown table separator rows in the `| --- | --- |` style.

## Quick Output Templates

### Working-note thesis

```markdown
- core_thesis: [一句话说明文章真正要证明的判断]
```

Use this as an internal drafting aid. In the final article, fold the thesis into the introduction and conclusion instead of leaving it as a standalone bullet.

### Comparison close

```markdown
[真正决定选型的不是功能点数量，而是哪类成本、边界和团队条件更匹配当前问题。]
```

For fuller draft scaffolds and illustration templates, use [the article scaffold](references/article-template.md) and [the illustration workflow](references/illustration-workflow.md).

## Self-Review Checklist

- [ ] 去 AI 味，写给人看，不是写给模型看
- [ ] 没有使用“自然是/自然地/显然/值得注意的是/综上所述”等模板连接词来假装推进
- [ ] 关键术语已经翻译成易懂中文；必要英文只在首次出现时作为补充
- [ ] 难懂概念配了具体场景、失败例子或操作动作，而不是只堆抽象名词
- [ ] 核心概念已经在前文用人话定义，并且后续章节持续回扣它
- [ ] 只读每个标题后的第一句话，也能看出文章主线在递进而不是拼贴
- [ ] 开篇先解释为什么值得写，而不是直接堆定义
- [ ] 开头两三段里已经明确表达作者判断，而不只是铺背景
- [ ] 全文围绕一个明确问题和一个明确判断展开
- [ ] 每个重点章节至少解释了问题、设计原因、收益或代价中的两项
- [ ] 示例真的支撑了论点，并且附带解释
- [ ] Mermaid 和表格是按需使用，而不是为了形式硬加
- [ ] 没有落回“讲义腔”“标准答案腔”或过度匀称的三段论节奏
- [ ] 标题像博客标题，不像汇报提纲或课件小节
- [ ] 已完成插画决策，且该决策不作为流程块暴露在发布稿里
- [ ] 如果插画决策不是 `none`，已按 [illustration workflow](references/illustration-workflow.md) 生成图片或明确记录阻塞原因
- [ ] 结尾给出了综合判断、边界或建议
- [ ] 外部资料已保留在 `## 参考资料` 小节
- [ ] 引用链接已逐条核对
- [ ] 发布稿中不包含 `- core_thesis:`、`## Illustration Decision` 等过程性脚手架
