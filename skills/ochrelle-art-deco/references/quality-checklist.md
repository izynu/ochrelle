# Art Deco - Quality Checklist

Ship gate for Art Deco. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** Ivory `#F2EBDA` ground, warm near-black `#211D16` structure, metallic gold `#D4AF37` drawn as line; no pure white, no pure black, no gradients anywhere.
2. **(gate)** Jewel discipline: at most two of emerald, midnight, oxblood per view; champagne for bands and hovers.
3. Radius 0 on every component; curves are constructed arcs (fans, arches), never `border-radius`.
4. Double hairline frames wrap every content block; stepped corners appear at most once per card; one sunburst per view.
5. Two families max: one geometric marquee display face, one geometric sans; labels uppercase tracked `0.18em`. No cursive, no script.
6. Symmetry holds: centered masthead and title blocks, equal gutters, mirrored columns where columns exist.

## B. Components & states

7. **(gate)** Buttons, nav links, tabs, inputs, and cards all define default, hover, `:focus-visible`, active, disabled (and selected/current where applicable) per style-guide section 8.
8. Button hover is a fill step (midnight to emerald to oxblood), not a color fade with easing tricks; transitions are 180ms and even.
9. Disabled controls use `#E7E0CD` fill with `#6E6353` text (5.5:1), gold frame intact - never opacity hacks.
10. Nav marks the current page with the deep-gold underline plus `aria-current="page"` (two cues, not color alone).
11. Forms wire `aria-invalid` + `aria-describedby` to the oxblood chip message (ivory text on oxblood, 10.3:1); never color-only.
12. Tabs implement roving tabindex with ArrowLeft/ArrowRight/Home/End, `aria-selected`, and `hidden` panels (recipe A in [references/implementation-examples.md](references/implementation-examples.md)).

## C. Accessibility

### Verified pair reference (computed WCAG ratios)

| Text | Fill | Ratio | Verdict |
|---|---|---|---|
| `#211D16` ink | `#F2EBDA` ivory | 14.1:1 | ✓ body |
| `#211D16` ink | `#FBF7EC` card | 15.7:1 | ✓ body |
| `#6E6353` muted | ivory / card | 5.0:1 / 5.5:1 | ✓ secondary text |
| `#FBF7EC` ivory | `#1F2A44` midnight | 13.3:1 | ✓ buttons, bands |
| `#D4AF37` gold | midnight / ink | 6.8:1 / 8.0:1 | ✓ gold text on dark only |
| `#7E5E10` deep gold | ivory | 5.1:1 | ✓ gold text on light |
| `#FBF7EC` ivory | `#1D5C4D` emerald | 7.3:1 | ✓ panels |
| `#FBF7EC` ivory | `#6B2230` oxblood | 10.3:1 | ✓ errors, emphasis |
| `#D4AF37` gold | `#F2EBDA` ivory | 3.0:1 | ✗ never as text |

13. **(gate)** Every text/fill pair matches a passing row above or a separately measured ≥4.5:1 pair; metallic gold text never appears on ivory or card.
14. **(gate)** Focus visible on every interactive element: `outline: 2px solid var(--ink); outline-offset: 3px`, flipped to `#FBF7EC` on midnight/emerald/oxblood surfaces; ring contrast ≥3:1.
15. Ornament (fans, chevrons, stepped corners, sunburst dividers) is `aria-hidden="true"` and carries no information.
16. No text over ornament bands; body text sits on flat ivory, card, or jewel ground only.
17. `prefers-reduced-motion: reduce` collapses all transitions and the one-time fan animation.
18. Links underlined; interactive targets ≥44×44px; page works at 200% zoom without frame text clipping.
19. Landmarks (`header`, `nav[aria-label]`, `main`), one `h1`, heading order logical.

## D. Performance

20. Two families, used weights only, subset with `font-display: swap` (display faces are heavy - subset rigorously).
21. All ornament is CSS (`repeating-conic-gradient`, layered `linear-gradient`) - no decorative raster PNGs for fans or chevrons.
22. Images have explicit `width`/`height` or `aspect-ratio`; symmetric facade layouts must not shift on late load.
23. No `backdrop-filter`, no glow filters, no animated gradients; transitions touch `background`/`border-color`/small transforms only.

## E. Responsive

24. Display clamps to 2.25rem at 360px; double frames keep 16px minimum page gutters, symmetric left/right.
25. Nav stacks to a centered list below 640px with the sunburst divider retained; 44px rows.
26. Ornament bands shrink (48 to 24px) without disappearing; stepped corners reduce to one per card on mobile.
27. Jewel bands and framed cards never overflow the viewport; `overflow-x` clean at every width.

---

## 10-point pre-delivery pass

- [ ] 1. Grep the CSS for `gradient` (only conic fans and stepped-corner strips allowed), `radius` (only 0), `glow`/`drop-shadow` (zero hits), `opacity` (zero hits on controls).
- [ ] 2. Measure every text/fill pair against the C table; gold-on-ivory must show zero instances.
- [ ] 3. Tab the page: 2px outlines visible on ivory and flipped on jewel grounds; nothing trapped.
- [ ] 4. Keyboard-test the programme tabs: arrows move, Home/End jump, panels toggle, focus follows.
- [ ] 5. Unplug motion: reduced-motion users get instant state steps; the fan (if animated) never runs.
- [ ] 6. Zoom to 200% and test 360px: frames intact, no clipped display type, no horizontal scroll.
- [ ] 7. Walk the state matrix for button, tab, nav link, input against style-guide section 8.
- [ ] 8. Confirm symmetry: screenshot three viewports and fold a sheet down the middle - masses should balance.
- [ ] 9. Count families (2), jewel tones per view (2 max), sunbursts per view (1).
- [ ] 10. Ask the facade question: does it read as engineered 1930s glamour, or as a party flyer? Fix gradient bling, script fonts, or ornament noise either way.
