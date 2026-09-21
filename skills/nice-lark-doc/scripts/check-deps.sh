#!/usr/bin/env bash
# check-deps.sh — Check and install nice-lark-doc dependencies
# Usage: bash scripts/check-deps.sh [--fix]
#
# Checks:
#   1. lark-cli binary is installed
#   2. Required skills (lark-doc, lark-whiteboard, lark-drive) exist
#   3. lark-cli auth is active
#
# With --fix: attempts to install missing skills via npx skills add

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

FIX=false
[[ "${1:-}" == "--fix" ]] && FIX=true

SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
# Fallback to ~/.agents/skills if that exists
[[ ! -d "$SKILLS_DIR/lark-doc" && -d "$HOME/.agents/skills/lark-doc" ]] && SKILLS_DIR="$HOME/.agents/skills"

REQUIRED_SKILLS=(lark-shared lark-doc lark-whiteboard lark-drive)
MISSING_SKILLS=()
ERRORS=0

echo "🔍 nice-lark-doc 依赖检查"
echo "========================="
echo ""

# 1. Check lark-cli
echo -n "1. lark-cli binary: "
if command -v lark-cli &>/dev/null; then
    VERSION=$(lark-cli version 2>/dev/null | head -1 || echo "unknown")
    echo -e "${GREEN}✓ $VERSION${NC}"
else
    echo -e "${RED}✗ 未安装${NC}"
    echo "   安装: npm install -g @larksuiteoapi/cli"
    ERRORS=$((ERRORS + 1))
fi

# 2. Check required skills
echo ""
echo "2. 依赖 skill（来源: larksuite/cli）:"
for skill in "${REQUIRED_SKILLS[@]}"; do
    echo -n "   $skill: "
    if [[ -d "$SKILLS_DIR/$skill" ]]; then
        echo -e "${GREEN}✓${NC}"
    else
        echo -e "${RED}✗ 缺失${NC}"
        MISSING_SKILLS+=("$skill")
    fi
done

if [[ ${#MISSING_SKILLS[@]} -gt 0 ]]; then
    ERRORS=$((ERRORS + 1))
    echo ""
    if $FIX; then
        echo -e "${YELLOW}⏳ 正在安装缺失 skill...${NC}"
        echo "   执行: npx skills add larksuite/cli -g -y"
        npx skills add larksuite/cli -g -y 2>&1 | sed 's/^/   /'
    else
        echo -e "${YELLOW}💡 一键安装: npx skills add larksuite/cli -g -y${NC}"
        echo "   或带 --fix 重新运行本脚本自动安装"
    fi
fi

# 3. Check auth
echo ""
echo -n "3. lark-cli 认证: "
if command -v lark-cli &>/dev/null; then
    AUTH_STATUS=$(LARKSUITE_CLI_NO_UPDATE_NOTIFIER=1 LARKSUITE_CLI_NO_SKILLS_NOTIFIER=1 \
        lark-cli auth status --json --verify 2>/dev/null || echo '{"ok":false}')
    if echo "$AUTH_STATUS" | python3 -c "import sys,json; d=json.load(sys.stdin); sys.exit(0 if d.get('ok') and d.get('data',{}).get('verified') else 1)" 2>/dev/null; then
        USER_NAME=$(echo "$AUTH_STATUS" | python3 -c "import sys,json; print(json.load(sys.stdin).get('data',{}).get('identities',{}).get('user',{}).get('userName','unknown'))" 2>/dev/null)
        echo -e "${GREEN}✓ $USER_NAME${NC}"
    else
        echo -e "${RED}✗ 未认证或已过期${NC}"
        echo "   授权: lark-cli auth login --domain docs --domain drive --no-wait --json"
        ERRORS=$((ERRORS + 1))
    fi
else
    echo -e "${YELLOW}⊘ 跳过（lark-cli 未安装）${NC}"
fi

# Summary
echo ""
echo "========================="
if [[ $ERRORS -eq 0 ]]; then
    echo -e "${GREEN}✅ 所有检查通过，可以开始使用 nice-lark-doc${NC}"
    exit 0
else
    echo -e "${RED}❌ 发现 $ERRORS 个问题，请修复后再使用${NC}"
    exit 1
fi
