# Material Design - Quality Checklist

Ship gate for Material Design. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** Every shadow in the stylesheet matches a level from the elevation table (style-guide §5); zero invented blur/offset combos.
2. **(gate)** One generation per product: M3 pill buttons + M3 radii, or M2 4dp everywhere. No mixing generations.
3. Color ships as verified pairs (role + `on-` partner), not loose swatches; custom seeds have a measured pair table.
4. `--md-outline` is used for borders and dividers only; body text uses `on-surface`/`on-surface-variant`.
5. Radius tokens applied per component family (fields 8, cards 12, sheets 16, buttons/FAB pill); no per-screen exceptions.
6. Icons are one Material Symbols style (filled or outlined), 24dp grid, consistent weight.
7. Dark theme expresses elevation with the surface-container ramp, not shadows.

## B. Components & states

8. **(gate)** Every control implements the §8 matrix: default, hover (8% layer), focus-visible (3px outline + 10%), pressed (10%), disabled (38%/12% spec pattern), error where applicable.
9. **(gate)** State layers use `currentColor` overlays clipped to the control (`position: relative; overflow: hidden`).
10. Ripples animate `transform`/`opacity` only, start from the pointer position, and are removed from the DOM when done.
11. Buttons ship all needed variants (filled/tonal/outlined/text) from the same base class; no one-off button styles.
12. Text fields have floating or top labels, focus moves the indicator to 2dp primary, errors set `aria-invalid` + supporting text.
13. One FAB per screen, docked with margins, never overlapping content; scroll regions reserve space under it.
14. Navigation marks the active destination with the pill/indicator plus `aria-current="page"`.
15. Snackbars/dialogs use live regions or focus management per role; dialogs trap focus and restore it on close.

## C. Accessibility

### Verified pair reference (computed WCAG ratios, M3 baseline)

| Text | Fill | Ratio | Verdict |
|---|---|---|---|
| `#1D1B20` on-surface | `#FFFBFE` surface | 16.65:1 | ✓ body |
| `#49454F` on-surface-variant | `#FFFBFE` | 9.11:1 | ✓ body |
| `#1D1B20` | `#F3EDF7` container | 14.85:1 | ✓ body |
| `#FFFFFF` on-primary | `#6750A4` primary | 6.44:1 | ✓ body |
| `#FFFFFF` | `#B3261E` error | 6.54:1 | ✓ body |
| `#1D1B20` | `#E8DEF8` primary-container | 13.20:1 | ✓ body |
| `#6750A4` | `#E8DEF8` | 4.98:1 | ✓ body (large-safe) |
| `#79747E` outline | `#FFFBFE` | 4.44:1 | ✗ body / ✓ 3:1 borders |

16. **(gate)** All body text 4.5:1; large text 3:1; measure the composite *with* state layers applied.
17. **(gate)** Focus indicator visible on every control: 3px outline, 2px offset, primary (light) / on-surface (dark); never removed (WCAG 2.4.7, 2.4.11).
18. Touch targets 48x48dp minimum, including visually smaller icon buttons (invisible padding extension allowed).
19. `prefers-reduced-motion: reduce` removes ripples/transforms; state changes remain visible via instant layer swaps (WCAG 2.3.3 practice).
20. Dynamic-color seeds verified pair-by-pair with automated contrast tests before shipping themes.
21. Screens have landmarks and one `h1`; nav items expose `aria-current`; icon-only controls carry `aria-label`.
22. Text survives 200% zoom; the role scale uses rem-based sizing, not fixed px-only.

## D. Performance

23. Ripples and state layers touch `transform`/`opacity` only; no layout properties animated.
24. Roboto/Noto self-hosted or `font-display: swap`; weights limited to 400/500/700.
25. Shadows are cheap constant paint; no `backdrop-filter` or large blur regions.
26. Icon set subset (single weight, used glyphs only) rather than the full variable font when payload matters.
27. Elevation changes do not trigger layout; `will-change` used sparingly or not at all.

## E. Responsive

28. Compact: bottom navigation, FAB docked, single column, full-width sheets for dialogs.
29. Medium/expanded: rail replaces bottom bar; list-detail under 840dp content caps; no stretched single lists.
30. Touch targets hold 48dp at every breakpoint; hover layers are pointer-only enhancements.
31. Screens usable at 360px width: no horizontal scroll, FAB does not cover the last row (padding reserved).

---

## 10-point pre-delivery pass

- [ ] 1. Grep the CSS for `box-shadow`: every hit equals a level token; delete orphans.
- [ ] 2. Grep for `rgba(`: state layers (8/10/16%) and scrims only; no decorative translucency.
- [ ] 3. Tab the page: 3px outlines visible everywhere; focus order matches visual order.
- [ ] 4. Measure contrast with state layers composited (hover + focus + pressed) for every control fill.
- [ ] 5. Toggle dark mode: elevation reads correctly from the container ramp; no invisible shadows relied on.
- [ ] 6. Reduced motion on: no ripple, no transform; every state still visibly distinct.
- [ ] 7. Verify the FAB: one per screen, margins correct, no content occlusion at 360px.
- [ ] 8. Walk the §8 matrix per control: hover, focus, pressed, disabled, error, dragged where relevant.
- [ ] 9. Check the generation rule: one button language (pill vs 4dp) across the whole product.
- [ ] 10. Dynamic-color test: force three different seeds and re-run the contrast table; log failures.
