# Client and authentication

Consult current [Claude Code documentation](https://code.claude.com/docs/en/overview), [Anthropic API errors](https://docs.anthropic.com/en/api/errors) and [Claude Help Center](https://support.claude.com/) for version-specific options and official fixes.

## Installation and startup

- macOS/Linux: `command -v claude`, `type -a claude`, `claude --version`.
- Windows PowerShell: `Get-Command claude -All`, `claude --version`.
- If Claude Code launches, use `claude doctor` to check installation health; inspect `claude --help` for the installed version's supported commands. Redact any sensitive output before reporting.
- If missing or duplicated, identify the installed distribution (native installer, package manager, or legacy npm) and shell PATH. Repair the existing installation using its supported update procedure or migrate per official docs. Do not install Node.js unless the chosen installation method requires it.
- For Desktop startup, distinguish app launch failure from blank web content or login errors. Check OS compatibility, installed version, available disk space and recent application error logs. On Windows check relevant Application events; on macOS check Console for the app. Read only relevant redacted entries. Restart the affected app after saving work; install updates from the official distribution. Preserve user data and sessions.

## Settings and login

Claude Code may have user settings at `~/.claude/settings.json`, project settings at `.claude/settings.json` and `.claude/settings.local.json`, and managed settings. Consult current [settings documentation](https://code.claude.com/docs/en/settings) for precedence and platform paths. Check JSON validity, effective scope and duplicate or conflicting endpoint/authentication settings. Report only relevant key names, presence and sanitized values. Back up and change only the conflicting user-owned setting; do not override managed policy.

Check presence (not value) of relevant environment variables such as `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_BASE_URL`, `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY` and their lowercase proxy variants. Distinguish subscription OAuth, direct Anthropic API and an explicitly configured authorized provider. Verify the intended endpoint before any authenticated request to avoid sending credentials to an unexpected host.

For OAuth, use the official login flow, confirm the browser callback reaches the client and check clock/time synchronization. Use `claude auth status` if supported by the installed version; otherwise use the documented in-client login/status commands. Let the user complete authentication, MFA and verification. Do not read credential stores or ask for tokens, passwords or cookies. Do not sign out or delete session data as a first diagnostic step.

## Errors

| Error | Interpretation and action |
| --- | --- |
| 401 / authentication failed | Check intended auth method, credential presence and expiration; use supported reauthentication. |
| 403 / permission denied | Check account/org permissions, eligibility and official verification or restriction notices. If restrictions persist, contact official support. Do not bypass the restriction. |
| 429 / rate limit | Distinguish rate limit, usage allowance and provider-specific quotas from the sanitized error. Respect retry-after, reduce concurrency and wait for reset or adjust the authorized plan. |
| 5xx / overloaded | Check official status; retry a bounded number of times with backoff only if appropriate. Do not change local DNS based solely on a server error. |
| ENOTFOUND / EAI_AGAIN | Follow network DNS diagnosis. |
| ETIMEDOUT / ECONNRESET / certificate errors | Follow network transport and TLS diagnosis. |
| Invalid configuration / startup crash | Isolate the failing setting, extension or installation error using logs and supported diagnostics; preserve unrelated configuration. |

For browser-only errors, try a private window or clean profile with standard browser settings; do not clear all browsing data. For escalation provide a redacted request ID, timestamp, client version, OS, exact error category and verified network findings. Never include prompts, API secrets, account cookies or raw debug logs.
