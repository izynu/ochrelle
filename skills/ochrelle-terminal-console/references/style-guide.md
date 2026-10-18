# Terminal Console - Style Guide

Complete design tokens and rules for Terminal Console. Follows the SKILL.md definition.

---

## 1. Color

### Principles
- **One phosphor hue per product.** Pick green or amber for the session. Status colors (`warn`, `error`) are fixed guests, never a second theme.
- **Brightness = hierarchy.** Bright for active/labels, mid for body, dim for secondary. Do not invent a fourth level.
- **Borders are tonal, not colored.** Functional borders pass 3:1 (WCAG 1.4.11); hairlines are decoration only and never carry meaning.

### Green phosphor theme (default)
| Token | Value | Contrast vs `--bg` | Use |
|---|---|---|---|
| `--bg` | `#0A0F0A` | - | Page ground |
| `--panel` | `#101812` | ink 13.7:1 on it | Pane fill |
| `--select` | `#1C2E22` | bright 10.7:1 on it | Selected rows |
| `--ink` | `#A8F0BC` | 14.6:1 | Body text |
| `--bright` | `#33FF77` | 14.5:1 | Labels, active, caret |
| `--dim` | `#6FA57E` | 6.8:1 | Secondary text, timestamps |
| `--line` | `#4A7D58` | 4.0:1 | Functional borders |
| `--hairline` | `#1F3526` | decorative | Frame joints, rules |
| `--warn` | `#FFB454` | 11.0:1 | Warnings |
| `--error` | `#FF6B66` | 7.0:1 | Errors, `[fail]` tags |

### Amber phosphor theme (alternate)
| Token | Value | Contrast vs bg `#140D04` | Use |
|---|---|---|---|
| `--ink` | `#FFD9A0` | 14.4:1 | Body text |
| `--bright` | `#FFB454` | 10.9:1 | Labels, active |
| `--dim` | `#B08657` | 5.9:1 | Secondary text |
| `--error` | `#FF6B66` | 6.5:1 on `#0C1626`-class darks | Errors (keep text tags alongside) |

Rule: never mix the two themes. If the brand demands both, they live in different products, not different panes.

---

## 2. Typography

- **Family:** one monospace stack everywhere: `ui-monospace, "SF Mono", Menlo, Consolas, "DejaVu Sans Mono", monospace`. Optional second family (a plain sans) only for long prose paragraphs, and only if the product has them.
- **Scale:**

| Step | Size | Weight | Use |
|---|---|---|---|
| display | `clamp(1.75rem, 4vw, 2.75rem)` | 700 | Hero command-line statements |
| h1 | `1.5rem` (24px) | 700 | Pane titles on landing |
| h2 | `1.25rem` (20px) | 700 | Section labels |
| body | `1rem` (16px) | 400 | Paragraphs, logs (floor: never below 16px) |
| label | `0.8125rem` (13px) | 500, uppercase, `0.08em` tracking | Pane title bars, tags, nav |
| micro | `0.75rem` (12px) | 400 | Timestamps only, in `--dim`, never body |

- Line-height: 1.5 body, 1.2 labels. No italics (CRTs did not slant); emphasis = `--bright` or inverse video.
- Widths in `ch`: measure column layouts with `ch` units (e.g. 80ch max text width) so alignment survives font swaps.
- Links: always prefixed or decorated beyond color - underline + `→` glyph, or inverse on hover.

---

## 3. Spacing & density

- Base unit: 4px. Scale: 4 / 8 / 12 / 16 / 24 / 32 / 48.
- Pane internal padding: 12-16px. Pane gaps: 16px (dashboard panes sit flush-ish; density is the point).
- Status bar height: 28-32px. Pane title bars: 26-30px.
- Log rows: 24px tall (single line + 4px breathing); do not let rows wrap into ragged heights - truncate with `…` and expand on focus.
- Max text measure: 80ch (the terminal heritage width), hard cap for paragraphs.

---

## 4. Shapes, radii, borders

- Radius: 0-2px. A rounded terminal pane is a broken metaphor.
- Borders: 1px solid. `--line` for anything that marks an interactive boundary or pane edge; `--hairline` for internal rules, title-bar dividers, zebra hints.
- Box-drawing frames are the signature. Two legal idioms:
  - CSS borders on a real element (recommended: screen readers see real structure).
  - Literal box-drawing characters (`┌ ─ ┐ │ └ ┘`) only inside `<pre>`-like content blocks, never as layout scaffolding.
- Corner glyphs: a `+` or `·` may punctuate frame joints via positioned pseudo-elements; they are decorative and `aria-hidden`.
- No drop shadows. Depth is expressed by tone steps (`--bg` → `--panel` → `--select`).

---

## 5. Lighting, shadows, materials

