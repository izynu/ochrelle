# Bento Grid - Style Guide

Reference for the `ochrelle-bento-grid` skill. Values below are contextual
recommendations for typical web products, not universal laws; adjust with
reason and note deviations.

---

## 1. Grid architecture

### 1.1 Base definition

```css
.bento {
  display: grid;
  /* Dashboard scale: 12 columns. Small compositions (about page, hub):
     use repeat(4, 1fr) and halve the span vocabulary. */
  grid-template-columns: repeat(12, 1fr);
  /* Rows have a floor and can grow with content - never a fixed px height. */
  grid-auto-rows: minmax(140px, auto);
  /* Default auto-placement: row order, no dense repacking. */
  grid-auto-flow: row;
  gap: var(--bento-gap, 16px); /* token: 12–24px, one value per layout */
}
```

Why these choices:

- **`1fr` columns** keep tiles aligned to one shared rhythm; percentage or
  mixed column widths make spans unpredictable.
- **`grid-auto-rows: minmax(140px, auto)`** guarantees a minimum tile height
  (so tiny content still forms a readable tile) while letting tall content
  expand its row instead of clipping. 140 px suits dashboards; use 160–180 px
  for marketing tiles with imagery.
- **`grid-auto-flow: row` (not `row dense`)** keeps visual placement
  deterministic. `dense` back-fills holes with later DOM items and silently
  breaks the reading order (see implementation-examples, section 3).

### 1.2 Gap token

| Context | Gap |
| --- | --- |
| Dense dashboard | 12–16 px |
| Marketing / portfolio | 16–24 px |
| Mobile reflow | 12 px |

One value per layout, defined once:

```css
.bento { --bento-gap: 16px; gap: var(--bento-gap); }
@media (max-width: 480px) { .bento { --bento-gap: 12px; } }
```

Never mix two gaps in one grid; uneven gutters read as breakage, not style.

### 1.3 Span vocabulary

Keep a deliberately small vocabulary of tile sizes. On a 12-column grid:

| Span class | Size | Typical content |
| --- | --- | --- |
| `span 12` | full row | page-level banner inside the grid (rare) |
| `span 6 × rows 2` | hero | primary metric, hero feature, main chart |
| `span 6` | half | secondary chart, primary setting group |
| `span 4` | third | list tiles, tables, feeds |
| `span 3` | quarter | KPI tiles, quick actions |
| `span 2` | sixth | micro-stats, legend chips |

Rule of thumb: **one hero, two to three medium sizes, small tiles for
atomic facts**. If you need more than four distinct sizes, the content set is
probably not grouped correctly yet.

---

## 2. Sizing semantics

### 2.1 The priority rule

Tile area is a ranking device. Users infer importance from size before they
read a word. Therefore:

1. Rank content by importance to the user's primary task (not by how visual it
   looks).
2. Assign the largest span to rank 1, and step down as priority steps down.
3. Content of equal priority gets equal spans. Do not differentiate peers.

### 2.2 The sizing justification test

For every tile whose span differs from the base tile (the smallest standard
span in the layout), complete:

> "This tile is **[size]** because its content is **[why that matters to the
> user]**."

Worked example (analytics dashboard):

| Tile | Span | Justification |
| --- | --- | --- |
| Revenue overview | 6×2 | Primary question users open the dashboard to answer; holds a metric + trend chart. |
| Active users | 3 | Secondary KPI, one number + delta. |
| Conversion | 3 | Secondary KPI, same class as Active users - must match its size. |
| Traffic chart | 6 | Supporting trend, detail level below the hero. |
| Recent activity | 4×2 | Scannable list; height earns scan-ability, width does not need it. |
| Top products | 4×2 | Peer of Recent activity - equal size, same row pair. |
| Storage | 2 | Atomic fact. |
| Team | 2 | Atomic fact. |
| System status | 4 | Composed of several atomic facts, still tertiary. |

If a justification cannot be written in one honest sentence, resize the tile or
replace the content.

### 2.3 Anti-patterns

- Two hero-sized tiles competing for attention (splits the argument about what
  matters; pick one).
- A giant tile containing one number (size promises content depth that is not
  there - demote it or add the supporting trend/detail that justifies it).
- A tiny tile containing a long list (size promises brevity - promote it or
  truncate with a real link to the full list).

---

## 3. Responsive reflow strategy

Canonical strategy: **12 → 6 → 2 columns** at approximately 1024 px and
768 px/480 px. The mapping is done per tile, not by formula, because content
priority - not arithmetic - decides what stays side by side.

- **≥ 1025 px** - 12 columns, span classes as in section 1.3.
- **769–1024 px** - 6 columns. The hero keeps a full row; KPI pairs stay
  paired; list tiles take thirds. Use `grid-template-areas` for exact control
  (preferred) or per-tile span overrides.
- **≤ 768 px** - 2 columns. Most tiles full width; only genuinely paired
  atomic tiles (two KPIs, two micro-stats) share a row.
- **≤ 480 px** - same 2-column grid with reduced gap (12 px) and padding
  (16 px); verify tiles still clear `minmax` row floors.

