# 流程图主题规范（Flowchart Theme）

> 从「火车发布上线流程图」提炼的标准流程图主题参考。适用于 SVG 画板路径生成发布流程、审批流程、时间线流程等场景。

## 主题概览

| 属性 | 值 | 说明 |
|---|---|---|
| 主题名称 | **Rail Release** | 火车发布上线风格 |
| 布局方向 | 左→右（时间轴） + 上→下（泳道分层） | 适合有时间维度的流程 |
| 字体 | Noto Sans SC / PingFang SC | 中文优先 |
| 字号 | 标题 14px / 时间标记 14px / 描述 12px | 统一可读 |
| 字重 | regular（标题与正文均为 normal） | 不过度强调 |
| 节点圆角 | `rx="19"` / `ry="19"`（药丸形） | 现代、柔和 |
| 连线宽度 | 2px | 标准粗细 |
| 箭头样式 | 线形三角 `line_arrow` | 简洁专业 |

---

## 色彩系统

### 1. 阶段头部色带（Phase Banners）

流程顶部的阶段分区使用饱和色带，每个阶段一个颜色，形成视觉时间轴：

| 阶段语义 | 填充色 HEX | 文字色 | 用途示例 |
|---|---|---|---|
| **创建/启动** | `#fde2e2`（浅红） | `#1f2329` | 创建火车、项目启动、需求录入 |
| **集成/执行** | `#4e83fd`（蓝色） | `#FFFFFF` | 集成阶段、开发阶段、主流程 |
| **冻结/管控** | `#fff258`（黄色） | `#1f2329` | 冻结阶段、审批阶段、管控期 |
| **部署/发布** | `#ffa53d`（橙色） | `#FFFFFF` | 部署阶段、上线窗口、发布期 |

**设计规则**：
- 阶段色带高度统一 `38px`，宽度根据阶段时长比例分配
- 色带之间用 `1px` 间距分隔
- 饱和色带（蓝/橙）用白字，浅色带（红/黄）用深色字 `#1f2329`

### 2. 流程节点色（Node Fills）

| 节点类型 | 填充色 | 边框色 | 文字色 | 语义 |
|---|---|---|---|---|
| **标准节点** | `#eff0f1` | `#bbbfc4` | `#1f2329` | 普通步骤、信息节点 |
| **成功/通过** | `#d9f5d6` | `#62d256` | `#2b2f36` | 通过审批、测试通过、完成 |
| **警告/检测** | `#feead2` | `#ffa53d` | `#2b2f36` | 需要检测、待确认、风险项 |
| **关键流程** | `#fde2e2` | `#f76964` | `#2b2f36` | 关键操作、紧急流程、阻塞点 |
| **拒绝/超时** | `#bbbfc4` | `#000000` | `#2b2f36` | 拒绝、超时、终止 |
| **紧急操作** | `#fde2e2`（无显式边框） | — | `#1f2329` | 紧急修复、补票 |
| **阶段动作** | `#e1eaff`（无显式边框） | — | `#1f2329` | 自动化操作、系统行为 |
| **阶段入口** | 同阶段色带色 | — | 同上 | 截止提交等阶段标记 |

### 3. 连线色（Connector Colors）

| 连线类型 | 颜色 | 线型 | 用途 |
|---|---|---|---|
| **主流程** | `#bbbfc4` | 实线，箭头 | 正常流程推进 |
| **成功路径** | `#62d256` | 实线，箭头 | 通过/完成路径 |
| **时间线分隔** | `#bbbfc4` | 虚线 `dasharray="4 4"` | 时间点垂直分隔线 |
| **反馈/循环** | `#bbbfc4` | 曲线 `curve`，箭头 | 回到前序阶段 |

### 4. 时间标记色（Time Markers）

| 属性 | 值 |
|---|---|
| 填充 | `#eff0f1` |
| 边框 | `#bbbfc4` |
| 文字 | `#1f2329` |
| 尺寸 | `81×28px`（小药丸） |
| 位置 | 阶段色带下方，对齐时间轴 |

---

## 布局模式

### 模式 A：时间轴 + 泳道流程（主模式）

```
[时间轴]  9:00  ───  11:00  ───  15:00  ───  16:00  ───  19:00
          │          │          │          │          │
[阶段色带] ═══创建═══│═══集成阶段═══│═冻结═│═══部署阶段═══│══结束══
          │          │          │          │          │
[流程层]  ┌──────┐   ┌──────┐   ┌──────┐   ┌──────┐
          │步骤 A │──→│步骤 B │──→│步骤 C │──→│步骤 D │
          └──────┘   └──────┘   └──────┘   └──────┘
                        │          │          │
[泳道分层]           ┌──────┐   ┌──────┐   ┌──────┐
                      │ 小流量 │──→│ 单机房 │──→│ 全流量 │
                      └──────┘   └──────┘   └──────┘
```

**布局参数**：
- 阶段色带高度：`38px`
- 节点间距（水平）：`88-100px`
- 节点间距（垂直）：`48-86px`
- 时间线分隔线：从色带底部延伸至画板底部，虚线
- 泳道标题（如"上线流程"）：左侧垂直排列，使用关键流程色

### 模式 B：线性审批流程

