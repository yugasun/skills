---
name: aliyun-image-gen
description: Use when generating images with Aliyun Bailian or DashScope Qwen-Image APIs, especially when you need region-aware HTTP calls, async task polling, or downloading temporary image URLs.
---

# Aliyun Image Generation

使用阿里云百炼 Qwen-Image 文生图接口生成图片，默认走官方 HTTP API，不依赖 DashScope SDK。

## 何时使用

- 需要通过阿里云百炼 API 做文生图。
- 需要区分北京与新加坡地域 endpoint。
- 需要提交异步任务、轮询任务状态，或把返回的临时图片 URL 下载到本地。

## 快速开始

先配置环境变量：

```bash
export ALIYUN_API_KEY="sk-xxx"
```

兼容旧变量名 `DASHSCOPE_API_KEY`，但优先读取 `ALIYUN_API_KEY`。

同步生成一张图并下载：

```bash
skills/aliyun-image-gen/scripts/aliyun_image_gen.py generate \
  "一张极简风格的科技海报，白底，中心是蓝色折纸鹤" \
  --model qwen-image-2.0-pro \
  --size 1024*1024 \
  --download
```

异步提交并等待完成：

```bash
skills/aliyun-image-gen/scripts/aliyun_image_gen.py generate \
  "一张写实风格的咖啡馆照片，暖色夕阳光线" \
  --mode async \
  --model qwen-image-plus \
  --wait \
  --download
```

按任务 ID 查询异步结果：

```bash
skills/aliyun-image-gen/scripts/aliyun_image_gen.py status <task_id> --download
```

## 工作流约定

- 默认地域是 `beijing`；新加坡需显式传 `--region singapore`。
- 同步模式默认模型是 `qwen-image-2.0-pro`，适合大多数文生图调用。
- 异步模式当前只允许 `qwen-image-plus` 和 `qwen-image`，脚本会先做本地校验。
- 返回图片 URL 默认只有 24 小时有效期；如果要保留结果，立即加 `--download`。

## 关键参数

- `--negative-prompt`: 反向提示词。
- `--size`: 输出分辨率，格式如 `1024*1024`、`1664*928`。
- `--image-count`: 期望输出张数；实际是否支持以模型约束为准。
- `--no-prompt-extend`: 关闭模型自动扩写提示词。
- `--watermark`: 打开水印，默认关闭。
- `--json`: 输出完整 JSON，方便二次处理。

## 参考资料

- 接口细节、模型能力和 endpoint 见 [references/api-reference.md](references/api-reference.md)

<!--
Source references:
- https://bailian.console.aliyun.com/cn-beijing?tab=api&productCode=p_efm&switchAgent=13556636#/api/?type=model&url=2975126
-->