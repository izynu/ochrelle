Ship gate for vaporwave. Every item must pass before delivery.

## A. Art direction

- [ ] The night base owns the view: `--bg`/`--panel` cover roughly 70% of pixels; accents are spent on actions, focus, prices and display type only.
- [ ] Magenta/pink and violet hues appear as historically correct genre content, always through the measured pairings (pink text 7.26:1 on base, `#26061F` on pink fills 7.54:1, violet reserved for large text/UI strokes at 5.50:1).
- [ ] One statuary focal element (bust, column) and one obsolete-tech artifact per view, composed with a ground cue; nothing floats unprompted.
- [ ] Chrome display type uses the 5-7 stop gradient with the light band at 50-54% and is 32px bold minimum with a solid-ink `@supports` fallback.
- [ ] VHS texture is present but restrained: static scanlines at 3-4% white, chroma offset shadows on display type only, one tracking-bar burst per interaction maximum.
- [ ] Win95-style pastiches use beveled box-shadows, not rounded corners; the rest of the UI uses 8-12px radii and pill buttons.
- [ ] Every visual is original: no real brand UI assets, no unlicensed stills, no sampled artwork.

## B. Components & states

- [ ] Buttons: solid pink fill with `#26061F` label (7.54:1) and soft glow; ghost buttons are 1px cyan outlines; press is a 1px dip plus glow change.
- [ ] All controls implement default, hover, active, focus-visible and disabled, distinct without color alone.
- [ ] Nav links are mono with underline on the active item; the sunset strip is decorative and never the only active indicator.
- [ ] Tiles/cards are `--panel` plates with 1px white-alpha borders; hover lifts border to violet, never animates blur or filter.
- [ ] Inputs are `--bg` filled with 1px violet borders, visible labels, mono helper text; error state uses `--alert` border plus an `--ink` message at 16.16:1.
- [ ] Prices, timestamps and system text render in mono with tabular numerals in `--ink-soft` (10.06:1+) or `--mint` (13.76:1).

## C. Accessibility

- [ ] Text contrast verified per pairing: `#F6F1FF` on `#1B1035` 16.16:1, `#C9BCE4` 10.06:1, `#FF71CE` 7.26:1, `#01CDFE` 9.53:1; small body text never uses `#B967FF` (5.50:1 is large-text/UI only). WCAG 2.2 AA 1.4.3.
- [ ] Non-text contrast: focus outlines, input borders, underlines and icon strokes reach 3:1 against adjacent surfaces (1.4.11).
- [ ] `:focus-visible` is the 2px `#01CDFE` outline with 2px offset on every control; glow never substitutes for focus indication.
- [ ] Motion safety: nothing flashes more than 3 times per second (2.3.1); glitch bursts are one-shot 300-900ms on user action, never ambient loops.
- [ ] `prefers-reduced-motion`: all loops stop, glitch renders one static frame, entrances become 150ms opacity fades, layout unchanged.
- [ ] Japanese strings carry `lang="ja"`; meaningful ones have an English equivalent nearby; decorative ones are `aria-hidden="true"`.
- [ ] Chrome gradient text remains real DOM text (never images) and its `@supports` fallback renders solid `--ink`.
- [ ] Decorative scene layers (sun, grid, scanlines, bust) are `aria-hidden`; state meaning is always in text.

## D. Performance

- [ ] Scene layers are CSS gradients/masks; no full-bleed hero bitmaps without AVIF/WebP + gradient fallback.
- [ ] Animated properties limited to `transform`, `opacity`, `box-shadow`; zero transitions on `filter` or `backdrop-filter` (grep confirms).
- [ ] At most two ambient loops visible at once, both 6s+ and opacity/transform only.
- [ ] Scanline overlays use `repeating-linear-gradient` on pseudo-elements with `pointer-events: none`, not tiled images.
- [ ] Fonts: system stacks or two weights max; no 300KB display fonts for one headline.

## E. Responsive

- [ ] No horizontal scroll at 320px; scene wrapper uses `overflow: hidden` with 16px content edges.
- [ ] Display type scales via `clamp()` to a 32px floor without mid-word wrapping.
- [ ] Tiles collapse 3 -> 2 -> 1 columns at 1080/768/480; text panels are the last layer sacrificed.
- [ ] Below 480px the scene compresses to a sunset strip plus horizon; grid and checkerboard may drop, panels never.
- [ ] Touch: glitch bursts fire on press; no information is hover-gated; targets are 44x44px.
- [ ] Contrast re-verified at mobile widths where panels densify over scene layers.

---

## 10-point pre-delivery pass

1. **Palette audit**: base/panels at ~70% of pixels; accent hues follow the budget (pink actions, cyan links/focus, mint prices, violet structure).
2. **Contrast run**: measure every text pairing including pink-fill buttons and mint prices; small text stays out of the violet zone.
3. **Chrome audit**: display type is 32px+ bold, real text, with the solid-ink fallback verified in a non-supporting engine.
4. **Prop audit**: bust + artifact + texture per view, all original drawings; zero borrowed brand assets.
5. **State sweep**: tab through controls; the cyan outline is visible on panels, base and scene; hover/press/disabled distinct.
6. **Motion audit**: count ambient loops (max 2), confirm glitch is action-triggered and one-shot; enable reduced motion and verify a static, usable page.
7. **Flash check**: scan all animations for >3 flashes/second; none pass.
8. **Language audit**: `lang="ja"` present on Japanese strings; ornament is `aria-hidden`; meaning available in English.
9. **Mobile pass**: 375px and 320px: no overflow, chrome text scales to the 32px floor, panels keep 16px edges, targets 44px.
10. **Mood check**: deadpan nostalgia reads in copy and composition; the page is not a generic neon-rave template.
