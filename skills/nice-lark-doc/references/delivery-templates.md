# 交付模板与渲染细节

## SDK 优先级链

```
1. document.blocks.batchCreateOrReplace  ← 主力 API（单次最多 50 blocks）
2. Document SDK (@larksuiteoapi/document) ← 复杂表格（合并单元格）
3. Document Merge SDK (@larksuiteoapi/document-merge) ← .docx 模板场景
```

## batch 分页策略

```
总 blocks ≤ 50：单次调用
总 blocks > 50：按 50 分页，每页间隔 500ms（避免 rate limit）
```

## 错误恢复

| 错误码 | 含义 | 恢复策略 |
|---|---|---|
| 99991 | QPS rate limit | 等待 2s 后重试，最多 3 次 |
| 1310005003 | 不支持的 block 类型 | 降级为 text block + 文字说明 |
| 1310005202 | document_index 超出范围 | 重新获取最新 index 后重试 |
| 403 | 无编辑权限 | 提示用户检查共享设置，终止 |

## 设计决策摘要模板

交付时固定输出：

```
> 📋 **设计决策**
> - **Recipe**：{recipe_name}（{recipe_slug}）
> - **画板**：{total_count} 个（{mermaid_count} Mermaid + {svg_count} SVG）
>   - {chapter}: {type}（{description}）
> - **表格**：{table_count} 个
> - **Callout**：{callout_count} 个（{emoji_breakdown}）
> - **Checkbox**：{checkbox_count} 个
> - **特殊处理**：{special_handling}
```

## 画板审查记录

每个画板插入后必填：

```
| 画板 | 章节 | 类型 | 审查结论 |
|---|---|---|---|
| {名称} | {章节} | Mermaid/SVG | ✅ 通过 / ⚠️ 需修改 / ❌ 需重做 |
```

## 文档质量自评卡

交付时固定输出：

```
### 📊 文档质量自评卡
| 维度 | 目标 | 实际 | 状态 |
|---|---|---|---|
| 画板覆盖率 | ≥ {target}% h2 | {actual}% ({count}/{total}) | {status} |
| 表格覆盖率 | ≥ {target}% h2 | {actual}% ({count}/{total}) | {status} |
| SVG 画板 | ≥ 1（技术方案） | {svg_count} | {status} |
| 文字墙 | 0 处 | {wall_count} 处 | {status} |
| Callout 分布 | 均匀 | {callout_count}/{total_chapters} | {status} |
| 对比度安全 | 100% | {safe_count}/{total_whiteboard} | {status} |
```

状态标记：✅ 达标 / ⚠️ 接近（差 1-2） / ❌ 未达标（差 3+）

## Recipe 自动择优交付格式

```
> 📋 **Recipe 选型**：{recipe_name}（{recipe_slug}）
> 自动匹配理由：{reason}
> 如需调整风格，告诉我"换 XX 风格"
```
