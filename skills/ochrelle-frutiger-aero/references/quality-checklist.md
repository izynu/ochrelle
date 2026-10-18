Ship gate for Frutiger Aero. Every item must pass before delivery.

## A. Art direction

- [ ] A real scene exists behind every glass surface: sky gradient plus at least one nature subject (grass band, water, leaf, bubbles, fish). No glass or gel floats over flat color.
- [ ] Exactly one light source, top-center: all speculars and sheen lines on top/top-left, all drop shadows falling down.
- [ ] Gel material is correct: 3-stop vertical gradient ending in `#0A6FA6` under the label, 1px bright rim, `inset 0 1px 0 rgba(255,255,255,0.8)` sheen, specular dot on pill buttons.
- [ ] Glass material is correct: 0.62 white fill, blur 10-16px with saturate, 1px bright border, glossy top reflection band on cards.
- [ ] One hero material per region: gel only on primary actions, glass on containers, flat white plastic for supporting chrome. No all-gloss pages.
- [ ] Nature layer present: at least one natural subject per viewport plus one eco cue; decorative elements carry `aria-hidden="true"`.
- [ ] Radii match the system (12/16/24px, pills for gel); no sharp corners and no dark 2px+ borders anywhere.

## B. Components & states

- [ ] Every interactive element implements default, hover, active/press, focus-visible and disabled, each visually distinct without relying on color alone.
- [ ] Press states dip 1px with an inset press shadow; release lifts; hover lift is 1-2px, never a scale bounce.
- [ ] Nav active item uses the small gel capsule; hover pills use white alphas (0.18 / 0.3), not a second accent color.
- [ ] Inputs use `--glass-strong` (0.85+) fill with visible labels; error state is a 2px `#8A1C2B` rim plus a message at 4.5:1+.
- [ ] Progress/meters are gel channels with a glossy fill at 3:1 non-text contrast against the channel.
- [ ] Disabled controls sit at 55% opacity with `cursor: not-allowed`, no hover lift, no sheen.

## C. Accessibility

- [ ] Body text reaches 4.5:1 against the busiest region that can scroll behind each glass plate (verified at worst case, not average). WCAG 2.2 AA 1.4.3.
- [ ] Non-text contrast (rims, focus rings, meter fills, icon strokes) reaches 3:1 against adjacent colors. WCAG 2.2 AA 1.4.11.
- [ ] White text appears only on `#0A6FA6` gel bottoms or darker (5.47:1+); `#0F9AD1` carries text only at 24px+ bold (3:1 large-text rule).
- [ ] `:focus-visible` shows the 3px `#0A7099` outline with 2px offset on every control, on both glass and scene backgrounds.
- [ ] `prefers-reduced-motion`: ambient loops (bubbles, fish, disc spin) stop completely; entrances become 150ms opacity fades; hover transforms become none.
- [ ] `prefers-reduced-transparency` (where supported): glass swaps to 0.95 white plates, blur removed, layout unchanged.
- [ ] `@supports not (backdrop-filter: blur(1px))` fallback renders near-solid white plates with unchanged ink; the page is fully usable in the fallback.
- [ ] Touch targets are at least 44x44px, including nav pills and transport buttons.
- [ ] Decorative media (droplets, fish, bubbles, disc) is `aria-hidden`; no information is encoded in imagery alone.

## D. Performance

- [ ] Blur budget: at most 6 blurred panes visible per desktop viewport, at most 3 on mobile.
- [ ] No transition or animation targets `backdrop-filter` or `filter` (grep the stylesheet; zero hits).
- [ ] Animated properties are limited to `transform`, `opacity`, `background-color`, `box-shadow`.
- [ ] Ambient loops are transform/opacity only, 10s or longer, and removed under reduced motion.
- [ ] The scene background is CSS gradients (no multi-megabyte hero JPEG on kiosk/mobile views); any photo ships in AVIF/WebP with a gradient fallback.
- [ ] `background-attachment: fixed` is used only on views tested for mobile repaint cost; dropped below 768px if scrolling stutters.

## E. Responsive

- [ ] No horizontal scroll at 320px; page-edge padding stays 16px minimum; floating bars respect `env(safe-area-inset-*)`.
- [ ] At 768px the scene simplifies (sky + grass band), heroes stack, and glass cards go full-width with 16px margins.
- [ ] Below 480px, blur drops to 10px and glass fill rises to 0.72 (or 0.85 where text sits) to protect contrast on busier backgrounds.
- [ ] Hover-only affordances are gated behind `@media (hover: hover)`; touch uses press states.
- [ ] Worst-case text contrast re-verified at 375px after scene compression.

---

## 10-point pre-delivery pass

1. **Scene audit**: every glass/gel surface has a composed natural scene behind it; screenshot the page and confirm no pane sits on flat color.
2. **Light audit**: every specular top/top-left, every shadow down; one sun across the page.
3. **Material audit**: gel = actions, glass = containers, plastic = chrome; nothing else shines.
4. **Contrast run**: measure body text against the busiest scene region under every plate; 4.5:1 body, 3:1 large text and UI.
5. **State sweep**: tab through all controls; hover/press/focus/disabled all present and distinct; focus ring visible on glass and scene.
6. **Motion audit**: grep transitions for `backdrop-filter`/`filter` (must be zero); enable reduced motion and confirm loops stop and layout holds.
7. **Fallback render**: force the no-backdrop-filter path; confirm solid plates, unchanged ink, full usability.
8. **Mobile pass**: 375px and 320px: no overflow, targets 44px, blur budget respected, contrast re-verified.
9. **Nature budget**: exactly one natural subject and one ambient loop per viewport; no screensaver pages.
10. **Mood check**: the page still reads optimistic and airy; nothing dark, gritty or ironic crept into copy, imagery or states.
