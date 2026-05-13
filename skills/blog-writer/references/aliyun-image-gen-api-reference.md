---
name: aliyun-image-gen-api-reference
description: Aliyun Bailian Qwen-Image HTTP API notes for text-to-image generation, including regions, models, payload shapes, and response parsing.
---

# Aliyun Bailian Qwen-Image API Reference

这份参考只保留创建 skill 和调用脚本时需要反复查的部分。

## 地域与鉴权

- 北京 base URL: `https://dashscope.aliyuncs.com/api/v1`
- 新加坡 base URL: `https://dashscope-intl.aliyuncs.com/api/v1`
- 认证头: `Authorization: Bearer $DASHSCOPE_API_KEY`
- 本仓库脚本优先从 `ALIYUN_API_KEY` 读取密钥，也兼容 `DASHSCOPE_API_KEY`
- 注意：北京和新加坡 API Key 独立，不能跨地域混用。

## 同步文生图

- 路径: `POST /services/aigc/multimodal-generation/generation`
- 推荐默认模型: `qwen-image-2.0-pro`
- 主要请求体:

```json
{
  "model": "qwen-image-2.0-pro",
  "input": {
    "messages": [
      {
        "role": "user",
        "content": [
          { "text": "一张白底极简海报，中心是一只蓝色纸鹤" }
        ]
      }
    ]
  },
  "parameters": {
    "negative_prompt": "低清晰度，构图混乱",
    "size": "1024*1024",
    "n": 1,
    "watermark": false,
    "prompt_extend": true
  }
}
```

- 主要响应路径: `output.choices[].message.content[].image`

## 异步文生图

- 提交路径: `POST /services/aigc/text2image/image-synthesis`
- 查询路径: `GET /tasks/{task_id}`
- 额外请求头: `X-DashScope-Async: enable`
- 当前文档标注仅 `qwen-image-plus`、`qwen-image` 支持异步 HTTP 接口。
- 建议轮询间隔: 10 秒。

### 异步提交请求体

```json
{
  "model": "qwen-image-plus",
  "input": {
    "prompt": "一张写实风格的城市夜景照片",
    "negative_prompt": "低清晰度，噪点过多"
  },
  "parameters": {
    "size": "1664*928",
    "n": 1,
    "watermark": false,
    "prompt_extend": true
  }
}
```

### 异步状态查询

- 状态流转: `PENDING` -> `RUNNING` -> `SUCCEEDED` / `FAILED`
- 成功结果路径: `output.results[].url`
- `task_id` 和结果 URL 默认仅保留 24 小时。

## 模型选择建议

- `qwen-image-2.0-pro`: 默认首选，同步接口，文本渲染和语义遵循更强。
- `qwen-image-2.0`: 同步接口，加速版，效果与速度平衡。
- `qwen-image-max`: 同步接口，真实感更强。
- `qwen-image-plus`: 支持异步，成本更友好。
- `qwen-image`: 支持异步，与 `qwen-image-plus` 同类。

## 参数提示

- `size` 格式为 `宽*高`。
- `negative_prompt` 适合抑制模糊、畸形、过饱和、AI 感等问题。
- `prompt_extend=true` 时模型会自动补充提示词细节；想要更强可控性时关闭。

## 返回结果处理

- 无论同步还是异步，真正可长期保存的是你自己下载后的本地文件或 OSS 对象，不是 API 返回的临时 URL。
- 若调用失败，关注响应中的 `code`、`message`、`request_id`。

<!--
Source references:
- https://bailian.console.aliyun.com/cn-beijing?tab=api&productCode=p_efm&switchAgent=13556636#/api/?type=model&url=2975126
-->