- Materials: dark glass-less matte. No gradients, no glass, no inner light.
- Glow: allowed only as decoration - `box-shadow: 0 0 12px rgba(51, 255, 119, 0.15)` on a pane edge or the caret block. Never on text. The plain text color must pass 4.5:1 with the glow layer removed.
- Scanlines: if the brand insists, one repeating-linear-gradient overlay at ≤4% opacity on non-text decorative regions only, disabled under reduced motion and `forced-colors`.
- Cursor: a block caret in `--bright`; blink with `steps(1)` at 1s, paused under reduced motion.

---

## 6. Imagery & iconography

- **No photography.** If a screenshot must appear, frame it in a pane with a title bar like any other output region.
- Icons: Unicode/ASCII first - `▸ ▾ ● ○ ✓ ✗ ⚠ → ↑ ↓` - or a mono-weight stroke icon set at 1.5px matching hairlines. Icon-only controls need visible text labels (console convention).
- Charts: block-character sparklines (`▁▂▃▅▇`) and `<pre>` ASCII bar charts are idiomatic; give each chart an accessible table or `aria-label` with the actual values.
- Severity tags are text: `[ok]`, `[warn]`, `[fail]`. Color may reinforce but never carry alone.

---

## 7. Composition & alignment

- **Cell grid:** columns align to the monospace rhythm. Tables and key-value lists align on `ch` columns; pad with spaces inside `<pre>`, with `grid-template-columns` in `ch` elsewhere.
- **Tiling layout:** panes tile like tmux - a dominant pane (log/output) plus 1-3 auxiliary panes (stats, controls). Fixed gutters, no free-floating cards.
- **Status line:** persistent bottom (or top) bar: session/brand left, current context center, clock/status right. It is the product's anchor; never let a page scroll it away on desktop.
- **Alignment:** everything flush-left. Centered text is banned except a single ASCII-art masthead, which must be inside a `<pre role="img" aria-label="...">`.
- Density is a feature: an empty console page is a failed console page, but density must stay aligned, not crowded.

---

## 8. Interaction states (complete matrix)

Signature control (`.btn`) - every interactive component must define all of these:

| State | Visual | Notes |
|---|---|---|
| default | `--panel` bg (or transparent), `--ink` text, 1px `--line` border, `[ ]` brackets in `--dim` | Brackets are decorative; keep real text labels. |
| hover | inverse video: `background: var(--ink); color: var(--bg)`, 0ms | Hover never the only state channel. |
| active/pressed | brighter inverse: `background: var(--bright); color: var(--bg)`, instant | No easing; machines do not ease. |
| focus-visible | `outline: 2px solid var(--bright); outline-offset: 2px` (flips to `--bg` when on bright fill) | Never suppressed. |
| disabled | `--dim` text on `--bg`, `--hairline` border, `not-allowed` cursor, brackets removed | Contrast of `#6FA57E` still 6.8:1. |
| selected (list rows/tabs) | persistent inverse video or `--select` bg with `--bright` text + `▸` marker | Also mirrored in `aria-current`/`aria-selected`. |
| loading | label swaps to `LOADING` + frames `⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏` at 100ms; width locked | Use `aria-busy="true"`. |
| error (inputs) | 1px `--error` border + `[!] message` line in `--error` (7.0:1) | Message text, not color alone. |

Menu items and tabs reuse hover/selected rows. Links: underline + `→`, hover = inverse or brighten to `--bright`.

---

## 9. Motion

- **Durations:** state changes 0ms (hover/active/focus instant); allow 80ms linear maximum if a product-wide fade is unavoidable.
- **Legal animations only:** cursor blink (`steps(1)`, 1s), spinner frames (100ms/step, `steps(10)` on a keyframe list), streaming text reveal for log lines (translateY 8px, 80ms), progress bars (width in `ch`).
- **Banned:** flicker filters, CRT curvature distortions on scroll, glow pulsing on text, parallax of any kind.
- Reduced motion contract:

```css
@media (prefers-reduced-motion: reduce) {
  .caret { animation: none; }
  .spinner { animation: none; }
  .log-line { transition: none; }
}
```

- Streaming logs: batch DOM insertions at most every 250ms; new rows get no animation when reduced motion is set.

---

## 10. Responsive adaptation

- **Mobile (<768px):** panes stack in reading order (status first, primary output, controls last); body stays 16px; status bar becomes a wrapping two-row bar; wide log lines scroll horizontally *inside* the pane with `overflow-x: auto` - never widen the page.
- **Touch:** targets ≥44x44px; inverse-video hover states double as touch feedback on `:active`; brackets enlarge to 12px padding for tap comfort.
- **Tablet (768-1024px):** two-pane splits (output + controls); status bar single row.
- **Desktop (>1024px):** full tiling, 80ch measures, keyboard shortcut hints visible in panes.
- Test with browser zoom 200%: panes must reflow, not clip; `ch`-based columns may scroll within their pane but the document never scrolls sideways.
