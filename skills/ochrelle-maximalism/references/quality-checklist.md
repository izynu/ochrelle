# Maximalism - Quality Checklist

Check every item. **(gate)** items block ship on failure.

---

## A. Art direction

1. **(gate)** Anchor neutral covers ≥50% of every viewport (cream or ink ground); hues occupy stated roles against it.
2. Hue count: 4–6 saturated hues, each with one job; no hue introduced for a single element.
3. **(gate)** 2–3 typographic voices with permanent jobs (display / workhorse / annotator; optional rare accent); no voice swaps jobs.
4. Exactly one mega focal element per viewport; nothing else at display size competes for it.
5. Patterns are CSS-first, flat, and live only on surfaces that carry no readable text (bands, grounds, sticker fills).
6. Density is zoned: loud zones cluster (8–16px), calm zones breathe (32–48px); no uniform noise top-to-bottom.
7. Rotation bounds respected: display text ≤4deg, stickers 3–8deg, images ≤6deg, body text 0deg.
8. Shadows are hard ink offsets (or none); no soft blurs anywhere.
9. Border/radius identities are consistent per component (a sticker is 0px+3px ink; a blob card is 24px+; never mixed within one component).
10. Photo treatments are consistent per zone (all duotone or all full-color within a band).

## B. Components & states

11. **(gate)** Full state matrix for button, input, nav link, chip/filter: default, hover, `:focus-visible`, active, disabled, loading, error.
12. **(gate)** Hover fills re-verified for contrast (a hue-swap button must pass in *both* fills).
13. Disabled state uses the dedicated muted pair (`--muted-fill`/`--muted-ink`, ≥4.5:1) - never opacity on rich colors.
14. Selected/filter state communicates via ≥2 channels (fill + rotation/shadow) plus `aria-pressed`/`aria-current`.
15. Loading states preserve size (label swap / pattern sweep on background-position).
16. Error messages sit on solid chips with ≥4.5:1 text - never directly on pattern or hue.
17. Nav stays on solid backing regardless of surrounding noise; current page marked with `aria-current`.
18. Forms: solid-ground inputs, real labels, `aria-invalid` + `aria-describedby` wired.

## C. Accessibility

19. **(gate)** All body text ≥4.5:1 measured against its **island fill** (not the ambient page); large display text ≥3:1 against its actual ground (scrim over photos).
20. **(gate)** Z-scale contract enforced: no decorative layer above `--z-content`; interactive elements at `--z-interactive` (10).
21. **(gate)** `prefers-reduced-motion: reduce` stops marquees, wiggles, and staggers; content fully usable without motion.
22. Decorative layers (patterns, marquee text, sticker clouds) are `aria-hidden="true"` / `alt=""`; meaningful text is never hidden.
23. Focus outlines (3px ink or cobalt, +offset) beat both island fill and ambient pattern; on busy grounds, add the halo treatment.
24. Text never depends on the pattern behind it for meaning; no text over photos without a scrim.
25. Touch targets ≥44px; hover wiggle does not move targets away from the pointer/touch point.
26. Marquee pauses on hover and `:focus-within`; duplicated loop content is `aria-hidden`.
27. Cognitive load: one focal point, zone transitions clearly signaled (band/hue change) - the page is navigable while loud.
28. Works at 200% zoom: islands reflow, collage anchors hold, nothing clips the viewport.

## D. Performance

29. **(gate)** Patterns are CSS gradients (no pattern image requests); grain textures ≤8% opacity and tiny (data-URI/SVG).
30. Collage images: ≤7 per viewport, `srcset` + `sizes`, `width`/`height` set, lazy-loaded below the fold.
31. Motion animates only `transform`, `opacity`, `background-position`; no layout properties.
32. Fonts: ≤4 files total (2–3 voices), subset, `font-display: swap`.
33. `mix-blend-mode` / `clip-path` usage is limited to 1–2 elements per viewport (they are paint-expensive on mobile).

## E. Responsive

34. **(gate)** Below 768px layers are *reduced by design*: overlaps flatten, rotation ≤2deg, stickers inline, hue count per viewport ≤4.
35. Hierarchy survives simplification: mobile still has one focal point, islands, and zone bands.
36. Marquee degrades to static on small/reduced-motion contexts; no autoplaying media walls on cellular.
37. Tap targets and z-order re-verified on mobile (decoration-over-controls bugs surface at narrow widths).

---

## 10-point pre-delivery pass

1. **The rest-stop test:** scan the page top to bottom - is there a calm zone to read in every screen-height? Uniform noise fails.
2. **The ledger:** for each decorative element, name what it does (draws eye / carries voice / organizes). Anything without a job gets deleted.
3. **Contrast on the actual grounds:** measure body text against island fills and headline text against scrims/patterns - record every ratio.
4. **Z-order audit:** tab through the page; confirm focus outlines are never covered by stickers, marquees, or collage cutouts.
5. **Voice check:** list every font loaded and its job; any family used outside its job (or loaded and unused) fails.
6. **Anchor check:** screenshot each viewport and estimate anchor-neutral coverage - below ~50%, the palette vibrates; rebalance.
7. **Motion off:** reduced-motion reload - marquees static, wiggles gone, all content intact.
8. **State matrix:** walk button/input/chip/nav through all states including both hover fills of hue-swap buttons.
9. **Mobile flatten:** 360px viewport - collages flattened, one focal point, ≤4 hues visible, all targets ≥44px, z-order clean.
10. **The chaos sniff test:** show a stranger two screens - can they name the one loudest element per screen? If not, demote until they can.
