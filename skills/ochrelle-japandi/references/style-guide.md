# Japandi - Style Guide

Complete design tokens and rules for Japandi. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **Warm, low-chroma, never low-legibility.** Every text token passes AA with margin; quietness comes from hue and saturation, not from failing contrast.
- **Layered off-whites on beige.** The ground is warm beige; raised surfaces are off-white. Pure white and pure black do not appear.
- **Two earth accents.** Clay for actions, moss for confirmation and nature cues. No brights, no blues.

### Palette and verified contrast
| Token | Value | Pairing | Ratio | Role |
|---|---|---|---|---|
| `--bg` | `#F2EDE3` | ink text | 11.9:1 | Page ground |
| `--card` | `#FAF7F1` | ink text | 13.0:1 | Cards, inputs, raised layers |
| `--ink` | `#2E2C28` | on bg / card | 11.9:1 / 13.0:1 | Headings, body |
| `--muted` | `#6A655C` | on bg / card | 5.0:1 / 5.4:1 | Secondary text, captions (lightest permitted) |
| `--clay` | `#96614A` | off-white text | 5.1:1 | Primary buttons, accents |
| `--clay-deep` | `#85543F` | off-white text | 6.3:1 | Button hover |
| `--moss` | `#67714E` | off-white text | 5.2:1 | Confirmations, tags |
| `--line` | `#D9D0C0` | decorative | 1.5:1 | Hairlines and borders only, never text |
| `--charcoal` | `#3B3833` | bg text on it | 10.0:1 | Inverted footer, immersive panel |

- Forbidden: gray text lighter than `#6A655C`, white text on `--line` or `--bg`, blue links, neon accents of any kind.
- Dark adaptation: keep the beige; do not build a dark theme by inverting to charcoal ground unless every muted pair is re-measured (target: muted text ≥4.5:1 on the new ground).

---

## 2. Typography

### Families
- **Display:** a light-contrast serif or a refined geometric sans at 300-500 weight (Lora, Cormorant-class, or Inter/Work Sans at 400). Airy, not bold.
- **Text:** the same family at 400, or a quiet companion sans. Two families maximum.
- **Labels:** same sans, uppercase, `letter-spacing: 0.1em`, weight 500, `--muted` color.

### Scale
| Step | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| h1 | `clamp(2rem, 4.5vw, 3.25rem)` | 400-500 | 1.15 | Page titles |
| h2 | `1.375rem` | 500 | 1.3 | Section titles |
| h3 | `1.0625rem` | 600 | 1.4 | Card titles |
| body | `1.0625rem` (17px) | 400 | 1.75 | Paragraphs |
| small | `0.875rem` | 400 | 1.6 | Captions, metadata (muted only) |
| label | `0.75rem` | 500, uppercase, `0.1em` | 1 | Nav, forms, tags |

- Headlines never go bold-heavy; hierarchy comes from size and weight *lightness contrast* (400 vs 600), not from shouting.
- Body measure 60-72ch. Links: ink text with 1px underline in `--muted`; hover moves the underline to clay and thickens to 2px.

---

## 3. Spacing & density

- Scale: `8 / 16 / 24 / 40 / 64 / 96 / 128` - the most generous in the library. Sections breathe at 96-128px; cards pad 24px.
- Negative space is budgeted, not leftover: every view reserves at least one full void region (empty margin, quiet band) as a deliberate component.
- Density is low and uneven: one dense block (a menu, a list) earns its air with a wide void beside it.
- Lines and rules separate content instead of boxes; borders are the exception, not the rule.

---

## 4. Shapes, radii, borders

- Radius 2-4px on interactive components; images 4px or full-bleed edge-to-edge. No pills, no 16px bubbles.
- Borders: 1px `--line` on cards and inputs. The border *is* the container; shadows are not used to box content.
- Brush-like rules: full-width 1px `--line` horizontal rules separate sections; a single 2px charcoal rule may anchor the masthead.
- Asymmetric corners (one rounded corner on a panel) are acceptable as a signature, used once per view at most.

---

## 5. Lighting, shadows, materials

- Lighting is soft daylight: no hard shadows, no gloss. The one shadow token: `0 8px 24px rgba(46, 44, 40, 0.08)` for overlays and the single lifted element per view.
- Materials on screen: matte paper texture at 3-5% opacity on the ground (optional), linen and wood shown through photography, hairline metal rules.
- No gradients. A subtle vertical tone shift inside a hero image is photography, not a CSS gradient; CSS gradients are limited to the optional paper grain.
- Elevation is expressed by layer shift (beige to card) plus the hairline border - not by stacking shadows.

