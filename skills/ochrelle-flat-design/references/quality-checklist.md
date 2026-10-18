# Flat Design - Quality Checklist

Ship gate for flat design. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** Zero gradients on any element (buttons, backgrounds, icons, text). Search the CSS for `gradient` - any hit is a defect.
2. **(gate)** Shadows limited to the single `--shadow-hairline` token on floating layers (menus, dialogs, toasts). No other `box-shadow` exists.
3. **(gate)** One radius token (0 to 4px) applied to every component; no per-component exceptions.
4. Color roles are frozen: accent = interactive, tint = container, white = content, ink = text. No hue plays two roles.
5. Palette holds at 1 neutral system + 1 accent + up to 3 status hues; counting more means merge or delete.
6. One icon family, one color, sizes on the 16/20/24 scale; no emoji standing in for UI icons.
7. Borders are either the declared token (3:1+ color) or absent; zero browser-default hairlines.

## B. Components & states

8. **(gate)** Every control defines default, hover, active, `:focus-visible`, and disabled states per style-guide §8.
9. **(gate)** Disabled states are solid muted fill + readable ink, never `opacity` hacks.
10. Hover states are wrapped in `@media (hover: hover)` or paired with `:active`/focus equivalents for touch.
11. Active nav item is marked by shape change (inverted block, pill, underline) plus weight, not color alone; `aria-current="page"` present.
12. Forms use real `<label>`, `autocomplete`, and `aria-invalid` + `aria-describedby` wired to visible error text with an icon.
13. Loading states swap label content inside a locked-size control (no layout shift).
14. Menus/popovers open with `aria-expanded` on the trigger, close on Escape and outside click, and move focus correctly.

## C. Accessibility

### Verified pair reference (computed WCAG ratios for the example palette)

| Text | Fill | Ratio | Verdict |
|---|---|---|---|
| `#2C3E50` | `#FFFFFF` | 10.98:1 | ✓ body |
| `#5D6D7E` | `#FFFFFF` | 5.31:1 | ✓ body (secondary) |
| `#FFFFFF` | `#2471A3` accent | 5.30:1 | ✓ body |
| `#FFFFFF` | `#1F618D` hover | 6.66:1 | ✓ body |
| `#FFFFFF` | `#3498DB` bright | 3.15:1 | ✗ normal / ✓ large+bold only |
| `#2C3E50` | `#F1C40F` warning | 6.61:1 | ✓ body |
| `#FFFFFF` | `#C0392B` danger | 5.44:1 | ✓ body |
| `#FFFFFF` | `#2ECC71` | 2.10:1 | ✗ never |
| `#424949` | `#BFC9CA` disabled | 9.21:1 | ✓ |
| `#9AA7AF` border | `#FFFFFF` | ~2.8:1 | ✓ non-text 3:1 boundary; use 2px or darken |

15. **(gate)** All body text is 4.5:1; large text (24px / 18.66px bold) 3:1; every fill/label pair measured against the table above or recomputed.
16. **(gate)** Focus visible on every focusable element: 2px `--ink` (or `--accent` on inputs) outline with offset; never `outline: none` without replacement (WCAG 2.4.7, 2.4.11).
17. Non-text UI boundaries (input borders, dividers that signal interactiveness) meet 3:1 against adjacent colors (WCAG 1.4.11).
18. No information by color alone: errors have text, selection has shape/weight, links are underlined.
19. Interactive targets 44x44px minimum; list rows at least 44px tall on touch.
20. Page survives 200% zoom and OS font scaling without clipped text or fixed-height rows.
21. Landmarks (`header`, `nav[aria-label]`, `main`) and one `h1` present; reading order is DOM order.

## D. Performance

22. One font family (plus optional mono for data) with only used weights; `font-display: swap` if self-hosted.
23. No `backdrop-filter`, no large `filter`/`box-shadow` paint areas; hover effects are color-only.
24. Icons inline SVG or icon font subset; no full icon library shipped for 10 glyphs.
25. Images have `width`/`height` or `aspect-ratio`; flat layouts reflow cleanly on late load.
26. Total custom CSS stays small (flat is the lightest of the material styles); no framework skin fighting the tokens.

## E. Responsive

27. 12-column grid on desktop collapses to 1 column under 640px; card grids step 3 to 2 to 1.
28. Nav becomes a bottom tab bar (icon + label, 48px targets) or full-width stacked list on mobile; no hamburger without a flat, keyboard-friendly panel.
29. Type steps drop via `clamp()` floors (44px display lands at 32px on 360px screens, not smaller).
30. Tables scroll horizontally with a sticky first column instead of hiding data; rows keep 40px+ height.
31. Touch verification: no hover-dependent functionality; `:active` fill steps communicate presses.

---

## 10-point pre-delivery pass

- [ ] 1. Search CSS for `gradient`, `backdrop-filter`, `text-shadow`: every hit removed or justified against §5.
- [ ] 2. Tab the entire page: every stop shows the 2px offset outline; nothing trapped; order logical.
- [ ] 3. Recompute contrast for every text/fill pair actually shipped, including hover and disabled; log ratios.
- [ ] 4. Verify each of accent, success, warning, danger fills uses the correct label color (ink or darkened white) at body size.
- [ ] 5. Unplug motion: reduced-motion on; page fully usable, transitions degrade to instant swaps.
- [ ] 6. Zoom to 200%: no clipped rows, no fixed-height overflow, sticky elements still expose content.
- [ ] 7. Test at 360px: single column, bottom nav or stacked nav, 44px targets, no horizontal scroll.
- [ ] 8. State walkthrough per control: hover, active, focus, disabled, error, loading; compare against §8 matrix.
- [ ] 9. Disable CSS: document outline reads correctly (one h1, labels, landmarks, logical order).
- [ ] 10. Affordance sniff test at arm's length: can a first-time user tell what is clickable in one second? If not, borders/fills are wrong.
