# 画板配色系统

> 基于飞书画板特性，以蓝色系为核心，支持主题切换，强制对比度安全规则。

## ⚠️ 第一规则：对比度安全

**这是最重要的规则，违反会导致画板内容不可读。**

### 文字-背景对比铁律

| 背景亮度 | 文字颜色 | 适用背景色 |
|---|---|---|
| **深色背景**（亮度 ≤ 50%） | **白色** `#FFFFFF` | #0050E0, #1A3A6E, #2070E0, #2E5090 |
| **中深色背景**（亮度 50-62%） | **白色** `#FFFFFF` | #3B6DB5, #4A6FA5 |
| **中浅色背景**（亮度 62-78%） | **深色** `#1E293B` | #60A0E0, #5B8EC9, #7BA7D6 |
| **浅色背景**（亮度 > 78%） | **深色** `#1E293B` | #93C5FD, #BFDBFE, #DBEAFE, #EFF6FF |

### 速记口诀

```
深色底 → 白字        （品牌蓝、深蓝 → 白字 ✓）
浅色底 → 深色字      （浅蓝、淡蓝、冰蓝 → 深色字 ✓）
中色底 → 查色阶表     （不确定就查下方完整表）
```

### ❌ 绝对禁止的组合

| 禁止组合 | 原因 |
|---|---|
| 浅蓝 `#93C5FD` / `#A0C8E8` + 白色文字 | 对比度不足 2.5:1，不可读 |
| 淡蓝 `#BFDBFE` / `#C8E0F0` + 白色文字 | 同上 |
| 冰蓝 `#DBEAFE` / `#E0F0F8` + 白色文字 | 同上 |
| 中蓝 `#60A0E0` + 白色文字 | 对比度仅 2.8:1，不达标 |
| 深蓝灰 `#1E293B` + 深色文字 | 文字融入背景 |
| 纯白底 + 浅灰文字 `#94A3B8` | 对比度不足，至少用 `#334155` |

### ✅ 正确的文字颜色速查表

| 背景色 | 背景 HEX | 文字色 HEX | 对比度 |
|---|---|---|---|
| 品牌蓝 | `#0050E0` | `#FFFFFF` | 6.8:1 ✅ |
| 皇家蓝 | `#1A3A6E` | `#FFFFFF` | 10.2:1 ✅ |
| 钴蓝 | `#2070E0` | `#FFFFFF` | 4.7:1 ✅ |
| 钢蓝 | `#2E5090` | `#FFFFFF` | 7.1:1 ✅ |
| 矢车菊 | `#4A6FA5` | `#FFFFFF` | 4.6:1 ✅ |
| 天蓝 | `#5B8EC9` | `#1E293B` | 4.8:1 ✅ |
| 中蓝 | `#60A0E0` | `#1E293B` | 4.2:1 ✅ |
| 浅蓝 | `#93C5FD` | `#1E293B` | 3.5:1 ✅ |
| 淡蓝 | `#BFDBFE` | `#1E293B` | 5.2:1 ✅ |
| 冰蓝 | `#DBEAFE` | `#1E293B` | 7.4:1 ✅ |
| 极浅蓝 | `#EFF6FF` | `#1E293B` | 10.8:1 ✅ |
| 白色 | `#FFFFFF` | `#1E293B` | 14.5:1 ✅ |
| 成功浅 | `#DCFCE7` | `#166534` | 8.1:1 ✅ |
| 警告浅 | `#FEF9C3` | `#854D0E` | 7.3:1 ✅ |
| 错误浅 | `#FEE2E2` | `#991B1B` | 6.9:1 ✅ |

---

## 默认主题：Ocean Blue（海洋蓝）

> 精心调校的默认主题，兼顾专业感与视觉舒适度。

### 核心色板

#### 主色系（蓝色家族）

