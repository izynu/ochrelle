# Art Deco - Style Guide

Complete design tokens and rules for Art Deco. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **Ivory ground, ink structure, gold line.** The page is a deco facade: light limestone ground, near-black joinery, brass drawn as line.
- **Gold is metal, not light.** Flat `#D4AF37` for rules and small fills on dark grounds; deepened `#7E5E10` when gold must be text on ivory. No gradients, no shine.
- **Two jewel tones per view.** Emerald, midnight, and oxblood are the panel palette; pick at most two per screen.

### Palette and verified contrast
| Token | Value | Pairing | Ratio | Role |
|---|---|---|---|---|
| `--bg` | `#F2EBDA` | ink text | 14.1:1 | Page ground |
| `--card` | `#FBF7EC` | ink text | 15.7:1 | Panels |
| `--ink` | `#211D16` | on bg / card | 14.1:1 / 15.7:1 | Text, frames |
| `--muted` | `#6E6353` | on bg / card | 5.0:1 / 5.5:1 | Secondary text (lightest permitted) |
| `--gold-line` | `#D4AF37` | on ink / midnight | 8.0:1 / 6.8:1 | Rules, ornament, text on dark only |
| `--gold-text` | `#7E5E10` | on ivory | 5.1:1 | Small gold text on light grounds |
| `--emerald` | `#1D5C4D` | ivory text | 7.3:1 | Panels, secondary buttons |
| `--midnight` | `#1F2A44` | ivory text / gold | 13.3:1 / 6.8:1 | Primary buttons, footer |
| `--oxblood` | `#6B2230` | ivory text | 10.3:1 | Alerts-as-panels, emphasis bands |
| `--champagne` | `#E2D3A8` | ink text | 11.3:1 | Bands, badges, hovers |

- Forbidden: metallic gold text on ivory (3.0:1), white text on gold, muted text on jewel panels (below 4.5:1 - use ivory), pure white and pure black (breaks the warm ledger).
- Dark variant: invert to `--bg: #17150F` with `#F2EBDA` text (13:1) and gold lines unchanged; re-measure jewel panels before shipping.

---

## 2. Typography

### Families
- **Display (one only):** a geometric marquee face of the Broadway/Limelight class - tall, stepped, unapologetic. Uppercase by default.
- **Text:** a geometric sans (Josefin Sans, Futura class) for body and UI; 400-600 weight.
- **Labels:** same sans, uppercase, `letter-spacing: 0.18em`, weight 600.

### Scale
| Step | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| display | `clamp(2.25rem, 5vw, 4rem)` | 400 (display faces are naturally heavy) | 1.1 | Page titles, hero words |
| h2 | `1.5rem` | 600 | 1.25 | Section titles (text face, tracked) |
| h3 | `1.0625rem` | 600 | 1.35 | Card titles |
| body | `1rem` (16px floor) | 400 | 1.7 | Paragraphs |
| small | `0.875rem` | 400 | 1.5 | Captions, credits (muted only) |
| label | `0.75rem` | 600, uppercase, `0.18em` | 1 | Nav, buttons, kickers |

- Display never sits on patterned bands; it sits on flat ivory, midnight, or emerald.
- Measure 60-75ch. Links: ink text, 1px underline offset `0.15em`; hover moves the underline to `--gold-text` and thickens to 2px.

---

## 3. Spacing & density

- Scale: `8 / 16 / 24 / 40 / 64 / 96`. Symmetry extends to spacing: left and right gutters are always equal.
- Sections breathe at 64-96px vertically; ornament bands get 24px clear space above and below.
- Density is moderate and even - deco pages read like a titled facade: masthead, band, content block, band, footer.
- Content blocks are centered with equal side air (max-width plus auto margins); internal text is left-aligned inside its frame.

---

## 4. Shapes, radii, borders

- **Radius 0 everywhere.** A deco curve is a constructed arc (fan, arch, quarter-round panel), not a `border-radius`.
- **Double hairline frame** is the signature container: 1px ink border, 3-4px ground gap, 1px ink or gold outer line (built with `border` + `box-shadow: 0 0 0 Npx var(--card), 0 0 0 N+1px var(--ink)`).
- **Stepped corners:** ziggurat stacks of 2-3 rectangles in gold or ink, built from layered `linear-gradient` strips; used on one corner per card at most.
- Chevron and sunburst bands: `repeating-conic-gradient` fans and zigzag strips, gold or ink on champagne, 16-48px tall, `aria-hidden`.

---

## 5. Lighting, shadows, materials

