#!/usr/bin/env bash
# setup.sh — One-shot setup for nice-lark-doc
# Installs lark-cli skills and checks auth status
# Usage: bash scripts/setup.sh

set -euo pipefail

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo "🚀 nice-lark-doc 环境设置"
echo "========================="
echo ""

# 1. Check/install lark-cli
echo "📦 Step 1: 检查 lark-cli"
if command -v lark-cli &>/dev/null; then
    echo -e "   ${GREEN}✓ lark-cli 已安装${NC}"
else
    echo -e "   ${YELLOW}⏳ 安装 lark-cli...${NC}"
    npm install -g @larksuiteoapi/cli
    if command -v lark-cli &>/dev/null; then
        echo -e "   ${GREEN}✓ lark-cli 安装成功${NC}"
    else
        echo -e "   ${RED}✗ lark-cli 安装失败，请手动安装: npm install -g @larksuiteoapi/cli${NC}"
        exit 1
    fi
fi

# 2. Install lark skills
echo ""
echo "📦 Step 2: 安装飞书 skill"
SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
NEED_INSTALL=false

for skill in lark-shared lark-doc lark-whiteboard lark-drive; do
    if [[ ! -d "$SKILLS_DIR/$skill" && ! -d "$HOME/.agents/skills/$skill" ]]; then
        NEED_INSTALL=true
        break
    fi
done

if $NEED_INSTALL; then
    echo -e "   ${YELLOW}⏳ 安装飞书 skill（来源: larksuite/cli）...${NC}"
    npx skills add larksuite/cli -g -y
    echo -e "   ${GREEN}✓ 飞书 skill 安装完成${NC}"
else
    echo -e "   ${GREEN}✓ 飞书 skill 已安装${NC}"
fi

# 3. Check auth
echo ""
echo "🔐 Step 3: 检查认证状态"
AUTH_OK=false
if command -v lark-cli &>/dev/null; then
    AUTH_STATUS=$(LARKSUITE_CLI_NO_UPDATE_NOTIFIER=1 LARKSUITE_CLI_NO_SKILLS_NOTIFIER=1 \
        lark-cli auth status --json --verify 2>/dev/null || echo '{"ok":false}')
    if echo "$AUTH_STATUS" | python3 -c "import sys,json; d=json.load(sys.stdin); sys.exit(0 if d.get('ok') and d.get('data',{}).get('verified') else 1)" 2>/dev/null; then
        USER_NAME=$(echo "$AUTH_STATUS" | python3 -c "import sys,json; print(json.load(sys.stdin).get('data',{}).get('identities',{}).get('user',{}).get('userName','unknown'))" 2>/dev/null)
        echo -e "   ${GREEN}✓ 已认证: $USER_NAME${NC}"
        AUTH_OK=true
    fi
fi

if ! $AUTH_OK; then
    echo -e "   ${YELLOW}⚠ 需要授权飞书 API 访问${NC}"
    echo ""
    echo "   请运行以下命令完成授权："
    echo "   lark-cli auth login --domain docs --domain drive --no-wait --json"
    echo ""
    echo "   然后在浏览器中打开返回的 verification_url 完成授权。"
    echo "   授权完成后，再次运行本脚本确认状态。"
fi

# Summary
echo ""
echo "========================="
if $AUTH_OK; then
    echo -e "${GREEN}✅ 设置完成！可以开始使用 nice-lark-doc 了。${NC}"
    echo "   试试: 帮我美化这个飞书文档 <URL>"
else
    echo -e "${YELLOW}⚠ 设置基本完成，还需完成飞书授权。${NC}"
fi