| 角色 | 名称 | HEX | 文字色 | 用途 |
|---|---|---|---|---|
| **强调** | 品牌蓝 | `#0050E0` | `#FFFFFF` | 核心节点、关键路径、CTA |
| **主色** | 皇家蓝 | `#1A3A6E` | `#FFFFFF` | 标题栏、重要模块底色 |
| **主色** | 钴蓝 | `#2070E0` | `#FFFFFF` | 主按钮、活跃节点 |
| **中色** | 钢蓝 | `#2E5090` | `#FFFFFF` | 次级强调、分组标题条 |
| **中色** | 矢车菊 | `#4A6FA5` | `#FFFFFF` | 次级节点、标签底色 |
| **浅色** | 天蓝 | `#5B8EC9` | `#1E293B` | 信息卡片底色 |
| **浅色** | 中蓝 | `#60A0E0` | `#1E293B` | 次要填充色 |
| **背景** | 浅蓝 | `#93C5FD` | `#1E293B` | 分组区域背景 |
| **背景** | 淡蓝 | `#BFDBFE` | `#1E293B` | 容器背景、卡片底色 |
| **背景** | 冰蓝 | `#DBEAFE` | `#1E293B` | 最外层背景色 |
| **背景** | 极浅蓝 | `#EFF6FF` | `#1E293B` | 画板底色 |

#### 中性色

| 名称 | HEX | 用途 |
|---|---|---|
| 墨色 | `#0F172A` | 最深文字（极少使用） |
| 深色 | `#1E293B` | **主文字色**（浅色底一律用它） |
| 深灰 | `#334155` | 次要文字 |
| 中灰 | `#64748B` | 辅助文字、图例 |
| 浅灰 | `#94A3B8` | 弱化文字、标签（白底可用） |
| 分割线 | `#CBD5E1` | 分割线、弱边框 |
| 浅边框 | `#E2E8F0` | 卡片边框 |
| 背景灰 | `#F1F5F9` | 中性背景色 |
| 白色 | `#FFFFFF` | 卡片底色、深色底文字 |

#### 语义色（按需使用，不超过画板面积 10%）

| 语义 | 底色 | 边框/线条 | 文字色 | 用途 |
|---|---|---|---|---|
| 成功/推荐 | `#DCFCE7` | `#16A34A` | `#166534` | 完成、推荐方案、健康状态 |
| 成功深 | `#16A34A` | — | `#FFFFFF` | 成功节点、达标标记 |
| 警告/注意 | `#FEF9C3` | `#CA8A04` | `#854D0E` | 风险、待确认、注意 |
| 警告深 | `#CA8A04` | — | `#FFFFFF` | 警告标记 |
| 错误/风险 | `#FEE2E2` | `#DC2626` | `#991B1B` | 故障、错误、阻塞 |
| 错误深 | `#DC2626` | — | `#FFFFFF` | 错误节点、危险标记 |

### 渐变色预设

```xml
<defs>
  <!-- 品牌渐变：核心模块/标题栏 -->
  <linearGradient id="grad-brand" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#0050E0" />
    <stop offset="100%" stop-color="#1A3A6E" />
  </linearGradient>

  <!-- 钴蓝渐变：主按钮/活跃节点 -->
  <linearGradient id="grad-cobalt" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#3B82F6" />
    <stop offset="100%" stop-color="#2070E0" />
  </linearGradient>

  <!-- 天空渐变：卡片底色/次级模块 -->
  <linearGradient id="grad-sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#DBEAFE" />
    <stop offset="100%" stop-color="#BFDBFE" />
  </linearGradient>

  <!-- 中性渐变：背景区域 -->
  <linearGradient id="grad-neutral" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#F1F5F9" />
    <stop offset="100%" stop-color="#E2E8F0" />
  </linearGradient>

  <!-- 成功渐变 -->
  <linearGradient id="grad-success" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#DCFCE7" />
    <stop offset="100%" stop-color="#BBF7D0" />
  </linearGradient>

  <!-- 警告渐变 -->
  <linearGradient id="grad-warning" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#FEF9C3" />
    <stop offset="100%" stop-color="#FDE68A" />
  </linearGradient>

  <!-- 卡片阴影 -->
  <filter id="shadow-card">
    <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#1E293B" flood-opacity="0.08" />
  </filter>

  <!-- 强调阴影 -->
  <filter id="shadow-emphasis">
    <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#0050E0" flood-opacity="0.15" />
  </filter>
</defs>
```

### 标准 SVG 模板片段

#### 核心模块（深色底 + 白字）