```
[开始] → [提交] → [检测] → [审批] → [合入] → [完成]
                    │            │
                    ▼            ▼
              [需补票]      [超时拒绝]
```

**适用场景**：无时间维度的简单审批流程，节点水平排列。

### 模式 C：分支决策流程

```
[提交] → [检测] ──通过──→ [批准] → [执行]
                │
                └──未通过──→ [修复] → [重新提交]
```

**适用场景**：有明确分支判断的流程，使用绿色/红色语义色区分路径。

---

## SVG 生成模板

### 节点模板

```svg
<!-- 标准节点（药丸形） -->
<g transform="translate(x, y)">
  <rect width="178" height="38" rx="19" ry="19"
        fill="#eff0f1" stroke="#bbbfc4" stroke-width="2"/>
  <text font-size="14" font-family="Noto Sans SC" font-weight="normal"
        fill="#2b2f36" text-anchor="middle" dominant-baseline="alphabetic"
        x="89" y="25">节点文字</text>
</g>

<!-- 成功节点 -->
<g transform="translate(x, y)">
  <rect width="169" height="38" rx="19" ry="19"
        fill="#d9f5d6" stroke="#62d256" stroke-width="2"/>
  <text font-size="14" font-family="Noto Sans SC" font-weight="normal"
        fill="#2b2f36" text-anchor="middle" dominant-baseline="alphabetic"
        x="84" y="25">小组通过</text>
</g>

<!-- 阶段色带 -->
<g transform="translate(x, y)">
  <rect width="325" height="38" rx="0" ry="0"
        fill="#4e83fd"/>
  <text font-size="14" font-family="Noto Sans SC" font-weight="normal"
        fill="#FFFFFF" text-anchor="middle" dominant-baseline="alphabetic"
        x="162" y="25">集成阶段</text>
</g>
```

### 连线模板

```svg
<!-- 主流程连线（带箭头） -->
<marker id="arrow-main" markerWidth="40" markerHeight="40"
        refX="7" refY="0" orient="auto" overflow="visible">
  <path fill="none" stroke="#bbbfc4" stroke-width="2"
        stroke-linecap="round" stroke-linejoin="round"
        d="M 0 -6 L 6 0 L 0 6 M 0 0 L 6 0"/>
</marker>

<!-- 水平连线 -->
<path fill="none" stroke="#bbbfc4" stroke-width="2"
      marker-end="url(#arrow-main)"
      d="M 0 0 L 88 0"/>

<!-- 垂直连线 -->
<path fill="none" stroke="#bbbfc4" stroke-width="2"
      marker-end="url(#arrow-main)"
      d="M 0 0 L 0 48"/>

<!-- 时间线虚线 -->
<path fill="none" stroke="#bbbfc4" stroke-width="2"
      stroke-dasharray="4 4"
      d="M 0 0 L 0 634"/>

<!-- 折线连线（跨越） -->
<path fill="none" stroke="#bbbfc4" stroke-width="2"
      marker-end="url(#arrow-main)"
      d="M 0 236 L 245 236 A 8 8 0 0 0 253 228 L 253 8 A 8 8 0 0 1 261 0 L 288 0"/>
```

---

## 语义色彩速查

| 你想表达什么？ | 用什么颜色 |
|---|---|
| 普通步骤 | 灰底 `#eff0f1` + 灰边框 `#bbbfc4` |
| 通过/成功/完成 | 绿底 `#d9f5d6` + 绿边框 `#62d256` |
| 需要检查/警告 | 橙底 `#feead2` + 橙边框 `#ffa53d` |
| 关键/紧急/阻塞 | 红底 `#fde2e2` + 红边框 `#f76964` |
| 拒绝/超时/终止 | 灰底 `#bbbfc4` + 黑边框 `#000000` |
| 自动化/系统行为 | 蓝底 `#e1eaff`（无边框） |
| 阶段分区 | 饱和色带（蓝 `#4e83fd` / 橙 `#ffa53d` / 黄 `#fff258` / 红 `#fde2e2`） |

---

## 与 Ocean Blue 主题的关系

此流程图主题**独立于** Ocean Blue 画板配色系统。主要差异：

| 对比项 | Ocean Blue（架构/关系图） | Rail Release（流程图） |
|---|---|---|
| 核心色系 | 蓝色家族（#0050E0~#EFF6FF） | 灰+多色语义（红绿橙蓝黄） |
| 节点形状 | 矩形卡片 + 圆角 | 药丸形（rx=19） |
| 布局 | 分层容器嵌套 | 时间轴 + 线性/泳道 |
| 连线 | 蓝实线/紫虚线 | 灰实线/灰虚线 |
| 适用场景 | 架构图、关系图、模块图 | 流程图、审批流、时间线 |

**选择规则**：
- 流程图（有时间维度、审批步骤）→ 使用本主题
- 架构图（分层、模块、依赖）→ 使用 Ocean Blue 主题
- 两者可共存于同一文档中

---

## 来源

- **原始文档**：[火车发布上线流程图](https://bytedance.larkoffice.com/docx/ZDoud0ANJoof7Cxa3uBcH8RsnMb)
- **画板 Token**：`VO06wvmmOh4XpmbAGELcaokwnlc`
- **提炼日期**：2026-07-27
