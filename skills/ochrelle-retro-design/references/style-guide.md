# Retro Design - Style Guide

Complete design tokens and rules for retro mid-century Americana and 1970s warmth. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **Spot color, not atmosphere.** Colors behave like silkscreen inks: flat regions with crisp edges. No gradients, no translucency except the single letterpress shadow token.
- **Warm ground always.** The cream `#F7EFD9` ground is the style's signature. Pure white pages break the period read; keep `#FFFDF5` for raised paper panels only.
- **Brown, not black.** Ink is `#3D2B1F`. Pure `#000000` reads cold and modern against this palette.

### Palette and verified contrast
| Token | Value | Pairing | Ratio | Role |
|---|---|---|---|---|
| `--bg` | `#F7EFD9` | ink text | 11.7:1 | Page ground |
| `--paper` | `#FFFDF5` | ink text | 13.2:1 | Cards, panels |
| `--ink` | `#3D2B1F` | on cream | 11.7:1 | Body text, borders, outlines |
| `--muted` | `#6B5138` | on cream | 6.4:1 | Secondary text, captions |
| `--accent` | `#AD4E1A` burnt orange | cream text | 5.4:1 | Primary buttons, bursts, links on paper |
| `--mustard` | `#D9A404` | ink text | 5.9:1 | Starburst fills, highlight bands |
| `--avocado` | `#6B7C33` | cream text | 4.6:1 | Section fills, secondary buttons |
| `--cherry` | `#A32E2E` | cream text | 7.0:1 | Sale flags, error accents, badges |

### Forbidden pairings (measured, not guessed)
- White or cream text on mustard: about 1.9:1 - never.
- Brown ink text on burnt orange: about 2.5:1 - never.
- Brown ink text on avocado or cherry: below 3:1 - never.

Rule of thumb: **light text on dark-warm fills (orange, avocado, cherry, ink); dark text on light-warm fills (cream, paper, mustard).** Four saturated fills is the ceiling; a fifth destroys the era.

---

## 2. Typography

### Families
- **Display (one only):** a groovy rounded or heavy warm face - Cooper Black-class shapes (rounded terminals, low contrast, snug apertures). Load 700-800 weight, subset, `font-display: swap`.
- **Text:** a sturdy humanist sans or warm slab (system stack is acceptable: `system-ui, -apple-system, "Segoe UI", sans-serif`). Never a second display face.
- **Labels:** same text face, uppercase, `letter-spacing: 0.08em`, weight 600.

### Scale
| Step | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| display | `clamp(2.5rem, 6vw, 4.5rem)` | 700-800 | 1.02 | Hero words, section posters |
| h2 | `2rem` | 700 | 1.15 | Section titles |
| h3 | `1.375rem` | 700 | 1.25 | Card titles |
| body | `1rem` (16px floor) | 400 | 1.6 | Paragraphs |
| small | `0.875rem` | 400 | 1.45 | Captions, footnotes (muted token only) |
| label | `0.8125rem` | 600, uppercase, 0.08em | 1.2 | Kickers, prices, menu heads |

- Display may tighten tracking to `-0.01em`; labels go the other way. Body text never uses the display face - it fails at 16px.

---

## 3. Spacing & density

- Scale: `4 / 8 / 16 / 24 / 40 / 64 / 96` (`--s1` to `--s7`). No arbitrary values.
- Menu-board rhythm: rows are tight inside (8-12px between line items) and generous between groups (24-40px). Dotted leaders join name to price.
- Page gutter: 24px mobile, 40px desktop. Section padding: 40px mobile, 64-96px desktop.
- Whitespace is warm but structured: it groups menu sections, it does not float lone sentences in emptiness.

---

## 4. Shapes, radii, borders

- Radii: `10px` panels and inputs, `999px` pills and ovals, badges follow their shape (oval, shield, burst). One size per component class - no mixed corner radii inside a component.
- Borders: `2px solid var(--ink)` on cards, inputs, and buttons. They draw the "printed" edge; shadows never replace them.
- Dotted rules (`border-bottom: 2px dotted var(--muted)`) are the signature join for name-price rows and table-of-contents lines.
- Corner flourishes (scallops, ticket notches) are allowed on decorative bands only - never on interactive components, where they erode target size.

---

## 5. Lighting, shadows, materials

- One shadow token: `0 3px 0 rgba(61, 43, 31, 0.35)` - a letterpress slab. Pressed state shrinks it to `0 1px 0`.
- Optional soft ambient for modals only: `0 12px 32px rgba(61, 43, 31, 0.18)`. Nowhere else; blur never appears inside normal components.
- Materials: coated paper, enamel, formica, neon. Simulate with flat color and 2px edges; never with gradient "shines" except a single subtle top highlight on badge fills if desired (`linear-gradient(#FFFDF5 at 20% opacity, transparent)` on non-text regions).
- Halftone screens: `radial-gradient` dot grids at 6-10px pitch, decorative only, in ink at 25-40% alpha or in a fill color at full strength on non-text areas.

