# Terminal Console - Quality Checklist

Ship gate for Terminal Console. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** Exactly one phosphor hue per product (green or amber); the only other colors are the fixed status pair (`--warn`, `--error`) and tonal steps of the hue.
2. **(gate)** Monospace stack on every structural element (labels, tables, logs, buttons, nav); any sans is restricted to optional long prose and never mixes into UI chrome.
3. Body text is 16px or larger; 13px is reserved for uppercase labels; 12px only for timestamps in `--dim` - never for body.
4. All panes have a 1px border in `--line` plus a title bar; frame joints and corner glyphs are `aria-hidden` decoration.
5. No drop shadows, no gradients, no rounded corners beyond 2px; depth comes only from the `--bg` / `--panel` / `--select` tone ladder.
6. Column layouts are measured in `ch` and actually align (inspect two tables side by side at the same viewport).
7. A persistent status bar anchors the page (bottom or top) with brand, context, and state zones.

## B. Components & states

8. **(gate)** Every interactive element implements the full matrix: default, hover (inverse video), active (bright inverse), `:focus-visible`, disabled, selected (persistent inverse), loading (`aria-busy`), error. See style-guide §8.
9. **(gate)** State changes are instant (0-80ms); no easing curves on hover/active/focus.
10. Buttons keep real text labels; `[ ]` brackets are decorative pseudo-elements, not the only affordance.
11. Disabled controls use `--dim` (6.8:1) plus `--hairline` borders - readable, not faded.
12. Tabs/lists mirror visual selection in `aria-selected` / `aria-current`; roving tabindex with Arrow, Home, End support on tab bars.
13. Forms use prompt-line inputs with visible uppercase labels, `aria-invalid`, and `[!]` error text in `--error` - never color alone.
14. Log panes: rows single-line with in-pane horizontal scroll; timestamps in `--dim`; severity as text tags (`[ok]` / `[warn]` / `[fail]`).

## C. Accessibility

### Verified pair reference (green theme, computed WCAG ratios)

| Text | Ground | Ratio | Verdict |
|---|---|---|---|
| `#A8F0BC` ink | `#0A0F0A` bg | 14.6:1 | body |
| `#33FF77` bright | `#0A0F0A` bg | 14.5:1 | body |
| `#6FA57E` dim | `#0A0F0A` bg | 6.8:1 | body (secondary) |
| `#6FA57E` dim | `#1C2E22` select | 5.0:1 | body |
| `#FFB454` warn | `#0A0F0A` bg | 11.0:1 | body |
| `#FF6B66` error | `#0A0F0A` bg | 7.0:1 | body |
| `#4A7D58` line | `#0A0F0A` bg | 4.0:1 | UI boundary (1.4.11) |
| glow layer | anywhere | - | decoration only, never text |

15. **(gate)** All text meets 4.5:1 on its actual ground (including `--panel` and `--select` fills); measure, do not assume.
16. **(gate)** No `text-shadow` or glow on any readable text; glow exists only as `box-shadow` on non-text containers and is removed harmlessly.
17. Focus visible everywhere: 2px `--bright` outline, offset -2 to 2px, flipped to dark on bright fills; never `outline: none`.
18. `prefers-reduced-motion: reduce` stops cursor blink, spinners, and streaming reveals; polling timers are paused or slowed, and a visible Pause control exists for live regions.
19. Live regions: log streams are `aria-live="polite"` or `off` with batched updates (≤1 announcement/second); counters do not spam announcements.
20. Sparklines and ASCII charts carry `aria-label` or an adjacent accessible table with the actual values.
21. Severity and state are never color-only: text tags or glyphs accompany every color signal.
22. Touch targets ≥44x44px; in-pane horizontal scroll never traps touch scroll (page-level horizontal scroll stays at zero).

## D. Performance

23. One font family, system mono stack preferred (zero network cost); if self-hosting a mono font, subset to used weights and set `font-display: swap`.
24. Animations touch only `transform`, `opacity`, or character content swaps - no layout properties per frame.
25. Log streaming batches DOM insertions (≥250ms) and caps rendered rows (e.g. 500, virtualize beyond) so long sessions do not leak memory.
26. No backdrop-filter, no full-page blur overlays, no per-frame `text-shadow` repaint.
27. `::selection` styled (`background: var(--bright); color: var(--bg)`) so selection stays legible on dark grounds.

## E. Responsive

28. Below 768px panes stack in reading order; the status bar wraps without clipping; body text stays 16px.
29. Wide tables/logs scroll inside their pane; the document never scrolls horizontally at 360px width.
30. Tap feedback uses the inverse-video `:active` state (hover is not assumed on touch).
31. 200% zoom: panes reflow, `ch` columns may scroll within panes, no clipped labels.
32. `forced-colors: active` tested: borders and text remain distinguishable (use `system` colors or transparent fallbacks where needed).

---

## 10-point pre-delivery pass

- [ ] Tab the whole interface: every control reachable, focus ring visible on dark grounds, tab order matches reading order.
- [ ] Unplug motion: reload with OS reduced motion on - cursor static, spinner static, streams still readable and pausable.
- [ ] Run the contrast audit on every text/ground pair including inverse-video states; record ratios against the §C table.
- [ ] Grep the CSS for `text-shadow` and `blur`: zero hits on text selectors.
- [ ] Count phosphor hues: exactly one (green or amber) plus warn/error. More = fail; merge before ship.
- [ ] State matrix walkthrough on button, tab, input, log row: default, hover, active, focus, disabled, selected, loading, error vs style-guide §8.
- [ ] Feed 2,000 log lines: in-pane scroll only, no layout shift, no unbounded DOM growth.
- [ ] Test 360px viewport: panes stack, status bar wraps, no horizontal page scroll.
- [ ] Screen reader pass on a live stream: announcements rate-limited, pause control operable, sparkline summarized.
- [ ] Ask "would a sysadmin trust this?": misaligned columns, mixed hues, or decorative flicker are defects, not style.
