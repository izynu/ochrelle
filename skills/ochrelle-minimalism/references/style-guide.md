# Minimalism - Style Guide

Full art direction for Swiss-grounded minimalism.

---

## 1. Color

### Palette architecture
| Token | Light | Dark (optional) | Role |
|---|---|---|---|
| `--bg` | `#FFFFFF` or `#FAFAF7` (warm) | `#0E0F11` | Ground |
| `--surface` | `#FFFFFF` on warm bg; `#F7F7F5` for alternate zones | `#17181B` | Cards, wells |
| `--ink` | `#111111` | `#F4F4F5` | Primary text |
| `--muted` | `#5F6368` (6.0:1) | `#A1A1AA` (7.5:1) | Secondary text - the *floor* is `#767676` (4.54:1), not darker |
| `--line` | `#E5E7EB` | `#2A2C31` | Hairlines, borders, dividers |
| `--accent` | **one** color, e.g. `#2563EB` (5.2:1 as text on white - passes AA normal; 3:1+ as UI boundary) | lighten one step for dark | Primary action, active state, focus |

### Rules
- **Accent budget:** the accent appears at most ~3 times per viewport (one primary button, one active state, one focus ring). If a link, icon, badge, and chart all share the accent, the hierarchy is broken.
- **Semantic colors** (success `#0F766E`, warning `#92400E`, error `#B91C1C`) exist only for status, are used sparingly, and always pair color with an icon or text label (never color alone).
- **No gradients.** Flat fills and hairlines only. A single very-low-alpha shadow is the ceiling of atmosphere.

---

## 2. Typography

### Family
One sans-serif family. Grid-era heritage (Helvetica/Neue Haas) or contemporary equivalents (Inter, IBM Plex Sans, Public Sans, Source Sans 3). Host locally, ship 400 + 600 (add 700 only for a single display use). Tabular lining figures (`font-variant-numeric: tabular-nums`) for tables and data.

### Scale (modular, ~1.333 steps with px floors)
| Step | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| display | `clamp(2.5rem, 6vw, 4rem)` (40–64px) | 600–700 | 1.1 | Hero/page title (one per page) |
| h1 | `2rem` (32px) | 600 | 1.2 | Major section |
| h2 | `1.5rem` (24px) | 600 | 1.25 | Card/section title |
| h3 | `1.25rem` (20px) | 600 | 1.3 | Sub-block |
| body-lg | `1.125rem` (18px) | 400 | 1.6 | Lede paragraphs |
| body | `1rem` (16px) | 400 | 1.6 | Everything default |
| small | `0.875rem` (14px) | 400 | 1.45 | Meta/captions - minimum size, muted token only |
| overline | `0.75rem` (12px), 500, `+0.08em` tracking, uppercase | 500 | 1.2 | Labels above content, not body text |

### Setting rules
- **Flush-left, ragged-right** everywhere (the Swiss default). No justified text, no centered paragraphs - centered is allowed only for a single hero statement or empty-state.
- Hierarchy steps should be unmistakable: adjacent steps differ by ≥1.25× in size or a full weight class. If two levels look alike, delete one.
- `letter-spacing` slightly negative (−0.01em) at display sizes, 0 at body.

---

## 3. Spacing & density

- Scale: **8 / 16 / 24 / 48 / 96** (`--s1…--s5`). Optional 4px half-step for icon-text gaps only.
- **Proximity law:** space between related elements < space between unrelated elements. Intra-component gaps: 8–16. Component-to-component: 24. Section-to-section: 48. Page/hero rhythm: 96.
- Whitespace is *assigned*, not leftover: every gap should be traceable to a scale token. If you need 32, use 24 or 48 - the scale only works when it's consistent.
- **Density tiers by product surface:** dashboards/tools use compact rows (40px rows, 8px cell padding); marketing/docs use the full rhythm. Declare your tier once.
- Prose measure `60–68ch`; content column max-width `~1040px`; 12-column grid with 24px gutters for composed layouts.

---

## 4. Shapes, radii, borders

- Radius: `4–8px` on interactive surfaces, one value (e.g. `--radius: 6px`), plus `999px` reserved for pills/badges. Stricter Swiss variant: `0` everywhere. Never mix large radii (16px+) into the system.
- Borders: `1px solid var(--line)` are the workhorse - card outlines, table rules, dividers, input outlines. Minimalism builds elevation from **hairlines**, not shadows.
- Dividers between list rows; full-width, `--line` color. No decorative dividers (no dots, no ornaments).

---

## 5. Lighting, shadows, materials

- Default: **no shadow**. A flat card with a hairline border is the canonical surface.
- If elevation is needed (dropdowns, popovers, toasts - things that truly float): one token `--shadow-raised: 0 4px 16px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.04)` plus a 1px border. This is the only shadow in the system.
- Never stack shadows for drama, never glow. Materials are flat paper; the only "light" is the ambient assumption of a well-lit room.

