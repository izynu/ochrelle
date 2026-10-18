# Hand Drawn - Style Guide

Complete design tokens and rules for Hand Drawn. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **Ink on paper.** Every readable string is `--ink` (or `--ink-soft`) on a paper-family ground. Color fills carry state, not text color.
- **Markers are fills.** Marker accents sit *behind* ink text or as graphic fills; light text on markers is banned.
- **Warm, not neon.** All accents are tinted toward yellow/coral/sky to sit beside warm paper.

### Palette (with verified contrast)
| Token | Value | Ink `#33302A` on it | Role |
|---|---|---|---|
| `--paper` | `#FFFCF2` | 12.8:1 | Page ground |
| `--card` | `#FFEFD9` | 11.7:1 | Card/panel fill |
| `--highlight` | `#FFE45C` | 10.3:1 | Marker highlights, primary buttons |
| `--leaf` | `#B9E4A8` | 9.2:1 | Success fills, positive markers |
| `--sky` | `#7CC7F2` family (`#8FC7F2`) | 7.3:1 | Info fills, links-in-bubbles |
| `--coral` | `#FF8A75` | 5.7:1 | Accent fills, large text only |
| `--ink` | `#33302A` | - | Text, borders, doodles |
| `--ink-soft` | `#5A544A` | 7.3:1 on paper | Secondary text, hints |
| `--error` | `#8A2E1F` | 8.2:1 on paper | Error text |
| `--success` | `#1F5C3D` | 7.7:1 on paper | Success text |

Rules: 1 paper ground + 1 card tone + 3-4 marker accents maximum. A fifth marker color fails the palette gate. Grid/rule textures are `rgba(51, 48, 42, 0.06)` or lighter - decorative only.

---

## 2. Typography

- **Body:** one humanist sans: `"Comic Neue", "Trebuchet MS", "Segoe UI", sans-serif`, weight 500, 16-17px floor, line-height 1.6. Never smaller.
- **Accents:** one handwriting face: `"Caveat", "Patrick Hand", "Segoe Print", cursive`, used at 20-28px for hints, margin notes, and short labels. Script never sets body copy, numbers tables, or all-caps strings.
- **Display:** the body sans at 700-800 weight (or a chunky rounded display), `clamp(2rem, 5vw, 3.5rem)`, line-height 1.1, letter-spacing 0 to -0.01em.
- **Scale:** display / h2 1.5rem 700 / h3 1.25rem 700 / body 1.0625rem 500 / small 0.875rem 500 (meta only) / hand-note 1.25-1.75rem 400.
- Emphasis: `<strong>` plus optional marker `<mark>`; underline by hand (2-3px slightly wavy `border-image` or SVG) rather than default underline on links.
- Numbers: keep the sans for numerals; script digits are illegible at small sizes.

---

## 3. Spacing & density

- Scale: 4 / 8 / 12 / 16 / 24 / 40 / 64 (`--s1..--s7`).
- Page gutter: 24-40px. Card padding: 24px. Section gaps: 40-64px - generous whitespace is part of the warmth.
- Density: medium-low. This style breathes; if a layout needs tables of 20 rows, the row style stays crisp (solid 1px separators, sans text) while the chrome stays sketchy.
- Annotations offset 8-16px from their target with an arrow path connecting them; never let a note float farther than one line-height from its referent.

---

## 4. Shapes, radii, borders

- **Wobbly radius token:** `border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px` on cards, buttons, and bubbles; a small variant `125px 10px 120px 10px / 10px 120px 10px 125px` for chips. Nothing uses a perfect circle or perfect rectangle.
- **Borders:** 3px solid `--ink` for primary surfaces; 2px for secondary chips and dividers. One weight per element, two weights in the system.
- **Wobble lines:** for SVG frames use a turbulence filter (`feTurbulence` + `feDisplacementMap`, scale 2-4) applied to a rect stroke; for pure CSS use the radius token. Both are fine; pick one per project.
- **Dividers:** 2px ink lines with a slight rotation (-0.5deg) or a dashed 2px line for "draft" zones.
- Rotation discipline: elements rotate -1.5deg to 1.5deg; the angles come from a fixed set (`-1.5, -0.5, 0.5, 1.5`), not arbitrary values.

---

## 5. Lighting, shadows, materials

