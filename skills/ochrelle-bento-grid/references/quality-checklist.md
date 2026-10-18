# Bento Grid - Quality Checklist

Reference for the `ochrelle-bento-grid` skill. Every item is checkable on the
delivered implementation. Mark each ✓ / ✗ / N-A before delivery.

---

## A. Grid and reflow (7)

- [ ] A1. Layout is CSS Grid with `1fr` column tracks (`repeat(12, 1fr)` or `repeat(4, 1fr)`); no float/flex emulation of the grid.
- [ ] A2. One gap token (12–24 px) used for the whole grid; no mixed gutters.
- [ ] A3. Rows use `grid-auto-rows: minmax(min, auto)`; no fixed pixel row heights anywhere.
- [ ] A4. `grid-auto-flow` is `row` - `dense` is not used (reading-order protection).
- [ ] A5. Tile spans come from a small vocabulary; at most one hero-size tile per grid.
- [ ] A6. Reflow at ~1024 px / ~768 px / ~480 px keeps the canonical reading order (no tile promotes above a higher-priority tile).
- [ ] A7. No holes or overlaps at any tested viewport width (spot-check 1440, 1024, 900, 768, 480, 375, 320 px).

## B. Content and hierarchy (7)

- [ ] B1. Every non-default-size tile passes the sizing justification test with a content-based reason recorded in the PR/notes.
- [ ] B2. The largest tile contains the highest-priority content (verified against the stated content ranking).
- [ ] B3. Equal-priority peer tiles have equal spans (e.g., the two KPIs match).
- [ ] B4. Each tile contains exactly one idea; no tile mixes unrelated payloads.
- [ ] B5. Each tile has exactly one heading; heading levels do not skip.
- [ ] B6. Tile content fits at every breakpoint - nothing clipped, no vertical overflow, no horizontal overflow inside tiles (`min-width: 0` set where needed).
- [ ] B7. At most one primary action per tile; link text is specific ("View revenue report", not repeated "Read more").

## C. Accessibility (9)

- [ ] C1. DOM order equals the intended reading order (verified by reading the HTML source, not the rendering).
- [ ] C2. Tab order matches the reading order (tab-through test performed); no `tabindex` patches over order problems.
- [ ] C3. No keyboard trap: focus moves out of every tile and control with Tab/Shift+Tab alone.
- [ ] C4. Every interactive element inside tiles is natively focusable (`a`, `button`) with a visible `:focus-visible` indicator.
- [ ] C5. No hover-only information: anything revealed on hover is also visible, focusable, or available on another interaction.
- [ ] C6. Whole-tile links: the accessible name is meaningful and unique per tile.
- [ ] C7. Text contrast ≥ 4.5:1 (large text ≥ 3:1) against the actual tile surface - tested with the chosen skin and the busiest background region for translucent tiles.
- [ ] C8. Status/meaning never conveyed by color alone (icons, text, or patterns accompany color).
- [ ] C9. Layout survives 400 % zoom / 320 px width without horizontal page scrolling (WCAG 1.4.10 reflow).

## D. Responsive (4)

- [ ] D1. Mobile (≤ 768 px) keeps only genuinely paired tiles side by side; all others go full width.
- [ ] D2. Tile padding steps down (e.g., 24 px → 16 px) on small screens; internal spacing stays on the product scale.
- [ ] D3. Images and charts inside tiles reserve their space (`aspect-ratio` or width/height attributes) - no late-arrival layout shift.
- [ ] D4. Touch targets inside tiles are ≥ 24×24 px with spacing (WCAG 2.2 target size minimum), including footer links and chips.

## E. Performance (4)

- [ ] E1. No layout-shift during load: fonts, media, and charts are size-reserved; CLS contribution of the grid is negligible.
- [ ] E2. If a glass skin is applied: `backdrop-filter` is feature-detected with an `@supports` fallback, limited in area, and not animated.
- [ ] E3. Shadows/radius are cheap and uniform (no per-tile bespoke multi-layer shadows unless the skin calls for it - then budget it).
- [ ] E4. No JavaScript is required for the layout itself; any JS (charts, feeds) degrades to static content that still fits its tile.

---

## 10-point pre-delivery pass

Run this final pass in order; a single ✗ sends the work back:

1. **Source read:** HTML tile order reads as the intended narrative aloud.
2. **Tab-through:** every link/button reached in reading order; focus always visible; no trap.
3. **Sizing audit:** every non-default tile has a one-sentence justification on record.
4. **Hole scan:** screenshot-free check - resize through 1440 → 320 px and confirm no gaps/overlaps.
5. **Overflow scan:** tallest tile content (long list, long locale strings) fits at every breakpoint.
6. **Skin contrast:** worst-case text/background pair passes 4.5:1 (use the busiest background region).
7. **Hover audit:** disable hover (touch emulation) and confirm no information becomes unreachable.
8. **Reflow sanity:** KPI pairs still paired on tablet/mobile; hero still first; status cluster still last.
9. **Token audit:** one gap, one radius, one border treatment, one padding scale - grep the CSS for stray values.
10. **Honesty note:** record which viewports, skins, and assistive behaviors were actually tested and which were not.

Keep the completed checklist with the deliverable; untested items must be
marked as untested, never silently checked.
