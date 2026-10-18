# Y2K Design - Quality Checklist

Ship gate for Y2K design. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** At most three material recipes in use (chrome, gel, translucent plastic), each from the token definitions; no improvised gradients.
2. **(gate)** At most one decorative flare/orb accent per view, `aria-hidden`, never overlapping text; nothing animates by default except the declared slow sweep.
3. Candy accents stay within one family per view (gel blue + one of bubble/sun); the base remains silver/white.
4. Radius is soft everywhere (pills for controls, 12-24px for panels); zero sharp-cornered boxes.
5. Shadows are soft drops with one light source (top); no hard offsets, no bevel-everything emboss.
6. Chrome gradient text appears at display sizes only, with a dark solid color fallback.
7. Photography and illustration sit in rounded frames inside the palette; no clashing stock styles.

## B. Components & states

8. **(gate)** Every control implements the §8 matrix: default, hover, `:focus-visible`, active (material sinks or tints), selected, disabled, error, loading.
9. **(gate)** Focus indicators are solid outlines (2px navy or gel blue), never glow-only (WCAG 2.4.7).
10. Pressed states move *into* the material: inset shadows on gel, tint fills on inputs; consistent across controls.
11. Disabled states use the gray gel ramp with `#3D4A63`-grade labels (5:1+ on the darker stop), not opacity.
12. Errors pair the deep raspberry border with visible inline text and `aria-invalid`/`aria-describedby` wiring.
13. Tabs/nav expose state beyond color: selected pill + `aria-selected`/`aria-current`; 44px+ targets.
14. Loading swaps content inside locked-size controls (no layout shift).

## C. Accessibility

### Verified pair reference (computed WCAG ratios for the Y2K palette)

| Text | Fill | Ratio | Verdict |
|---|---|---|---|
| `#14213D` navy | `#EAF2FB` ice | 14.14:1 | ✓ body |
| `#14213D` | `#BFE7FA` ice tint | 12.19:1 | ✓ body |
| `#14213D` | `#FFD166` sun | 11.08:1 | ✓ body |
| `#14213D` | `#FF8FD3` bubble | 7.70:1 | ✓ body |
| `#FFFFFF` | `#1B6CA8` gel blue | 5.59:1 | ✓ body |
| `#3D4A63` | gray gel ramp | ~5.6:1 | ✓ (disabled label) |
| `#D7DEE8` | `#10151D` LCD | ~12:1 | ✓ body |
| `#FFFFFF` | light gel top stop | <3:1 | ✗ never at body size |
| `#7A8AA5` | translucent panel composite | often <4.5:1 | ✗ use navy |

15. **(gate)** Body text 4.5:1, large text 3:1, measured against the *composite* background (panel over scene), not the panel color alone.
16. **(gate)** Gradient fills behind text verified at the lightest stop; white labels only on `#1B6CA8`-grade or darker fills.
17. Chrome wordmarks carry a dark solid fallback color and clear 3:1 at their darkest stop; never used below 24px.
18. `prefers-reduced-motion: reduce` stops shimmer sweeps, pulses, and parallax; effects become static (WCAG 2.3.3 posture).
19. Nothing flashes more than 3 times per second (WCAG 2.3.1); flares are static.
20. Translucent panels ship a solid `@supports not (backdrop-filter)` fallback that keeps the same contrast pairs.
21. Landmarks, one `h1`, real labels, `aria-current`; LCD readouts are real text (selectable, zoomable), not images.
22. Page usable at 200% zoom; body text never below 16px.

## D. Performance

23. `backdrop-filter` limited to hero/primary panels (or replaced with 92% solid fills on low-end surfaces); never animated.
24. Gradients are static CSS (no gradient image payloads); decorative flares are CSS radial-gradients, not PNGs.
25. Two font families maximum plus system mono; `font-display: swap`; display face subset.
26. Shimmer sweep animates `transform`/`background-position` only, with long intervals (6s+) or hover-only.
27. Images sized explicitly; layered scenes use CSS backgrounds rather than stacked full-width JPEGs.

## E. Responsive

28. Hero scene simplifies on mobile (one gradient + one accent); wordmark floors at the clamp minimum.
29. Nav becomes a bottom pill tab bar (48px targets) under 640px; tabs remain ARIA-wired.
30. Panels go full-width with 16px gutters; floating decor reflows without horizontal scroll.
31. Forms use full-width gel buttons on small screens; 48px input heights maintained.
32. No horizontal scroll at 360px; orbiting decor is clipped, not overflowing.

---

## 10-point pre-delivery pass

- [ ] 1. Count gradient rules in the CSS: all match the three recipes; orphans removed.
- [ ] 2. Count lens flares/orbs per view: one maximum, `aria-hidden`, clear of text.
- [ ] 3. Recompute contrast at the lightest stop of every gradient behind text; log ratios.
- [ ] 4. Verify chrome text: display-size only, dark fallback color present, works with gradients disabled.
- [ ] 5. Tab the page: solid outlines everywhere; glow never load-bearing.
- [ ] 6. Reduced motion on: sweep/pulse/parallax gone; state still visible via fill and shadow changes.
- [ ] 7. Composite-contrast check: screenshot panels over scenes and re-measure text areas.
- [ ] 8. Test 360px: bottom tab nav, full-width gels, no horizontal scroll, 48px targets.
- [ ] 9. State walkthrough per control: hover, focus, active, selected, disabled, error, loading; matches §8.
- [ ] 10. Nostalgia sniff test: would a 1999 art director recognize it, and would an accessibility auditor pass it? Both must answer yes.