---

## 6. Imagery & iconography

- Photography: real, warm-graded (slightly lifted reds/yellows), matte finish. Frames: 2px ink border, 10px radius, optional paper "polaroid" mat.
- Illustration: flat spot-color shapes with 2px brown outlines, period subject matter (cars, record players, coffee pots). No 3D renders, no soft plastic gradients.
- Halftone treatment on photos is a deliberate poster effect - use on hero art, never on functional thumbnails.
- Icons: 2px stroke or chunky filled glyphs matching border weight (arrows, mugs, records, stars). Emoji are not icons.

---

## 7. Composition & alignment

- **Menu-board logic.** Content is organized into named blocks with uppercase tracked headers, ruled or dotted joins, and price-aligned columns. The page reads like a laminated menu, top to bottom.
- **One burst per viewport.** Starbursts and seals mark the single most important claim (today's special, primary CTA, rating). Two competing bursts equal zero.
- **Badges pin corners:** offset outside the card edge by 8-16px, rotated -4deg to 4deg, always with their 2px ink outline.
- Alignment: left-aligned text is the default; centered type belongs to hero posters and badge labels only.
- Scale jumps: display sits far above body (72px vs 16px is normal). Hierarchy is loud here - that is period-correct.

---

## 8. Interaction states (complete matrix)

| Control | Default | Hover | Focus-visible | Active/pressed | Disabled |
|---|---|---|---|---|---|
| Primary button | Burnt orange fill, cream text, 2px ink border, `0 3px 0` slab | Lifts 2px, slab grows to `0 5px 0` | `outline: 3px solid var(--ink); outline-offset: 3px` | Presses down: `translateY(1px)`, slab `0 1px 0` | Solid `#E7DFC8` fill, `--muted` text (5.2:1), no slab, `cursor: not-allowed` |
| Secondary button | Paper fill, ink text, 2px border | Mustard tint fill `#F3E3B2` | Same 3px outline | Same press | As above |
| Nav link | Tracked uppercase, ink | Underline 2px in accent | 3px outline | Underline thickens | n/a |
| Current page | Underline 2px solid accent + dot marker | none | same | n/a | n/a |
| Card | Paper, 2px border, radius 10px | Lifts 2px with slab | Card CTA carries focus | CTA presses | Cards are not focusable as wholes |
| Input | Cream fill, 2px ink border, 10px radius | Border darkens to `#2A1C11` | 3px outline; border 3px | n/a | `#E7DFC8` fill, muted text |
| Input error | 2px cherry border + message below | n/a | outline unchanged | n/a | n/a |
| Link (body) | Underline 2px dotted accent, ink text | Solid underline | 3px outline | n/a | n/a |

- Error text: `#8F2424` on cream (about 6:1) with the cherry border; never color-only - include a text message and `aria-invalid`.
- Selected/filter chips: mustard fill with ink text and 2px border; unselected are paper with border.

---

## 9. Motion

- Timing: `180ms ease-out` is the default; modals may use `220ms`. Nothing exceeds 250ms - period interfaces snap.
- Property scope: `transform` (lifts, presses) and `box-shadow` (slab) only. Colors change instantly; fading fills look modern, not retro.
- Signature moves: button letterpress press; starburst rotates 8deg on hover; marquee "specials" ticker allowed at 60-90s per loop, paused on hover and `:focus-within`.
- Reduced-motion contract:
  ```css
  @media (prefers-reduced-motion: reduce) {
    .btn-retro, .card-retro { transition: none; }
    .btn-retro:hover, .card-retro:hover { transform: none; }
    .starburst:hover { transform: none; }
    .ticker__track { animation: none; }
  }
  ```

---

## 10. Responsive adaptation

- **Mobile (<768px):** single column menu-board; display clamps to 2.5rem; badge pins shrink to 64px; page gutter 24px; nav collapses to a stacked menu-board list (tracked uppercase rows with dotted leaders) rather than a hamburger.
- **Tablet (768-1024px):** two-column menu sections; burst may accompany the hero only.
- **Desktop (>1024px):** full menu-board with 2-3 columns, larger badges, decorative halftone bands between sections.
- Images carry explicit `width`/`height` or `aspect-ratio` - poster-style layouts jump visibly when art loads late.
- Tap targets: 44px minimum height on all menu rows made interactive and on every pill button.
