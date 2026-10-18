---
name: ochrelle-bento-grid
description: "Bento Grid specialist skill for the Ochrelle design library. Teaches the bento grid as an information-architecture and layout pattern first: a modular, asymmetric tile layout popularized by Apple and named after compartmentalized bento lunch boxes, built with CSS Grid and sized by content priority rather than decoration. Use when the user asks for a bento grid, bento layout, tile dashboard, modular feature overview, portfolio or about page with mixed-size cards, a settings hub, or asks to reorganize scattered content into a scannable grid. Covers grid architecture, tile sizing semantics, responsive reflow, semantic reading order, keyboard access, accessibility, and pairing the layout with visual skins such as minimalist, glass, or brutalist treatments."
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: layout-spatial
---

# Ochrelle - Bento Grid

## 1. What this skill teaches

A **bento grid** is a modular tile layout: content is divided into rectangular
tiles of varied size, arranged edge to edge in a gap-separated grid, like food
sorted into the compartments of a Japanese bento box. Apple popularized the
pattern in keynote slides, product overview pages (mixing hero imagery, feature
summaries, and small stat tiles in one composition), and later in OS surfaces
such as widget grids and settings hubs.

This skill treats the bento grid **primarily as information architecture and a
layout pattern, not a visual style**. This distinction is core to Ochrelle:

- The **layout layer** decides *what content exists, how it is grouped, how much
  space each group earns, and in what order it is read*. It is built from CSS
  Grid and survives any restyle.
- The **visual skin** (minimalist, glass, brutalist, clay, anything) decides
  *what the tiles look like*: surfaces, borders, blur, shadows, color.

A bento layout with no styling is still a bento. Rounded corners and soft
shadows are optional conventions of the pattern's popular Apple-flavored form,
not requirements. Never "add bento-ness" by decorating - bento-ness lives in
the grid definition and the content-to-size mapping.

## 2. When to use a bento layout

Use it when the content is a **set of peers that deserve unequal emphasis** and
will be scanned rather than read linearly:

- **Dashboards and analytics overviews** - KPI tiles beside charts, feeds, and
  status indicators.
- **Feature overviews** on product pages - one hero capability plus several
  supporting capabilities, each self-contained.
- **Portfolio and about pages** - bio, selected work, skills, contact, each in
  its own compartment.
- **Settings or control hubs** - grouped controls that users navigate by
  recognition, not by reading.

Do **not** use it for:

- **Linear narrative content** - articles, documentation, tutorials. A grid
  fights the reading flow and forces arbitrary truncation.
- **Long-form reading** - body text wider than one tile and longer than a few
  paragraphs belongs in a single-column reading measure.
- **Simple marketing pages that need one CTA and one message** - a bento
  fragments attention; use a focused landing layout.
- **Dense data tables or complex forms** - cells and fields need stable rows
  and columns of their own, not decorative tile frames.

## 3. Grid architecture at a glance

The full specification lives in [references/style-guide.md](references/style-guide.md).
Summary:

| Decision | Recommendation |
| --- | --- |
| Layout engine | CSS Grid (`display: grid`) |
| Desktop columns | `repeat(12, 1fr)` (dashboards) or `repeat(4, 1fr)` (small compositions) |
| Row sizing | `grid-auto-rows: minmax(120px, auto)` - rows grow, never clip |
| Gap | 12–24 px, one token, never mixed within one grid |
| Tile sizing | `grid-column: span N` / `grid-row: span N` from a small span vocabulary |
| Reflow | 12 → 6 → 2 columns at roughly 1024 px / 768 px / 480 px breakpoints |

## 4. Sizing semantics: size follows content priority

The single most important rule of this pattern:

> **A tile's size is an argument about importance. The biggest tile must contain
> the most important content. Size follows priority - never aesthetics, never
> arbitrary variety.**

Apply the **sizing justification test**: for every tile that is not the default
size, complete the sentence -

> "This tile is larger/smaller than the base tile because its content is
> ______ for the user."

If the only honest answer is "because it looks better" or "to break the
monotony", change the size or change the content. Full procedure and a worked
example are in [references/style-guide.md](references/style-guide.md).

## 5. Component guidance

### Tile anatomy

Every tile is a self-contained unit with three optional zones:

```
+--------------------------------+
| header   - label, context      |
| content  - the payload         |
| footer   - one action, or none |
+--------------------------------+
```

- **Header**: short label plus optional meta line ("Last 30 days"). Never more
  than one heading per tile.
- **Content**: the payload - a metric, a chart, a list, an image, a paragraph.
  Content must fit its tile at every breakpoint; if it overflows, the tile is
  the wrong size or the content is the wrong content.
- **Footer**: at most one primary action. A tile with three links is a page
  fragment, not a tile - split it or move the links into the content.

### What belongs in a tile

One idea per tile. Good tile payloads: one KPI with trend, one chart, one
notification list, one setting group, one image with caption, one feature
summary with a single link. Bad tile payloads: mixed unrelated KPIs, a table
plus a chart plus text, multi-step forms.

### Interactive tiles

If the whole tile is clickable, implement it as one real link or button
(wrapping element or stretched-link pattern) with `:focus-visible` styling -
never a hover-only affordance. Keyboard tab order is covered in
[references/implementation-examples.md](references/implementation-examples.md).

