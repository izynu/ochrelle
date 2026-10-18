# Japandi - Quality Checklist

Ship gate for Japandi. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** Warm grounds only: beige `#F2EDE3` page, `#FAF7F1` cards; no pure white ground, no pure black text.
2. **(gate)** Palette holds: beige/card/charcoal neutrals + muted + two earth accents (clay, moss). No blues, no brights, no gradients.
3. Two font families maximum; display stays light (300-500 weight); labels are uppercase, tracked `0.1em`.
4. Radius 2-4px on components; borders are 1px `--line`; the one diffuse shadow (`0 8px 24px rgba(46,44,40,0.08)`) appears only on overlays or the single lifted element per view.
5. Composition is asymmetric: one mass, one void, one line per view; no mirrored three-column rows; at least one deliberate void per screen.
6. Imagery is matte natural material, warm-graded, asymmetric crops; at most one decorative texture layer, `aria-hidden`.

## B. Components & states

7. **(gate)** Buttons, nav links, inputs, cards, and the accordion all define default, hover, `:focus-visible`, active, disabled (and selected/current where applicable) per style-guide section 8.
8. Primary buttons darken on hover (`#96614A` to `#85543F`), never lighten; active state is a 1px settle.
9. Disabled actions use `#E5DFD3` fill with `#8B857A` text plus `aria-disabled="true"` and a visible explanation nearby - no opacity hacks.
10. Nav marks the current page in clay with a 2px underline offset plus `aria-current="page"`.
11. Forms keep visible labels (never placeholder-only), `autocomplete` on identity fields, and `aria-invalid` + `aria-describedby` wired to the rust error message (`#8F3F2B`, 6.0:1 on card).
12. The accordion uses real `<button>` elements with `aria-expanded`/`aria-controls`, one open at a time, keyboard operable (recipe A in [references/implementation-examples.md](references/implementation-examples.md)).

## C. Accessibility

### Verified pair reference (computed WCAG ratios)

| Text | Fill | Ratio | Verdict |
|---|---|---|---|
| `#2E2C28` ink | `#F2EDE3` beige | 11.9:1 | ✓ body |
| `#2E2C28` ink | `#FAF7F1` card | 13.0:1 | ✓ body |
| `#6A655C` muted | beige / card | 5.0:1 / 5.4:1 | ✓ secondary text (lightest permitted) |
| `#FAF7F1` | `#96614A` clay | 5.1:1 | ✓ primary button |
| `#FAF7F1` | `#85543F` clay-deep | 6.3:1 | ✓ hover state |
| `#FAF7F1` | `#67714E` moss | 5.2:1 | ✓ tags, confirmations |
| `#F2EDE3` | `#3B3833` charcoal | 10.0:1 | ✓ inverted panels |
| `#8F3F2B` error | card | 6.0:1 | ✓ error text |
| `#8B857A` | `#E5DFD3` disabled | 3.3:1 | disabled label only (non-essential) |

13. **(gate)** All body text ≥4.5:1; muted `#6A655C` is the absolute lightest text color in the shipped CSS; anything lighter is a defect.
14. **(gate)** Focus visible everywhere: `outline: 2px solid var(--ink); outline-offset: 3px`, flipped to `#F2EDE3` on charcoal surfaces; ring contrast ≥3:1 on every surface it crosses.
15. Links are underlined; hover changes thickness or color, never the only cue.
16. `prefers-reduced-motion: reduce` collapses the 220ms fades and the accordion settle animation to instant states.
17. Imagery alt text names material and moment; decorative textures and voids are `aria-hidden` or empty alt.
18. Landmarks and heading outline present (`header`, `nav[aria-label]`, `main`, `footer`); one `h1`; whitespace never replaces document structure.

## D. Performance

19. Two families, used weights only, `font-display: swap`; no heavy icon font (stroke SVGs or text glyphs instead).
20. Images sized explicitly (`width`/`height`/`aspect-ratio`), `object-fit: cover` for crops, lazy-loaded below the fold.
21. Motion budget: a handful of 220ms transitions; no scroll listeners doing animation work.
22. No gradient rasters, no `backdrop-filter`; the paper-grain layer (if used) is a tiny tiled PNG or pure CSS at ≤5% opacity.

## E. Responsive

23. h1 clamps to 2rem at 360px; measure holds 60-72ch via ch-based columns; no horizontal scroll at any width.
24. Hero stacks below 768px with the figure ordered first; the void survives as breathing room rather than vanishing.
25. Section air scales down proportionally (128 to 96 to 64) instead of collapsing to cramped stacks.
26. Tap targets ≥44px (buttons, nav links, accordion rows) verified on a real touch viewport.

---

## 10-point pre-delivery pass

- [ ] 1. Tab the page: 2px charcoal outlines visible on every stop; on charcoal surfaces the ring flips to beige.
- [ ] 2. Keyboard-test the accordion: Enter toggles, one open at a time, focus stays sensible.
- [ ] 3. Audit every text/fill pair against the C table; grep the CSS for any gray lighter than `#6A655C`.
- [ ] 4. Unplug motion: reduced-motion users get instant fades; nothing animates, nothing loops.
- [ ] 5. Read a full screenful at 100% zoom: measure, rhythm, and quiet hold; muted text never used for primary copy.
- [ ] 6. Check every image: matte, warm-graded, alt text names material and moment, no layout shift on load.
- [ ] 7. Count gradients (target: zero CSS gradients outside optional grain), blues (zero), radii over 4px (zero outside imagery).
- [ ] 8. Walk the state matrix for button, nav link, input, accordion row against style-guide section 8.
- [ ] 9. Test 360px and 200% zoom: voids breathe, no clipped text, no horizontal scroll.
- [ ] 10. Ask the stillness question: does this page feel like a warm, quiet room, or a gray template with a plant photo? Fix composition or tokens either way.
