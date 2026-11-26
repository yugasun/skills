---
name: deploy-server
description: >-
  Use when a user wants to deploy a locally developed app, website, API, or service to a server or VPS they administer, including first-time deployment, SSH access setup for deployment, and updating an existing deployment. Matches requests such as 把本地项目部署到服务器、上线、更新服务器上的服务.
---

# Deploy to a Server

Take the project from the local workspace to a verified running service on the user's authorized server. Use the user's language, explain the next action in plain words, and do the work directly where access and scope permit.

## 1. Find the deployment target

- Inspect the project's README, deployment configuration and build/start commands. Identify the intended release, existing deployment method, environment variable names, persistent data, and how to check that the app works. Do not print secret values.
- Reuse the target from the request or project. Prefer its existing SSH alias and OpenSSH settings (user, port, identity, agent, jump host); don't override them with defaults. If there is no clear target, ask for just the SSH alias, server IP, or hostname. Ask for a port only if it is nonstandard or needed to resolve a connection problem.
- Probe the selected target with a harmless noninteractive command, for example `ssh -o BatchMode=yes -o ConnectTimeout=10 prod-web true`. Run it with a bounded deadline and without an interactive terminal. For a bare IP or hostname, honor an explicit or configured login; if neither exists, use `root` as the stated default instead of implicitly trying the local username. Keep normal host-key verification enabled. A successful probe means no password or onboarding questions are needed.

## 2. First connection: handle the actual SSH error

| Observation | Next action |
| --- | --- |
| Existing access works | Continue to deployment; detect the server OS after login. |
| Unknown host key | Have the user compare the SHA256 fingerprint with a trusted source, such as their hosting console, before accepting it interactively. If a known key changed, resolve the identity mismatch first. |
| Timeout, connection refused, DNS failure, or unreachable jump host | Resolve host, port, or network route first. A password does not fix this. |
| `Permission denied` or an existing key cannot be used | Check the intended account, configured identity and agent access before falling back. On a first deployment, if existing access still cannot work, use the onboarding message below. |

Ask for only missing non-secret details. Use a message like this, localized to the user:

> 现有 SSH 免密登录没成功。请提供服务器 IP（也可以是域名）、系统（默认 Linux）和 SSH 登录名（默认 root）；已提供的不用再发。如果这个账号只能用密码登录，请在你自己的终端看到 SSH 密码提示时输入，不要把密码贴到聊天里。

- If the user already logs in interactively with a key, help them make that key available through their SSH agent and repeat the probe. If the host does not accept password login for the chosen account, use the provider's documented login or console to get the correct account or register a public key; don't enable password or root login to get past the error.
- For a password-only account, give the user the exact SSH target and options resolved above. Have them type the password only at the native SSH prompt. To continue unattended, explain that registering a public key changes access to that account; with the user's authorization, guide them to add the matching local **public** key (for example with `ssh-copy-id -i` when available), preserving existing keys. Never request a private key or move a password through chat, command arguments, environment variables, files, or logs. If noninteractive access cannot be established, continue useful local preparation and give the user only the remote steps that require their terminal.
- After setup, rerun the noninteractive probe against the same target. Continue remote work only when that probe succeeds.

## 3. Deploy and verify

1. **Preflight.** Read the actual OS and architecture, available disk space, relevant runtimes, ports, and current app state before writing. Linux is an onboarding default, not a reason to assume `apt`, systemd, or Docker. Reuse the project's deployment and the server's service conventions. If none exists, choose the simplest compatible option: existing Compose setup for a containerized app; existing web server for static output; a supported service manager for a long-running process.
2. **Stage and release.** Summarize the target, selected release, and any downtime or database changes before applying them. Build with project-defined commands and transfer only needed files, excluding credentials, development-only files, and local data. Keep server-side configuration and persistent data intact. For updates, identify a recoverable prior version before switching; follow the project's backup and migration procedure. Keep app privileges minimal even if the SSH login is `root`. Configure public access only to the extent requested; don't expose a database or internal port just to get a successful check.
3. **Verify the outcome.** Check service state, recent logs, and an application-level health check or smoke test. If public access was requested, verify the actual user-facing URL from outside the server; a successful start or loopback check alone does not prove external access. If verification fails, diagnose and fix within scope, or restore the last known working release when safe; don't blindly reverse database migrations.
4. **Hand over.** Report what is running, where to access it, the check that passed, and the actual commands or paths for logs, updates, and rollback as applicable. If not deployed, name the blocker and distinguish completed preparation from unverified remote work.
