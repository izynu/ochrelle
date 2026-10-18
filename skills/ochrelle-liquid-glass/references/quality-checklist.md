# Liquid Glass - Quality Checklist

Check every item. **(gate)** items block ship on failure. "Glass" below = the web approximation of the regular form unless stated otherwise.

---

## A. Art direction & material fidelity

1. **(gate)** Layer contract holds: content is opaque; only floating controls/chrome use glass. Zero glass on paragraphs, tables, forms, or cards.
2. **(gate)** Honesty rule: code comments, docs, and design reviews describe the web effect as an *approximation* (blur + highlight), never as refraction/lensing. No claims of "real Liquid Glass on the web".
3. Fill alphas are in the material's range (controls ~0.55–0.62 light / ~0.5–0.55 dark) - not milky, not transparent.
4. Blur follows the ladder (controls 8–12px, docks 14–18px, panels 20–30px) with `saturate(1.6–1.8)`; no blur above ~30px.
5. The edge system is present: top specular highlight, bottom interior shade, outer hairline; light direction is identical on every glass element in view.
6. Shadows are soft/ambient (one per element); no hard offset shadows anywhere.
7. Radius system respected (pills for controls, 16–24px for docks/panels); one radius per element.
8. One glass cluster per region (mobile hard limit: one per viewport; desktop max two).
9. Tints are semantic and applied to fills, never to the blur; ≤1 accent in chrome.
10. Labels on glass are 1–2 words, 15–16px class; no body copy on glass.

## B. Components & states

11. **(gate)** Full state matrix for every glass control: rest, hover, `:focus-visible`, active, selected, disabled, loading.
12. Hover brightens (alpha step) rather than moves; active presses (`scale(0.96–0.97)`); selected state uses accent tint + `aria-current`/`aria-pressed`.
13. Focus style is visible over both light and dark media (ring + halo), on every focusable element in chrome.
14. Scrolled-under elevation implemented via class toggle + transition (rAF-throttled), not per-frame style writes.
15. Morphs/expansions animate `transform`/`opacity` only - no width/height animations on glass elements, no `backdrop-filter`/alpha keyframes.
16. Nested glass eliminated: one glass container per cluster; inner controls are solid or tinted.
17. Scroll containers reserve clearance (dock height + `env(safe-area-inset-bottom)`); last content row never sticks under chrome.

## C. Accessibility

18. **(gate)** `prefers-reduced-transparency: reduce` → fully opaque fallback that is complete, tested, and itself contrast-compliant (no dependence on the glass variant).
19. **(gate)** `@supports not (backdrop-filter…)` fallback shipped and tested (opaque `#F2F2F7`/`#1C1C1E` class fills).
20. **(gate)** Busiest-background audit: control labels ≥4.5:1 and boundaries ≥3:1 over every supported media scenario (bright sky, white-on-black video, dense text, saturated gradients) - scrim added where a scenario fails.
21. `prefers-contrast: more` → opaque fill + strong border variant.
22. `prefers-color-scheme: dark` → dark fill + dimmed edges + deepened shadow (not a naive inversion).
23. `prefers-reduced-motion: reduce` → springs/morphs become instant or ≤150ms opacity fades; nothing functional depends on motion.
24. Disabled labels still ≥4.5:1 against their fill; no raw `opacity: 0.4` text.
25. Touch targets ≥44px (dock tabs incl. 64px-wide min, FAB 52px); safe-area insets respected on notched devices.
26. Decorative scrims/gradients are `aria-hidden`/background-only; chrome is a real `<nav>`/`<button>`/`<a>` with labels (icon-only controls have `aria-label`).

## D. Performance

27. **(gate)** `backdrop-filter` element count audited: ≤3 per viewport on mobile (cluster counts as its elements); no glass rows in lists.
28. Zero animations of `backdrop-filter` or fill alpha; motion is transform/opacity only.
29. Scroll listeners are `passive` + rAF-throttled; class-toggle pattern used for scroll-linked changes.
30. No UA sniffing - capability detection via `@supports`; the fallback is real code, not a comment.
31. Paint cost spot-check on a low-end device profile (DevTools 4× throttle): scroll stays smooth with chrome visible.

## E. Responsive

32. **(gate)** Mobile grammar: bottom dock/tab bar primary; panels become bottom sheets; one glass cluster per viewport.
33. Desktop grammar: top bar/sidebar allowed; clusters ≤2; insets 12–24px maintained.
34. Blur step-down on mobile (12px class) verified for low-power devices.
35. Orientation change re-verified: cluster count constant, scrim placement correct, no chrome overlap of content in either orientation.

---

## 10-point pre-delivery pass

1. **Honesty read-through:** grep the repo for "Liquid Glass" - every web-facing mention says "approximation" where it should; no refraction claims.
2. **Settings sweep:** enable reduced transparency, increased contrast, dark mode, reduced motion (one at a time) - the UI is complete and legible in all four modes, with zero glass variants leaking through.
3. **Busiest-media test:** play/serve the brightest and busiest content under every glass cluster; measure label and boundary contrast in each; add scrims until all pass.
4. **Tab walk:** keyboard through the chrome in both color schemes - ring + halo visible everywhere; selected states announced (`aria-current`/`aria-pressed`).
5. **Jank check:** low-end throttle, scroll and morph simultaneously - 60fps or a documented, accepted trade-off; no `backdrop-filter` in any transition list.
6. **Cluster audit:** count glass containers per viewport per breakpoint; mobile ≤1, desktop ≤2.
7. **Fallback flip:** disable `backdrop-filter` (DevTools) - the page still works and looks intentional (this is what the `@supports` path sees).
8. **Safe-area check:** notch/home-indicator simulators - dock clears both; last list row reachable.
9. **Copy check:** labels ≤2 words; any wrapped or truncated label is redesigned, not squeezed.
10. **Layer audit:** screenshot with glass hidden (CSS toggle) - content must stand alone as a complete page. If hiding the glass breaks the design, the glass was load-bearing, which it must never be.
