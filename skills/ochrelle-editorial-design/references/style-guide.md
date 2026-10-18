# Editorial Design - Style Guide

Complete design tokens and rules for editorial design. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **Paper first.** Ivory `#FAF7F0` ground, near-black ink. Pure white is for raised matter (cards, modals), pure black is too cold for long reading.
- **One accent, institutional.** Deep red `#8C1D1D` for kickers, links, and flags. If the brand has a real accent (navy, forest), swap it in - but keep exactly one.
- **Color never carries hierarchy alone.** Rank is type-driven; color only confirms it.

### Palette and verified contrast
| Token | Value | Pairing | Ratio | Role |
|---|---|---|---|---|
| `--bg` | `#FAF7F0` | ink text | 16.3:1 | Page ground |
| `--card` | `#FFFFFF` | ink text | 17.4:1 | Raised cards, modals |
| `--ink` | `#1A1A1A` | on bg | 16.3:1 | Headlines, body |
| `--muted` | `#565650` | on bg | 6.9:1 | Decks, captions, metadata |
| `--accent` | `#8C1D1D` | on bg | 8.5:1 | Links, kickers, small flags |
| `--accent` fill | `#8C1D1D` | white text | 9.1:1 | Solid buttons, badges |
| `--ink` fill | `#1A1A1A` | white text | 17.4:1 | Primary buttons |
| `--rule` | `#D6CFBF` | decorative | 1.4:1 | Hairlines only - never text |

- Muted `#565650` is the lightest permitted text color. Anything lighter fails long-form reading even when it technically passes AA.
- Inverted matter (photo credits over dark images): white text on a `rgba(26,26,26,0.6)` scrim minimum; measure the actual image.

---

## 2. Typography

### Families (three voices, no more)
- **Text voice:** serif for body - Georgia or a Source Serif/Lora-class webfont, 400 regular and 600 semibold, true italics for emphasis.
- **Display voice:** the headline face - can be the same serif at heavy weight or a contrast display serif; `clamp(2.25rem, 5vw, 3.75rem)` for h1.
- **Label voice:** one grotesque sans (Helvetica/Arial class) for kickers, folios, buttons, captions metadata - always uppercase, tracked.

### Scale
| Step | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| h1 headline | `clamp(2.25rem, 5vw, 3.75rem)` | 700 | 1.08 | Article titles |
| h2 crosshead | `1.5rem` | 700 | 1.2 | In-body section breaks |
| h3 | `1.125rem` | 600 | 1.3 | Card titles |
| deck | `1.25rem` | 400 | 1.5 | Standfirst, muted, 45-55ch |
| body | `1.125rem` | 400 | 1.7 | Article text |
| caption | `0.8125rem` | 400 | 1.45 | Figure captions, credits |
| kicker/label | `0.8125rem` | 600, caps, `0.12em` | 1 | Kickers, folios, buttons |

- Headlines may tighten to `-0.01em`; labels loosen to `0.12em`. Body never tracks or compresses.
- Measure: body 60-75ch, decks and captions 45-55ch, pull quotes 45ch max.
- Links: underlined 1px with `text-underline-offset: 0.12em`; hover goes 2px accent. Body links take the accent color.

---

## 3. Spacing & density

- Baseline rhythm on a 4px unit; body paragraphs separated by one blank line (`1.5rem`), never indented on web.
- Article column: `max-width: 68ch`, centered, with a wider outer margin column (20-30% of viewport) that hosts pull quotes, footnotes, and marginalia on desktop.
- Sections separated by `4rem`; hairline rules may mark section starts.
- Density is uneven by design: dense text columns against generous margin air. Do not pad the body column to fake luxury.
- Folio line (section name - page marker) sits in the top or bottom margin, not in the content flow.

---

## 4. Shapes, radii, borders

- Radius 0 everywhere. Rounded corners read as app chrome, not publication.
- Hairlines: `1px solid var(--rule)` between related items (article cards, figure from caption); `2px solid var(--ink)` under the masthead and above the footer.
- Pull quotes and asides get top+bottom hairlines, no side borders, no background fill.
- Buttons are rectangles: 1px border, or solid fill with no border. No pills, no chips with radius.

---

## 5. Lighting, shadows, materials

