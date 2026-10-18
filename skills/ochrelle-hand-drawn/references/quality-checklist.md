# Hand Drawn - Quality Checklist

Ship gate for Hand Drawn. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** Exactly two radius tokens (`--radius-wobble`, `--radius-chip`) used everywhere; no perfect rectangles, circles, or one-off radius values.
2. **(gate)** Border system holds: 3px ink on primary surfaces, 2px on secondary; no 1px browser-default borders anywhere.
3. Palette holds: 1 paper ground + 1 card tone + max 4 marker accents; a fifth marker color fails the gate.
4. Grid/ruled texture is ≤6% alpha and sits behind a solid text island when it would touch dense text; no paper noise over paragraphs.
5. Rotation discipline: element rotations come from the fixed set (-1.5, -0.5, 0.5, 1.5deg); nothing beyond ±3deg except tape strips (≤5deg).
6. Exactly one icon set (hand-drawn strokes or doodle fills); no mixing with crisp geometric icons.
7. Every doodle/arrow/tape strip is `aria-hidden` and points at real content (or is removed).

## B. Components & states

8. **(gate)** Full state matrix on every interactive element: default, hover, `:focus-visible`, active, disabled, selected, loading (`aria-busy`), error. See style-guide §8.
9. **(gate)** All feedback is dual-coded: glyph or text word plus color (check + "correct", cross + "try again"); color alone never carries state.
10. Buttons keep min 48px height including borders; hover rotation ≤1deg and removed under reduced motion.
11. Nav marks current page with `aria-current="page"` plus a non-color cue (fill change + position in folder tabs).
12. Forms: real `<label>`, visible handwriting hints at ≥20px, `aria-invalid` + text error line in `--error` (8.2:1).
13. Disabled controls: 2px `--ink-soft` border and `--ink-soft` text (7.3:1) - readable, not faded.
14. `<mark>` highlights only wrap real emphasis; never used to patch low contrast.

## C. Accessibility

### Verified pair reference (computed WCAG ratios)

| Text | Ground | Ratio | Verdict |
|---|---|---|---|
| `#33302A` ink | `#FFFCF2` paper | 12.8:1 | body |
| `#33302A` ink | `#FFE45C` highlight | 10.3:1 | body |
| `#33302A` ink | `#B9E4A8` leaf | 9.2:1 | body |
| `#33302A` ink | `#8FC7F2` sky | 7.3:1 | body |
| `#33302A` ink | `#FF8A75` coral | 5.7:1 | body (large/graphic fills preferred) |
| `#5A544A` soft ink | `#FFFCF2` paper | 7.3:1 | secondary |
| `#8A2E1F` error | `#FFFCF2` paper | 8.2:1 | error text |
| `#FFF` white | `#FF8A75` coral | ~2.5:1 | never |

15. **(gate)** All text meets 4.5:1 (or 3:1 for ≥24px/18.66px bold) on its actual ground; measure real pairs, including text over textures.
16. **(gate)** Focus visible on every focusable element: `outline: 3px dashed var(--ink); outline-offset: 4px` (light variant on dark fills); never removed.
17. Handwriting restricted to accents: ≥20px, short strings, never body copy, never all-caps, never numbers in tables.
18. Body text stays in the humanist sans at ≥16px with line-height ≥1.5; measure ≤70ch.
19. `prefers-reduced-motion: reduce`: draw-ins render complete with no animation, hover transforms removed, transitions off.
20. Decorative SVG arrows/scribbles are `aria-hidden="true"` with `focusable="false"`; no information lives only in a doodle.
21. Icons with meaning carry accessible names; doodle bullets are aria-hidden with list semantics intact.
22. 200% zoom: highlights, borders, and annotations do not clip or overlap text.

## D. Performance

23. Fonts: max 2 families (body sans + one handwriting); weights limited to used set; `font-display: swap`; handwriting face subsetted (Latin basic).
24. Texture uses one repeating gradient or one small SVG pattern - no full-page noise images, no large base64 textures.
25. Draw-in animations animate `stroke-dashoffset`/`transform` only; no layout-thrashing keyframes.
26. Shadows limited to the single ink-bleed recipe; no per-element blur chains.
27. Cards have explicit `aspect-ratio` or dimensions when they contain images (taped snapshots shift otherwise).

## E. Responsive

28. Mobile: annotations reflow below their referent (no cross-column absolute positioning); rotations reduce to ±1deg; gutter 16-24px.
29. Touch targets ≥48px including 3px borders; hover-only affordances also fire on first tap or exist without hover.
30. Folder-tab nav becomes a scrollable strip on tablet; all tabs keep visible ink borders while scrolled.
31. 360px width: no horizontal scroll; wobbly cards keep 2px+ visible ink on all sides.
32. `forced-colors: active`: ink borders and text map to system colors; marker fills degrade to system highlight safely.

---

## 10-point pre-delivery pass

- [ ] Tab the page: dashed focus ring visible on every control, including inside rotated cards.
- [ ] Reduced motion on: page fully still after load; draw-ins already complete; hover adds color only.
- [ ] Contrast audit on every text/ground pair, including text over texture and marker fills; record ratios vs the §C table.
- [ ] Radius audit: grep CSS for `border-radius` - only the two tokens and tape/nav tab values appear.
- [ ] Marker count: ≤4 accent fills; each maps to one meaning (highlight, success, info, error/accent).
- [ ] State matrix walkthrough: button, choice row, input, tab vs style-guide §8; every state has glyph+text, not hue alone.
- [ ] Doodle budget: ≤3 decorative elements per section; each is aria-hidden and anchored to content.
- [ ] Read a full paragraph aloud: body is sans, 16px+, comfortable; handwriting appears only as notes.
- [ ] Test 360px: annotations below referents, no overlap, no horizontal scroll, targets ≥48px.
- [ ] Ask "does this feel like a caring teacher's notebook?": random wobble, rainbow markers, or script walls of text mean fix before ship.
