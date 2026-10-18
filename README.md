<div align="center">

<img src="docs/assets/banner.svg" alt="Ochrelle - 28 Agent Skills for interface art direction. A row of earth-pigment chips beneath the Ochrelle wordmark." width="100%"/>

# Ochrelle

### The Design Intelligence Layer for AI Agents

**Give AI a design sense.**

[![License](https://img.shields.io/badge/License-MIT-C2410C?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.0.0-1C1917?style=flat-square)](CHANGELOG.md)
[![Format](https://img.shields.io/badge/Format-Agent_Skills-C2410C?style=flat-square)](https://agentskills.io/specification)
[![Skills](https://img.shields.io/badge/Skills-28-1C1917?style=flat-square)](#the-28-skills)
[![Unit tests](https://img.shields.io/badge/Unit_tests-29_passing-C2410C?style=flat-square)](#verification)

[![Validate skills](https://github.com/izynu/ochrelle/actions/workflows/validate.yml/badge.svg)](https://github.com/izynu/ochrelle/actions/workflows/validate.yml)
[![Deploy website](https://github.com/izynu/ochrelle/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/izynu/ochrelle/actions/workflows/deploy-pages.yml)

[Install](#quickstart) · [Skill catalog](#the-28-skills) · [How it works](#how-the-pieces-work-together) · [Verification](#verification) · [Showcase](#run-the-showcase) · [Docs](#documentation) · [Maintainers](#maintainers)

</div>

---

Ochrelle is an open-source ecosystem of [Agent Skills](https://agentskills.io/specification) for design intelligence: one master skill that reasons about *which* visual style a product needs, and 27 specialist skills that execute a *specific* style with production-quality guidance.

**The name is coined, not borrowed.** Ochrelle derives from ochre, the earth pigment people have used to make surfaces meaningful for tens of thousands of years, with a made-up suffix chosen so the whole word is unique: at naming time it had zero exact matches on the web and npm. The repository itself is plain markdown, CSS, and Python that you can read, copy, and audit in an afternoon; the closest thing to an installer is a small copy script (`scripts/install.sh`).

| | |
| --- | --- |
| **License** | MIT (see [LICENSE](LICENSE)) |
| **Format** | [Agent Skills](https://agentskills.io/specification): a `SKILL.md` with YAML frontmatter plus supporting `references/` files per skill |
| **Status** | `2.0.0` (see [CHANGELOG.md](CHANGELOG.md)) |

## Why

Ask an AI coding agent to "make it look good" and you will usually get the same interface back: a centered card, a soft gradient, `border-radius: 12px`, Inter, and a shadow somewhere between Tailwind's `shadow-md` and `shadow-lg`. The result is technically correct and aesthetically generic, because three ingredients are missing:

1. **Art-direction reasoning.** Models know what glassmorphism *is*, but they are rarely asked to weigh it against neumorphism or brutalism for the product at hand, then commit to one coherent direction.
2. **Per-style craft knowledge.** Each style has non-obvious rules: neumorphism demands monochrome low-contrast surfaces and dies on busy backgrounds; brutalism is deliberately "ugly" in structured ways; claymorphism needs three stacked shadows to read as soft 3D. Generic training data averages these away.
3. **Accessibility guardrails.** Many expressive styles are contrast traps. Guidance must be written so that an agent can ship a bold interface without failing WCAG 2.2 AA.

Ochrelle packages these ingredients as skills an agent can load on demand. The agent keeps its own coding ability; Ochrelle supplies the taste, the rules, and the checklists.

## Quickstart

The public, documented install path is **Claude Code**, which loads Agent Skills from a skills directory.

```bash
# 1. Get the skills
git clone https://github.com/izynu/ochrelle.git
cd ochrelle

# 2. Copy whole skill directories into your Claude Code skills folder
mkdir -p ~/.claude/skills
cp -r skills/ochrelle-design-master ~/.claude/skills/
cp -r skills/ochrelle-minimalism   ~/.claude/skills/

# 3. Start a new Claude Code session and ask for design work
```

**Installing on any agent:** the repository ships `scripts/install.sh`, a dependency-free installer that covers the two common cases. `./scripts/install.sh --claude` copies all 28 skills into `~/.claude/skills`, and `./scripts/install.sh <destination>` copies them into any folder, such as a project's `skills/` directory. Add `--only <skill-name>` to install a single skill (for example `./scripts/install.sh --claude --only ochrelle-minimalism`). The script only writes to the destination; the full compatibility matrix for Claude, Cursor, Codex, Gemini CLI, Aider, and other agents lives in [docs/installation.md](docs/installation.md).

Notes:

- **Copy whole directories.** Each skill is self-contained by design; partial copies break the relative references inside `SKILL.md`.
- **Start with the master** if you don't know which style you want; load a specialist directly if you do.
- **Other agent platforms:** most tools that read the Agent Skills format can point at a skill directory. Platform-specific notes and troubleshooting live in [docs/installation.md](docs/installation.md).

## The 28 skills

### The master skill

[`ochrelle-design-master`](skills/ochrelle-design-master/SKILL.md) is the orchestrator. It interviews the product context (audience, platform, brand temperature, content density), compares candidate styles, and picks one, or a primary with an accent. It then delegates to the matching specialist. Use it whenever the style is *not* already decided.

### The 27 specialists

| Skill | Type | Best for |
| --- | --- | --- |
| [`ochrelle-skeuomorphism`](skills/ochrelle-skeuomorphism/SKILL.md) | Specialist | Real-world metaphors: calculators, note apps, tape decks, vintage controls, tactile familiarity |
| [`ochrelle-neumorphism`](skills/ochrelle-neumorphism/SKILL.md) | Specialist | Soft-UI panels on monochrome surfaces: music players, smart-home controls, device dashboards |
| [`ochrelle-glassmorphism`](skills/ochrelle-glassmorphism/SKILL.md) | Specialist | Frosted translucent layers over vivid media: overlays, players, widgets, OS-like panels |
| [`ochrelle-claymorphism`](skills/ochrelle-claymorphism/SKILL.md) | Specialist | Playful, friendly products: kids' apps, onboarding flows, brand moments with chunky soft 3D |
| [`ochrelle-brutalism`](skills/ochrelle-brutalism/SKILL.md) | Specialist | Statement sites, portfolios, counter-design, raw typographic honesty |
| [`ochrelle-minimalism`](skills/ochrelle-minimalism/SKILL.md) | Specialist | Productivity tools, docs, enterprise dashboards, content-first reading experiences |
| [`ochrelle-maximalism`](skills/ochrelle-maximalism/SKILL.md) | Specialist | Editorial, culture, fashion, and campaign pages that celebrate abundance |
| [`ochrelle-liquid-glass`](skills/ochrelle-liquid-glass/SKILL.md) | Specialist | Modern OS-level translucency: adaptive, dynamic material layers à la visionOS/iOS |
| [`ochrelle-bento-grid`](skills/ochrelle-bento-grid/SKILL.md) | Specialist | Modular card compositions: landing pages, feature summaries, information-dense dashboards |
| [`ochrelle-spatial-ui`](skills/ochrelle-spatial-ui/SKILL.md) | Specialist | Depth-driven and 3D interfaces: AR/VR, visionOS-style windows, parallax scenes |
| [`ochrelle-flat-design`](skills/ochrelle-flat-design/SKILL.md) | Specialist | Solid-color, no-shadow production skins: SaaS dashboards, admin panels, settings screens, docs |
| [`ochrelle-material-design`](skills/ochrelle-material-design/SKILL.md) | Specialist | Android and Google-ecosystem products: elevation levels, ripples, Material You dynamic color |
| [`ochrelle-neo-brutalism`](skills/ochrelle-neo-brutalism/SKILL.md) | Specialist | Loud indie brands: thick black borders, hard offset shadows, sticker badges for merch, events, and creator tools |
| [`ochrelle-y2k`](skills/ochrelle-y2k/SKILL.md) | Specialist | Dot-com futurism: candy plastics, chrome gradients, and gel buttons for rave, fashion, and revival campaigns |
| [`ochrelle-cyberpunk`](skills/ochrelle-cyberpunk/SKILL.md) | Specialist | Neon-noir atmosphere: games, club nights, security and developer brands, dark portfolios |
| [`ochrelle-retro-design`](skills/ochrelle-retro-design/SKILL.md) | Specialist | Mid-century Americana: cafes, diners, breweries, vinyl stores, food packaging, event posters |
| [`ochrelle-editorial-design`](skills/ochrelle-editorial-design/SKILL.md) | Specialist | Magazine craft on the web: blogs, digital magazines, essays, press pages, story-driven marketing |
| [`ochrelle-memphis-design`](skills/ochrelle-memphis-design/SKILL.md) | Specialist | Postmodern play: squiggles, terrazzo, and clashing pastels for youth, music, and party brands |
| [`ochrelle-japandi`](skills/ochrelle-japandi/SKILL.md) | Specialist | Quiet warmth: wellness and mindfulness apps, boutique hospitality, calm productivity, skincare and tea brands |
| [`ochrelle-frutiger-aero`](skills/ochrelle-frutiger-aero/SKILL.md) | Specialist | 2004-2013 glossy optimism: aqua gel, glass shine, and nature-tech for throwback marketing and kiosks |
| [`ochrelle-corporate-memphis`](skills/ochrelle-corporate-memphis/SKILL.md) | Specialist | Flat vector illustration systems: onboarding, HR tools, empty states, community pages, friendly SaaS heroes |
| [`ochrelle-vaporwave`](skills/ochrelle-vaporwave/SKILL.md) | Specialist | 80s/90s consumer-tech nostalgia: Roman busts, VHS glitch, and sunset gradients for music releases and streetwear |
| [`ochrelle-pixel-art`](skills/ochrelle-pixel-art/SKILL.md) | Specialist | 8-bit/16-bit sprite discipline: games, launchers, emulation frontends, retro-gaming brands, achievement systems |
| [`ochrelle-terminal-console`](skills/ochrelle-terminal-console/SKILL.md) | Specialist | Text-mode UI: monospace grids, box-drawing frames, phosphor palettes for developer tools, log viewers, and status pages |
| [`ochrelle-hand-drawn`](skills/ochrelle-hand-drawn/SKILL.md) | Specialist | Sketchbook warmth: education platforms, kids' tools, creative apps, onboarding and how-to guides |
| [`ochrelle-art-deco`](skills/ochrelle-art-deco/SKILL.md) | Specialist | Geometric luxury: boutique hotels, cocktail bars, theaters, jewelry and spirits brands, gala invitations |
| [`ochrelle-futuristic-hud`](skills/ochrelle-futuristic-hud/SKILL.md) | Specialist | Sci-fi instrument panels: robotics and drone telemetry, launch events, mission-control-style pages |

Every skill directory is self-contained: a `SKILL.md` (frontmatter + workflow) and at least a `references/style-guide.md` with concrete tokens, component recipes, anti-patterns, and WCAG 2.2 AA notes.

## How the pieces work together

A typical agent session flows through three hops:

1. **Load.** The agent (e.g. Claude Code) discovers the skills you copied into its skills directory and reads each `SKILL.md`'s frontmatter: the `description` tells it *when* the skill is relevant, without burning context on the full body.
2. **Route.** With `ochrelle-design-master` loaded, the agent interviews your product context (audience, platform, brand temperature, content density), scores the candidate styles, and commits to a direction, or you skip this step by loading a specialist directly.
3. **Go deep.** The chosen skill's `references/` files are read on demand: the style guide for tokens and rules, implementation examples for complete code, the quality checklist for a final pass. This progressive-disclosure pattern keeps the expensive content out of context until it is actually needed.

Because every skill is plain markdown, the same files work as reading material for humans. Reviewing a skill in a PR is exactly like reviewing any other doc.

## Anatomy of a skill

```text
ochrelle-glassmorphism/
├── SKILL.md
│     ---
│     name: ochrelle-glassmorphism          # must equal the directory name
│     description: Frosted translucent ... # what + when, 1-1024 chars
│     license: MIT
│     metadata:
│       version: "2.0.0"
│     ---
│
│     # Glassmorphism
│     (when to use, the workflow, pointers into references/)
└── references/
    ├── style-guide.md          # required for specialists: tokens, rules,
    │                           # component recipes, WCAG 2.2 AA notes
    ├── implementation-examples.md
    └── quality-checklist.md
```

The frontmatter follows the [Agent Skills specification](https://agentskills.io/specification): `name` (1-64 chars, `^[a-z0-9]+(-[a-z0-9]+)*$`, identical to the directory name), `description` (1-1024 chars), plus optional `license`, `compatibility`, `metadata`, and `allowed-tools`. Everything else (reference resolution, placeholder scanning, the specialist style-guide requirement) is enforced by the bundled validators, so drift gets caught in CI instead of in front of your users.

## Style comparison at a glance

A summary matrix of the ten original specialist styles; the full dimension-by-dimension comparison across all 27 specialists lives in [docs/style-comparison.md](docs/style-comparison.md).

| Style | Signature cue | Surface and depth | Contrast risk | Reach for it when |
| --- | --- | --- | --- | --- |
| Skeuomorphism | Physical metaphor | Textured, beveled, "real" materials | Low (high fidelity aids recognition) | The UI should feel like a familiar object |
| Neumorphism | Dual light/dark shadow | Monochrome, extruded/pressed | **High** (low-contrast edges) | Monochrome control panels, calm hardware UIs |
| Glassmorphism | Frosted blur | Translucent layers over vivid backgrounds | Medium (depends on backdrop) | Media-forward overlays and widgets |
| Claymorphism | Puffy 3D softness | Chunky radius, stacked soft shadows | Low to medium | Playful, friendly, youth-oriented products |
| Brutalism | Raw HTML honesty | Hard borders, default-ish typography | Low (usually extreme contrast) | Statement design, portfolios, subcultures |
| Minimalism | Subtraction | Flat or near-flat, whitespace-led | Low | Productivity, reading, enterprise tools |
| Maximalism | Controlled overload | Layered pattern, rich color, big type | Medium | Editorial, culture, fashion, campaigns |
| Liquid Glass | Refractive adaptive material | Dynamic translucent "glass" that reacts to content | Medium to high | Modern OS-like surfaces, dynamic content over media |
| Bento Grid | Modular tiling | Card grid, mixed spans, rounded corners | Low | Feature summaries, dashboards, landing pages |
| Spatial UI | Depth and perspective | Layered z-space, eye/hand affordances | Medium | AR/VR, 3D scenes, immersive product demos |

## Choosing a style quickly

If you want a one-line decision procedure before reading any comparison:

- **The product must feel like a physical object?** → `ochrelle-skeuomorphism`
- **A calm, tactile control surface on one monochrome background?** → `ochrelle-neumorphism`
- **Vivid media behind frosted panels?** → `ochrelle-glassmorphism` (or `ochrelle-liquid-glass` for a modern, adaptive OS feel)
- **Friendly, playful, chunky?** → `ochrelle-claymorphism`
- **The design itself is the statement?** → `ochrelle-brutalism` (or `ochrelle-maximalism` for rich editorial abundance)
- **The content is the interface; chrome must disappear?** → `ochrelle-minimalism`
- **Many features to summarize in tiles?** → `ochrelle-bento-grid`
- **Depth, 3D, or headset-sized canvases?** → `ochrelle-spatial-ui`

When in doubt, or between two of the above, load `ochrelle-design-master` and let it route.

## Usage examples

Example 1, you know the style:

> Load the `ochrelle-minimalism` skill and redesign this settings page. Follow its style guide and keep the result at WCAG 2.2 AA contrast.

Example 2, you don't know the style:

> I'm building a smart-home dashboard for a hardware startup. Use `ochrelle-design-master` to choose between `ochrelle-neumorphism` and `ochrelle-liquid-glass`, explain the trade-off, then apply the winning style.

Example 3, restructuring a page:

> Use the `ochrelle-bento-grid` skill to restructure this landing page into a bento composition: hero tile, three feature tiles, one stats tile. Keep copy from the current page.

Example 4, checking your own work:

> Using the `ochrelle-glassmorphism` skill's anti-patterns list, review this component and list every violation with a fix.

## Verification

The repository ships two stdlib-only validators and a unittest suite. CI runs all three on every push and pull request to `main`. Run them yourself, expect the numbers below:

```bash
# 1. Lint every skill directory (frontmatter, references, placeholders)
python3 scripts/validate_skills.py
# expect: 28/28 skill(s) passed

# 2. Check repository structure (docs, showcase, workflow, links, empty files)
python3 scripts/validate_repository.py
# expect: 9/9 check(s) passed

# 3. Run the unit tests (includes negative tests against fixtures)
python3 -m unittest discover -s tests -v
# expect: 29 tests, all passing
```

Both validators support `--json` for machine-readable output; `validate_repository.py` also accepts `--root` and `validate_skills.py` accepts `--skills-dir` for use outside a checkout.

## Run the showcase

`examples/web-showcase/` is a static, dependency-free page that renders the same card component in the ten original specialist styles side by side. It is also the source of the showcase linked from the main website.

```bash
# Option A: just open it
open examples/web-showcase/index.html        # macOS
xdg-open examples/web-showcase/index.html    # Linux

# Option B: serve it (recommended, avoids local-file quirks)
python3 -m http.server 8000 --directory examples/web-showcase
# then visit http://localhost:8000
```

The showcase is a hand-built illustration, not a generated artifact. See [Known limitations](#known-limitations).

## Repository layout

```text
ochrelle/
├── skills/                    # 28 Agent Skills: 1 master + 27 specialists
│   └── <skill-name>/
│       ├── SKILL.md           # YAML frontmatter + workflow body
│       └── references/        # 3 files per specialist (style-guide.md,
│                              # implementation-examples.md, quality-checklist.md);
│                              # the master ships 7 reference files
├── examples/
│   └── web-showcase/          # static side-by-side demo (index/styles/script)
├── website/                   # this project's website (Next.js, static export)
├── docs/                      # architecture, installation, research, assets
├── scripts/                   # stdlib-only validators + universal installer
│   ├── validate_skills.py
│   ├── validate_repository.py
│   └── install.sh
├── tests/                     # unittest suite + validator fixtures
├── DEPLOY.md                  # publish the website on GitHub Pages
└── .github/                   # CI + Pages workflows, PR & issue templates
```

## The website

The project website (the page with the skill catalog, verification commands, privacy policy, and terms) lives in [`website/`](website/README.md) and is a static Next.js export: no database, no server runtime.

`.github/workflows/deploy-pages.yml` builds and publishes it to GitHub Pages on every push to `main`, so the site is hosted for free at `https://izynu.github.io/ochrelle/` once Pages is enabled. The complete walkthrough, including serving the site from your own domain, is in [DEPLOY.md](DEPLOY.md).

## Documentation

| Document | What it covers |
| --- | --- |
| [docs/architecture.md](docs/architecture.md) | How the master/specialist split works and how skills compose |
| [docs/installation.md](docs/installation.md) | Per-platform install notes beyond the Claude Code quickstart |
| [docs/style-comparison.md](docs/style-comparison.md) | The full style comparison matrix with per-dimension detail |
| [docs/research-methodology.md](docs/research-methodology.md) | How the style guidance was researched and curated |
| [docs/source-catalog.md](docs/source-catalog.md) | The source catalog behind the methodology |
| [docs/examples.md](docs/examples.md) | Worked prompt/response examples for every skill |
| [docs/troubleshooting.md](docs/troubleshooting.md) | Common failure modes and fixes |

## Contributing

Contributions are welcome: new style guidance, sharper anti-patterns, better accessibility notes, fixed references. Start with [CONTRIBUTING.md](CONTRIBUTING.md), which covers the frontmatter spec, the quality bar (original content, WCAG 2.2 AA integration, complete code examples), and the PR checklist. If you are an AI agent working in this repository, read [AGENTS.md](AGENTS.md) first: it contains the rules your changes must satisfy, and the validators will enforce them.

Run the validators before opening a PR: the CI workflow (`.github/workflows/validate.yml`) runs exactly these commands, and a red build is an annoying way to learn about a broken reference.

## Security and support

- Vulnerabilities: follow the private disclosure process in [SECURITY.md](SECURITY.md).
- Questions and bug reports: see [SUPPORT.md](SUPPORT.md).

## FAQ

**Do skills execute anything?** No. Skills are markdown documents (plus reference files). The agent reads them; nothing is installed, compiled, or run. The only executable code in this repository is the stdlib-only Python validator in `scripts/` and the `scripts/install.sh` copy script, and neither runs unless you (or CI) invoke them.

**Can I use this outside Claude Code?** Any agent that can read files and follows the Agent Skills format can use these skills. The mechanics differ per platform; see [docs/installation.md](docs/installation.md).

**Can I use Ochrelle commercially?** Yes, MIT. See [LICENSE](LICENSE).

**Can I edit a skill for my own team?** Yes. Fork the directory, tweak the tokens and rules to your brand, and keep the directory self-contained so the validators still pass. If your improvement is generic, upstream it via [CONTRIBUTING.md](CONTRIBUTING.md).

**Why markdown instead of a database or API?** Skills must travel with the agent, be reviewable in PRs, and work offline. Markdown with a strict frontmatter header is the lowest-common-denominator that satisfies all three, and it is exactly what the Agent Skills ecosystem expects.

**How do I add a twenty-ninth style?** Open a *Skill proposal* issue first (naming and routing need to fit the master skill), then follow [CONTRIBUTING.md](CONTRIBUTING.md). The validators and tests will walk you through everything else.

## Known limitations

Being honest up front, because design advice given with false confidence is worse than none:

- **The web showcase is an approximation.** It is a hand-written static page meant to communicate the *gestalt* of each style. It is not rendered by agents, not pixel-exhaustive, and not a conformance suite.
- **Agent environments are not exhaustively verified.** The skills follow the public Agent Skills specification and are documented against Claude Code's skill loading; behavior in other agent runtimes (context limits, tool filtering, frontmatter quirks) may vary and has not been systematically tested.
- **Style guidance is editorial, not empirical.** The style guides are curated, opinionated synthesis from public design writing and practice, traceable via [docs/research-methodology.md](docs/research-methodology.md), not peer-reviewed research. Treat them as strong defaults, not laws.
- **WCAG integration is guidance, not an audit.** Skills flag the common contrast/focus/motion traps per style, but nothing here replaces running an actual accessibility audit on your output.

## Maintainers

<div align="center">

<table>
  <tr>
    <td align="center" width="50%">
      <a href="https://github.com/izynu">
        <img src="https://github.com/izynu.png" width="96" alt="Zynu's avatar on GitHub"/><br/>
        <sub><b>Zynu</b></sub>
      </a><br/>
      <a href="https://github.com/izynu"><sub>@izynu</sub></a><br/>
      <sub>Co-maintainer · creator</sub>
    </td>
    <td align="center" width="50%">
      <a href="https://github.com/xhraddha">
        <img src="https://github.com/xhraddha.png" width="96" alt="Shraddha's avatar on GitHub"/><br/>
        <sub><b>Shraddha</b></sub>
      </a><br/>
      <a href="https://github.com/xhraddha"><sub>@xhraddha</sub></a><br/>
      <sub>Co-maintainer</sub>
    </td>
  </tr>
</table>

</div>

Ochrelle is maintained by **Zynu** ([@izynu](https://github.com/izynu)) and **Shraddha** ([@xhraddha](https://github.com/xhraddha)). The copyright line in [LICENSE](LICENSE), the citation authors in [CITATION.cff](CITATION.cff), and the contact channels in [SECURITY.md](SECURITY.md), [SUPPORT.md](SUPPORT.md), and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) all point at the repository's GitHub channels. If ownership ever moves, update those files and the repository URLs in [CHANGELOG.md](CHANGELOG.md) and the docs.

## License

[MIT](LICENSE). Skills are documentation and code samples; use them freely, including commercially, with attribution appreciated but not required beyond the license notice.

---

<div align="center">

<sub><b>Ochrelle</b> v2.0.0 · MIT · maintained by <a href="https://github.com/izynu">Zynu</a> and <a href="https://github.com/xhraddha">Shraddha</a></sub><br/>
<sub>Named after ochre, the earth pigment people have used to make surfaces meaningful for tens of thousands of years.</sub>

</div>