- Materials: paper and ink. Texture is optional: faint ruled/grid lines via repeating gradients at ≤6% alpha, or a paper-grain SVG at ≤4%.
- Shadows: minimal. One allowed recipe: `0 2px 0 rgba(51, 48, 42, 0.15)` as an "ink bleed" under primary buttons. No blurred elevation, no glass.
- Depth comes from stacking drawn shapes: a card behind a card offset 4-8px with 2px ink border (comic panel stack), not from blur.
- Marker texture: highlights are slightly transparent (0.85) so the paper shows through; edges may be uneven via the radius token on the `<mark>` box.

---

## 6. Imagery & iconography

- **Icons:** hand-drawn stroke set (2.5px ink strokes, open corners, slightly irregular) or filled doodle set; one set only. Do not mix crisp geometric icons with sketch icons.
- **Doodles:** arrows, stars, spirals, underlines - single-weight ink paths, `aria-hidden`, always anchored to real content. Budget: 1-3 per section.
- **Thought bubbles:** card variant with a tail (pseudo-element rotated square with ink border); use for tips, warnings, and character voice.
- **Photos:** rare; when used, frame them as taped-in snapshots (white border + tape strip + 1deg rotation). No duotone, no filters that fight the ink.
- **Illustration:** single-weight line illustration matches the ink token; colored illustration must reuse marker tokens exactly.

---

## 7. Composition & alignment

- Grid exists but reads loose: columns align, while individual elements rotate ±1.5deg and offset 2-6px to feel placed by hand.
- **Alignment anchors:** every section has one strongly aligned element (heading, form row, or full-width card) so the looseness composes instead of scatters.
- Reading order = DOM order; annotations are positioned absolutely relative to their referent and must not break linear flow.
- Max text measure 60-70ch. Lists get hand-drawn bullets (`✏`, `▸`, or a 6px ink dot with irregular shape).
- Vertical rhythm on the ruled-line grid: 32px baseline matches the 32px repeating gradient in the canonical recipe.

---

## 8. Interaction states (complete matrix)

Signature button - every interactive control defines all of these:

| State | Visual | Notes |
|---|---|---|
| default | marker or paper fill, 3px ink border, wobbly radius | Text `--ink`, weight 700. |
| hover | rotate -1deg, translateY(-2px), ink-bleed shadow appears | 200ms ease-out. |
| focus-visible | `outline: 3px dashed var(--ink); offset 4px` | Never removed; dashed = sketchy but high contrast. |
| active | translateY(1px), shadow removed, border stays 3px | Press feedback immediate. |
| disabled | 2px `--ink-soft` border, `--ink-soft` text on paper, cursor not-allowed | 7.3:1 text, readable. |
| selected (chips/tabs) | marker fill + 3px ink border + drawn check glyph | Also `aria-pressed` / `aria-current`. |
| loading | label swaps to "drawing..." + animated pencil path (dash offset), width locked | `aria-busy="true"`; static fallback text. |
| error (inputs) | 3px `--error` border + hand-drawn cross glyph + text line in `--error` (8.2:1) | Never color alone. |

Quiz/choice rows: correct = leaf fill + check glyph + word "correct"; incorrect = coral fill (large) + cross glyph + word "try again"; both include text.

---

## 9. Motion

- Durations: 150-250ms, `cubic-bezier(0.22, 1, 0.36, 1)` (gentle overshoot without full spring). Hover 200ms; page transitions 250ms.
- **Legal moves:** small rotations on hover, draw-in strokes (SVG `stroke-dashoffset`) once on first view, wobble-on-hover for chips (1 keyframe cycle), button press.
- **Banned:** continuous floating/bobbing of UI chrome, looping wiggle on text, parallax notebooks, cursor trails.
- Draw-in contract: fires once, total ≤600ms, and under reduced motion the stroke renders complete with no animation:

```css
@media (prefers-reduced-motion: reduce) {
  .btn, .card, .chip { transition: none; }
  .btn:hover { transform: none; }
  .draw path { stroke-dashoffset: 0; animation: none; }
}
```

---

## 10. Responsive adaptation

- **Mobile (<768px):** gutter 16-24px; wobbly radius persists; annotations collapse below their referent (no absolute positioning across columns); touch targets ≥48px incl. border; rotation reduces to ±1deg to avoid neighbor overlap.
- **Tablet (768-1024px):** two-column card grids; folder-tab nav becomes a horizontal scrollable tab strip with visible ink borders on all tabs.
- **Desktop (>1024px):** full annotations with arrows; margin-note column allowed (handwriting at 24-28px).
- Zoom 200%: ink borders and dashes stay visible; nothing relies on texture to communicate.
- Print styles: drop texture backgrounds, keep ink borders - the style naturally prints well if paper texture is behind solid text islands.
