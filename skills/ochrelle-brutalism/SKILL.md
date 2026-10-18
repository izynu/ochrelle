---
name: ochrelle-brutalism
description: Art direction and implementation skill for digital brutalism and neo-brutalism - raw structure, harsh borders, hard offset shadows, flat saturated color, and intentional anti-polish with preserved accessibility. Use when a project calls for brutalist, neo-brutalist, raw HTML, anti-design, raw-web, stark, or bold-outline aesthetics; when building portfolio sites, editorial/media sites, indie products, creative agencies, or Gen Z-facing brands; or when a user mentions thick black borders, hard shadows, unstyled-feeling layouts, or deliberately unpolished design.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: typographic-expressive
---

# Brutalism & Neo-Brutalism

## Definition

Brutalism in interface design is the deliberate display of structure instead of its concealment. Where mainstream design smooths, rounds, and shadows, brutalism leaves the skeleton visible: raw borders, exposed grids, default-feeling type, flat color, and interaction that answers instantly rather than easing.

There are two distinct branches, and they must never be blurred:

| | Classic digital brutalism | Neo-brutalism (2020s) |
|---|---|---|
| Attitude | Anti-decoration, anti-corporate, systems-honest | Playful, sticker-like, "ugly-cute" |
| Borders | 2–4px harsh, often inconsistent on purpose | Uniform 3–4px solid black |
| Shadows | None, or crude | Hard offset `6px 6px 0 0 #000`, zero blur |
| Color | Stark primaries on white/black, or near-monochrome | Flat saturated pastels/brights (#FF6B6B, #4ECDC4, #FFDB58) |
| Radius | 0 | 0 (non-negotiable) |
| Type | System UI / monospace, default-feeling | Bold 700+ sans, oversized |
| Motion | Instant or none (0–80ms) | Mechanical press (translate onto the shadow) |
| Read of | "This is real, this is built" | "This is loud, this is fun" |

If a request says "raw", "unstyled", "like the early web", "honest HTML" → classic. If it says "Gumroad-style", "bold borders", "hard shadows", "playful startup" → neo-brutalism. Both share the same spine: visible structure, flat color, zero radius, bold type, instant feedback.

## Philosophy

1. **Structure is the aesthetic.** The grid, the border, the raw element boundary are shown, not hidden. Nothing pretends to be something else - a button looks like a rectangle with a label because that is what it is.
2. **Honesty over polish.** Materials are not faked. There are no gradients simulating depth, no blurred shadows simulating elevation. Elevation, when it exists, is a literal drawn offset - an honest, graphical statement of "this sits above that".
3. **Intentionality, not neglect.** Brutalism is authored roughness. Every "unstyled" element is a decision. The difference between brutalism and a broken page is that brutalism's roughness is consistent, legible, and repeatable.
4. **Speed as a value.** Instant feedback (near-zero transitions) is part of the ideology: the interface responds at the speed of the machine, not the speed of an easing curve.
5. **Tension without harm.** The style courts discomfort - harsh contrast, dense blocks, abrupt edges - but never at the cost of readability. This is the single most important teaching point in this skill.

## How it differs from similar styles

- **vs. neo-brutalism:** Neo-brutalism is a *commercialized, friendly* descendant of brutalism. It keeps borders, flatness, and zero radius but adds saturated color systems, hard shadows as a depth metaphor, and mechanical press interactions. Classic brutalism has no shadow system and no obligation to charm.
- **vs. maximalism:** Both are loud, but brutalism is loud through *starkness* (few colors, hard edges, big blocks) while maximalism is loud through *accumulation* (many layers, patterns, mixed type). Brutalism never uses blur, gradient, or ornament for its own sake.
- **vs. broken/unstyled pages:** An unstyled HTML document uses browser defaults by accident. Brutalism uses a *token system* (border widths, offsets, one palette) so the roughness composes. If your "brutalist" page has five different border widths by accident, it is broken, not brutalist.

## Brief historical context (verifiable)

- The name descends from architecture's **New Brutalism** (post-WWII Britain/Europe), from the French *béton brut* - "raw concrete" - associated with Le Corbusier's postwar work and theorized by Reyner Banham in the 1950s. Values: material honesty, visible structure, anti-ornament.
- On the web, brutalism surfaced in the **mid-2010s**, most visibly when fashion houses (Balenciaga's deliberately raw site is the commonly cited example) rejected gloss, alongside a revival of early-web aesthetics (plain HTML, Times New Roman, default blue links). Sites like Craigslist are frequently referenced as accidental precursors.
- **Neo-brutalism** crystallized around **2020–2021** - Gumroad's 2021 redesign is the widely cited mainstream catalyst - and spread through Figma Community templates into startup, indie, and Gen Z-facing products.

## When to use / when NOT

**Use for:**
- Design portfolios, studio sites, personal sites of technologists - audiences that read structure as taste.
- Editorial, culture, and media sites where the raw feel signals editorial independence.
- Indie tools, developer products, CLI-adjacent SaaS - brutalism's honesty matches "it just does the thing".
- Gen Z-facing brands, merch drops, event sites, Figma-adjacent apps - where neo-brutalism's energy fits.
- Prototypes and MVPs where honesty-of-state (this is a draft, this is a beta) is a feature.

**Do NOT use for:**
- Banking, healthcare, insurance, government - audiences read the roughness as untrustworthy.
- Long-form reading products (e-reader-like experiences, dense dashboards) - the style taxes sustained scanning.
- Luxury brands - neo-brutalism's sticker energy and classic brutalism's rawness both undercut premium cues.
- Products legally required to meet strict accessibility certifications without room for the extra contrast/motion care this style demands.

## Quick art-direction token sketch

- `--bg: #FFFDF5` (warm paper white) or `#FFFFFF`; dark variant `#111111` with light ink.
- `--ink: #000000` - text and borders share one ink; hierarchy comes from size/weight, not color.
- `--accent: #FF4D00` or `#2563EB` - one flat saturated accent; neo-brutalism may carry 3–4 (e.g. `#FF6B6B`, `#FFDB58`, `#4ECDC4`, `#7C5CFF`) used as **fills**, never gradients.
- `--border-width: 3px` (neo) / `2px–4px` mixed deliberately (classic) / `--border-style: solid #000`.
- `--shadow-hard: 6px 6px 0 0 #000` - offset only, blur 0. Press state translates to `2px 2px` and shrinks the shadow to `2px 2px 0 0 #000`.
- `--radius: 0` everywhere; corners are corners.
- `--font-body: system-ui/monospace stack; --font-weight-strong: 700–900`; display type oversized (clamp up to 4–8rem).
- `--transition: 0ms` (classic) or `80ms linear` (neo, for the press snap only).

## Component guidance summary

**What shines in brutalism:** buttons (border + hard shadow + press translate is the signature interaction), cards/panels (bordered blocks that read like print columns), announcement banners and sticker badges, nav bars as literal bars with visible borders, tables and code-heavy UI (monospace belongs here), forms with thick focus treatment.

**What stays restrained:** body copy (keep line length ~60–75ch, normal weight, comfortable size - loudness lives in structure, not in 16px bold walls of text), forms must keep standard semantics (labels, real inputs, visible focus), imagery stays unfiltered and rectangular (no rounded masks, no soft vignettes), iconography should be stroke-based and geometric or plain text glyphs.

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Canonical CSS recipe

```css
/* Signature neo-brutalist button: border + hard shadow + mechanical press */
:root {
  --ink: #000;
  --paper: #fffdf5;
  --accent: #ff4d00;
  --bw: 3px;
  --press-x: 4px; --press-y: 4px;
}
.btn-brutal {
  border: var(--bw) solid var(--ink);
  background: var(--accent);
  color: #000;
  font-weight: 700;
  padding: 0.75rem 1.5rem;
  border-radius: 0;
  box-shadow: 6px 6px 0 0 var(--ink);
  transition: transform 80ms linear, box-shadow 80ms linear;
}
.btn-brutal:hover { transform: translate(-1px, -1px); box-shadow: 7px 7px 0 0 var(--ink); }
.btn-brutal:active {
  transform: translate(2px, 2px);                 /* move onto the shadow */
  box-shadow: 4px 4px 0 0 var(--ink);             /* shadow shrinks by the same amount */
}
.btn-brutal:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
```

## Accessibility notes (mandatory)

Brutalism ≠ inaccessible design. The aesthetic is harsh; the ergonomics must not be.

- **Contrast:** body text still meets WCAG 2.1 AA - 4.5:1 (normal) / 3:1 (≥18.66px bold or 24px). The real trap is **white text on warm saturated fills**: white on `#FFDB58` is ~1.4:1, white on `#FF6B6B` ~2.8:1. Ink on those same fills passes easily (ink on `#FFDB58` ≈ 15.5:1, ink on `#FF4D00` ≈ 6.3:1). Keep ink as the label color on mid-tone fills; reserve white text for ink grounds. Ink on mid-blue `#2563EB` (~4.1:1) is large/bold text only.
- **Focus:** always visible - `outline: 3px solid var(--ink); outline-offset: 3px`. Never remove focus rings to look cleaner; brutalism makes focus rings *bigger*, not smaller. (WCAG 2.4.7.)
- **No hover-only information:** anything revealed on hover must also exist in the DOM and be reachable by keyboard/touch.
- **Motion:** press interactions are tiny translations; still respect `prefers-reduced-motion: reduce` by removing the transform and keeping the shadow change.
- **Target size:** thick borders are not padding. Keep interactive targets ≥ 44×44px.
- **Text as decoration:** oversized display text must still be real text (not images) so it scales, translates, and screen-reads.

## Top-5 failure modes

1. **Broken-page drift** - inconsistent border widths/offsets that read as CSS bugs, not style. Fix with the token system in [references/style-guide.md](references/style-guide.md).
2. **Light-on-warm-fill contrast failures** - white text on warm saturated fills (white on `#FFDB58` ≈ 1.4:1). Ink-on-fill passes; white-on-fill usually doesn't. See the corrected pair table in [references/quality-checklist.md](references/quality-checklist.md).
3. **Blur creep** - adding soft shadows or gradients "just a little". One blur breaks the whole contract; use offsets only.
4. **Radius creep** - rounding one card "to soften it". Zero radius everywhere or the style collapses.
5. **Press interaction without focus/motion parity** - mechanical `:active` with no `:focus-visible` and no reduced-motion fallback. The full state matrix is in [references/implementation-examples.md](references/implementation-examples.md).

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