## 6. Combining the pattern with a visual skin

The layout is fixed; the skin is a free variable. Common pairings:

| Skin | Tile treatment | Watch out for |
| --- | --- | --- |
| Minimalist | White/neutral surfaces, 1 px borders or shadowless flat tiles, strong type hierarchy | Gray-on-gray text below contrast minimums; removing affordances |
| Glass | Translucent tiles with `backdrop-filter: blur()` over a rich background | Contrast that depends on what is behind the tile; see the Ochrelle glassmorphism skill |
| Brutalist | Flat fills, solid 2 px borders, hard offset shadows, no radius | Decorative harshness breaking readability; keep focus states loud and clear |
| Clay / soft | Large radii, layered soft shadows | Shadow cost per tile; muddy boundaries between adjacent tiles |

Rules for any combination:

1. One radius token, one gap token, one padding scale across all tiles.
2. The skin must not change tile *sizes* - the sizing semantics in section 4
   are skin-independent.
3. A skin may not introduce hover-only information. What appears on hover must
   also be reachable by keyboard and visible on touch.

## 7. Responsive strategy summary

- Desktop (≥ 1025 px): 12 columns, explicit span classes, auto-flow row.
- Tablet (≈ 769–1024 px): 6 columns; spans remapped via `grid-template-areas`
  or per-tile overrides.
- Mobile (≤ 768/480 px): 2 columns; most tiles full width, only genuinely
  paired small tiles (e.g., two KPIs) stay side by side.
- Never let a fixed pixel tile height clip content; use `minmax(min, auto)`.
- The exact CSS for all three breakpoints is in
  [references/implementation-examples.md](references/implementation-examples.md).

## 8. Accessibility summary

- **DOM order is the reading order.** Place tiles in the HTML in the order they
  should be read; do not rely on visual placement, `order`, or
  `grid-auto-flow: dense` to assemble meaning. Screen readers and Tab follow
  the DOM.
- **Semantic structure**: the grid is a `<section>` (or `<ul>` of tiles when
  tiles are list-like), each tile is an `<article>` or `<li>` with exactly one
  heading; heading levels must not skip.
- **Keyboard**: every interactive element inside every tile is reachable and
  operable by keyboard, with a visible `:focus-visible` indicator; the Tab
  order matches the reading order because the DOM does.
- **No hover-only content**; no color-only status; text contrast ≥ 4.5:1
  (WCAG 2.2 AA) against the tile surface in every skin.
- **Zoom and reflow**: the layout must survive 400 % zoom / 320 px CSS width
  (WCAG 1.4.10) - the mobile reflow handles this if tiles go full width.
- Full checklist: [references/quality-checklist.md](references/quality-checklist.md).

## 9. Failure modes - top 5

1. **Decoration-driven sizing.** Big tiles for trivial content because "the
   composition needed it". Fix: run the sizing justification test on every
   non-default tile; demote or resize.
2. **Broken reading order.** DOM order diverges from visual order (via `order`,
   dense flow, or negative line placement), so screen-reader and Tab order
   zig-zag. Fix: DOM order = canonical order; audit with the tab-through test.
3. **Overflow and squish.** Fixed row heights or long content clip inside
   tiles, or tiles stretch and leave holes at intermediate viewports. Fix:
   `minmax(..., auto)` rows, test every tile at every breakpoint, split
   oversized content.
4. **Monotony or chaos.** All tiles equal size (not a bento, just cards) or
   random spans with no priority story (visual noise). Fix: one hero tile, a
   small span vocabulary (2×2, 2×1, 1×1 …), everything else default.
5. **Skin overrides structure.** A glass or brutalist skin introduces contrast
   failures or hover-only reveals that the clean layout did not have. Fix:
   re-run the accessibility checklist after applying any skin.

## 10. How to apply this skill (workflow)

1. **Inventory content.** List every unit of content and rank its priority for
   the user's main task.
2. **Group and order.** Cluster related content into tiles; decide the reading
   order; write the HTML in that order.
3. **Size by priority.** Assign spans top-down from the priority ranking; run
   the sizing justification test.
4. **Build the grid.** Use the reference CSS (12 → 6 → 2 reflow); keep tokens
   (gap, radius, padding) single-sourced.
5. **Skin it.** Apply the chosen visual treatment without changing sizes or
   order.
6. **Verify.** Walk [references/quality-checklist.md](references/quality-checklist.md)
   and the 10-point pre-delivery pass before delivering.

## 11. Bundled references

- [references/style-guide.md](references/style-guide.md) - grid architecture,
  sizing semantics, breakpoint CSS, tile anatomy, skin pairings.
- [references/implementation-examples.md](references/implementation-examples.md)
  - complete working dashboard and marketing-page layouts with reflow and
  keyboard notes.
- [references/quality-checklist.md](references/quality-checklist.md) - 30+
  checkable items and the 10-point pre-delivery pass.

Companion Ochrelle skills (install separately if needed): `ochrelle-design-master`
for routing and style selection; `ochrelle-minimalism`, `ochrelle-glassmorphism`,
`ochrelle-brutalism` for the corresponding tile skins.
