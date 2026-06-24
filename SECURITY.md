# Security Policy

## Supported Versions

Security fixes are applied on the `main` branch. Install or sync skills from the latest `main` release when possible.

## Reporting A Vulnerability

Please do **not** open a public GitHub issue for security vulnerabilities.

Email **yugasun.ai@gmail.com** with:

- A description of the issue
- Steps to reproduce
- Impact assessment, if known
- Suggested fix, if you have one

You should receive a response within a few business days. We will coordinate disclosure and credit contributors when appropriate.

## Scope

This policy covers:

- Scripts under `skills/*/scripts/`
- Repository automation under `.github/`
- Documentation that could lead to unsafe defaults (for example, hardcoded secrets or unsafe command examples)

It does not cover third-party services used by individual skills (AWS, Aliyun, Tavily, and so on). Report those issues to the respective providers.
