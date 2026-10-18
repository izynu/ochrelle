# Support

## Where to get help

| Need | Where |
| --- | --- |
| Bug in a validator, doc, or the showcase | [GitHub Issues](https://github.com/izynu/ochrelle/issues) using the **Bug report** template |
| Proposal for a new style skill | [GitHub Issues](https://github.com/izynu/ochrelle/issues) using the **Skill proposal** template |
| Usage questions, "which style should I pick", discussion | [GitHub Discussions](https://github.com/izynu/ochrelle/discussions) (enable Discussions in the repository Settings first; until then, ask in Issues) |
| Security vulnerabilities | **Not here** - see [SECURITY.md](SECURITY.md) for private disclosure |

## Before asking

1. **Run the validators** - most "skill doesn't load / agent ignores it" problems are caught by them:
   ```bash
   python3 scripts/validate_skills.py
   python3 scripts/validate_repository.py
   ```
2. **Check [docs/troubleshooting.md](docs/troubleshooting.md)** for the common failure modes (skill not appearing, partial directory copy, frontmatter parse errors).
3. **Search existing issues** - your problem may already be reported.

## What to include

For the fastest useful answer, include:

- What you were trying to do (the prompt and the skill involved).
- Your agent platform and how the skill was installed (e.g. copied to `~/.claude/skills/ochrelle-minimalism`).
- Full output of the relevant validator run (paste as text).
- For content questions: the exact section of `SKILL.md` or `references/style-guide.md` you followed.

## Response expectations

- This is a volunteer-maintained open-source project; support is **best effort** with no SLA.
- Bugs affecting the validators or CI are prioritized; content guidance questions are answered when maintainers have design-context bandwidth.
- If a question reveals a documentation gap, the best outcome is often a PR - see [CONTRIBUTING.md](CONTRIBUTING.md).
