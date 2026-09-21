# 设计规则到 Blocks API 映射表

## Block Type 速查

| block_type | 名称 | 用途 |
|---|---|---|
| 1 | page | 文档根节点 |
| 2 | text | 普通文本段落 |
| 3-12 | heading1-heading9 | 标题（3=h1, 4=h2, ...11=h9） |
| 13 | bullet | 无序列表 |
| 15 | ordered | 有序列表 |
| 14 | code | 代码块 |
| 17 | todo | Checkbox 待办 |
| 19 | callout | 高亮块 |
| 27 | image | 图片 |
| 31 | table | 表格 |
| 36 | diagram | 画板/图表 |

## 设计规则映射

### 标题

| Recipe 规则 | API 参数 | 说明 |
|---|---|---|
| 标题编号（1. / 1.1） | block_type = 3-12 | 编号作为文本内容前缀写入 |
| 不使用中文大编号 | 同上 | Recipe 约束层，非 API 层 |
| h1 仅用于文档标题 | block_type = 3 仅在 page 下 | 正文从 block_type=4 (h2) 开始 |

### 段落与文本样式

| Recipe 规则 | API 参数 | 说明 |
|---|---|---|
| 段落字体大小 | text.style.font_size | 数值，单位 pt |
| 加粗 | text_run.text_element_style.bold = true | — |
| 斜体 | text_run.text_element_style.italic = true | — |
| 删除线 | text_run.text_element_style.strikethrough = true | 用于已完成项 |
| 超链接 | text_run.text_element_style.link | URL 字符串 |
| 对齐方式 | text_run.text_element_style.align | 1=left, 2=center, 3=right |

### 表格

| Recipe 规则 | API 参数 | 说明 |
|---|---|---|
| 表头背景色 | table.cells[header_row].paragraph.style.bg_color | 数值色码 |
| 列数限制 | table_property.column_size | Recipe 约束层限制不超过 N 列 |
| 单元格合并 | blocks API 不支持 | 需合并时必须降级到 Document SDK |
| 单元格边框色 | blocks API 不支持 | 只能通过背景色区分 |
| 列宽控制 | blocks API 不支持 | 表格列等宽 |
| 最大列数 | 无硬限制 | Recipe 建议不超过 5 列 |

### 高亮块 (callout)

| Recipe 规则 | API 参数 | 说明 |
|---|---|---|
| 背景色 blue | callout.background_color = 3 | 3=blue |
| 背景色 red | callout.background_color = 1 | 1=red |
| 背景色 yellow | callout.background_color = 7 | 7=yellow |
| 背景色 green | callout.background_color = 2 | 2=green（部分版本支持） |
| emoji 图标 | callout.emoji_id | 如 "bulb", "warning", "info" |
| 边框显示 | callout.border_display | 1=显示, 0=隐藏 |

### Checkbox (todo)

| Recipe 规则 | API 参数 | 说明 |
|---|---|---|
| 未选中 | todo.done = false | 默认状态 |
| 已选中 | todo.done = true | — |
| @提及人 | text_run.text_element_style.mention_user | user_id |

### 图片

| Recipe 规则 | API 参数 | 说明 |
|---|---|---|
| 插入图片 | image.file_token | 上传后返回的 token |
| 图片宽度 | image.width | 像素值 |
| 图片对齐 | image.align | 1=left, 2=center, 3=right |

### 画板 (diagram)

| Recipe 规则 | API 参数 | 说明 |
|---|---|---|
| 嵌入画板 | diagram.diagram_type | 画板类型标识 |
| 画板 ID | diagram.diagram_id | lark-whiteboard 创建后返回 |

## 颜色值速查

### 画板配色（SVG / 飞书画板）

> 详见 `color-palette.md`

| 名称 | HEX | 用途 |
|---|---|---|
| 品牌蓝 | #0050E0 | 核心节点、关键路径 |
| 亮蓝 | #2070E0 | 次要强调 |
| 中蓝 | #60A0E0 | 填充色、次要节点 |
| 浅蓝 | #93C5FD | 分组区域背景 |
| 淡蓝 | #BFDBFE | 容器背景、卡片底色 |
| 冰蓝 | #DBEAFE | 最外层背景色 |
| 深色 | #1E293B | 主文字色（替代纯黑） |
| 中灰 | #64748B | 辅助文字、图例 |
| 浅蓝灰 | #C0C0E0 | 分割线 |
| 成功绿 | #16A34A | 语义色：成功/推荐 |
| 警告橙 | #CA8A04 | 语义色：注意/待确认 |
| 风险红 | #DC2626 | 语义色：警告/风险 |

### 文档元素配色（callout / 表格）

| 语义 | 飞书色值 | callout background_color |
|---|---|---|
| blue（信息） | #EDF4FF | 3 |
| red（警告） | #FFF1F0 | 1 |
| yellow（注意） | #FFFBE6 | 7 |
| green（成功） | #F0FFF0 | 2 |
| light-gray（表头） | #F5F5F5 | — |

## batch 分页策略

```
total_blocks = len(all_blocks)

if total_blocks <= 50:
    单次 batchCreateOrReplace
else:
    pages = ceil(total_blocks / 50)
    for page in range(pages):
        start = page * 50
        end = min(start + 50, total_blocks)
        batchCreateOrReplace(blocks[start:end])
        if page < pages - 1:
            sleep(500ms)  # 避免 rate limit
```

## 错误码速查

| 错误码 | 含义 | 恢复策略 |
|---|---|---|
| 99991 | QPS rate limit | 等待 2s 后重试，最多 3 次 |
| 1310005003 | 不支持的 block 类型 | 降级为 text block + 文字说明 |
| 1310005202 | document_index 超出范围 | 重新获取最新 index 后重试 |
| 403 | 无编辑权限 | 提示用户检查共享设置，终止 |
| 1310005001 | block 不存在 | 检查 document_index，可能已被修改 |
