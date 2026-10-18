# Memphis Design - Style Guide

Complete design tokens and rules for Memphis Design. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **Five flat fills, one referee.** Yellow, lilac, coral, teal, blue - all flat, all outlined in ink. No gradients, no translucency, no blur.
- **Ink text on every fill.** The near-black ink is what makes clashing colors compose. White text belongs only on the ink ground.
- **The ground stays warm white.** Fills sit on `#FFF9EF`; a fill-colored page background destroys the figure-ground snap.

### Palette and verified contrast (ink `#101010` text)
| Token | Value | Ink text on it | Role |
|---|---|---|---|
| `--bg` | `#FFF9EF` | 18.2:1 | Page ground |
| `--yellow` | `#FFD23F` | 13.2:1 | Highlights, badges, chips |
| `--lilac` | `#C9B1F5` | 10.1:1 | Secondary cards, tags |
| `--blue` | `#4EA8DE` | 7.2:1 | Feature fills, illustration |
| `--coral` | `#FF6B5B` | 6.8:1 | Primary buttons, alerts (with text) |
| `--teal` | `#0FA3A3` | 6.2:1 | Alternate fills, success cues (with text) |
| `--ink` | `#101010` | white text on it: 19.0:1 | Text, outlines, shadows, nav ground |

- Every ink-on-fill pair above passes AA body-text contrast; any of them can carry labels.
- **Forbidden:** white text on any fill (best case 3.1:1 on teal; 2.0:1 on lilac). Ink fills carrying white text are the only light-on-dark exception.
- Dark mode: flip the ground to `#141312` and keep the five fills unchanged with ink outlines swapped to `#FFF9EF`; re-measure before shipping.

---

## 2. Typography

### Families
- **Display:** one chunky geometric or slab face at 800-900 weight (rounded terminals are welcome). Carries headlines, big numbers, sticker text.
- **Body/UI:** one clean sans (system stack fine) at 400-600. Body text never uses the display face.
- Two families maximum. Adding a third face breaks the toy-box discipline faster than any color mistake.

### Scale
| Step | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| display | `clamp(2.5rem, 7vw, 5rem)` | 800-900 | 0.98 | Hero words |
| h2 | `1.875rem` | 800 | 1.1 | Section titles |
| h3 | `1.25rem` | 700 | 1.25 | Card titles |
| body | `1rem` (16px floor) | 400-500 | 1.6 | Paragraphs, UI text |
| small | `0.875rem` | 500 | 1.4 | Captions, meta |
| label | `0.75-0.8125rem` | 700, uppercase, `0.05em` | 1 | Chips, tags, buttons |

- Display may sit on fills and rotate up to 2deg. Body text never rotates, never sits on patterns.
- Links in body: ink text with 2px wavy or solid underline in ink; hover thickens to 3px and may take the coral color.

---

## 3. Spacing & density

- Scale: `8 / 16 / 24 / 40 / 64 / 96`. Memphis is generous: pattern bands need 40px clearance on each side.
- Cards pad 24px inside; section padding 64-96px; the composition needs room for the shapes to miss each other.
- Density is deliberately uneven: dense sticker clusters against big empty warm-white fields. Uniform density reads as a template.
- One anchored composition rule: each section has one axis-aligned block (headline, nav, or figure) and may rotate or offset the rest around it.

---

## 4. Shapes, radii, borders

- Borders: `3px solid var(--ink)` on interactive elements and small cards; `6px` on feature cards. No borderless raised elements.
- Radius is a chosen mix: `0` for graphic blocks that quote geometry (arch shapes, zigzag panels), `12px` for cards and inputs, `999px` for chips, pills, and blob buttons.
- Squiggles, zigzags, and arcs are SVG or CSS-drawn decorations with the same 3px ink stroke; they are `aria-hidden` and never interactive.
- Starburst stickers (see the retro clip-path or SVG) pin card corners at -6deg to 6deg, one per card.

---

## 5. Lighting, shadows, materials

- **Hard offset shadows only:** `4px 4px 0 0 var(--ink)` buttons/badges, `6px 6px 0 0 var(--ink)` cards, `8px 8px` for hero panels. Blur is always 0.
- Pressed state translates onto the shadow (2px move, shadow shrinks to 2px). Selected state keeps the element permanently pressed.
- Materials: laminate, terrazzo, enameled metal, printed plastic. Simulate with flat color and ink outlines - never with gradients, glows, or `backdrop-filter`.
- Terrazzo recipe: flat cream base with `radial-gradient` speckles from the palette at 4-6px, tiled at 90x60px, used in bands 32-64px tall.

