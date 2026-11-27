---
name: claude-doctor
description: Use when Claude, Claude Desktop, Claude Code or the Anthropic API fails to install, launch, sign in, connect, resolve DNS, or respond on a personal computer (macOS, Windows, Linux), including proxy errors, TLS errors, timeouts, HTTP 401/403/429/5xx, and intermittent connections. 触发词：Claude 打不开、登录失败、Claude Code 连不上、DNS 异常、网络排查、修复 Claude。
---

# Claude Doctor

Restore normal, authorized Claude access on the user's computer using evidence-driven troubleshooting. Distinguish local client, network, authentication, account and service faults before changing configuration.

## Commands

| Invocation | Behavior |
| --- | --- |
| `claude-doctor` or `claude-doctor check` | Default. Run read-only diagnostics and report findings. |
| `claude-doctor repair` | Repair confirmed issues from the latest check, within the user's approved scope. |

Interpret natural-language requests the same way. A generic request to fix Claude starts with `check`; an explicit `repair` without a current diagnostic report starts with `check` too. Never transition automatically from check to repair.

In `check`, do not write configuration, install/update software, restart applications or services, clear caches, sign out, or change DNS, proxy or credentials. Reference documents describe possible remedies, not permission to apply them.

If all checks pass, report the result and stop. If actionable issues are found, present the evidence, proposed changes, expected outcomes and any rollback steps. Ask the user to confirm `repair` for the proposed scope. An explicit confirmation after seeing that plan authorizes repair within that scope; do not ask again for each already approved change. If new issues require different changes, present them for confirmation first. If the user declines or does not confirm, leave the system unchanged.

## Check workflow

1. **Identify the failing surface.** Determine OS, shell, Claude web/Desktop/Code/API, client version, exact redacted error, when it started and whether other clients work. Detect the environment using local tools; ask only for missing facts. If the agent runs remotely, collect results from the affected computer rather than diagnosing its own host.
   If no symptom is specified, run a general health check: detect installed Claude clients and versions, check official status, DNS and HTTPS connectivity for Claude web/API, and inspect relevant proxy and authentication configuration presence. Mark unavailable or inapplicable checks SKIP; do not require an error before starting.
2. **Check service and eligibility.** Check [official service status](https://status.claude.com/) and [supported countries/regions](https://www.anthropic.com/supported-countries). An outage, unsupported location or account restriction is not a local DNS fault.
3. **Collect evidence.** Follow the relevant branches below. Run read-only probes yourself where available, record the failing layer, and distinguish observations from hypotheses. Never print credentials, cookies, authorization headers, complete settings or environment dumps.
4. **Report findings.** Classify each relevant check as PASS, FAIL, WARN or SKIP (with reason). For actionable failures, propose a scoped repair plan and wait for confirmation as described above. For an outage or account restriction, report the official next step rather than proposing unrelated local changes.

## Repair workflow

1. Verify that the approved findings still apply. If the check is stale or missing, repeat relevant read-only probes; obtain confirmation for any new repair scope.
2. **Repair one cause at a time.** Prefer application-local changes over system-wide ones. Back up affected settings, preserve unrelated settings and apply only approved changes using supported configuration and official installation instructions.
3. **Verify.** Repeat the failed probe and the original operation in the affected client. If login requires user interaction or a test would consume paid API usage, let the user perform or authorize it. Roll back ineffective changes; do not claim a repair based only on a successful DNS lookup.

## Branch selection

| Symptom | Read / action |
| --- | --- |
| DNS failure, timeout, TLS, proxy, intermittent connectivity | [Network diagnosis](references/network.md) |
| CLI missing, install/update, Desktop startup, settings conflicts | [Client and authentication](references/client.md) |
| Login, OAuth, 401, 403, 429, 5xx | [Client and authentication](references/client.md) |
| Browser only | Check browser extensions, site-specific settings, system clock and official login flow; compare with a clean browser profile without deleting the existing one. |

Use third-party diagnostics only as optional observations with the user's consent. Do not infer Anthropic's private risk decisions from IP reputation scores. For access restrictions, use official eligibility, verification and support channels; do not alter identity signals or bypass access controls. Keep TLS certificate validation enabled.

## Result

Respond in the user's language. Report:

- **症状 / Symptom:** affected client and original error.
- **检测结果 / Evidence:** relevant probe, observed result and interpretation.
- **原因 / Cause:** confirmed, likely, or unresolved.
- **修复方案 / Repair plan:** in check mode, proposed changes and confirmation request only when actionable issues exist; in repair mode, applied changes and rollback instructions.
- **验证 / Verification:** in check mode, diagnostic results only; in repair mode, whether the original operation succeeded, still fails, or awaits user interaction.

Do not require the user to run commands the agent can safely execute on the affected host.
