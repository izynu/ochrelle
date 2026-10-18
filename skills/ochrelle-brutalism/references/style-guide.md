# Brutalism & Neo-Brutalism - Style Guide

Full art direction for both branches. Where the branches differ, each section says so.

---

## 1. Color

### Principles
- **Flat only.** No gradients, no blurs, no translucency. A color is a region, not an atmosphere.
- **Ink is shared.** Text, borders, and shadows use the same `--ink` (usually pure `#000`). Hierarchy is built from size, weight, and block position - not from gray ramps.
- **Accent as fill, not garnish.** Accents are used as large flat regions (banner fills, badge backgrounds, button faces), not as thin highlights.

### Classic digital brutalism palette
| Token | Value | Use |
|---|---|---|
| `--bg` | `#FFFFFF` (or `#FFFDF5` warm variant) | Page ground |
| `--ink` | `#000000` | Text, borders, rules |
| `--primary` | `#FF0000`, `#0000FF`, or `#FFFF00` | One primary per site, used in blocks |
| `--secondary` | `#00FF00` or `#FF00FF` | Sparingly; one extra at most |
| `--muted` | none - if needed, `#767676` minimum (4.54:1 on white) | De-emphasized text |

### Neo-brutalism palette (example system)
| Token | Value | Contrast of `#000` on it | Role |
|---|---|---|---|
| `--paper` | `#FFFDF5` | 20.6:1 | Page ground |
| `--sun` | `#FFDB58` | 15.5:1 | Banners, highlights, safe fill for body text |
| `--coral` | `#FF6B6B` | 7.6:1 | Cards, badges, warm fills (ink text passes AA) |
| `--mint` | `#4ECDC4` | 10.9:1 | Cards, success-ish regions |
| `--sky` | `#7FB5FF` (softened from #2563EB family for fills) | 10.0:1 | Secondary fills |
| `--accent` | `#FF4D00` | 6.3:1 | Buttons and decorative blocks (ink text passes AA) |

Rule: pick **1 anchor neutral + 2–4 saturated fills**. If a fifth saturated color appears, the palette has failed. Keep ink (`#000`) as the text color on all saturated fills - white text on warm fills fails badly (see §8 and the checklist).

### Dark-mode adaptation
Classic brutalism inverts well: `--bg: #0A0A0A`, `--ink: #FFFFFF`, borders white, hard shadows in white (`6px 6px 0 0 #fff`). Neo-brutalism keeps saturated fills but darkens the ground (`#161616`) and verifies each fill against WCAG 1.4.11 non-text contrast (3:1) against the dark ground.

---

## 2. Typography

### Families
- **Classic:** system stack first (`system-ui, -apple-system, "Segoe UI", sans-serif`) or monospace (`ui-monospace, "SF Mono", Menlo, Consolas, monospace`) for body. Default-feeling is the point - but *chosen*, with consistent application.
- **Neo:** one heavy geometric/grotesk sans for display and UI (e.g. a locally-hosted 700–900 weight), monospace for data/labels/code. Never more than two families.

### Scale (both branches; classic may skip the two smallest display steps)
| Step | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| display-2 | `clamp(2.75rem, 8vw, 6rem)` | 800–900 | 0.95 | Hero statements |
| display-1 | `clamp(2rem, 5vw, 3.5rem)` | 800 | 1.0 | Section titles |
| h1 | `1.875rem` (30px) | 700 | 1.15 | Page titles |
| h2 | `1.5rem` (24px) | 700 | 1.2 | Card titles |
| h3 | `1.25rem` (20px) | 700 | 1.3 | Sub-blocks |
| body | `1rem` (16px), floor 16px on mobile | 400 (classic) / 500 (neo) | 1.5–1.6 | Paragraphs |
| small | `0.875rem` (14px) | 500 | 1.4 | Meta only - never body |
| mono-label | `0.8125rem` (13px) | 500, `letter-spacing: 0.05em`, uppercase | 1.2 | Tags, dates, indices |

- Display headings may use `letter-spacing: -0.02em`. Mono labels go the other way: `0.05em` tracked uppercase.
- **Body text never goes below 16px and never below 4.5:1.** Loudness lives in display sizes and structure.
- Underline links by default (classic) or underline on hover + 2px solid ink underline offset `0.15em` (neo). Links must be distinguishable without color alone.

---

## 3. Spacing & density

- Base scale: **4 / 8 / 16 / 24 / 40 / 64 / 96** (`--space-1 … --space-7`). Brutalism tolerates density; it does not tolerate arbitrary gaps.
- **Classic:** dense, editorial. Section padding 24–40px; grids can sit flush; column gutters 16–24px. The page may feel like a printed broadsheet.
- **Neo:** medium density. Section padding 40–64px; cards breathe 24px inside; page gutter 24–40px.
- Whitespace is structural (it groups blocks like borders do) - but brutalism does not use *generous* whitespace as a luxury cue. If a layout needs >96px of ambient emptiness to feel designed, it has drifted toward minimalism.

---

## 4. Shapes, radii, borders

- **Radius: 0 everywhere** - cards, buttons, inputs, images, badges. A single rounded corner breaks the contract. (If a client insists, the compromise is a uniform tiny `2px` on *everything*, never mixed.)
- **Borders:** solid, one ink. Widths:
  - Classic: 2px for internal rules, 3–4px for outer frames; deliberate weight variation is allowed but must follow a stated pattern (e.g. "outer frame 4px, inner rules 2px").
  - Neo: uniform `3px` (or 4px at very large sizes). Never mixed ad hoc.
- **Corners/frames:** visible page frame or column rules are idiomatic (classic). Sticker badges (rotated `-3deg` to `3deg`) with 2–3px borders are idiomatic for neo.
- **Dividers:** `border-top: 2px solid var(--ink)` - never soft, never dashed unless referencing form-field semantics.

---

## 5. Lighting, shadows, materials

- **Classic: no shadows.** Depth does not exist; the page is a flat print. If hierarchy needs help, use border weight, block inversion (ink block, paper text), or position.
- **Neo: hard offset shadows only.** `box-shadow: Xpx Ypx 0 0 var(--ink)`. Blur must be 0. Standard offsets: `4px 4px`, `6px 6px`, `8px 8px`. One offset size per component scale (e.g. small=4, large=6); do not randomize.
- No gradients (including subtle "sheen"), no `backdrop-filter`, no inner glows. Materials are paper and ink, period.

---

## 6. Imagery & iconography

- **Images:** rectangular, unfiltered, often bordered with the same ink border. No rounded masks, no duotone washes, no soft vignettes. Grayscale is acceptable in classic brutalism (newspaper feel); neo-brutalism usually keeps full flat color.
- **Layout role:** images are blocks in the grid - they align to columns, they do not float free or overlap text except as deliberate collage (neo, sparingly).
- **Icons:** stroke-based, geometric, 2px strokes matching border weight, or plain text glyphs (`→`, `✕`, `↗`). No filled, rounded, or multicolor icon sets.
- **Decorative elements:** repeating patterns are acceptable in neo-brutalism (e.g. `repeating-linear-gradient(45deg, #000 0 2px, transparent 2px 8px)` as a stripe band) - flat, hard-edged, ink-colored only.

---

## 7. Composition & alignment

- **Exposed grid:** multi-column editorial layouts (2–6 columns) with visible column rules or bordered blocks. The grid is a character in the design.
- **Asymmetry with anchors:** classic brutalism allows aggressive asymmetry (blocks jammed left, ragged right); anchor every composition with at least one full-width or strongly-aligned element so the page doesn't read as broken.
- **Alignment:** hard flush-left is the default. Centered text is rare (maybe a hero statement) - never body copy.
- **Scale jumps:** display type sits in stark jumps (30px → 96px), not gentle ramps. Brutalism's hierarchy is stair-like.

---

## 8. Interaction states (complete matrix)

Every interactive component must define all of these. Example values for the signature button (see implementation-examples.md for full set):

| State | Visual | Notes |
|---|---|---|
| `:hover` | Translate `-1px,-1px`; shadow grows to `7px 7px` (neo). Classic: invert block colors (`background: var(--ink); color: var(--bg)`) with **no** transition. | Hover must not be the only channel for information. |
| `:focus-visible` | `outline: 3px solid var(--ink); outline-offset: 3px` | Never suppressed; identical for pointer and keyboard users. |
| `:active` | Translate onto shadow: `transform: translate(2px,2px)`, shadow shrinks `6px→4px` | The mechanical press. |
| `:disabled` | `opacity: 1` (keep!), `background: #E5E2D9`, text `#595650` (≥4.5:1), shadow removed, cursor `not-allowed` | A grayed-out 40%-opacity button fails contrast; brutalism uses solid muted fills instead. |
| `[aria-pressed="true"]` / selected | Shadow removed + component translated onto shadow position (stays "pressed") | Persistent state mirrors the press. |
| Loading | Label swaps to mono `LOADING…` + striped `repeating-linear-gradient` band; block size does not change | Prevents layout shift. |
| Error | 3px `#C81E1E` border + inline message; message text `#8A1111` on paper (≥4.5:1) | Never color-only. |

Links: underlined by default (classic) or underline + hover shift (neo). Focus ring identical to buttons.

---

## 9. Motion

- **Classic: 0ms.** State changes are instant. The absence of transition is a statement; do not "smooth it out later".
- **Neo: one motion idea only - the mechanical snap.**
  - Duration: `80ms`; easing: `linear` (mechanical, not springy).
  - Property scope: `transform` and `box-shadow` on press/hover only.
  - Marquee/ticker elements (idiomatic for announcements): pure CSS `@keyframes`, `60–90s` linear loop, `animation-play-state: paused` on `:hover` and **stopped entirely** under reduced motion.
- **Reduced motion contract:**
  ```css
  @media (prefers-reduced-motion: reduce) {
    .btn-brutal { transition: none; }
    .btn-brutal:hover, .btn-brutal:active { transform: none; }
    .ticker { animation: none; }
  }
  ```

---

## 10. Responsive adaptation

- **Mobile (<768px):**
  - Display scale drops via `clamp()` floors: `display-2` lands ~2.75rem, not shrunken 6rem.
  - Multi-column exposed grids collapse to single column; keep the *borders* so structure stays visible.
  - Hard shadows reduce from `6px 6px` to `4px 4px` to avoid overflowing narrow viewports; add `overflow-x: clip` safety on `body`.
  - Nav becomes a full-width bordered bar list - brutalism's bordered stack is more honest than a hamburger, and keyboard-friendly by default.
  - Tap targets ≥ 44×44px; press shadow shrinks so the translate doesn't push content.
- **Tablet (768–1024px):** 2-column grids; classic may keep 3 if gutters ≥16px.
- **Desktop (>1024px):** full exposed grid, larger offsets, optional page frame.
- Images get explicit `width`/`height` (or `aspect-ratio`) - brutalist layouts shift ugly if images load late.
