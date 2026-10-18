# Neo-Brutalism - Style Guide

Complete design tokens and rules for neo-brutalism. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **Flat only.** No gradients, no translucency, no blur. A color is a region of the sticker sheet.
- **One ink to rule them all.** Text, borders, and shadows share `#000`. Hierarchy comes from size, weight, and border pattern.
- **Candy fills carry energy, ink carries meaning.** Labels on fills are always ink.

### Palette (all pairs pre-verified with ink labels)
| Token | Value | Ink (`#000`) contrast | Role |
|---|---|---|---|
| `--paper` | `#FFFDF7` | 20.65:1 | Page ground |
| `--yellow` | `#FFC900` | 13.61:1 | Primary actions, banners |
| `--sky` | `#8BE0FD` | 14.18:1 | Secondary fills, info blocks |
| `--pink` | `#FF90E8` | 10.41:1 | Highlights, badges |
| `--lime` | `#B8FF65` | 17.53:1 | Success-ish regions, tags |
| `--coral` | `#FF5C5C` | 6.94:1 | Errors, alerts (ink label passes) |
| `--muted` | `#EDEAE2` fill / `#57534E` text | ~7:1 pair | Disabled, secondary surfaces |

Rules: 1 neutral + up to 4 candy fills on a page (coral reserved for errors). White text is for ink grounds only: white on `#FFC900` is 1.43:1, white on `#FF90E8` is 2.02:1, both fail at any size.

### Dark-mode adaptation
Keep the candy fills, flip the ground: `--ink-bg: #111111`, paper becomes the ink (text/borders/shadows `#FFFDF7`). Verify each candy fill against `#111` for non-text contrast (all five above clear 3:1 against near-black easily); focus outlines and hard shadows switch to paper.

---

## 2. Typography

- **Families:** one chunky geometric/grotesk sans for display and UI (700-900 weight, locally hosted or subset), monospace for labels, indices, and data. Two families maximum.
- **Scale:**
  | Step | Size | Weight | Use |
  |---|---|---|---|
  | display | `clamp(2.75rem, 8vw, 6rem)` | 800-900 | Hero statements |
  | h1 | 2.25rem | 800 | Page titles |
  | h2 | 1.5rem | 700 | Card titles |
  | body | 1rem (16px floor) | 400-500 | Paragraphs |
  | small | 0.875rem | 500 | Meta, never body |
  | mono-label | 0.8125rem, 0.05em tracking, uppercase | 500-700 | Indices, tags, prices |
- Display may tighten to `letter-spacing: -0.02em`; mono labels widen the other way.
- **Body text never shrinks below 16px and never goes bold-wall-of-text.** Loudness lives in display and structure.
- Links: underlined by default, 2-3px underline offset 0.15em, or boxed links with 2px borders.

---

## 3. Spacing & density

- Scale: **8 / 16 / 24 / 40 / 64** (`--s1` to `--s5`). Off-scale gaps read as broken.
- Cards pad 24px inside; page gutters 16px mobile / 24-40px desktop; section rhythm 40-64px.
- **Density is medium:** neo-brutalism breathes more than classic brutalism but never luxuriates; >96px of ambient emptiness is minimalist drift.
- Press interactions need 8px clearance from neighbors so the 4-5px shadow growth never overlaps siblings.

---

## 4. Shapes, radii, borders

- **Radius: 0 everywhere.** Cards, buttons, inputs, images, badges. One rounded corner breaks the contract.
- **Border ladder (stated pattern):**
  - 2px: internal rules, dividers, sticker borders, table cell rules.
  - 3px: default component border (buttons, inputs, cards, nav frame).
  - 4px: hero frames and full-page frames only.
- Always `solid` and always the shared ink. Never dashed except for literal "tear here" affordances on ticket motifs.
- Sticker badges rotate -3 to 3 degrees; anything past 5 degrees is chaos, not style.

---

## 5. Lighting, shadows, materials

- **Hard offset shadows only:** `box-shadow: Xpx Ypx 0 0 var(--ink)`, blur 0, no `rgba`.
- **Offset ladder:** small components `4px 4px`; large panels `8px 8px`. Hover may grow by exactly 1px; press shrinks by the translate amount (4px offset with 2px translate, or 5/3, pick one and standardize).
- **Materials are paper and ink:** no gradients (including "sheen"), no `backdrop-filter`, no inner glows, no soft ambient light.
- Optional texture: hard-edged ink stripe bands via `repeating-linear-gradient(45deg, #000 0 2px, transparent 2px 8px)` used as flat decoration.

