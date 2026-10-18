# Security Policy

## Supported versions

| Version | Supported |
| --- | --- |
| 2.0.x | yes |
| < 2.0 | no |

## What this repository is (scope setting)

Ochrelle is a documentation-and-tooling repository: markdown skills, a static HTML/CSS/JS showcase, and two Python validators. There is no server, no runtime that executes downloaded content, and no package you are expected to install. That shapes the realistic threat model:

**In scope**

- **CI supply-chain risks**: tampering with `.github/workflows/validate.yml`, script injection through untrusted input in the validators, or unsafe `pull_request_target`-style patterns. Workflow changes are reviewed like code and run with the default (least) GitHub Actions permissions.
- **Validator integrity**: `scripts/*.py` are stdlib-only by policy. Introduction of a third-party runtime dependency into the validators is a supply-chain regression and will be treated as a security-relevant change.
- **The showcase**: `examples/web-showcase/` is plain static files with no build step. Reports of XSS-viable patterns there (e.g. injecting remote scripts) are accepted.
- **Content integrity**: systematic injection of malicious instructions into skill markdown (prompt-injection payloads aimed at agents that load these skills).

**Out of scope**

- Design opinions in the skill content.
- Vulnerabilities in third-party agent platforms (report those to the platform vendor).

## Reporting a vulnerability

Please report privately - **do not open a public GitHub issue** for anything security-related.

1. Use GitHub's *Report a vulnerability* (private security advisory) feature on this repository: [github.com/izynu/ochrelle/security/advisories/new](https://github.com/izynu/ochrelle/security/advisories/new). This reaches the maintainer (Zynu) privately and never publishes your report.
2. Include: affected files or workflows, a minimal reproduction, your assessment of impact, and any suggested fix.
3. You will get an acknowledgement. If you receive no reply within the target window below, assume the contact is stale and open a plain issue asking (without details) for the current security contact.

## Response targets (soft commitments)

These are best-effort targets for a volunteer-maintained project, not an SLA:

- **Acknowledgement**: within 5 business days of receipt.
- **Triage & severity assignment**: within 10 business days.
- **Fix or mitigation**: within 30 days for high-severity findings; best effort otherwise.
- **Public disclosure**: coordinated with the reporter after a fix ships; credit given unless the reporter prefers anonymity.

## Safe-harbor note

We consider good-faith research and reporting of the issues above to be legitimate and welcome; we will not pursue action against reporters who follow this policy.