- Flat and drawn, not lit. Page elements carry no shadows; elevation is expressed by frames, ground shifts (ivory to card), and gold edges.
- Materials: polished brass, lacquer, marble, velvet. Simulate with flat color and hairline edges; never with gradients, gloss, or `backdrop-filter`.
- One exception: modal overlays may use `0 24px 48px rgba(33, 29, 22, 0.25)`.
- Gold leaf moments (a thin gold rule inside a jewel panel) are the maximum "shine" permitted.

---

## 6. Imagery & iconography

- Photography: architectural and object photography, warm-graded, symmetric crops, framed by the double hairline. Subjects centered like portraits.
- Illustration: flat geometric shapes in the palette with ink edges - fans, arcs, gazelle-class deco silhouettes. No 3D, no soft gradients.
- Icons: geometric, 1.5px stroke or solid minimal glyphs (stars, fans, keys, glasses); set in gold on dark, ink on light.
- Ornament layers are `aria-hidden` and never carry text; they occupy dedicated bands, frames, and corners.

---

## 7. Composition & alignment

- **Center axis:** the page is composed on a vertical center line - masthead, ornament, title block, columns mirrored around it.
- **Framed blocks:** every content unit sits inside a double hairline or stepped frame; unframed text floats look unfinished.
- **Hierarchy by elevation:** title block tallest (display face), then jewel band, then framed content. Deco hierarchy is architectural, not subtle.
- Body text left-aligned inside frames; headings centered above them.
- One sunburst per view, one stepped corner per card, one jewel emphasis band per section - repetition is rhythm, overuse is noise.

---

## 8. Interaction states (complete matrix)

| Control | Default | Hover | Focus-visible | Active | Disabled |
|---|---|---|---|---|---|
| Primary button | Midnight fill, ivory label, gold inset frame | Emerald fill | `outline: 2px solid var(--ink); outline-offset: 3px` (flips to `#FBF7EC` on dark panels) | Oxblood fill | `#E7E0CD` fill, `#6E6353` text (5.5:1), frame stays, `not-allowed` |
| Secondary button | Card fill, ink label, 1px ink + gold frame | Champagne fill | Same outline | Ink inverts to fill, ivory text | As above |
| Nav link | Tracked uppercase, ink | Gold underline 2px (`--gold-text`) | 2px ink outline | n/a | n/a |
| Current page | Gold underline 2px + diamond marker (rotated square) | none | same | n/a | n/a |
| Card link | Frame holds; title underlines | Outer frame line turns gold | Inner link carries ring | n/a | n/a |
| Input | Card fill, 1px ink bottom border | Border `#211D16` full | 2px gold bottom line + ink outline | n/a | `--bg` fill, muted text |
| Input error | 1px oxblood border + ivory-text message on oxblood chip (10.3:1) | n/a | unchanged | n/a | n/a |
| Tab (programme) | Card fill, ink label, 1px frame | Champagne fill | 2px outline | n/a | n/a |
| Selected tab | Midnight fill, gold label, frame holds | none | same | n/a | n/a |

- Errors pair the oxblood chip with `aria-invalid` + inline text; never color-only.
- Current-page markers always pair gold underline with weight or a geometric marker.

---

## 9. Motion

- Timing: `180ms ease-out` standard; overlays 220ms. Nothing springs, bounces, or fades slowly.
- Scope: background swaps, border-color steps, small 2px lifts. Color changes are instant steps - the deco click.
- Signature move: the "step" - hover shifts a frame's outer gold line from 5px to 6px offset, one deliberate click of the machinery.
- Ornament animation (a fan sweeping open) is allowed once on load, 400ms, and only under `prefers-reduced-motion: no-preference`.
- Reduced-motion contract:
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { transition-duration: 0ms; animation: none; }
    html { scroll-behavior: auto; }
  }
  ```

---

## 10. Responsive adaptation

- **Mobile (<768px):** display clamps to 2.25rem; frames keep their double lines but drop stepped corners to one; gutters compress symmetrically (16px); nav becomes a centered stacked list with sunburst divider between masthead and links.
- **Tablet (768-1024px):** two-column framed blocks appear, still mirror-balanced; jewel bands widen.
- **Desktop (>1024px):** full facade - centered masthead, framed columns with a clear center axis, footer as a midnight band with gold rules.
- Ornament bands shrink in height (48 to 24px) rather than disappearing; the rhythm must survive.
- Images keep explicit dimensions; symmetric layouts shift visibly when one framed image loads late.
- Tap targets ≥44px; squared buttons pad generously so the geometry never erodes the hit area.
