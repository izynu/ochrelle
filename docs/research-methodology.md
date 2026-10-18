# Ochrelle Research Methodology

How Ochrelle knowledge was produced, what was verified and how, and how
contributors should keep it true.

---

## 1. Spec-first verification

The Agent Skills specification (agentskills.io/specification) is the
contract every Ochrelle skill must satisfy. It was **verified against the
published Agent Skills specification during initial development**: frontmatter
fields, name/directory correspondence, description constraints, and the
progressive-disclosure pattern (compact SKILL.md, bundled relative
references) were checked while writing the skills, and again via the
repository's own validators (`scripts/validate_skills.py`).

Rules that follow:

- Skill `name:` must equal its directory name.
- Descriptions are third person, state what the skill does and when to use
  it, include trigger keywords, and respect the specification's length limit.
- All bundled links are relative; no skill references another skill's files.
- When the specification changes, treat it as a maintenance event: re-verify
  every SKILL.md and note the pass in CHANGELOG.md.

## 2. Source hierarchy

Ochrelle ranks authorities explicitly:

1. **Platform specifications and official vendor documentation** - Apple
   Human Interface Guidelines, Apple's Liquid Glass documentation, Material
   Design 3. These are the only sources allowed to define platform behavior
   (visionOS input model, Liquid Glass materials, elevation systems).
2. **Web standards** - W3C WCAG 2.2 and WAI material. Accessibility
   requirements in skills cite or track WCAG success criteria (contrast,
   reflow, target size, dragging alternatives, pause/stop/hide, animation
   from interactions) rather than folklore.
3. **Reference documentation** - MDN Web Docs for CSS/JS mechanics
   (`backdrop-filter`, grid, `prefers-reduced-motion`, `forced-colors`,
   WebGL/WebGPU availability), including honest browser-support caveats.
4. **The Agent Skills ecosystem itself** - the agentskills.io specification,
   the agentskills repository, and Anthropic's public skills repository, as
   structural references for what a well-formed skill looks like.

Design-trend articles, blog posts, and community lore are treated as
*hypotheses*, not sources: anything they contribute must be re-derived from
tiers 1–3 or explicitly labeled as contextual recommendation.

## 3. Style research approach

Each specialist skill was researched with the same template:

1. **Define and differentiate.** Establish what the style/pattern/paradigm
   *is* and - more importantly - what it is *not* relative to its nearest
   neighbors (glassmorphism vs. liquid glass; bento grid vs. generic card
   grids; spatial UI vs. "anything with a shadow").
2. **Establish applicability.** Which products it serves, which it harms,
   and why, in terms of user tasks (scanning vs. reading, choosing vs.
   operating).
3. **Derive art direction** (color, type, spacing, shape, light, motion,
   states) as *contextual recommendations with working values*, never as
   invented universal laws.
4. **Build working code.** Original, runnable HTML/CSS/JS with coherent
   tokens and complete states; platform-specific sketches are labeled
   illustrative and pointed at official docs.
5. **Enumerate failure modes** concretely, with fixes.
6. **Convert to checklists.** Every claim that can be tested becomes a
   checklist item an agent can actually run against its own output.

## 4. Citation honesty rules

These rules are binding on Ochrelle content and on contributors:

- **No manufactured citations.** Every source listed in
  `docs/source-catalog.md` is real, with a real URL and publisher.
- **Claim–verification distance.** Each entry records what was actually
  consulted and to what extent; a source consulted for structure is not
  thereby a source for every specific claim in a skill.
- **No invented platform APIs or capabilities.** Platform specifics come
  from tier-1 sources or are labeled "illustrative - verify against official
  documentation".
- **No invented benchmarks or test results.** Performance statements are
  either generic engineering guidance (labeled as such) or measured results
  with the measurement context recorded.
- **Verified vs. unverified labeling** appears wherever it matters -
  installation docs, browser-support notes, and every skill's delivery
  checklist ("record what was tested and what was not").
- **Dates matter.** Platform guidance and web standards move; entries carry
  their verification timeframe ("referenced during initial development") and
  contributors re-verify before relying on specifics.

## 5. Refreshing the research (for contributors)

Trigger-based, not calendar-based - refresh when:

- **The Agent Skills specification changes** → re-verify all frontmatter and
  reference conventions; update validators if needed.
- **A platform ships relevant changes** (e.g., Apple material or visionOS
  updates, Material 3 revisions) → update the affected skill(s), re-verify
  against the new official documentation, bump the skill's
  `metadata.version`.
- **WCAG or browser support shifts** (e.g., a CSS feature's support status)
  → update the relevant style-guide and troubleshooting sections, including
  compat claims.

Refresh procedure:

1. Re-read the primary source; do not patch from memory.
2. Diff the skill's claims against it; fix or re-label (recommendation vs.
   verified).
3. Update the entry in `docs/source-catalog.md` with the re-verification
   note and date.
4. Bump the skill version and run `python3 scripts/validate_skills.py`.
5. Record what changed and why in CHANGELOG.md.

## 6. Known limits of this methodology

- Ochrelle was authored without access to physical devices for every platform
  claim; headset-specific guidance therefore sticks to documented,
  verifiable principles and labels everything else.
- Browser support statements reflect what was checked during initial
  development plus MDN's published compatibility data; they are explicitly
  not a substitute for testing on target browsers.
- Design "trend" judgments (what suits a product category) are argued from
  task analysis, not measured in user studies; they are recommendations,
  and the skills say so.
