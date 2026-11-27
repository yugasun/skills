# Network diagnosis

## Read-only probes

Test `claude.ai` for the web surface and `api.anthropic.com` for the API/CLI surface. Substitute the actual configured authorized API host if different. Run each probe on the affected host and note which client/network context it represents. A shell, browser and desktop app may use different proxy and resolver settings.

| Layer | macOS | Linux | Windows PowerShell |
| --- | --- | --- | --- |
| OS resolver | `dscacheutil -q host -a name api.anthropic.com` | `getent ahosts api.anthropic.com` | `Resolve-DnsName api.anthropic.com` |
| DNS configuration | `scutil --dns` | `resolvectl status` (if available) | `Get-DnsClientServerAddress` |
| Proxy settings | `scutil --proxy` | Inspect desktop network settings and proxy variable presence | `netsh winhttp show proxy` and Settings > Network & internet > Proxy |
| Clock | `date -u` | `date -u` | `Get-Date` |

Filter output locally: resolver addresses, network names, internal hostnames and proxy URLs can reveal private infrastructure. Do not output proxy userinfo or query strings. `netsh winhttp` describes WinHTTP, not all Windows apps. DNS configuration output is not proof of which resolver answered a given request.

For an unauthenticated HTTPS check (use `curl.exe` in Windows PowerShell):

```sh
curl -sS -o /dev/null --connect-timeout 8 --max-time 20 -w 'http=%{http_code} dns=%{time_namelookup}s connect=%{time_connect}s tls=%{time_appconnect}s total=%{time_total}s\n' https://api.anthropic.com/
```

On Windows replace `/dev/null` with `NUL`. Run against the web host as needed. HTTP 401, 403 or 404 can still show that HTTPS reached a responding server, but cannot prove account authorization or that an intermediary did not respond. Do not send credentials in this probe or interpret it as an authenticated API call. Curl may not inherit the browser's network settings.

## Interpret and repair

| Evidence | Next step |
| --- | --- |
| Name resolution fails | Check current network connection, configured resolver and local resolver service. Correct accidentally stale or invalid DNS settings using the OS-supported UI and approved network configuration. Repeat OS resolver and HTTPS checks. |
| DNS works but TCP times out | Check local connectivity and whether existing approved proxy/firewall configuration is reachable. Consult network administrator if required. |
| TLS certificate or handshake error | Check system clock, OS trust-store updates and authorized enterprise inspection configuration. Validate certificate chain through supported tooling. Never disable verification or install an unknown root CA. |
| IPv4/IPv6 differences | Inspect A/AAAA responses and OS connectivity; treat address-family failure as evidence of a local network issue, not an account-risk signal. Repair the affected network stack or contact the administrator rather than disabling IPv6 globally. |
| Web works but CLI fails | Inspect shell proxy variable presence and CLI-specific settings; compare the CLI's actual endpoint and trust configuration with the documented supported settings. |
| Intermittent slow requests | Record a small number of timestamped observations, distinguish DNS, TCP, TLS and application time, check service incidents and reduce unnecessary parallel requests. Respect retry-after and service quotas. |

Inspect existing proxy settings for stale or invalid addresses, conflicting application/system settings and credential errors. Do not invent a universal proxy configuration: configuration keys and behavior vary by product. Use only authorized network access and preserve managed settings. Verify fixes in the original client, not just curl.

## Reference sources

The user-provided [Claude Code guide](https://ip.net.coffee/claude/claudecode.html#dns) discusses DNS, IP address families, transport, connection reuse, concurrency and latency. These are useful diagnostic dimensions, but its recommendations about risk controls are third-party claims rather than official requirements.

The [Claude IP diagnostic page](https://ip.net.coffee/claude/) displays connectivity, DNS and network attributes. It is an external service and can receive IP and device information; use only with consent. Its scores are not proof of account health. For actual eligibility and service availability, use the official sources linked in the main skill.
