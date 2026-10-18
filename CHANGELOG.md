# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- _Nothing yet._

## [2.0.0] - 2026-10-18

### Breaking

- Renamed the project twice before its first release, both times for brand
  uniqueness: AesthOS to StyleSmith (exact name collision), then StyleSmith
  to Ochrelle (common-word compounds collide with many unrelated companies;
  "ochrelle", coined from the pigment ochre, had zero web and npm matches
  and no `ochrelle.dev` DNS record at adoption). The skill prefix is now
  `ochrelle-`, and the repository folder and site were renamed to match.
  Update any external references to either old name or prefix.

### Added

- **Skills (17 new, 28 total):** `ochrelle-flat-design`,
  `ochrelle-material-design`, `ochrelle-neo-brutalism`, `ochrelle-y2k`,
  `ochrelle-cyberpunk`, `ochrelle-retro-design`,
  `ochrelle-editorial-design`, `ochrelle-memphis-design`,
  `ochrelle-japandi`, `ochrelle-frutiger-aero`,
  `ochrelle-corporate-memphis`, `ochrelle-vaporwave`,
  `ochrelle-pixel-art`, `ochrelle-terminal-console`,
  `ochrelle-hand-drawn`, `ochrelle-art-deco`, and
  `ochrelle-futuristic-hud` - each a self-contained Agent Skill with
  `SKILL.md` and `references/` (style guide, implementation examples, quality
  checklist), grouped into the material-styles, typographic-expressive,
  period-aesthetics, and thematic-genres families.
- **Installer:** `scripts/install.sh`, a universal installer with Claude Code
  mode (`--claude`), single-skill mode (`--only`), project mode, and explicit
  destination mode, plus a cross-agent compatibility matrix in
  `docs/installation.md`.

### Changed

- All skill versions bumped to 2.0.0.
- Master routing tables (category distinctions, per-style choose/avoid tables,
  combination rules) and `docs/style-comparison.md` extended from ten to 27
  specialists.

## [1.0.0] - 2026-10-18

### Added

- **Skills (11):** the master skill `ochrelle-design-master` plus ten specialist
  skills - `ochrelle-skeuomorphism`, `ochrelle-neumorphism`,
  `ochrelle-glassmorphism`, `ochrelle-claymorphism`, `ochrelle-brutalism`,
  `ochrelle-minimalism`, `ochrelle-maximalism`, `ochrelle-liquid-glass`,
  `ochrelle-bento-grid`, `ochrelle-spatial-ui` - each a self-contained Agent
  Skill with `SKILL.md` and `references/` (style guide, tokens, anti-patterns,
  WCAG 2.2 AA notes).
- **Documentation:** `docs/architecture.md`, `docs/installation.md`,
  `docs/style-comparison.md`, `docs/research-methodology.md`,
  `docs/source-catalog.md`, `docs/examples.md`, `docs/troubleshooting.md`, and
  the root documents (README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY,
  SUPPORT, CHANGELOG, CITATION.cff, AGENTS.md, LICENSE).
- **Web showcase:** `examples/web-showcase/` - a static, dependency-free page
  rendering one component in all ten specialist styles side by side.
- **Validators:** `scripts/validate_skills.py` (frontmatter, references,
  placeholders, specialist style-guide requirement; stdlib-only) and
  `scripts/validate_repository.py` (structure, links, empty files), both with
  `--json` output.
- **Tests:** `tests/test_skill_metadata.py` and
  `tests/test_repository_structure.py` (unittest, including negative tests
  against `tests/fixtures/`).
- **CI:** `.github/workflows/validate.yml` running both validators and the
  test suite on Python 3.11 for pushes and PRs to `main`.
- **Community templates:** pull-request template and issue templates
  (`bug_report.md`, `skill_proposal.md`).

[Unreleased]: https://github.com/izynu/ochrelle/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/izynu/ochrelle/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/izynu/ochrelle/releases/tag/v1.0.0