---

## 6. Imagery & iconography

- Photography carries the style: natural materials (linen, oak, stone, ceramic), matte finish, warm-neutral grading, soft daylight, honest imperfection (visible grain, slub, knot).
- Crops are asymmetric; subjects sit off-center with deliberate void. One hero image per view; thumbnails keep the same grading family.
- Illustration, if any: single-weight line drawings (1.5px) in charcoal, minimal, hand-drawn feeling. No flat vector mascots.
- Icons: 1.5px stroke, 20px grid, charcoal, used sparingly (10 or fewer per page). Emoji are never UI.
- All imagery gets descriptive alt text naming material and moment; decorative texture layers are `aria-hidden`.

---

## 7. Composition & alignment

- **Asymmetric balance:** weight compositions to one side - a 60/40 split with the mass left and the void right, then alternate down the page. Mirrored symmetric rows are the tell of a template.
- **One mass, one void, one line** per view: a content block, an empty region, a rule or image edge tying them.
- Left-aligned text; centered text only for short ceremonial moments (a single welcome line, a quote).
- Baseline alignment matters more than grid visibility: align first lines of text across columns.
- Vertical rhythm on the 8px scale; 96-128px between sections, 24-40px between related items.

---

## 8. Interaction states (complete matrix)

| Control | Default | Hover | Focus-visible | Active | Disabled |
|---|---|---|---|---|---|
| Primary button | Clay fill, off-white text | `#85543F` fill | `outline: 2px solid var(--ink); outline-offset: 3px` | `translateY(1px)`, fill `#7A4C39` | `#E5DFD3` fill, `#8B857A` text (3.3:1 decorative context) + `aria-disabled`, or removed from tab order |
| Ghost button | 1px `--line` border, ink text | Border `--ink`, bg `--card` | Same outline | bg `--line` | 1px `--line`, muted text, no hover |
| Nav link | Ink label voice | Clay text + underline | 2px ink outline | n/a | n/a |
| Current page | Clay text, 2px clay underline offset 6px | none | same | n/a | n/a |
| Card | Card fill, 1px `--line` | Border `--ink` (if clickable) | Inner link carries ring | n/a | n/a |
| Input | Card fill, 1px `--line`, ink text | Border `#B4AA97` | 2px charcoal bottom border + outline | n/a | `--bg` fill, muted text |
| Input error | 1px `#9B4A35` border + message `#8F3F2B` (6.0:1 on card) | n/a | unchanged | n/a | n/a |
| Checkbox/radio | 1px `--line`, card fill | border `--ink` | 2px ink outline | n/a | muted |
| Selected state | Moss fill, off-white text (tags, list rows) | none | outline | n/a | n/a |

- Disabled buttons: prefer removing the action over graying it; when disabled visually, keep `aria-disabled="true"` and an explanation nearby.
- Errors: warm rust `#8F3F2B` (6.0:1 on card) - it belongs to the palette while still reading as alert; never pure red.

---

## 9. Motion

- Timing: `220ms ease-out` default; page transitions may run 280ms. Nothing springs, bounces, or overshoots.
- Scope: opacity fades and transforms under 8px (rise, settle). No parallax, no scroll-triggered cascades beyond a single fade-in per section.
- Hover: background/border shifts and 1px lifts. The motion should feel like a breath, not a trick.
- Reduced-motion contract:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { transition-duration: 0ms; animation: none; }
    html { scroll-behavior: auto; }
  }
  ```

---

## 10. Responsive adaptation

- **Mobile (<768px):** single column; h1 clamps to 2rem; sections breathe at 64-96px; nav collapses to a full-screen quiet panel (beige, tracked links, hairlines) instead of a cramped bar.
- **Tablet (768-1024px):** asymmetric two-column layouts appear (60/40); imagery gains its margin void.
- **Desktop (>1024px):** full asymmetric grids, 128px section air, the single lifted card allowed.
- Images: explicit `width`/`height` or `aspect-ratio`; hero images crop (not stretch) via `object-fit: cover`.
- The void is the first casualty of small screens and the last thing to cut: shrink gaps proportionally (96 becomes 64) rather than removing air entirely.
