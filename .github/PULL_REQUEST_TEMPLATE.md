<!-- Thank you for contributing to Ochrelle! Please fill in the sections below. -->

## Summary

<!-- One or two sentences: what does this PR change and why? -->

## Changes

<!-- Bullet list of the concrete changes (files added/edited, content reworked). -->

## Type of change

- [ ] Skill content (a directory under `skills/`)
- [ ] Documentation (`docs/` or root documents)
- [ ] Web showcase (`examples/web-showcase/`)
- [ ] Tooling / CI (`scripts/`, `tests/`, `.github/`)

## Checklist

- [ ] `python3 scripts/validate_skills.py` passes (exit code 0)
- [ ] `python3 scripts/validate_repository.py` passes (exit code 0)
- [ ] `python3 -m unittest discover -s tests -v` passes
- [ ] The skill I touched is self-contained: every relative link and
      `references/`, `scripts/`, `assets/` path mentioned resolves to a file
      inside the skill directory
- [ ] Frontmatter follows the Agent Skills spec (`name` matches the directory
      name; `description` is 1-1024 chars; optional fields valid)
- [ ] No placeholder content (TODO, FIXME, lorem ipsum, [placeholder], <insert)
- [ ] Accessibility considered: guidance integrates WCAG 2.2 AA (contrast,
      focus visibility, motion safety) where the style allows it
- [ ] Content is original (no copied theme-forest or marketplace text)