---

## 6. Imagery & iconography

- Illustration outranks photography. Flat shapes, 3px ink outlines, palette-only fills. Photos, if used, get a 3px ink border and a 2deg max tilt.
- Icons: chunky filled or 3px-stroke glyphs matching the border system; no thin-line icon sets, no soft 3D emoji.
- Pattern library (all `aria-hidden`, ink strokes, palette fills): black-and-white stripes, zigzag ribbons, squiggle lines, dot grids, terrazzo speckle.
- Patterns are band-shaped (16-64px tall strips, sidebar ribbons) or container fills with text on a solid inset panel - never behind live text.

---

## 7. Composition & alignment

- **Asymmetric with an anchor:** every screen has one strongly aligned element (the nav bar, one headline block, or one full-width card). Everything else may offset, tilt, or overlap it slightly.
- **Overlap is compositional:** shapes may overlap by 8-24px with ink outlines keeping them legible; text blocks never overlap each other.
- **Left-aligned reading content; centered sticker text only** on badges and hero displays.
- **Scale jumps:** display 80px over body 16px is correct. Hierarchy here is louder than any corporate style.
- Grid discipline under the chaos: a real 12-column grid positions the anchored elements; decoration plays on top.

---

## 8. Interaction states (complete matrix)

| Control | Default | Hover | Focus-visible | Active/pressed | Disabled |
|---|---|---|---|---|---|
| Primary button | Coral fill, ink text, 3px border, 4px shadow | Lifts 1px, shadow 5px | `outline: 3px solid var(--ink); outline-offset: 3px` | Onto shadow: translate 2px, shadow 2px | `#E8E2D6` fill, `#5C584F` text (4.9:1), no shadow, `not-allowed` |
| Secondary button | White fill, 3px border, ink text | Yellow fill | Same outline | Same press | As above |
| Chip/tag | Lilac or yellow fill, 3px border, pill | Lifts 1px | Same outline | Pressed look persists when selected | `#E8E2D6`, muted text |
| Nav link (on ink bar) | White text, no underline | Wavy yellow underline | `outline: 3px solid #FFF9EF; outline-offset: 3px` | n/a | n/a |
| Current page | Yellow underline 3px + white bold text | none | same | n/a | n/a |
| Card link | Whole-card hover lifts 2px (shadow 8px) | same | inner CTA carries the focus ring | CTA presses | n/a |
| Input | White, 3px border, 12px radius | Border stays, bg to `#FFF3E0` | 3px outline + border stays | n/a | `#E8E2D6` fill, `#5C584F` text |
| Input error | 3px coral border + message (ink text on white, coral flag) | n/a | unchanged | n/a | n/a |
| Toggle/switch | 3px border track, yellow knob, ink outlines | Knob scales 1.05 | 3px outline on track | Knob slides 200ms | Track `#E8E2D6`, knob `#BDB6A8` |

- Error text: ink on white with a coral 3px flag border; never color-only, always with `aria-invalid` + message.
- Selected/pressed persistence: chips and toggles keep the translated, shadow-removed position.

---

## 9. Motion

- Timing: `200ms cubic-bezier(0.34, 1.56, 0.64, 1)` - the single overshoot curve. Entrance animations may use it once per element; nothing loops.
- Scope: `transform` and `box-shadow` only. Fill colors switch instantly.
- Signature moves: press-onto-shadow; sticker badges wiggle 2deg once on hover; hero shapes enter with one 200ms pop.
- Banned: infinite floating, bouncing squiggle loops, marquees without pause controls, parallax.
- Reduced-motion contract:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { transition-duration: 0ms; animation: none; }
    .btn-memphis:active { transform: none; box-shadow: 2px 2px 0 0 var(--ink); }
  }
  ```

---

## 10. Responsive adaptation

- **Mobile (<768px):** display clamps to 2.5rem; one column; hard shadows shrink to 4px cards / 3px buttons; pattern bands stay but halve in height; `overflow-x: clip` on `body` - offsets must never create horizontal scroll.
- **Tablet (768-1024px):** two-column card grids; terrazzo bands widen; stickers scale down to 64px.
- **Desktop (>1024px):** full asymmetric compositions, 8px hero shadows, sticker clusters allowed in the margins.
- Rotation caps tighten on small screens (1deg) to protect tap targets.
- All images and SVG shapes carry explicit dimensions; late-loading decoration must not shift the anchored composition.
