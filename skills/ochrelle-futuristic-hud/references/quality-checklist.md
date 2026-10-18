# Futuristic HUD - Quality Checklist

Ship gate for futuristic HUD interfaces. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** Ground is near-black `#05080D` with panels `#0B141F`; no purple/blue gradient backdrops, no star-field PNGs.
2. **(gate)** Palette discipline: cyan family + amber + alert + ok only; every colored element carries a status meaning; no decorative fourth hue.
3. Chamfered corners and/or corner brackets on panels and primary controls; radius 0-2px elsewhere.
4. Glow tokens applied only to panel borders, headers, and the system name; zero `text-shadow` on body, data, or label text; zero `filter: drop-shadow` blurs.
5. Two families max: monospace for data, squared sans for labels; values align monospace-to-monospace (no digit jitter).
6. Scanlines and grid hairlines live in dedicated decorative bands or under ≤5% overlays, never under live text.

## B. Components & states

7. **(gate)** Buttons, nav links, inputs, status chips, and steppers all define default, hover, `:focus-visible`, active, disabled (and current where applicable) per style-guide section 8.
8. **(gate)** State changes snap at 200ms; continuous animation exists only on `aria-hidden` decoration (radar, scanlines, blips) and is paused on hover and `:focus-within`.
9. Disabled controls use panel fill with `--dim` text (7.1:1) and `--grid` borders - data stays readable, interactivity leaves.
10. Nav marks the current zone with hud color plus a 2px underline (`aria-current="page"`); two cues, never color alone.
11. Status is never color-only: every chip carries a text word (NOMINAL / CAUTION / ALERT) and updates inside `role="status"` containers.
12. Forms wire `aria-invalid` + `aria-describedby` to the ALERT-prefixed message (8.0:1); micro-labels stay visible above inputs.
13. The power console (or equivalent stepper UI) disables at limits, keeps 44px targets, and announces changes via `aria-live="polite"` (recipe A in [references/implementation-examples.md](references/implementation-examples.md)).

## C. Accessibility

### Verified pair reference (computed WCAG ratios)

| Text | Fill | Ratio | Verdict |
|---|---|---|---|
| `#7FE9FF` hud | `#05080D` bg | 14.3:1 | ✓ primary text |
| `#7FE9FF` hud | `#0B141F` panel | 13.2:1 | ✓ panel text |
| `#EAF6FF` bright | bg | 18.3:1 | ✓ emphasis |
| `#8AA3B8` dim | bg / panel | 7.7:1 / 7.1:1 | ✓ labels, units |
| `#FFC069` amber | panel | 11.5:1 | ✓ caution |
| `#FF7B72` alert | bg | 8.0:1 | ✓ alerts |
| `#6EE7A0` ok | panel | 12.0:1 | ✓ confirmed |
| `#05080D` dark | `#19C8DE` fill | 9.9:1 | ✓ button labels |
| `#12202E` grid | bg | 1.2:1 | decorative only |

14. **(gate)** Every text pairing matches a passing row above or a separately measured ≥4.5:1 pair measured with glow OFF; no legibility depends on glow.
15. **(gate)** Focus visible on every interactive element: `outline: 2px solid var(--hud); outline-offset: 3-4px`, flipped to `#05080D` on cyan fill; the offset clears the chamfer cut.
16. Radar, sweep, blip, and scanline layers are `aria-hidden`; the radar container carries a text `aria-label` describing contacts.
17. `prefers-reduced-motion: reduce` stops sweeps and pulses; the radar degrades to a static needle; transitions collapse to instant.
18. Live telemetry uses `aria-live="polite"` on value containers only (never the whole panel); frequent updates do not flood screen readers.
19. Interactive targets ≥44×44px despite chamfers; 360px view keeps `overflow-x` clean; dense telemetry scrolls within its panel.
20. Landmarks (`header`, `nav[aria-label]`, `main`), one `h1`, heading order logical; the canopy never replaces document structure.

## D. Performance

21. Two families, used weights only, `font-display: swap`; monospace is a system stack by default (zero font cost).
22. Radar, brackets, and grid are pure CSS (`conic-gradient`, borders, layered gradients) - no canvas loops, no rasters, no video.
23. Animations touch `transform`/`opacity` only and run at most a handful of instances; nothing animates offscreen or loops in hidden panels.
24. No `backdrop-filter`, no blur filters beyond the two glow tokens, no box-shadow stacks on scroll-heavy surfaces.

## E. Responsive

25. Panels stack below 768px; system bar condenses to name + one status chip; chamfers shrink to 10px.
26. Data rows never wrap mid-value (`white-space: nowrap` on values); units drop to a second line instead of truncating.
27. Radar shrinks to a ≤160px widget or hides on mobile without losing information (the target list carries the same data in text).
28. Verified at 360px and 200% zoom: no horizontal scroll, no clipped descenders inside chamfers, no focus ring clipping.

---

## 10-point pre-delivery pass

- [ ] 1. Grep the CSS for `text-shadow` (headers/system name only), `drop-shadow`, `backdrop-filter` (zero), and any hue outside cyan/amber/red/green/dim.
- [ ] 2. Re-measure every text pair with glow disabled; record ratios; no pair below 4.5:1.
- [ ] 3. Tab the page: 2px cyan outlines everywhere, flipped to dark on cyan fill, never clipped by chamfers.
- [ ] 4. Keyboard-test the power console: steppers enable/disable at limits, values announce politely, total never exceeds cap.
- [ ] 5. Unplug motion: sweeps stop (static needle remains), pulses gone, blips static; no information lost.
- [ ] 6. Hover and focus the radar container: sweep pauses; resume on leave.
- [ ] 7. Walk the state matrix for button, ghost button, nav link, input, chip, stepper against style-guide section 8.
- [ ] 8. Confirm status semantics: no state conveyed by color alone; live regions scoped to values only.
- [ ] 9. Test 360px and 200% zoom: panels stack, values never truncate, chamfers keep 44px targets, no horizontal scroll.
- [ ] 10. Ask the instrument question: does every glowing thing carry data or frame it? If decoration glows without meaning, strip the glow.
