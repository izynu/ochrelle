# Cyberpunk - Quality Checklist

Ship gate for cyberpunk. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** Darkness budget holds: at least 90% of every view is dark surface; neon accents stay under ~10% of pixels.
2. **(gate)** At most 2 neon hues carry meaning per view (cyan interactive + one data/alert hue); hue roles never switch (cyan = interactive, magenta = alert, yellow = data).
3. Surfaces are blue-cast near-blacks from the token set; no pure `#000` grounds, no random grays.
4. Radius 0-2px; at most one `clip-path` corner cut per view; no pills, no soft blobs.
5. Scanlines/grain sit below content at 3-4% opacity; at most one hero glow element per viewport.
6. Effects are diegetic and quiet: no neon fills on large surfaces, no emboss, no soft drop-shadow elevation.
7. Mono layer (labels, readouts, prompts) frames the sans body layer; uppercase only on labels.

## B. Components & states

8. **(gate)** Every control implements the §8 matrix: default, hover, `:focus-visible`, active, selected, disabled, error, loading.
9. **(gate)** Neon fills always carry dark `#0B0F14` labels (verified 5.31:1+); hover fills flip label to `--bg` (12.02:1 on cyan).
10. Disabled states keep readable labels (`#7B8794` floor, 5.25:1) and lose the glow, never opacity-fade below AA.
11. Errors pair magenta border with mono `ERR:` text + `aria-invalid`/`aria-describedby`; never color-only.
12. Status badges pair a word (`OK`/`WARN`/`ERR`) with the fill; the log uses `role="log"` + `aria-live="polite"` and is capped in length.
13. Play/toggle state uses `aria-pressed` + label text; progress uses `role="progressbar"` with live `aria-valuenow`.
14. Nav exposes the active destination with the `>` glyph + cyan + `aria-current="page"`.

## C. Accessibility

### Verified pair reference (computed WCAG ratios against `#0B0F14`)

| Text | Fill | Ratio | Verdict |
|---|---|---|---|
| `#E8F0F2` ink | `#0B0F14` bg | 16.64:1 | ✓ body |
| `#E8F0F2` | `#121821` surface | 15.43:1 | ✓ body |
| `#8FA3B0` muted | `#0B0F14` | 7.35:1 | ✓ body |
| `#7B8794` floor | `#0B0F14` | 5.25:1 | ✓ body (absolute floor) |
| `#2DE2E6` cyan | `#0B0F14` | 12.02:1 | ✓ body |
| `#F6E71D` yellow | `#0B0F14` | 14.98:1 | ✓ body |
| `#FF2A6D` magenta | `#0B0F14` | 5.31:1 | ✓ body (use for emphasis) |
| `#FF9E64` orange | `#0B0F14` | 9.45:1 | ✓ body |
| `#0B0F14` ink | `#2DE2E6` fill | 12.02:1 | ✓ labels on neon fills |
| `#7B8794` | `#2A3442` chrome-line | ~1.4:1 | decorative only, never text |

15. **(gate)** All body text 4.5:1; large text 3:1; re-measure with glow, scanline overlay, and duotone imagery composited (WCAG 1.4.3).
16. **(gate)** Focus visible on every control: 2px solid cyan (or yellow on cyan-heavy regions) outline with offset; glow never substitutes (WCAG 2.4.7, 2.4.11).
17. Informational borders/rings hit 3:1 against their adjacent surface (WCAG 1.4.11); `--chrome-line` is decorative only.
18. Body text never glows; accent glow keeps 4.5:1 at the rendered edge.
19. Nothing flashes faster than 3 times per second (WCAG 2.3.1); glitch is interaction-only, 2 frames, once.
20. `prefers-reduced-motion: reduce` disables glitch, pulses, scanline drift, and transitions; state remains visible via fill/border changes.
21. Landmarks, one `h1`, mono labels tied to inputs via real `<label>`; readouts are real selectable text, not images.

## D. Performance

22. Scanlines/grain are single static CSS layers (no animated `backdrop-filter`, no full-screen repaints).
23. Glitch animates `transform`/`clip-path` only, runs once per interaction, then stops.
24. Glow uses `box-shadow`/`text-shadow` on small elements; no large blurred surfaces.
25. Dark surfaces minimize light emission; no autoplaying video backgrounds without paused/reduced controls.
26. Fonts: 2 families max (grotesk + mono), used weights only, `font-display: swap`.

## E. Responsive

27. Single column under 640px; terminal nav stacks to full-width mono rows with 48px targets.
28. Readout rails reflow below content; dashboard tiles step 3-2-1 columns.
29. Glow radii shrink ~30% on mobile; scanline overlay stays global at 3% without horizontal scroll.
30. Body 16px floor and mono 13px floor hold at every breakpoint; no fixed-height readout boxes clipping text at 200% zoom.

---

## 10-point pre-delivery pass

- [ ] 1. Darkness budget audit: screenshot each view, estimate neon pixel share under 10%; hue count at 2 or fewer.
- [ ] 2. Tab the page: every stop shows the solid 2px offset outline; order logical; nothing trapped in modals or logs.
- [ ] 3. Contrast re-measure with glow + scanlines composited: log every text pair; floor is `#7B8794` (5.25:1).
- [ ] 4. Photosensitivity sweep: play all interactions twice; count flashes per second (max 3); confirm glitch fires once per interaction.
- [ ] 5. Reduced motion on: glitch gone, pulses stopped, scanlines static; every state still distinguishable.
- [ ] 6. Glow removal test: disable all `text-shadow`/`box-shadow` via devtools; page still fully legible and states still visible.
- [ ] 7. State walkthrough per control: hover, focus, active, selected, disabled, error, loading; matches §8.
- [ ] 8. Log etiquette: `role="log"` announces politely, never steals focus, caps entries, scroll position sane.
- [ ] 9. Terminal-cosplay sniff: any uppercase mono walls, sub-13px mono, or sub-16px body? Fix before ship.
- [ ] 10. 360px + 200% zoom: no horizontal scroll, no clipped readouts, nav rows at 48px.