---

## 6. Imagery & iconography

- **Photography:** objective, unfiltered, generous margins - the Swiss "objective photography" tradition. Full-bleed is acceptable for one hero image; otherwise images sit inside the grid with the standard gutter.
- **Illustration:** sparse, single-weight line art matching the border weight (1.5px), one color (ink or accent). No mascot clusters, no scene illustrations on every empty state - one good diagram beats four decorative doodles.
- **Icons:** 1.5px stroke, geometric, 20/24px grid, single color, always paired with a text label in nav/actions. Icon-only buttons require `aria-label` and are used rarely (close ✕, overflow ⋯).
- **Charts:** single accent + grays, direct labeling over legends, gridlines at `--line`. Data-ink ratio is the aesthetic.

---

## 7. Composition & alignment

- **Grid discipline:** 12-column, 24px gutters, content max-width ~1040px (or prose-only `~720px` for docs). Elements snap to columns; nothing floats at arbitrary offsets.
- **One focal point per viewport:** exactly one element at display size or accent color. Everything else supports it.
- **Left edge is sacred:** every component shares the left margin line; the ragged right edge is the only expressive edge.
- **Progressive disclosure for complexity:** collapsible sections (`<details>`), multi-step forms, "show more" tables at 10 rows. Complexity is *sequenced*, never compressed into faint small type.

---

## 8. Interaction states (complete matrix)

| State | Visual | Notes |
|---|---|---|
| Hover (buttons) | Background darkens one step (`#111→#000`, accent→accent-700) | 200ms ease-out; color shift only - no movement |
| Hover (links) | Underline color `--line → --ink` (the underline was always there) | Never introduce underline only on hover |
| Hover (rows/cards) | `background: var(--surface)` tint or `border-color` darkens one step | Pick one convention system-wide |
| `:focus-visible` | `outline: 2px solid var(--accent); outline-offset: 2px` | Same ring everywhere; never removed |
| Active/pressed | Background darkens a second step; no scale/translate | Minimalism's press is calm |
| Selected (nav/filter) | Accent text + 2px accent underline (nav) or accent-filled pill | Plus `aria-current`/`aria-pressed` |
| Disabled | `background: var(--line)`, text `var(--muted)` (≥4.5:1), `cursor: not-allowed` | Visible at a glance; not faint ghost |
| Loading | Button label → `Saving…` + 200ms opacity pulse on label only; button keeps size | Never a spinner that shifts layout |
| Error (field) | 1px `--error` border + 13–14px error text below, `--error` color ≥4.5:1, `aria-invalid` + `aria-describedby` wired | Message states the fix, not just "invalid" |
| Empty | Centered or left-aligned statement + one primary action; illustration optional and single | Empty states carry copy, not just whitespace |

---

## 9. Motion

- **Durations:** 150ms for hover/focus color changes, 200ms for most transitions, 250ms ceiling for panel/accordion reveals. Anything longer feels theatrical here.
- **Easing:** `ease-out` for entrances, `ease-in` for exits, `linear` only for progress indicators. No springs, no bounces, no elastic.
- **Property scope:** `opacity`, `background-color`, `border-color`, `text-decoration-color`, and ≤2px `transform`. Never animate width/height/layout-affecting properties except within accordions (height, with `overflow: hidden`).
- **Accordion/disclosure pattern:** 200–250ms height + 150ms opacity fade on the inner content; `aria-expanded` on the trigger.
- **Reduced motion:**
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { transition-duration: 0ms !important; animation-duration: 0ms !important; }
  }
  ```
- Motion must never be the only signal: state changes also change color/text (e.g. accordion chevron rotates AND `aria-expanded` flips).

---

## 10. Responsive adaptation

- **Mobile (<768px):**
  - Spacing compresses by one step per tier (96→48, 48→24) but the *ratios* hold; do not flatten all spacing to 8px.
  - 12-col grid becomes 4-col; most content single-column; tables convert to stacked key-value rows (label above value) or horizontal scroll with sticky first column - never shrink text below 16px to fit.
  - Nav collapses to a disclosure (button + panel, `aria-expanded` wired) or a bottom tab bar for apps; minimalism prefers the plain full-width list.
  - Display type floors at 2.5rem via `clamp()`.
- **Tablet (768–1024px):** 8-col grid; docs keep the single prose column with wider margins.
- **Desktop (>1024px):** full grid; the extra width buys *margins*, not more columns of decoration - keep the content column honest.
- **Touch targets:** ≥44px height on all interactive elements; the compact dashboard tier uses 40px rows + 8px vertical hit-area padding to stay honest.
- Test the accent budget per viewport: a row of four accent buttons on desktop that wraps into a stack of four accent blocks on mobile has failed the one-voice rule - demote three to neutral.
