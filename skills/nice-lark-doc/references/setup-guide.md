# 环境设置指南

本 skill 依赖 `lark-cli` 及飞书相关 skill。首次使用前运行一键设置：

```bash
bash scripts/setup.sh   # 一键设置：安装 lark-cli + 飞书 skill + 检查 auth
```

设置脚本自动完成三步：

| # | 操作 | 命令 |
|---|---|---|
| 1 | 安装 `lark-cli` | `npm install -g @larksuiteoapi/cli` |
| 2 | 安装飞书 skill（lark-shared, lark-doc, lark-whiteboard, lark-drive） | `npx skills add larksuite/cli -g -y` |
| 3 | 检查 auth 认证状态 | `lark-cli auth status --json --verify` |

如果 auth 未通过，脚本会提示用户执行：

```bash
lark-cli auth login --domain docs --domain drive --no-wait --json
```

将返回的 `verification_url` 展示给用户，用户在浏览器中完成授权后，执行：

```bash
lark-cli auth login --device-code <device_code>
```

> 详细 auth 流程参见 `lark-shared` skill。每次启动本 skill 前可运行 `bash scripts/check-deps.sh` 快速验证环境。
