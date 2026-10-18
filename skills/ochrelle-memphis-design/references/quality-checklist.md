# Memphis Design - Quality Checklist

Ship gate for Memphis Design. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** Exactly five flat fills (yellow, lilac, blue, coral, teal) + ink + warm white ground. Count them; no gradients, no translucency, no blur anywhere in the stylesheet.
2. **(gate)** Ink outlines: 3px on interactive elements and small cards, 6px on feature cards; no raised element ships borderless.
3. Shadows are hard offsets only (`4/6/8px Npx 0 0 var(--ink)`); blur is 0; pressed states translate onto the shadow.
4. Patterns (terrazzo, stripes, zigzag, squiggle, dots) live in `aria-hidden` bands 16-64px tall or as container fills behind solid inset panels - never behind live text.
5. Rotation caps: decorative 2-3deg (1deg on mobile), interactive 0deg; one anchored axis-aligned block per section.
6. Two font families maximum: one chunky display (800-900), one clean text sans; body text never uses the display face.

## B. Components & states

7. **(gate)** Buttons, chips, nav links, inputs, toggles, and the modal all define default, hover, `:focus-visible`, active, disabled (and selected/current where applicable) per style-guide section 8.
8. **(gate)** Press interaction: `:active` translates 2px onto the shadow and the shadow shrinks to 2px; selected chips and toggles persist in the pressed position.
9. Disabled components use `#E8E2D6` fill with `#5C584F` text (4.9:1), shadow removed - never opacity hacks.
10. Nav is the ink anchor bar: white links, yellow current-page underline, focus outlines flipped to `#FFF9EF`.
11. Forms wire `aria-invalid` + `aria-describedby` to inline messages; error flag uses the coral 3px border with ink text, never color-only.
12. The modal moves focus in on open, traps Tab, closes on Escape and backdrop click, and restores focus to the opener (recipe A in [references/implementation-examples.md](references/implementation-examples.md)).

## C. Accessibility

### Verified pair reference (computed WCAG ratios)

| Text | Fill | Ratio | Verdict |
|---|---|---|---|
| `#101010` ink | `#FFF9EF` ground | 18.2:1 | ✓ body |
| `#101010` ink | `#FFD23F` yellow | 13.2:1 | ✓ labels |
| `#101010` ink | `#C9B1F5` lilac | 10.1:1 | ✓ labels |
| `#101010` ink | `#4EA8DE` blue | 7.2:1 | ✓ labels |
| `#101010` ink | `#FF6B5B` coral | 6.8:1 | ✓ button labels |
| `#101010` ink | `#0FA3A3` teal | 6.2:1 | ✓ labels (keep bold) |
| `#FFF9EF` ground | `#101010` ink bar | 19.0:1 | ✓ nav |
| `#5C584F` | `#E8E2D6` disabled | 4.9:1 | ✓ disabled only |
| `#FFFFFF` white | teal / coral / lilac / yellow | 2.0-3.1:1 | ✗ never on fills |

13. **(gate)** Every text/fill pair in the shipped page matches a passing row above or a separately measured ≥4.5:1 pair; white text appears only on the ink ground.
14. **(gate)** Focus visible on every interactive element: `outline: 3px solid var(--ink); outline-offset: 3px` (flipped to `#FFF9EF` on ink surfaces); ring contrast ≥3:1.
15. Patterns and stickers are `aria-hidden="true"` and carry no information that lacks a text equivalent.
16. `prefers-reduced-motion: reduce` removes the bounce, hover lifts, and any loop; press feedback survives via the shadow change.
17. Interactive targets ≥44×44px (shadows excluded); rotation never applied to interactive elements (target integrity).
18. Landmarks present (`header`, `nav[aria-label]`, `main`), one `h1`, decorative SVG marked `aria-hidden`, dialog uses `role="dialog"` + `aria-modal` + labelled heading.

## D. Performance

19. Two font families, used weights only, subset with `font-display: swap`.
20. Patterns are pure CSS (repeating-linear-gradient, radial-gradient tiles) - no decorative raster images for flat art.
21. Animations touch `transform`/`box-shadow` only and are finite; no continuous repaint work from loops.
22. Images and decorative SVG carry explicit dimensions so the anchored composition does not shift on load; `overflow-x: clip` on `body`.

## E. Responsive

23. Display clamps to 2.5rem at 360px; hero stacks without the sticker overlapping text.
24. Hard offsets shrink on mobile (3px buttons, 4px cards) and never create horizontal scroll at any width.
25. Pattern bands halve in height on mobile; tap targets stay ≥44px with rotation removed.
26. Modal fits 360px width without scrolling; focus trap verified on a touch keyboard and a hardware keyboard.

---

## 10-point pre-delivery pass

- [ ] 1. Count fills: 5 max. Search the CSS for `gradient` (only pattern recipes allowed), `rgba(0,0,0` (only the modal scrim), `blur`, `rotate` - any hit outside tokens is a defect.
- [ ] 2. Measure every text/fill pair against the C table; no white text on any fill, anywhere.
- [ ] 3. Tab the page: 3px ink outlines visible everywhere, flipped correctly on the ink nav bar.
- [ ] 4. Open and close the modal with keyboard only: focus in, Tab trapped, Escape out, focus returned.
- [ ] 5. Unplug motion: reduced-motion users get zero bounce and zero loops; press still reads via shadow change.
- [ ] 6. Test 360px: no horizontal scroll, shadows contained, pattern bands intact, sticker not overlapping text.
- [ ] 7. Walk the state matrix for button, chip, nav link, input, toggle against style-guide section 8.
- [ ] 8. Confirm every decorative squiggle, band, and sticker is `aria-hidden` and meaningless if removed.
- [ ] 9. Ask the anchor question per section: is there one aligned block holding the composition? Fix floating-chaos layouts.
- [ ] 10. Confirm the joke still lands: screenshot three viewports; if it reads as chaos rather than Memphis, re-anchor and re-cap rotations.
