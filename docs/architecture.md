# Ochrelle Architecture

How the Ochrelle repository is organized, why it is organized that way, and how
to extend it.

---

## 1. Repository layout

```
ochrelle/
├── README.md                      # Project overview, skill table, quickstart
├── CONTRIBUTING.md                # How to contribute skills and fixes
├── LICENSE                        # MIT
├── docs/                          # Human documentation (this folder)
│   ├── architecture.md            # ← you are here
│   ├── installation.md            # Installing skills into agent environments
│   ├── style-comparison.md        # All 10 skills side by side
│   ├── research-methodology.md    # How research was done and how to refresh it
│   ├── source-catalog.md          # Real, cataloged sources
│   ├── examples.md                # Guide to examples/web-showcase
│   └── troubleshooting.md         # Common problems and fixes
├── skills/                        # Distribution source - one directory per skill
│   ├── ochrelle-design-master/     # Master skill: routing, art direction, QA
│   │   ├── SKILL.md
│   │   └── references/…
│   ├── ochrelle-skeuomorphism/     # Visual style
│   ├── ochrelle-neumorphism/       # Visual style
│   ├── ochrelle-glassmorphism/     # Visual style
│   ├── ochrelle-claymorphism/      # Visual style
│   ├── ochrelle-brutalism/         # Visual style
│   ├── ochrelle-minimalism/        # Visual style
│   ├── ochrelle-maximalism/        # Visual style
│   ├── ochrelle-liquid-glass/      # Platform material
│   ├── ochrelle-bento-grid/        # Layout pattern
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── style-guide.md
│   │       ├── implementation-examples.md
│   │       └── quality-checklist.md
│   └── ochrelle-spatial-ui/        # Interaction paradigm
│       ├── SKILL.md
│       └── references/ (same three-file pattern)
├── examples/
│   └── web-showcase/              # Static, dependency-free demo of all 10
├── scripts/
│   ├── validate_skills.py         # Frontmatter, names, descriptions, references
│   └── validate_repository.py     # Docs, structure, internal consistency
├── tests/
│   ├── test_skill_metadata.py
│   ├── test_repository_structure.py
│   └── fixtures/
└── .github/
    └── workflows/validate.yml     # CI: runs validators and tests
```

## 2. Design decisions

### 2.1 Skills are self-contained

Every skill directory carries everything an agent needs to apply it: the
SKILL.md entry point plus bundled references under `references/`. A skill must
work when copied out of this repository **alone**, without the master skill or
its siblings. Consequences:

- No skill references another skill's files by path. Cross-skill pointers are
  prose ("see the Ochrelle glassmorphism skill"), never relative links that
  would break after a solo install.
- Each specialist repeats the accessibility, performance, and honesty rules
  relevant to it instead of delegating to a shared document - because a solo
  install has no shared document.

### 2.2 Progressive disclosure

SKILL.md files are deliberately compact (Ochrelle target: roughly 150–300
lines). They carry the mental model, decision rules, failure modes, and
pointers; the heavy material (full CSS systems, complete examples, long
checklists) lives in `references/` files that an agent reads on demand when
the task calls for that depth. This keeps the always-loaded context small and
the deep context accurate.

### 2.3 Distribution model: copy the directory

A skill is just a directory of Markdown files with YAML frontmatter. There is
no build step, no registry requirement, and no runtime: **installing a skill
means copying its directory into a location the target agent scans.** This
makes the whole library trivially forkable, vendorable into an existing repo,
and auditable - the agent only ever reads text that the user can also read.

### 2.4 The three-layer separation (styles / layouts / paradigms)

The ten skills are not interchangeable "styles". The repository enforces the
distinction:

- **Visual styles** (skeuomorphism, neumorphism, glassmorphism, claymorphism,
  brutalism, minimalism, maximalism) answer: *what do surfaces look like?*
- **Layout pattern** (bento grid) answers: *how is content organized and
  sized?*
- **Interaction paradigm** (spatial UI) answers: *how do content, space, and
  input relate?*
- **Platform material** (liquid glass) answers: *what does the platform itself
  provide, and what can only be approximated elsewhere?*

