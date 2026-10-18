# AGENTS.md - guidance for AI agents working in this repository

This file is for AI agents (Claude Code, Codex, autonomous pipelines, etc.)
that are modifying the Ochrelle repository itself. It tells you how the repo is
organized, which commands prove your work is correct, and which rules the
validators will enforce. Read it before writing anything.

## Repository map

| Path | Owned by | Purpose |
| --- | --- | --- |
| `skills/<skill-name>/` | skill workstream | 28 Agent Skills (1 master + 27 specialists) across the material-styles, typographic-expressive, period-aesthetics, thematic-genres, layout-spatial, and platform-materials families |
| `examples/web-showcase/` | showcase workstream | static side-by-side demo (`index.html`, `styles.css`, `script.js`) |
| `docs/` | docs workstream | 7 core pages (architecture, installation, style-comparison, research-methodology, source-catalog, examples, troubleshooting) |
| `scripts/` | tooling | stdlib-only Python validators |
| `tests/` | tooling | unittest suite + validator fixtures |
| `.github/` | tooling | CI workflow, PR/issue templates |
| root docs | tooling | README, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, CHANGELOG, CITATION.cff, AGENTS.md |

## Validation commands (run all three before you finish)

```bash
python3 scripts/validate_skills.py        # lint every skill directory
python3 scripts/validate_repository.py    # structure, links, empty files
python3 -m unittest discover -s tests -v  # unit tests (incl. negative tests)
```

All three must exit `0`. CI (`.github/workflows/validate.yml`) runs exactly
these on Python 3.11.

## Frontmatter spec for SKILL.md (enforced)

- Frontmatter sits between the first two `---` lines of `SKILL.md`.
- `name`: 1–64 chars, regex `^[a-z0-9]+(-[a-z0-9]+)*$`, and **must equal the
  parent directory name**.
- `description`: 1–1024 chars, non-empty; state what the skill does and when
  to use it.
- Optional: `license` (string), `compatibility` (1–500 chars), `metadata`
  (string → string map - quote values like `version: "1.0.0"`), `allowed-tools`
  (space-separated string).

## Content rules

1. **No placeholder content.** The strings `TODO`, `FIXME`, `lorem ipsum`,
   `[placeholder]`, and `<insert` are flagged anywhere in a skill's text
   files. Write real content or leave the section out.
2. **Self-containment.** Every relative path a skill mentions
   (`references/...`, `scripts/...`, `assets/...`) and every local markdown
   link (in `SKILL.md` *and* in the skill's other markdown files) must resolve
   to a file inside the skill. No `../` escapes, no absolute paths, no
   `file://` links. External `https://` links are fine.
3. **Specialist skills** (everything except `ochrelle-design-master`) must ship
   `references/style-guide.md`.
4. **Original content.** No copied marketplace/theme text. Curated synthesis
   with traced sources is the expected register.
5. **Accessibility.** Weave WCAG 2.2 AA into style guidance with concrete
   token values (contrast ratios, focus styles, `prefers-reduced-motion`),
   especially for the contrast-trap styles (neumorphism, glassmorphism,
   liquid glass).
6. **Complete examples.** Code snippets must be runnable as written - real
   values, no `...` gaps.
7. **Docs style.** Sentence-case headings, active voice, fenced code blocks
   with language tags, relative links inside the repo.

## Do-nots

- **Do not add dependencies to the validators.** `scripts/*.py` are
  stdlib-only by policy (PyYAML is used opportunistically if present, but must
  never be required). A new import is a supply-chain regression.
- **Do not break skill self-containment** by linking across skill directories
  or into repository-level files from a skill.
- **Do not rename a skill directory** without checking every reference to it:
  `scripts/validate_repository.py` and `tests/` pin the 28 expected names.
- **Do not commit empty (0-byte) files** anywhere in the repo - a validator
  check flags them.
- **Do not move or rename the root documents or `docs/` pages** - the README
  links to them and `validate_repository.py` verifies those links.
- **Do not modify `tests/fixtures/` to make failing tests pass.** The broken
  fixture is broken on purpose; fix the content or the validator, not the test.
- **Do not weaken the placeholder scan or the reference resolution** to make
  your content pass. Change the content.
- **Do not leave `[OWNER: ...]` placeholders in skills/** - they are allowed
  only in root docs and CI configuration until publish time.

## Definition of done

Your change is done when: the three validation commands exit `0`, your
content contains no placeholder markers, every file you reference exists, and
any behavioral change to the validators is covered by a test in `tests/`.