```xml
<!-- 核心模块/标题节点：深底白字，视觉最突出 -->
<g filter="url(#shadow-emphasis)">
  <rect x="100" y="50" width="200" height="60" rx="10" fill="url(#grad-brand)" />
  <text x="200" y="87" text-anchor="middle" fill="#FFFFFF" font-size="15" font-weight="600">
    核心模块名称
  </text>
</g>
```

#### 普通模块（浅色底 + 深色字）

```xml
<!-- 普通模块/卡片：浅底深色字，清晰可读 -->
<g filter="url(#shadow-card)">
  <rect x="100" y="150" width="200" height="60" rx="10"
        fill="url(#grad-sky)" stroke="#CBD5E1" stroke-width="1" />
  <text x="200" y="187" text-anchor="middle" fill="#1E293B" font-size="14" font-weight="500">
    普通模块名称
  </text>
</g>
```

#### 分组容器（极浅底 + 深色字）

```xml
<!-- 分组背景区域：最浅色，虚线边框区分层级 -->
<rect x="50" y="30" width="500" height="300" rx="16"
      fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5" stroke-dasharray="8,4" />
<text x="70" y="55" fill="#64748B" font-size="12" font-weight="500">
  分组标签
</text>
```

#### 连线与箭头

```xml
<defs>
  <marker id="arrow-blue" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" fill="#2070E0" />
  </marker>
  <marker id="arrow-gray" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" fill="#94A3B8" />
  </marker>
</defs>

<!-- 主流程连线 -->
<polyline points="300,80 350,80 350,180 300,180"
          stroke="#2070E0" stroke-width="2" fill="none"
          marker-end="url(#arrow-blue)" />

<!-- 次要连线 -->
<polyline points="300,210 350,210 350,280 300,280"
          stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="6,3" fill="none"
          marker-end="url(#arrow-gray)" />
```

---

## 配色模式

### 模式 A：单色渐变（推荐默认）

只用蓝色家族 + 中性色，通过明度变化创造层次。

```
品牌蓝 #0050E0 + 白字   ← 核心节点、关键路径
  ↓
矢车菊 #4A6FA5 + 白字   ← 次要强调
  ↓
天蓝   #5B8EC9 + 深色字  ← 信息卡片
  ↓
淡蓝   #BFDBFE + 深色字  ← 分组背景
  ↓
极浅蓝 #EFF6FF + 深色字  ← 最外层背景
```

适用：架构图、流程图、关系图、大多数技术图表

### 模式 B：双色对比

蓝色家族 + 一个语义色点缀，用于对比、分支、状态区分。

```
蓝色系 ← 主路径/正常状态/方案 A
  +
语义色  ← 对比路径/异常状态/方案 B
```

语义色选择规则：
- 成功 vs 失败 → 蓝 + 绿
- 当前 vs 目标 → 蓝 + 橙（警告）
- 正常 vs 异常 → 蓝 + 红
- 方案 A vs 方案 B → 蓝 + 蓝灰（冷色对比）

适用：对比图、决策树、状态机、方案对比

### 模式 C：多层分级

蓝色家族 + 色相微偏移区分不同模块/层级。

```
模块 A ← 蓝色：#0050E0 → #BFDBFE
模块 B ← 青色：#0E7490 → #CFFAFE
模块 C ← 紫色：#6D28D9 → #EDE9FE
```

适用：大型架构图、多模块系统图、组织关系图

---


## Tailwind 扩展色板（多色相场景）