The master skill routes by intent and composes across layers (a minimalist
bento dashboard; glass tiles on a spatial surface) while keeping each skill's
rules intact. This is why bento guidance talks about "skins" and spatial
guidance talks about environments - composition is expected, conflation is not.

### 2.5 Honesty as an architectural constraint

Skills label verified knowledge versus contextual recommendations, never
invent platform APIs, and ship checklists that distinguish "tested" from
"untested". This is a design decision, not a tone choice: an agent following
Ochrelle should never be the source of fabricated claims in the code it writes.

## 3. How the master skill routes to specialists

`ochrelle-design-master` acts as the design director:

1. **Understand the task** - product, audience, surface, constraints; inspect
   the existing codebase and respect its design system unless change is
   requested.
2. **Classify the intent** against the three layers:
   - "what should it look like?" → a visual style skill;
   - "how should content be organized?" → bento grid;
   - "should this feel dimensional/spatial?" → spatial UI (after naming the
     environment);
   - "should we use the platform's own material language?" → liquid glass.
3. **Select one primary skill** plus at most one or two supporting ones.
   Mixed selections are legitimate (e.g., `ochrelle-minimalism` +
   `ochrelle-bento-grid` for an analytics dashboard) - conflicting ones are
   not, and the master resolves conflicts by task priority, not aesthetics.
4. **Delegate** to the specialist's SKILL.md, loading its references only as
   needed (progressive disclosure again).
5. **Supervise** delivery using the specialist's quality checklist and the
   master's review pass; report what was verified and what was not.

The master carries no style rules of its own beyond routing, composition, and
review discipline - so specialists can evolve without touching it.

## 4. Versioning

- Versioning is **per skill**, declared in each SKILL.md frontmatter:
  `metadata.version` (semver, quoted string, e.g. `"1.0.0"`).
- **Patch** (x.y.Z): corrections that do not change guidance - typos, broken
  links, clarifications.
- **Minor** (x.Y.z): new guidance, new examples, new checklist items; existing
  guidance remains compatible.
- **Major** (X.y.z): guidance changes that invalidate previous practice (e.g.,
  a replaced grid strategy), or a restructure of the reference set.
- The repository itself is not versioned separately: `git` history plus each
  skill's version covers provenance. When the Agent Skills specification
  changes in a way skills must adopt, bump the affected skills and note it in
  CHANGELOG.md.
- Because distribution is copy-the-directory, a copied skill carries its
  version with it - users can always ask an agent to read the frontmatter to
  identify what is installed.

## 5. How to add a new skill (step by step)

1. **Research first.** Consult primary sources (platform docs, standards,
   MDN) and record them in `docs/source-catalog.md` with real URLs and what
   you actually verified. See `docs/research-methodology.md`.
2. **Classify the candidate.** Is it a visual style, a layout pattern, an
   interaction paradigm, or a platform material? If it duplicates an existing
   skill, contribute there instead.
3. **Create the directory** `skills/ochrelle-<name>/` - the directory name must
   exactly match the `name` field you will put in the frontmatter.
4. **Write SKILL.md** with valid frontmatter:
   - `name`: identical to the directory name;
   - `description`: third person, what the skill does and when to use it,
     including trigger keywords, within the specification's length limit;
   - `license: MIT`; `metadata` with `author: ochrelle`, `version`, and the
     appropriate `family`.
   Body target 150–300 lines: definition, when/when-not, core rules, failure
   modes, workflow, and relative pointers to references.
5. **Add references/** (`style-guide.md`, `implementation-examples.md`,
   `quality-checklist.md` at minimum for design skills). All bundled links
   must be relative and must resolve.
6. **Make it independent**: no relative links into other skills; repeat any
   shared rules the skill needs.
7. **Validate**: run `python3 scripts/validate_skills.py` and fix every
   failure (see `docs/troubleshooting.md` for common validator errors).
8. **Demonstrate**: for a visual skill, add or update a demonstration in
   `examples/web-showcase/` and describe it in `docs/examples.md`.
9. **Cross-document**: add the skill to the comparison table in
   `docs/style-comparison.md` and to the README skill table.
10. **Open a PR** with the checklist output, research notes, and honest
    verification notes (what was tested, on what).

---

*Every file in this repository must justify its existence: no placeholder
documents, no generic filler, no invented citations or capabilities.*
