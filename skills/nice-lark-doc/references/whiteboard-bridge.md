# 画板渲染接入指南

飞书画板是 nice-lark-doc 的**核心可视化引擎**。它是一个色彩丰富、可交互编辑的矢量画布，嵌入在飞书文档中，特别适合呈现难以用纯文字理解的复杂信息。

## 核心原则

1. **画板优先**：复杂概念（架构、流程、关系、对比）优先用画板呈现
2. **多画板策略**：一篇文档可以有多个画板，每个聚焦一个主题
3. **大胆设计**：SVG 路径下打破单调矩形牢笼，充分利用色彩、图标、渐变、阴影
4. **审查循环**：插入后导出 PNG 预览，不满意可重新生成

## 两条插入路径

### 路径 A：Mermaid（结构化图表）

**适用图表类型**：
- 思维导图（mindmap）
- 时序图（sequenceDiagram）
- 类图（classDiagram）
- 饼图（pie）
- 甘特图（gantt）
- 简单流程图（graph/flowchart）
- 状态图（stateDiagram）
- ER 图（erDiagram）

**插入方式**：
```xml
<whiteboard type="mermaid">
graph LR
    A[用户请求] --> B[API 网关]
    B --> C[服务 A]
    B --> D[服务 B]
    C --> E[(数据库)]
    D --> E
</whiteboard>
```

如果 Mermaid 已在本地文件中：
```xml
<whiteboard type="mermaid" path="@diagram.mmd"></whiteboard>
```

**优势**：语法简洁，画板直接解析渲染，无需额外处理。

### 路径 B：SVG（自由设计图表）

**适用图表类型**：
- 系统架构图
- 复杂流程图
- 关系图 / 拓扑图
- 数据流图
- 自定义图形 / 信息图
- 组织关系图
- 能力分层图
- 鱼骨图、金字塔图

**插入方式**：
```xml
<whiteboard type="svg">
<svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
    <!-- 大胆设计，色彩丰富 -->
</svg>
</whiteboard>
```

如果 SVG 已在本地文件中：
```xml
<whiteboard type="svg" path="@diagram.svg"></whiteboard>
```

**优势**：完全设计自由，可大胆使用色彩、渐变、阴影、图标路径。

## SVG 设计指南

### 核心心智

> **打破单调的 `<rect>` 牢笼！** 严禁通篇用矩形和文字应付用户。
> 大胆使用 `<path>` 图标、流畅的连接线、各种环境氛围点缀，充分发挥设计创造力。

### 可使用的 SVG 元素

| 元素类型 | SVG 标签 | 画板处理 |
|---|---|---|
| 形状 | `<rect>` `<circle>` `<ellipse>` `<polygon>` | 转为可编辑节点 |
| 连线 | `<line>` `<polyline>` `<path>` | 自动识别为直线/折线/曲线 |
| 文本 | `<text>` `<tspan>` | **必须用 `<text>`**（不是 `<path>`） |
| 分组 | `<g>` `<a>` `<use>` | 正常识别 |
| 变换 | `translate` `rotate` `scale` | 正常；避免 `skewX`/`skewY`/`matrix` |
| 阴影 | `<feDropShadow>` | 识别为节点阴影（drop 至多 1 个） |
| 渐变 | `<linearGradient>` `<radialGradient>` | 在 `<defs>` 中定义，通过 `fill="url(#id)"` 引用 |

### 不支持的 SVG 特性（避免使用）

- `<pattern>` / `<clipPath>` / `<mask>`
- 非阴影用途的 `<filter>`（blur、hue-rotate 等）
- `gradientUnits="userSpaceOnUse"`
- `spreadMethod="reflect|repeat"`
- 复杂 `gradientTransform`

### 设计建议

- 连线使用正交折线（`<polyline>` 带水平/垂直折点）效果更好
- 给重要节点加光环、高亮背景
- 对比项设计天平或对称结构
- 容器宽度留够——画板按 CJK ≈ 1em / Latin ≈ 0.6em 重排
- 文字用 `<text>`（不是 `<path>`），保证可编辑

## 配色系统

画板配色遵循 `references/color-palette.md` 中定义的色系规范。

### ⚠️ 对比度安全（最高优先级）

**浅色背景 + 白色文字 = 不可读！这是最常见的错误。**

速查规则：
- **深色底**（#4A6FA5 及更深）→ 用白色文字 `#FFFFFF`
- **浅色底**（#60A0E0 及更浅）→ 用深色文字 `#1E293B`
- **语义色浅色底**（#DCFCE7, #FEF9C3, #FEE2E2）→ 用对应深色文字（见 color-palette.md 速查表）

### 色板概要