---

## 6. Imagery & iconography

- **Images:** rectangular, unfiltered, framed with a 3px ink border; aligned to grid columns; no rounded masks, no vignettes, no duotones. Collage overlap is allowed only with borders on every layer and no occluded text.
- **Icons:** 2px stroke geometric sets (matching border weight) or plain text glyphs (`→`, `✕`, `↗`, `★`). No filled rounded icon sets, no emoji as UI icons.
- **Sticker badges:** small candy blocks with 2px borders and mono text; rotated within limits; one accent per region.
- **Barcode/tear motifs** on ticket components are idiomatic and should be built in CSS/SVG, not images of unclear size.

---

## 7. Composition & alignment

- **Visible grid:** 2-4 column layouts with bordered blocks and 2px column rules; the grid is a character. Page-wide 4px frame is idiomatic.
- **Alignment:** hard flush-left default; centered hero statements allowed once per page; centered body copy never.
- **Stair hierarchy:** display type jumps in big steps (24px body to 6rem display); no gentle ramps.
- **One loud region per viewport:** a candy banner or oversized sticker anchors each screen; the rest supports it in white/paper blocks.

---

## 8. Interaction states (complete matrix)

Reference control: the candy button (all controls follow the same press logic):

| State | Visual | Notes |
|---|---|---|
| Default | Candy fill + 3px border + `4px 4px` shadow | Label ink, 700 weight |
| Hover | Translate `-1px,-1px`, shadow grows to `5px 5px` | Never color-only; shadow/position move |
| Focus-visible | `outline: 3px solid var(--ink); outline-offset: 3px` | Identical for pointer and keyboard |
| Active/pressed | Translate `2px,2px`, shadow shrinks to `2px 2px` | Moves onto the shadow |
| Selected/`aria-pressed` | Stays translated with shadow removed | Persistent press |
| Disabled | `#EDEAE2` fill, `#57534E` text (~7:1), shadow removed | Solid muted, never opacity |
| Loading | Label swaps to mono `LOADING…`, striped band animates; size locked | No layout shift |
| Error (forms) | 3px `#FF5C5C` border + inline ink message | Never color alone |

Links: underlined, hover shifts shadow or background tint. Nav current page: ink fill + paper text. Cards are not interactive unless they contain a real control.

---

## 9. Motion

- **One motion idea: the mechanical snap.**
  - Duration 100ms, easing `linear` (mechanical, not springy).
  - Scope: `transform` and `box-shadow` on hover/press only.
- Fades (menus, reveals): 150-200ms `steps-end` or `ease-out`; no springs, no bounce.
- Marquee/ticker elements: pure CSS loop 60-90s linear, `animation-play-state: paused` on hover and `:focus-within`, removed under reduced motion.
- **Reduced motion contract:**
  ```css
  @media (prefers-reduced-motion: reduce) {
    .btn-brut { transition: none; }
    .btn-brut:hover, .btn-brut:active { transform: none; }
    .ticker__track { animation: none; }
  }
  ```
- Nothing animates continuously except declared tickers; nothing animates `width`, `height`, or `top/left`.

---

## 10. Responsive adaptation

- **Mobile (<640px):**
  - Display lands at the clamp floor (~2.75rem), not a shrunken 6rem.
  - Grids collapse to one column but keep their borders: structure stays visible.
  - Shadows drop to `4px 4px` (or 3px on the smallest cards); `overflow-x: clip` on `body` so offsets never create horizontal scroll.
  - Nav becomes a full-width bordered bar list (stacked blocks beat hamburgers for keyboard honesty); targets 48px.
- **Tablet (640-1024px):** 2-column grids; keep 2px column rules; stickers may grow.
- **Desktop (>1024px):** full exposed grid, 8px offsets on large panels, optional 4px page frame.
- **Always:** images carry explicit `width`/`height` or `aspect-ratio` (bordered layouts shift ugly on late load); press clearance re-checked at every breakpoint.