Concrete, complete breakpoint CSS for a nine-tile dashboard is in
[implementation-examples.md](implementation-examples.md).

Reflow principles:

1. **Preserve reading order.** The order established on desktop is canonical.
   Reflows regroup tiles but must not promote tertiary content above primary
   content.
2. **Preserve pairs.** Equal-priority peers that share a row on desktop should
   still share a row (or stack adjacently) on mobile.
3. **One decision per breakpoint.** Do not add breakpoints beyond what the
   content needs; each one is a maintenance liability.
4. **Test 320 px.** WCAG 1.4.10 reflow: no horizontal scrolling at 320 px CSS
   width. Full-width tiles guarantee this if inner content wraps.

---

## 4. Tile anatomy and internal spacing

### 4.1 Zones

```html
<article class="tile">
  <header class="tile__header">
    <h3>Label</h3>            <!-- exactly one heading per tile -->
  </header>
  <div class="tile__content"><!-- the payload --></div>
  <footer class="tile__footer">
    <a href="…">One action</a> <!-- optional; never more than one primary action -->
  </footer>
</article>
```

- **Header** - label plus optional meta line. Keep it one line on desktop,
  wrapping to two on mobile.
- **Content** - the payload. Vertical rhythm inside the tile should reuse the
  product's existing spacing scale; do not invent a tile-private scale.
- **Footer** - optional; usually a text link. Omit for purely informational
  tiles.

### 4.2 Padding scale

| Tile size | Padding |
| --- | --- |
| Small tiles (span 2–3) | 16 px |
| Medium tiles (span 4–6) | 24 px |
| Hero tiles | 24–32 px |

Define once, inherit everywhere:

```css
.tile { padding: var(--tile-pad, 24px); }
.tile--small { --tile-pad: 16px; }
@media (max-width: 480px) { .tile { --tile-pad: 16px; } }
```

Internal elements (header → content → footer) should be separated by steps of
the same scale (e.g., 8/12/16 px), so the whole composition reads as one
system.

### 4.3 Radius and borders

- **One radius token for tiles** (16–24 px is the common bento range; 20 px is
  a safe default). Inner elements (charts, images, buttons) may use smaller
  radii, but tiles must all match.
- **One border treatment**: either all tiles have a 1 px border, or none do.
  Mixed treatments look like an accident.
- Overflow: any media inside a tile needs `border-radius: inherit;
  overflow: hidden` on a wrapper so images respect the tile radius.

---

## 5. Combining the layout with visual skins

The grid definition never changes when the skin changes - only `.tile`
surface styles do.

### 5.1 Minimalist skin

```css
.tile {
  background: #ffffff;
  border: 1px solid #e5e5ea;   /* structure without shadow */
  border-radius: var(--bento-radius, 20px);
}
```

- Hierarchy comes from typography weight/size and tile size - not decoration.
- Keep at least 4.5:1 text contrast; avoid mid-gray body text on white.
- Empty space is part of the design; do not fill tiles to "use" them.

### 5.2 Glass skin

```css
.tile {
  background: rgba(255, 255, 255, 0.55);
  -webkit-backdrop-filter: blur(16px) saturate(1.4);
  backdrop-filter: blur(16px) saturate(1.4);
  border: 1px solid rgba(255, 255, 255, 0.6);
}
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .tile { background: rgba(255, 255, 255, 0.92); } /* opaque fallback */
}
```

- Contrast now depends on what is behind the tile: test the busiest region of
  the background, not an empty one.
- Provide the `@supports` fallback and consider `@media (prefers-reduced-transparency: reduce)`
  where supported, falling back to opaque surfaces.
- `backdrop-filter` costs GPU time on large areas; this pairing is a
  deliberate performance trade-off (see quality-checklist, Performance).

### 5.3 Brutalist / neo-brutalist skin

```css
.tile {
  background: #f5f0e6;
  border: 2px solid #111111;
  border-radius: 0;                 /* or a token, but consistent */
  box-shadow: 6px 6px 0 0 #111111;  /* hard offset shadow, one direction */
}
```

- One shadow direction and one border width everywhere; two directions or two
  widths look broken, not raw.
- Focus states must be louder than decoration: `outline: 3px solid` accent on
  `:focus-visible`.
- Raw ≠ hostile: line-height and spacing still follow readable defaults.

### 5.4 Cross-skin invariants

Whichever skin is chosen, these must hold (they are layout-level, so this
skill owns them):

1. Sizes and spans unchanged by the skin.
2. One gap, one radius token, one border treatment, one shadow system.
3. No hover-only information; `:focus-visible` always styled.
4. Text contrast ≥ 4.5:1 on the tiled surface in the worst case.

---

## 6. Design tokens (starter set)

```css
.bento {
  --bento-gap: 16px;        /* 12–24px */
  --bento-radius: 20px;     /* 16–24px, one value */
  --tile-pad: 24px;         /* 16px on small tiles / mobile */
  --tile-bg: #ffffff;
  --tile-border: #e5e5ea;
  --row-min: 140px;         /* grid-auto-rows floor */
}
```

Ship the tokens with the layout; skins override only surface tokens
(`--tile-bg`, `--tile-border`), never geometry tokens.