- **核心色系**：蓝色家族（#0050E0 → #4A6FA5 → #5B8EC9 → #93C5FD → #BFDBFE → #DBEAFE → #EFF6FF）
- **中性色**：（#0F172A → #1E293B → #334155 → #64748B → #94A3B8 → #CBD5E1 → #E2E8F0 → #F1F5F9 → #FFFFFF）
- **语义色**：仅按需使用（成功 #16A34A / 警告 #CA8A04 / 错误 #DC2626）

**配色模式选择**：
- 默认用**单色渐变**（蓝色家族 + 中性色）
- 需要对比/分支时用**双色对比**（蓝 + 1 个语义色）
- 大型多模块图用**多层分级**（色相微偏移区分模块）

**核心规则**：
- 不用纯黑，用 `#0F172A` 或 `#1E293B` 替代
- 暖色仅小面积点缀（< 10%）
- 用明度变化代替色相变化创造层次
- **每次生成 SVG 前，检查 color-palette.md 的自检清单**

> 完整色板、渐变色预设、SVG 模板片段、主题系统详见 `references/color-palette.md`

## SubAgent 并行创建

当文档需要多个独立画板时，可启动多个 SubAgent 并行创建：

```
主 Agent：规划 N 个画板的位置和主题
    ↓
并行启动 N 个 SubAgent：
    SubAgent 1 → 画板 A（架构图）
    SubAgent 2 → 画板 B（流程图）
    SubAgent 3 → 画板 C（关系图）
    ↓
每个 SubAgent 只负责一个画板，互不依赖
    ↓
主 Agent 收集结果，统一插入文档
```

每个 SubAgent 的最小上下文：
- doc token、插入位置（标题 / block_id / command）
- 图表目标、受众、源段落或数据
- SVG 必须完整自包含：包含 `<svg>` 根节点和 `viewBox`，不引用外部资源

## 审查循环

插入画板后，导出 PNG 预览确认效果：

```bash
lark-cli whiteboard +export \
  --whiteboard-token "wbcnxxxxxxxx" \
  --output-type preview \
  --output ./preview.png
```

如果设计不满意：
1. 修改 SVG / Mermaid 源码
2. 删除原来的画板
3. 重新插入

## 各 Recipe 的画板策略

| Recipe | 画板频率 | 推荐类型 | Mermaid vs SVG |
|---|---|---|---|
| 素雅编辑 | 每 h2 建议 1 个 | 概念关系图 | SVG 为主，风格素雅克制 |
| 技术严谨 | 每 h2 至少 1 个 | 架构图、流程图、ER 图 | 混合：时序图用 Mermaid，架构图用 SVG |
| 产品叙事 | 每 h2 至少 1-2 个 | 用户旅程、界面线框 | SVG 为主，风格活泼多色 |
| 行动导向 | 适度使用 | 流程图、决策树 | SVG 为主，风格简洁 |
| 数据密集 | 适度使用 | 趋势图、关系图 | SVG 为主，辅助表格 |
| 演示风格 | 每 h2 必须 1 个 | 大画板（视觉主体） | SVG 为主，大气高级感 |

## 可视化转译速查

| 内容类型 | 画板类型 | 路径 |
|---|---|---|
| 系统架构 / 组件关系 | 架构图 | SVG |
| 数据流转 / 请求链路 | 流程图 / 时序图 | SVG 或 Mermaid |
| 状态变迁 | 状态机图 | Mermaid |
| 数据库结构 | ER 图 | Mermaid |
| 用户使用流程 | 用户旅程图 | SVG |
| 角色与权限关系 | 角色关系图 | SVG |
| 功能模块分层 | 能力分层图 | SVG |
| 因果链条 / 演进过程 | 流程图 | SVG |
| 分类体系 / 层次关系 | 思维导图 | Mermaid |
| 项目排期 | 甘特图 | Mermaid |
| 占比分布 | 饼图 | Mermaid |
| 决策流程 | 决策树 | SVG |
| 风险链路 | 因果图 | SVG |
| 组织关系 | 组织关系图 | SVG |
| 里程碑 | 时间轴 | SVG |
| 指标趋势 | 趋势图 | SVG |

## 与 lark-whiteboard skill 的协作

nice-lark-doc 负责**规划**画板（类型、位置、主题），lark-whiteboard 负责**执行**画板的创建、渲染、写入：

| 职责 | 负责方 |
|---|---|
| 识别画板机会、规划主题 | nice-lark-doc |
| 选择 Mermaid / SVG 路径 | nice-lark-doc |
| 生成 Mermaid 代码 | nice-lark-doc（简单）/ lark-whiteboard（复杂） |
| 生成 SVG 代码 | lark-whiteboard SubAgent |
| 插入画板到文档 | lark-doc |
| 导出预览、审查 | lark-whiteboard |
| 修改已有画板 | lark-whiteboard |
