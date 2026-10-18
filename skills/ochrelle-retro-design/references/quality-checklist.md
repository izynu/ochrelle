# Retro Design - Quality Checklist

Ship gate for retro mid-century Americana design. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** The ground is cream `#F7EFD9` (or `#FFFDF5` panels); no pure-white page, no cool gray. Ink is warm brown `#3D2B1F`, never `#000000`.
2. **(gate)** Palette discipline: cream ground + at most 4 period fills (burnt orange, mustard, avocado, cherry). Count them; a fifth saturated color fails the gate.
3. Borders are 2px solid ink on cards, inputs, and buttons; the letterpress slab (`0 3px 0 rgba(61,43,31,0.35)`) is the only everyday shadow.
4. Exactly one groovy display face and one text face; labels are uppercase, tracked `0.08em`. No third family anywhere.
5. One starburst per viewport, one badge per card, badges rotated no more than 4deg; halftone dots and dotted leaders exist only in decorative bands and name-price joins.

## B. Components & states

6. **(gate)** Buttons, inputs, nav links, tabs, and cards all define: default, hover, `:focus-visible`, active, disabled (and selected for tabs/chips) - per the matrix in style-guide section 8.
7. **(gate)** Press interaction is the letterpress: `:active` translates down and the slab shrinks from `0 3px 0` to `0 1px 0`.
8. Disabled components use solid `#E7DFC8` fill with `#6B5138` text (about 5.2:1), slab removed - never an opacity hack.
9. Nav marks the current page with the accent underline plus `aria-current="page"` (two cues, not color alone).
10. Menu rows use the dotted-leader pattern; interactive rows keep 44px minimum height.
11. Forms wire `aria-invalid` and `aria-describedby` to an inline error message; the message text (`#8F2424`, about 6:1 on cream) is never color-only.
12. Tabs implement roving tabindex with ArrowLeft/ArrowRight/Home/End, `aria-selected`, and `hidden` panels (recipe A in [references/implementation-examples.md](references/implementation-examples.md)).

## C. Accessibility

### Verified pair reference (computed WCAG ratios)

| Text | Fill | Ratio | Verdict |
|---|---|---|---|
| `#3D2B1F` ink | `#F7EFD9` cream | 11.7:1 | ✓ body |
| `#3D2B1F` ink | `#FFFDF5` paper | 13.2:1 | ✓ body |
| `#6B5138` muted | cream | 6.4:1 | ✓ secondary text |
| `#FFFDF5` cream | `#AD4E1A` burnt orange | 5.4:1 | ✓ button label |
| `#3D2B1F` ink | `#D9A404` mustard | 5.9:1 | ✓ burst label |
| `#FFFDF5` cream | `#6B7C33` avocado | 4.6:1 | ✓ labels (AA body, barely - keep bold) |
| `#FFFDF5` cream | `#A32E2E` cherry | 7.0:1 | ✓ flags and badges |
| `#FFFFFF` white | mustard | 1.9:1 | ✗ never |
| `#3D2B1F` ink | burnt orange | 2.5:1 | ✗ never |

13. **(gate)** Every text/fill pair in the shipped page matches a passing row above or a separately measured ≥4.5:1 pair (3:1 for large text only).
14. **(gate)** Focus visible on every interactive element: `outline: 3px solid var(--ink); outline-offset: 3px`; ring contrast ≥3:1 against adjacent colors.
15. `prefers-reduced-motion: reduce` removes hover lifts, burst rotation, and stops any ticker entirely.
16. No text over halftone or textured regions; decorative art is `aria-hidden="true"`.
17. Links are underlined in body copy; interactive targets ≥44×44px; the page works at 200% zoom without clipped badge labels.
18. Landmarks present (`header`, `nav[aria-label]`, `main`), one `h1`, heading order logical.

## D. Performance

19. Display font is subset and locally hosted or `font-display: swap`; at most 2 families and only used weights.
20. Halftone and burst effects are pure CSS (radial-gradient, clip-path) - no decorative images for flat art.
21. Images have explicit `width`/`height` or `aspect-ratio`; hero art is lazy-loaded below the fold only.
22. No gradients, blur stacks, or `backdrop-filter` outside the single modal shadow; animations touch `transform`/`box-shadow` only.

## E. Responsive

23. Display clamps to 2.5rem at 360px; hero stacks with the burst above or beside copy without overlap.
24. Menu-board collapses to one column below 768px; nav becomes a stacked tracked-uppercase list with 44px rows.
25. Badges shrink to 64-104px on mobile and never overflow their card or the viewport; `overflow-x` stays clean.

---

## 10-point pre-delivery pass

- [ ] 1. Tab the page keyboard-only: every stop shows the 3px offset outline; menu rows and tabs are reachable in order.
- [ ] 2. Enable OS reduced motion: lifts, burst rotation, and any ticker are fully static; press feedback survives via the slab change.
- [ ] 3. Audit every text/fill pair against the C table; record measured ratios for any pair not listed.
- [ ] 4. Zoom to 200%: no clipped burst labels, no broken dotted leaders, no horizontal scroll.
- [ ] 5. Test at 360px: single-column menu board, 44px rows, badges contained, nav stacked and usable.
- [ ] 6. Count saturated fills: 4 max. Count display faces: 1. Count starbursts per viewport: 1.
- [ ] 7. Walk the state matrix (hover, focus, active, disabled, error, selected) for button, input, tab, nav link against style-guide section 8.
- [ ] 8. Confirm decorative art (`aria-hidden`) contains no information that exists nowhere else in text.
- [ ] 9. Screenshot three viewports and ask: does this read as one era, one hand - or a costume? Fix drift either way.
- [ ] 10. Check the dots: dotted leaders and halftone bands render at every breakpoint, and no dot grid ever sits under body text.
