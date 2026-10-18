# Brutalism & Neo-Brutalism - Quality Checklist

Check every item. Items marked **(gate)** must pass before delivery; failure of any gate item blocks ship.

---

## A. Art direction

1. **(gate)** Border radius is `0` on every component - no exceptions, no single rounded card.
2. **(gate)** All shadows are hard offsets with `0` blur (`Xpx Ypx 0 0 var(--ink)`); zero `rgba()` shadows or `filter: blur()` anywhere in the stylesheet.
3. Border widths follow the declared system (`--bw` 3px outer / `--bw-thin` 2px inner for neo; a stated pattern for classic) - no accidental 1px borders from browser defaults; text, borders, and shadows share one ink value (no `#333` drift).
4. Palette holds: 1 anchor neutral + at most 4 saturated flat fills for neo; 1 primary (+1 secondary max) for classic. No gradients, no translucency.
5. Decorative patterns (stripes) are flat, hard-edged, ink-colored - no soft or multicolor textures; sticker badges (if used) rotate within −3° to 3° and keep their 2–3px border.

## B. Components & states

6. **(gate)** Every interactive component defines the full state matrix: default, hover, `:focus-visible`, `:active`, disabled, and (where applicable) selected/pressed - see style-guide §8.
7. **(gate)** Press interaction is mechanical: `:active` translates onto the shadow and the shadow shrinks by the same offset (e.g. 6px→4px with 2px translate).
8. Disabled components use solid muted fills with ≥4.5:1 text - never `opacity` hacks below readable contrast.
9. `[aria-pressed="true"]` / selected state mirrors the pressed position (translated, shadow removed) persistently.
10. Loading states swap label content (e.g. mono `LOADING…` + striped band) without changing component size (no layout shift).
11. Error states use border color + inline message; the message itself meets 4.5:1 and is never color-only.
12. Nav links expose current location (`aria-current="page"` + inversion or other non-color cue).
13. Forms use real `<label>`, `autocomplete`, and `aria-invalid`/`aria-describedby` wiring for errors.

## C. Accessibility

### Verified pair reference (computed WCAG ratios for the example palette)

| Text | Fill | Ratio | Verdict |
|---|---|---|---|
| `#000` | `#FFFDF5` paper | 20.6:1 | ✓ body |
| `#000` | `#FFDB58` sun | 15.5:1 | ✓ body |
| `#000` | `#4ECDC4` mint | 10.9:1 | ✓ body |
| `#000` | `#FF6B6B` coral | 7.6:1 | ✓ body |
| `#000` | `#FF4D00` accent | 6.3:1 | ✓ body |
| `#000` | `#2563EB` mid-blue | 4.1:1 | ✗ normal / ✓ ≥18.66px bold (3:1) |
| `#FFF` | `#FFDB58` sun | 1.4:1 | ✗ never |
| `#FFF` | `#FF6B6B` coral | 2.8:1 | ✗ normal only if ≥24px/18.66px bold |
| `#FFF` | `#000` ink ground | 21:1 | ✓ body |

14. **(gate)** All body-size text meets 4.5:1 (WCAG 2.1 AA 1.4.3); large bold text (≥18.66px bold / 24px) meets 3:1. Measure the actual palette combos - use the pair reference above for the example palette.
15. **(gate)** Focus is visible on every focusable element: `outline: 3px solid var(--ink); outline-offset: 3px` (or paper ink in inverted sections) - focus rings are enlarged, never removed.
16. Focus ring contrast against adjacent backgrounds is ≥3:1 (WCAG 2.4.11 / 1.4.11).
17. No information is conveyed by hover alone; disclosures use `<details>`/buttons operable by keyboard and touch.
18. `prefers-reduced-motion: reduce` removes the press transform and stops marquees/tickers entirely (they degrade to static strips).
19. Interactive targets are ≥44×44px; thick borders are not counted as padding.
20. Marquees pause on hover AND `:focus-within`; duplicated loop copies are `aria-hidden`.
21. Links are distinguishable without color (underline present, or bordered/boxed link style).
22. Oversized display text is real text (no SVG/image headlines) so it scales with user font-size settings; page still works at 200% zoom.
23. Screen-reader landmarks exist (`header`, `nav[aria-label]`, `main`) - raw aesthetics never excuse missing document structure.

## D. Performance

24. Fonts are limited to ≤2 families with only the weights used; heavy display fonts are subset or locally hosted; `font-display: swap` is set.
25. The ticker (if used) animates only `transform` (compositor-friendly) and its track is `width: max-content` - no layout-thrashing keyframes.
26. Images have explicit `width`/`height` or `aspect-ratio` (brutalist layouts shift badly on late image load).
27. No shadow/gradient-heavy effects that trigger paint on scroll; hard offsets are cheap - keep it that way (no `backdrop-filter` snuck in).
28. Total custom CSS stays lean; no component library overrides fighting the token system.

## E. Responsive

29. Display sizes scale via `clamp()` with sane floors (hero lands ~2.5–3rem on 360px, not a shrunken 6rem).
30. Exposed grids collapse to single column below 768px while *keeping borders* so structure remains visible.
31. Hard offsets shrink to 4px on mobile and `overflow-x: clip` is on `body` - no horizontal scrollbar from a 6px shadow poking out.
32. Tap targets and press shadows verified on real touch viewport (no shadow-induced overlap of neighbors).

---

## 10-point pre-delivery pass

1. **Tab the whole page** with keyboard only: every stop visible with a 3px offset outline; nothing trapped; order logical.
2. **Unplug motion**: reload with OS reduced-motion on - page fully static, no moving ticker, press still communicates via shadow change.
3. **Run the contrast audit** on every text/background pair (including accent fills and inverted sections) - record the ratios.
4. **Zoom to 200%**: no clipped text inside bordered blocks, no horizontal scroll except intentional overflow.
5. **Test at 360px width**: grid collapsed, borders intact, shadows at 4px, nav usable.
6. **Consistency sweep**: search the CSS for `radius`, `rgba`, `blur`, `opacity` - any hit outside the token definitions is a defect.
7. **State matrix walkthrough**: hover → focus → active → disabled → error → loading for button, input, nav link, card CTA. Compare against style-guide §8.
8. **Broken-page sniff test**: screenshot 3 random viewports and ask "does this look authored-rough or buggy?" - inconsistent borders/spacing must be fixed either way.
9. **Structure check**: landmarks, heading order (one `h1`), form labels, `aria-current` - the document outline reads correctly with CSS disabled.
10. **Palette gate**: count saturated fills. More than 4 (neo) or more than 2 (classic)? Remove or merge before ship.