- The page is flat paper. No shadows on cards, nav, or figures.
- One exception: modal overlays and popovers may use `0 8px 24px rgba(26, 26, 26, 0.12)`.
- Photography is the material event: full-width figures, honest color or duotone, 2px ink border only when the image sits on the ivory ground and needs an edge.
- No gradients, no glass, no translucency except the photo scrim noted in section 1.

---

## 6. Imagery & iconography

- Every image is a `figure` with a `figcaption`: caption sentence (65-90 characters) plus credit in the label voice (`PHOTOGRAPH: NAME/AGENCY`).
- Portrait orientation belongs in the margin column at ~300px; landscape takes the full grid width.
- Iconography is nearly absent: use typographic marks (arrows, section signs, asterisks, bullets) before icon fonts. If icons are required, 1.5px stroke, ink color, 20px grid.
- Charts follow print conventions: hairline axes, direct labels, muted fills, one accent for the data series that matters.

---

## 7. Composition & alignment

- **Asymmetric grid:** 12-column print grid; body text spans columns 2-9, margin notes live in 10-12. Symmetrical centered layouts are reserved for the masthead and section fronts.
- **Left-aligned everything** in text columns; the masthead wordmark may center.
- **Ragged right, never justified** on web (hyphenation control is unreliable; rivers destroy long-form reading).
- **One dominant element per screen:** the headline on article pages, the lead photo on section fronts. Everything else yields.
- Scale jumps: headline 60px vs body 18px is correct contrast, not excess.

---

## 8. Interaction states (complete matrix)

| Control | Default | Hover | Focus-visible | Active | Disabled |
|---|---|---|---|---|---|
| Body link | Ink text, 1px underline | Accent text, 2px underline | `outline: 2px solid var(--accent); outline-offset: 3px` | Same as hover | n/a |
| Primary button | Solid ink fill, white label | Accent fill | 2px accent outline | Background darkens `#101010` | `#B9B4A6` fill, `#565650` text (4.6:1), no hover |
| Secondary button | 1px ink border, ink label | 2px border + light fill `#F1EBDD` | Same outline | Inverts to ink fill, white text | As above |
| Nav link | Label voice, ink | Accent underline 2px | Same outline | n/a | n/a |
| Current section | Accent text + 2px accent underline | none | same | n/a | n/a |
| Card (article teaser) | White card, 1px rule, kicker+headline+deck | Headline underlines, card border darkens to ink | Card link carries outline | n/a | n/a |
| Input | White fill, 1px `#B9B4A6` border, underline-style label | Border `#565650` | 2px accent outline, border accent | n/a | `#F1EBDD` fill, muted text |
| Input error | 1px accent border + message (accent red text, 8.5:1) | n/a | unchanged | n/a | n/a |
| Pagination | Label voice, ink numerals | Accent underline | outline | n/a | current page: solid accent block, white numeral |

- Current-page markers always pair color with position or weight (bold, underline) - never color alone.
- Form labels stay visible; placeholder text is never the only label.

---

## 9. Motion

- Default `160ms ease-out`. Nothing exceeds 250ms.
- Allowed: underline weight change, background swap on buttons, sticky masthead border appearing on scroll.
- Discouraged: parallax, scroll-triggered fades, carousel animations. If a figure must reveal, it fades once at `200ms` and never replays.
- Reduced-motion contract:
  ```css
  @media (prefers-reduced-motion: reduce) {
    * { transition-duration: 0ms; animation: none; }
    html { scroll-behavior: auto; }
  }
  ```

---

## 10. Responsive adaptation

- **Mobile (<768px):** single column; margin notes and pull quotes fold into the text flow between paragraphs; headline clamps to 2.25rem; masthead compresses to wordmark plus menu button; measure holds 60-75ch because it is ch-based.
- **Tablet (768-1024px):** body spans 8 of 10 columns; pull quotes gain the margin; section fronts show 2-column card grids.
- **Desktop (>1024px):** full asymmetric grid with margin column; 3-column teaser grids; folio line appears.
- Figures: explicit `width`/`height` or `aspect-ratio` always - reflowing longform must not jump.
- Typography is the responsive system: sizes clamp, the measure constant holds, and the grid bends around it.
