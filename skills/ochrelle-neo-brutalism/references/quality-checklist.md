# Neo-Brutalism - Quality Checklist

Ship gate for neo-brutalism. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** Radius is 0 on every component; one rounded corner fails the gate.
2. **(gate)** All shadows are hard offsets with blur 0 (`Xpx Ypx 0 0 var(--ink)`); zero `rgba()` shadows, zero gradients, zero `backdrop-filter` in the stylesheet.
3. Border ladder is the declared pattern (2px internal / 3px components / 4px hero frames); text, borders, and shadows share one ink (`#000`), no `#333` drift.
4. Palette holds at 1 neutral + up to 4 candy fills; coral is reserved for errors; no fifth fill without a redesign conversation.
5. Stickers rotate within -3 to 3 degrees, carry their 2px borders, never cover text or interactive elements, one per region.
6. Decorative stripes are hard-edged ink patterns; no soft or multicolor textures.

## B. Components & states

7. **(gate)** Every interactive component implements the full matrix: default, hover (+1px shadow), `:focus-visible` (3px ink outline, offset 3px), active (translate onto shadow), selected, disabled, loading, error.
8. **(gate)** The press is mechanical: `:active` translates by N px and the shadow shrinks by the same N; reduced motion keeps the shadow change and drops the transform.
9. Disabled states use solid muted fill + `#57534E`-grade text (around 7:1), never opacity hacks.
10. Loading states swap label content with size locked (no layout shift).
11. Errors use 3px coral border + inline ink message; never color-only.
12. Nav marks the current page by inversion (ink fill, paper text) plus `aria-current="page"`.
13. Forms use real `<label>`, `autocomplete`, `aria-invalid` + `aria-describedby` wiring.
14. Cards are static unless they contain real controls; the whole-card-as-link pattern uses a stretched link with visible focus.

## C. Accessibility

### Verified pair reference (computed WCAG ratios for the candy palette)

| Text | Fill | Ratio | Verdict |
|---|---|---|---|
| `#000` | `#FFFDF7` paper | 20.65:1 | ✓ body |
| `#000` | `#B8FF65` lime | 17.53:1 | ✓ body |
| `#000` | `#8BE0FD` sky | 14.18:1 | ✓ body |
| `#000` | `#FFC900` yellow | 13.61:1 | ✓ body |
| `#000` | `#FF90E8` pink | 10.41:1 | ✓ body |
| `#000` | `#FF5C5C` coral | 6.94:1 | ✓ body |
| `#57534E` | `#EDEAE2` muted | ~7:1 | ✓ (disabled label) |
| `#FFF` | `#FFC900` | 1.43:1 | ✗ never |
| `#FFF` | `#FF90E8` | 2.02:1 | ✗ never |
| `#FFFDF7` | `#000` ink ground | 20.65:1 | ✓ body |

15. **(gate)** All body text 4.5:1; large text (24px / 18.66px bold) 3:1; ink labels on every candy fill, white text only on ink grounds.
16. **(gate)** Focus visible on every focusable element: 3px solid ink, offset 3px (paper ink inside inverted blocks); rings are enlarged, never removed.
17. Focus ring contrast against adjacent colors is 3:1 or better (WCAG 2.4.11 / 1.4.11).
18. No hover-only information; stickers and reveals are keyboard/touch-reachable.
19. Interactive targets 44x44px minimum (48px on mobile nav); press clearance keeps shadows from overlapping neighbors.
20. Marquees/tickers pause on hover AND `:focus-within`; duplicated loop text is `aria-hidden`.
21. Links distinguishable without color (underline or boxed border).
22. Display headlines are real text; page works at 200% zoom; images have explicit dimensions.
23. Landmarks (`header`, `nav[aria-label]`, `main`) and one `h1`; CSS-disabled document outline reads correctly.

## D. Performance

24. Two font families maximum (chunky display + mono), only used weights, `font-display: swap`, subset or locally hosted.
25. Ticker animates `transform` only with `width: max-content` track; press/hover animate `transform`/`box-shadow` only.
26. No `backdrop-filter`, no large blur or gradient paint areas; hard offsets are the cheapest shadow there is.
27. Images have `width`/`height` or `aspect-ratio` (bordered layouts shift badly on late load).
28. CSS stays lean; no framework skin fighting the border/shadow tokens.

## E. Responsive

29. Display scale floors via `clamp()` (hero lands ~2.75rem at 360px, not a shrunken 6rem).
30. Grids collapse to single column under 640px while keeping borders visible.
31. Shadows shrink to `4px 4px` on mobile and `overflow-x: clip` is set on `body`; no horizontal scrollbar from offsets.
32. Nav is a full-width bordered bar or stacked blocks with 48px targets; hamburger only with a keyboard-friendly bordered panel.

---

## 10-point pre-delivery pass

- [ ] 1. Tab the page: every stop shows the 3px offset ink outline; order logical; nothing trapped.
- [ ] 2. Unplug motion (OS reduced-motion): page static; press still communicates via shadow change; tickers become static strips.
- [ ] 3. Run the contrast audit on every text/fill pair including hover and inverted regions; log the ratios.
- [ ] 4. Grep CSS for `gradient`, `rgba`, `blur`, `radius`: every hit is either removed or an explicit, documented token.
- [ ] 5. Zoom 200%: no clipped text inside bordered blocks; no horizontal scroll.
- [ ] 6. Test 360px: single column, borders intact, 4px shadows, nav usable, press clearance respected.
- [ ] 7. State walkthrough per control: hover, focus, active, selected, disabled, error, loading; matches style-guide §8.
- [ ] 8. Sticker audit: count rotations, degrees, overlaps; one accent per region, within -3 to 3 degrees.
- [ ] 9. Broken-page sniff test: screenshot three viewports; roughness must read as authored, borders/spacing consistent.
- [ ] 10. Palette gate: count candy fills. More than 4? Merge before ship.
