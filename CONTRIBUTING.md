# Contributing to Ochrelle

Thank you for helping give AI a design sense. This document explains how the repository is structured, what quality bar new content must clear, and how to get a PR merged.

## Ways to contribute

- **Improve an existing skill** - sharper rules, better component recipes, more anti-patterns, stronger WCAG notes.
- **Propose a new skill** - open an issue using the *Skill proposal* template first; the style space is large but the master skill's routing table must stay coherent.
- **Improve documentation** - `docs/` pages and root documents.
- **Improve tooling** - the validators, tests, and CI (stdlib-only Python).
- **Fix the web showcase** - CSS/JS corrections in `examples/web-showcase/`.

## Skill anatomy

Every skill lives in its own directory under `skills/` and must be **self-contained**:

```text
skills/<skill-name>/
├── SKILL.md                    # required: frontmatter + workflow body
└── references/
    ├── style-guide.md          # required for the 10 specialists
    └── <anything-else>.md      # optional supporting references
```

- The directory name is the skill's identity. `SKILL.md`'s `name` field must be **identical** to the directory name.
- Skills may not reach outside their own directory. No `../` links, no absolute paths, no dependencies on other skills at load time (the master may *name* specialists in prose, but must not link into their directories).

## Frontmatter specification

`SKILL.md` must begin with YAML frontmatter between the first two `---` lines. The rules below are enforced by `scripts/validate_skills.py` and follow the [Agent Skills specification](https://agentskills.io/specification):

| Field | Required | Rules |
| --- | --- | --- |
| `name` | yes | 1–64 chars, regex `^[a-z0-9]+(-[a-z0-9]+)*$`, must equal the directory name |
| `description` | yes | 1–1024 chars, non-empty; say what the skill does **and when to use it** |
| `license` | no | string, e.g. `MIT` |
| `compatibility` | no | 1–500 chars |
| `metadata` | no | map of string → string; quote values (e.g. `version: "1.0.0"`) so YAML parsers don't coerce them |
| `allowed-tools` | no | single space-separated string of tool names |

Minimal example:

```yaml
---
name: ochrelle-minimalism
description: Subtractive, content-first UI guidance for productivity tools, docs, and enterprise dashboards. Use when the product must recede and the work must surface.
license: MIT
metadata:
  version: "1.0.0"
---
```

## Quality bar for skill content

1. **Original content.** Write in your own words. Do not copy text from theme marketplaces, UI-kit docs, or tutorials. Curated synthesis with traced sources is fine; copied prose is not.
2. **WCAG 2.2 AA integration.** Every specialist's `references/style-guide.md` must include an accessibility section covering the style's specific contrast, focus-visibility, and motion risks, with concrete mitigation (token values, not vibes). Expressive styles are contrast traps; saying "be careful" is not enough.
3. **Complete code examples.** Snippets must be runnable as-is: real values for colors, shadows, and radii; no `...` gaps, no `<!-- your content here -->`. If a value depends on context, show the decision rule instead of a gap.
4. **Actionable over descriptive.** "Use `border: 2px solid #111` on interactive elements" beats "brutalism uses strong borders."
5. **No placeholder content.** The validators flag `TODO`, `FIXME`, `lorem ipsum`, `[placeholder]`, and `<insert` anywhere in a skill. Don't ship them.
6. **Specialists need `references/style-guide.md`.** The master skill is exempt.

## Style guide for docs

- Sentence case for headings; active voice; present tense.
- Short paragraphs. Tables over prose when comparing things.
- Fence code blocks with a language tag (`css`, `js`, `yaml`, `text`).
- Use relative links for anything inside the repository. Never link `file://` or absolute filesystem paths.
- Line length is soft-capped at ~100 characters in markdown; tables may exceed it.

## Running the validators locally

Before every PR - no exceptions:

```bash
python3 scripts/validate_skills.py        # lint all skill directories
python3 scripts/validate_repository.py    # check repo structure and links
python3 -m unittest discover -s tests -v  # run the unit-test suite
```

All three must exit `0`. Both validators accept `--json`; the repository validator also accepts `--root`. If a validator reports a failure you believe is spurious, fix the validator and its tests in the same PR - never work around a validator with generated content.

## PR process

1. **Discuss first for new skills.** Open a *Skill proposal* issue so routing and naming can be agreed before you write 300 lines of style guide.
2. **One logical change per PR.** A new skill, a docs overhaul, or a tooling change - not all three.
3. **Small diffs win.** Reformatting noise hides substantive changes; don't mix them.
4. **Fill the PR checklist.** The template mirrors this document.
5. **CI must be green.** The workflow in `.github/workflows/validate.yml` runs the validators and tests on Python 3.11.
6. **Review.** At least one maintainer approval is required. Content PRs are reviewed for accuracy of the design guidance and for accessibility soundness, not just for lint-cleanliness.

## Reporting problems

- Bugs in validators, docs, or showcase: use the *Bug report* template.
- Security issues: do **not** open a public issue - see [SECURITY.md](SECURITY.md).
- Questions: see [SUPPORT.md](SUPPORT.md).

## Licensing

By contributing, you agree that your contributions are licensed under the MIT License terms of this repository (see [LICENSE](LICENSE)).
