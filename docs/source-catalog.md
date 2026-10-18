# Ochrelle Source Catalog

A catalog of the real, external sources consulted as authoritative starting
points during Ochrelle development. Every entry below is a genuine, publicly
reachable source. Per-source claims were verified at build time to the extent
noted in each entry; **contributors must re-verify specifics against the
live source before relying on them** - platform guidance and web standards
change.

Status legend: all entries below are marked **referenced during initial
development**.

---

## Standards

### 1. Web Content Accessibility Guidelines (WCAG) 2.2
- **URL:** https://www.w3.org/TR/WCAG22/
- **Publisher:** W3C (World Wide Web Consortium)
- **Type:** Web standard (W3C Recommendation track)
- **Key relevance:** The accessibility baseline every Ochrelle skill targets
  (Level AA as default). Directly informs: contrast requirements (1.4.3),
  reflow at 320 px (1.4.10), hover/focus content behavior (1.4.13), pause/
  stop/hide for moving content (2.2.2), flash thresholds (2.3.1), dragging
  alternatives (2.5.7), target size (2.5.8), and focus appearance/visibility
  criteria - which surface throughout the bento-grid, spatial-ui, and
  visual-style checklists.
- **Status:** Referenced during initial development.

### 2. W3C Web Accessibility Initiative (WAI)
- **URL:** https://www.w3.org/WAI/
- **Publisher:** W3C WAI
- **Type:** Standards hub - guidelines, techniques, how-to guides
- **Key relevance:** Gateway to WCAG techniques and understanding documents
  used when translating WCAG criteria into concrete checklist items (e.g.,
  what "visible focus" and "target size" mean in practice).
- **Status:** Referenced during initial development.

## Reference documentation

### 3. MDN Web Docs
- **URL:** https://developer.mozilla.org/
- **Publisher:** Mozilla
- **Type:** Reference documentation (CSS, HTML, JavaScript, Web APIs)
- **Key relevance:** Mechanics reference for nearly every technique in the
  skills: CSS Grid, transforms and perspective, media queries,
  `prefers-reduced-motion`, `forced-colors`, WebGL/WebGPU availability, and
  browser-compatibility caveats phrased honestly rather than optimistically.
- **Status:** Referenced during initial development.

### 4. MDN - `backdrop-filter`
- **URL:** https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter
- **Publisher:** Mozilla
- **Type:** CSS property reference
- **Key relevance:** Syntax, behavior, and compatibility for the property
  underpinning glassmorphism and liquid-glass web approximations - including
  the `-webkit-` prefixed variant and `@supports` fallback patterns taught in
  the skills and troubleshooting docs.
- **Status:** Referenced during initial development.

## Platform design documentation

### 5. Apple Human Interface Guidelines
- **URL:** https://developer.apple.com/design/human-interface-guidelines/
- **Publisher:** Apple
- **Type:** Official platform design guidance
- **Key relevance:** Primary authority for Apple platform design principles -
  including the documented visionOS model (eyes + hand gestures as primary
  input, hover on look, system window materials, shared space, comfort
  considerations) that the spatial-ui skill relies on and deliberately does
  not embellish.
- **Status:** Referenced during initial development.

### 6. Apple - Liquid Glass (technology overview)
- **URL:** https://developer.apple.com/documentation/TechnologyOverviews/liquid-glass
- **Publisher:** Apple
- **Type:** Official technology overview
- **Key relevance:** The authoritative description of Apple's Liquid Glass
  material approach. Anchors the ochrelle-liquid-glass skill's central
  distinction: a platform material system versus generic CSS blur
  approximations, which the documentation explicitly labels as
  approximations.
- **Status:** Referenced during initial development.

### 7. Material Design 3
- **URL:** https://m3.material.io/
- **Publisher:** Google
- **Type:** Official design system documentation
- **Key relevance:** Structured reference for elevation systems, color roles
  and accessibility-aware theming, state layers, and component guidance -
  used as a comparative authority when deriving Ochrelle art-direction
  recommendations (depth ramps, tokens, state design).
- **Status:** Referenced during initial development.

## Agent Skills ecosystem

### 8. Agent Skills specification
- **URL:** https://agentskills.io/specification
- **Publisher:** agentskills.io
- **Type:** Open specification
- **Key relevance:** The format contract for every Ochrelle skill: frontmatter
  fields, name/directory correspondence, description constraints, relative
  reference conventions, and progressive disclosure. Verified during initial
  development; the repository's validators encode its rules.
- **Status:** Referenced during initial development.

### 9. Anthropic skills repository
- **URL:** https://github.com/anthropics/skills
- **Publisher:** Anthropic
- **Type:** Public reference implementations of agent skills
- **Key relevance:** Structural reference for how production skills organize
  SKILL.md entry points and bundled reference files in practice.
- **Status:** Referenced during initial development.

### 10. agentskills repository
- **URL:** https://github.com/agentskills/agentskills
- **Publisher:** agentskills
- **Type:** Specification ecosystem repository
- **Key relevance:** Companion to the specification - project context,
  issues, and format evolution that Ochrelle tracks for maintenance events
  (see research-methodology.md § 1).
- **Status:** Referenced during initial development.

---

## Honesty note

These entries were consulted as **authoritative starting points**: they
define the format, standards, and platform-principle layers Ochrelle builds
on. They were **not** systematically quoted line-by-line into the skills, and
per-source claims were verified at build time only to the extent noted above.
Platform documentation in particular evolves quickly (Apple's material and
visionOS guidance, MDN compatibility data); before relying on any specific
claim - or contributing a new one - re-verify against the live source and
update the entry with a dated re-verification note. Do not add sources you
have not actually consulted; see research-methodology.md § 4 for the binding
citation rules.