> 当画板需要 3 种以上色相区分模块时（如大型架构图、多层系统图），使用 Tailwind CSS 色板扩展。
> 参考文档：[Agentic System 2.0 设计](https://acnv2c6dzsvf.feishu.cn/wiki/SjzVwD55XiF75KkZXC3cWsJ7nBh)

### 核心原则

1. **容器用极浅色底**（Tailwind -50 级），卡片统一白底 + 彩色边框
2. **连线颜色与模块颜色一致**（蓝模块→蓝连线，紫反馈→紫连线）
3. **实线=主流程，虚线=反馈/跨层**
4. **文字层级**：主标题 #0f172a → 模块标题 色相-700 → 描述 #475569

### 四色相模板（架构/系统图常用）

| 色相 | 容器底 (-50) | 卡片边框 (-200/-300) | 模块标题 (-700) | 连线 (-600) | 语义 |
|---|---|---|---|---|---|
| **蓝** | `#eff6ff` | `#93c5fd` / `#bfdbfe` | `#1d4ed8` | `#2563eb` | 主链路、核心流程 |
| **紫** | `#f5f3ff` | `#c4b5fd` | `#6d28d9` | `#7c3aed` | 反馈、优化、复盘 |
| **橙** | `#fff7ed` | `#fed7aa` | `#b45309` | `#f97316` | 数据、知识、资产 |
| **绿** | `#ecfdf5` | `#bbf7d0` / `#86efac` | `#047857` | `#16a34a` | 成功、发布、健康 |

### 中性辅助

| 色相 | 容器底 (-50) | 边框 (-300/-400) | 文字 | 连线 (-500) | 语义 |
|---|---|---|---|---|---|
| **灰** | `#f8fafc` | `#cbd5e1` / `#94a3b8` | `#111827` / `#334155` | `#64748b` | 中性分组、辅助连线 |

### SVG 模板片段

```xml
<!-- 蓝色容器（主链路） -->
<rect fill="#eff6ff" stroke="#93c5fd" stroke-width="3" rx="6" />

<!-- 蓝色卡片（白底 + 蓝边框） -->
<rect fill="#ffffff" stroke="#bfdbfe" stroke-width="1" rx="6" />
<text fill="#1e40af" font-weight="bold">卡片标题</text>
<text fill="#64748b">卡片描述</text>

<!-- 紫色容器（反馈/优化层） -->
<rect fill="#f5f3ff" stroke="#c4b5fd" stroke-width="3" rx="6" />

<!-- 橙色容器（数据层） -->
<rect fill="#fff7ed" stroke="#fed7aa" stroke-width="3" rx="6" />
<text fill="#b45309" font-weight="bold">数据层标题</text>

<!-- 绿色容器（成功/发布） -->
<rect fill="#ecfdf5" stroke="#16a34a" stroke-width="2" rx="6" />

<!-- 蓝色主流程连线（实线） -->
<polyline stroke="#2563eb" stroke-width="3" fill="none" marker-end="url(#arrow-blue)" />

<!-- 紫色反馈连线（虚线） -->
<polyline stroke="#7c3aed" stroke-width="4" stroke-dasharray="8 4" fill="none" marker-end="url(#arrow-violet)" />

<!-- 灰色跨层连线（虚线） -->
<polyline stroke="#64748b" stroke-width="3" stroke-dasharray="8 4" fill="none" />
```

### 对比度速查（Tailwind 极浅色底 + 深色字）

| 背景 | 背景 HEX | 文字 HEX | 对比度 |
|---|---|---|---|
| blue-50 | `#eff6ff` | `#0f172a` / `#1d4ed8` | 13.5:1 / 7.5:1 ✅ |
| violet-50 | `#f5f3ff` | `#0f172a` / `#6d28d9` | 13.0:1 / 7.2:1 ✅ |
| orange-50 | `#fff7ed` | `#0f172a` / `#b45309` | 13.2:1 / 5.5:1 ✅ |
| emerald-50 | `#ecfdf5` | `#0f172a` / `#047857` | 13.8:1 / 7.8:1 ✅ |
| slate-50 | `#f8fafc` | `#0f172a` / `#111827` | 14.2:1 / 13.6:1 ✅ |

> 所有 Tailwind -50 级背景 + 对应 -700 级文字，对比度均 ≥ 4.5:1，满足 WCAG AA。

---

## 主题系统

> 默认主题 Ocean Blue 适用于绝大多数场景。特殊场景可切换主题。

### 主题切换规则

- 默认使用 **Ocean Blue**
- 用户明确要求特定风格时才切换
- 同一文档内所有画板应使用同一主题
- 主题只影响色板，不影响配色模式和对比规则

### Ocean Blue（默认）

专业、冷静、通用。适合技术文档、产品方案、分析报告。

```
强调: #0050E0  #1A3A6E  #2070E0
中色: #2E5090  #4A6FA5
浅色: #5B8EC9  #60A0E0
背景: #93C5FD  #BFDBFE  #DBEAFE  #EFF6FF
中性: #0F172A  #1E293B  #334155  #64748B  #94A3B8  #CBD5E1  #E2E8F0  #F1F5F9  #FFFFFF
```

### Slate Gray（石墨灰）

极简、高级感。适合架构概览、高层汇报。

```
强调: #1E293B  #334155
中色: #475569  #64748B
浅色: #94A3B8  #CBD5E1
背景: #E2E8F0  #F1F5F9  #F8FAFC
点缀: #0050E0（唯一彩色，用于核心路径）
```

### Emerald（翡翠绿）

清新、数据感。适合数据报告、监控系统。

```
强调: #059669  #047857  #065F46
中色: #10B981  #34D399
浅色: #6EE7B7  #A7F3D0
背景: #D1FAE5  #ECFDF5  #F0FDF4
中性: 复用 Ocean Blue 中性色
```

### Sunset（暖霞）

温暖、活力。适合产品叙事、用户故事。

```
强调: #EA580C  #C2410C  #9A3412
中色: #F97316  #FB923C
浅色: #FDBA74  #FED7AA
背景: #FFEDD5  #FFF7ED  #FFFBF5
中性: 复用 Ocean Blue 中性色
```

---

## 各 Recipe 配色指南

| Recipe | 配色模式 | 主题 | 核心色 | 特殊说明 |
|---|---|---|---|---|
| 素雅编辑 | 单色渐变 | Ocean Blue | 品牌蓝 + 淡蓝 | 最克制，只用 2-3 个色阶 |
| 技术严谨 | 单色/双色 | Ocean Blue | 品牌蓝 + 语义色 | 可用语义色标注状态 |
| 产品叙事 | 双色/多层 | Ocean Blue / Sunset | 品牌蓝 + 暖色点缀 | 最活泼，可用渐变和阴影 |
| 行动导向 | 单色渐变 | Ocean Blue | 品牌蓝 + 中性色 | 简洁，少用装饰 |
| 数据密集 | 单色渐变 | Ocean Blue / Emerald | 品牌蓝 + 语义色 | 色彩区分数据维度 |
| 演示风格 | 单色渐变 | Ocean Blue / Slate Gray | 品牌蓝 + 中性色 | 大气，大色块，强对比 |

---

## 自检清单（每次生成 SVG 前过一遍）

- [ ] 每个 `<text>` 元素的 `fill` 是否与其所在容器的背景色有足够对比？
- [ ] 浅色背景（`#93C5FD` 及以上）是否全部使用深色文字 `#1E293B`？
- [ ] 深色背景（`#4A6FA5` 及以下）是否全部使用白色文字 `#FFFFFF`？
- [ ] 是否避免了纯黑 `#000000`？（用 `#0F172A` 或 `#1E293B` 替代）
- [ ] 暖色（红/橙/绿）面积是否 < 画板总面积 10%？
- [ ] 是否使用了不超过 3 种色相？
- [ ] 分组容器是否使用了浅色背景 + 虚线边框以区分层级？
- [ ] 核心模块是否使用了深色底 + 白字以突出重要性？
- [ ] 连线和箭头颜色是否与源节点颜色一致或使用了中性灰？

---

## 禁忌

- ❌ 不使用纯黑 `#000000`，用 `#0F172A` 或 `#1E293B` 替代
- ❌ 不使用高饱和度暖色大面积填充
- ❌ 不使用超过 3 种色相
- ❌ 不使用彩虹色渐变
- ❌ **浅色背景 + 白色文字**（最常见的错误！）
- ❌ **中蓝色 `#60A0E0` + 白色文字**（对比度不足）
- ✅ 用明度变化代替色相变化创造层次
- ✅ 暖色仅用于小面积点缀（< 10%）
- ✅ 所有深色用深蓝系替代纯黑
- ✅ 浅色底一律用 `#1E293B` 深色字
- ✅ 渐变 `grad-brand` / `grad-cobalt` 底用白字
- ✅ 渐变 `grad-sky` / `grad-neutral` 底用深色字
