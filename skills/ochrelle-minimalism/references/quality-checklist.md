# Minimalism - Quality Checklist

Check every item. **(gate)** items block ship on failure.

---

## A. Art direction

1. **(gate)** Exactly one accent color in the palette; used only for primary action, active state, and focus ring.
2. **Accent budget held:** ≤3 accent appearances per viewport (count buttons, links, badges, icons, charts).
3. **(gate)** Every spacing value traces to the scale (8/16/24/48/96 + optional 4px half-step). No 13px, 27px, 41px arbitrary gaps.
4. Proximity law verified: gap(related) < gap(unrelated) in every component group.
5. One sans-serif family, ≤3 weights loaded (400/500/600 or 400/600/700); tabular figures on numeric tables.
6. Type scale is unmistakable: adjacent hierarchy steps differ by ≥1.25× size or a full weight class.
7. One focal point per viewport: exactly one element at display size or accent color.
8. Radius is a single value (4–8px, or 0 for the strict variant) + pills; no mixed radii.
9. Elevation via hairlines; the one `--shadow-raised` token appears only on true overlays (dropdown/popover/toast).
10. No gradients anywhere in the stylesheet.
11. Imagery is objective and gridded; illustration (if any) is single-weight line art, one color.

## B. Components & states

12. **(gate)** Full state matrix implemented for button, input, nav link, row/card: default, hover, `:focus-visible`, active, disabled, loading, error, empty.
13. **(gate)** Links are underlined at rest (or boxed); hover strengthens the underline rather than introducing it.
14. Disabled controls are solid + labeled (visible reason in copy or `title`), `cursor: not-allowed`, no opacity hack.
15. Nav current page marked by `aria-current="page"` AND a non-color cue (weight/underline bar).
16. Loading states preserve element size (label swap / overlay pattern, no width collapse).
17. Field errors wire `aria-invalid` + `aria-describedby`; message states the fix.
18. Complexity uses progressive disclosure (`<details>`, steps, overflow menus) - not shrunk text.
19. Tables use tabular numerals, right-aligned numbers, sticky header for long tables.

## C. Accessibility

20. **(gate)** All text ≥4.5:1 (WCAG 1.4.3). Muted text uses the floor token (`#5F6368` on white / `#A1A1AA` on dark) or darker - audit every gray.
21. **(gate)** Minimum text size: 16px body, 14px for meta/captions only. Nothing below 14px.
22. **(gate)** Focus visible: `2px solid var(--accent)` + `offset: 2px` on every interactive element; ring contrast ≥3:1 against surroundings.
23. No hover-only information (row actions, tooltips, revealed content all reachable by keyboard/touch).
24. `prefers-reduced-motion: reduce` zeroes transitions; nothing functional depends on motion (accordion state also encoded in `open`/`aria-expanded`).
25. Touch targets ≥44×44px (compact dashboard tier: ≥40px with padded hit areas).
26. Color never the only signal (status pairs color with icon/label; selected states add weight/underline).
27. Page works at 200% zoom and with 150% text scaling; no clipped type in hairline-bordered cards.

## D. Performance

28. Fonts subset and locally hosted where possible; `font-display: swap`; no more than 2 font files per weight group.
29. No large images without `width`/`height` or `aspect-ratio`; hero image is optimized (AVIF/WebP) and lazy-loaded when below the fold.
30. CSS uses the token system without a heavyweight framework fighting it; unused utility classes pruned.
31. Layout animations limited to accordion height with `overflow: hidden`; nothing animates layout on scroll.

## E. Responsive

32. **(gate)** Below 768px: single-column flow, spacing compresses by one step per tier (ratios preserved, not flattened to 8px).
33. Tables adapt on mobile (stacked key-value rows or horizontal scroll with sticky first column) - text never shrinks below 16px to fit.
34. Nav is operable on touch (disclosure with `aria-expanded` or visible list; no hover-dependent menus).
35. Display type floors at ~2.5rem on 360px viewports via `clamp()`; accent budget still holds after buttons wrap.

---

## 10-point pre-delivery pass

1. **The squint test:** blur your eyes - can you still point at the focal element and the primary action? If everything is equal gray, hierarchy failed.
2. **The stranger test:** hand the screen to someone unfamiliar - can they identify every clickable element *without hovering*? Any "what's clickable here?" is an affordance failure.
3. **Gray audit:** grep the CSS for every `color:` value; verify each against 4.5:1 on its actual background; record ratios in the design doc.
4. **Accent count:** screenshot each viewport; count accent occurrences. >3 = demote to neutral.
5. **Spacing trace:** inspect 10 random gaps in DevTools - every value should be a token multiple. Fix strays.
6. **Keyboard walk:** Tab through the page - ring visible everywhere, no skipped controls, logical order, skip-link to main content.
7. **Motion off:** reload with reduced motion enabled - everything instant, nothing essential lost.
8. **State matrix:** walk button/input/nav/row through default→hover→focus→active→disabled→loading→error; compare against style-guide §8.
9. **Zoom + mobile:** 200% zoom and a 360px viewport - no clipped text, no horizontal scroll, targets ≥44px.
10. **Restraint audit:** delete-test - remove any element whose absence loses no information. If you find three, the page was decorated-down, not minimal.
