---
name: ochrelle-cyberpunk
description: Art direction and implementation skill for cyberpunk interface design, the neon-noir canon of Blade Runner, Neuromancer, and Ghost in the Shell. Near-black blue-cast surfaces, sparing neon cyan, magenta, and yellow accents, glitch effects, terminal chrome, CRT scanlines, and rain-slick city mood in a high-tech low-life register. Use when a project calls for cyberpunk, neon-noir, dystopian, hacker, synthwave-adjacent, or retro-future design; when building games, night-mode tools, developer and security products, music or rave event sites, dark portfolios, and sci-fi dashboards; or when a user mentions neon accents, glitch, terminal UI, CRT effects, or a cyber aesthetic.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: thematic-genres
---

# Cyberpunk

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Cyberpunk UI is neon-noir: a city at night rendered as an interface. Surfaces are near-black with a blue cast; light comes only from neon signage, terminals, and readouts; texture arrives as scanlines, grain, and reflections. The mood is high-tech low-life: advanced machines, worn surfaces, rain on everything.

It is not vaporwave (pastel ironic nostalgia), not clean sci-fi HUD (pristine white glass), and not "black site with a blue accent". Cyberpunk earns its darkness with discipline: neon is scarce, typed, and meaningful.

| | Real cyberpunk system | Lazy version |
|---|---|---|
| Surfaces | 2-3 near-black tones, blue-cast | Pure `#000` with random grays |
| Neon | 1-2 accent hues, under ~10% of any view, borders and readouts | Every color glows, full neon fills |
| Text | Off-white ink at 15:1+, muted at 7:1+ | 4:1 gray-on-dark walls of text |
| Effects | Scanlines/grain as quiet overlays; glitch on hover only | Glitch loops, flicker, everything pulsing |
| Chrome | Terminal frames, corner brackets, mono readouts | Generic rounded cards with drop shadows |
| Result | Atmosphere with AA legibility | Unreadable theme-shop cyber soup |

If you can hear the theme music, but cannot read the paragraph, the lazy column wins.

## Philosophy

1. **Darkness is the default; neon is the exception.** At least 90% of any view is dark surface. Neon appears as hairline borders, status dots, key labels, and one glowing element per region.
2. **Neon is light, not paint.** Neon colors emit; they do not fill large surfaces. Where neon fills exist (badges, primary buttons), they are small and use dark ink labels.
3. **The city is always wet and old.** Scanlines, grain, reflections, and worn chrome give the surface history. Every effect is quiet enough to sit under text.
4. **Machines have voices.** Terminal chrome, monospaced readouts, timestamps, and system messages make the UI feel like equipment, not marketing.
5. **Contradiction is the aesthetic.** Polished neon against grime, precision against decay. But legibility never joins the decay: contrast floors are strict.

## Brief historical context (verifiable)

- **Blade Runner** (1982, directed by Ridley Scott) defined the visual canon: neon-drenched night city, holographic advertising, rain, and vertical sprawl.
- William Gibson's **Neuromancer** (1984) named the digital space ("cyberspace") and consolidated the genre's literary voice; the term "cyberpunk" itself comes from Bruce Bethke's 1983 short story of that name.
- **Akira** (1988, Katsuhiro Otomo) and **Ghost in the Shell** (1995, directed by Mamoru Oshii) gave the style its East-Asian megacity iconography and its glowing-signage palette.
- The genre's shorthand "high tech, low life" was popularized in 1980s science-fiction editing circles and remains the design brief: advanced systems in decayed environments.
- Web UI culture absorbed the canon through 2010s synthwave and cyber-themed toolkits; scanlines, terminal chrome, and neon-noir dashboards became the standard transposition.

## When to use / when NOT

**Use for:**
- Games and interactive fiction set in neon-noir worlds: the UI is diegetic set dressing.
- Music and rave events, club nights, festivals: darkness plus neon is the venue's own language.
- Developer tools, security products, and terminals that want a strong night-shift identity.
- Night-mode-first products and dark portfolios with a narrative streak.
- Sci-fi dashboards and themed campaigns where atmosphere is the point.

**Do NOT use for:**
- Healthcare, finance, government, or kids' products: the mood reads as untrustworthy or menacing.
- Long-form reading defaults: dark, glowing, dense surfaces tax sustained reading.
- Elderly- or accessibility-first audiences without heavy extra contrast work.
- Corporate SaaS that needs to feel calm and neutral.
- Print or brand surfaces where near-black ink dominates physically.

## Quick art-direction token sketch

- `--bg: #0B0F14` page, `--surface: #121821` panels, `--surface-2: #1A2230` raised; all blue-cast near-blacks.
- `--ink: #E8F0F2` (16.64:1 on bg, 15.43:1 on surface); `--muted: #8FA3B0` (7.35:1); never darker than `#7B8794` (5.25:1) for body.
- Neon accents (used sparingly, dark labels on fills): `--cyan: #2DE2E6` (12.02:1 on bg), `--magenta: #FF2A6D` (5.31:1, emphasis and alerts), `--yellow: #F6E71D` (14.98:1, warnings/key data), `--orange: #FF9E64` (9.45:1, secondary).
- Fills: neon badges carry `#0B0F14` ink (12.02:1 on cyan, 14.98:1 on yellow, 5.31:1 on magenta).
- Chrome: 1px `#2A3442` borders; corner brackets in accent color; scanline overlay `repeating-linear-gradient(0deg, rgba(255,255,255,0.03) 0 1px, transparent 1px 3px)`, never over body text.
- Type: mono for readouts/labels/terminal, clean grotesk sans for body; 16px body floor; uppercase mono labels with 0.08em tracking.
- Radius: 0 to 2px; cyberpunk corners are cut, not curved (optional `clip-path` corner cuts on hero panels).
- Motion: 150-250ms `ease-out`; glitch = 2-frame transform/clip jitter on hover only; glow pulses 3s+ or static; `prefers-reduced-motion` kills all of it.

## Component guidance summary

- **Buttons:** dark surface with 1px neon border and mono uppercase label; hover fills neon with dark ink label; primary CTA may be a full neon fill (small surface).
- **Cards/panels:** `--surface` fill, 1px chrome border, corner brackets, mono index label (`SYS.042`), body in off-white.
- **Forms:** dark inputs with 1px borders; focus = 2px cyan outline; caret cyan; errors in magenta with text, never color alone.
- **Nav:** terminal bar - brand as prompt (`~/nightcity`), links as mono commands, active link cyan with leading `>` glyph.
- **Readouts:** dark LCD islands with mono silver text, timestamped rows, `role="log"` for streams.
- **What stays restrained:** body copy (off-white grotesk, no glow), tables (hairline `#2A3442` rules), imagery (high-contrast night photos, optional cyan duotone).

## Canonical CSS recipe

```css
/* Cyberpunk tokens + the neon-border button */
:root {
  --bg: #0B0F14;
  --surface: #121821;
  --ink: #E8F0F2;          /* 16.64:1 on bg */
  --muted: #8FA3B0;        /* 7.35:1 on bg */
  --cyan: #2DE2E6;         /* 12.02:1 on bg */
  --magenta: #FF2A6D;      /* 5.31:1 on bg */
  --chrome-line: #2A3442;
  --ease: cubic-bezier(0.22, 0.61, 0.36, 1);
}
.btn-neon {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 10px 24px;
  background: var(--surface);
  color: var(--cyan);
  border: 1px solid var(--cyan);
  border-radius: 2px;
  font: 600 0.875rem/1 ui-monospace, "SF Mono", Menlo, monospace;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background-color 200ms var(--ease), color 200ms var(--ease),
              box-shadow 200ms var(--ease);
}
.btn-neon:hover {
  background: var(--cyan);
  color: var(--bg);                                   /* 12.02:1 */
  box-shadow: 0 0 18px rgba(45, 226, 230, 0.35);
}
.btn-neon:active { transform: translateY(1px); }
.btn-neon:focus-visible { outline: 2px solid var(--cyan); outline-offset: 3px; }
.btn-neon:disabled {
  border-color: var(--chrome-line);
  color: #7B8794;                                     /* 5.25:1 on surface */
  background: var(--surface);
  cursor: not-allowed;
  box-shadow: none;
}
```

## Accessibility notes (mandatory)

- **Contrast:** body 4.5:1, large 3:1 (WCAG 1.4.3). Dark themes make neon text tempting: cyan (12.02:1), yellow (14.98:1), and orange (9.45:1) pass at any size; **magenta `#FF2A6D` passes at 5.31:1 for body but reserve it for emphasis**. Muted text stops at `#8FA3B0` (7.35:1); `#7B8794` (5.25:1) is the absolute floor.
- **Glow:** text-shadow glows lower perceived contrast. Body text never glows; accent text may glow with tight radius (4 to 8px) and must still measure 4.5:1 at the rendered edge.
- **Scanlines/grain:** overlays sit under text or at 3-4% opacity; verify they do not drag any text pair below AA (WCAG 1.4.3).
- **Photosensitivity:** no flicker faster than 3 flashes per second (WCAG 2.3.1); glitch effects are hover/interaction-only, 2-frame, and fully removed under `prefers-reduced-motion: reduce`.
- **Focus:** `outline: 2px solid var(--cyan); outline-offset: 3px` on dark, magenta-free zones preferred; never glow-only focus (WCAG 2.4.7, 2.4.11).
- **Color-only states:** status colors pair with mono labels (`ERR`, `OK`, `WARN`); neon never carries meaning alone.

## Top-5 failure modes

1. **Neon rainbow.** Four glowing hues at 40% of the surface: the darkness budget is gone. Fix: 1-2 accent hues per view, under 10% of pixels, budget table in [references/style-guide.md](references/style-guide.md).
2. **Gray-on-dark walls of text.** `#6B7686` at 3.9:1 fails and strains. Fix: `#E8F0F2` body, `#8FA3B0` secondary, `#7B8794` absolute floor.
3. **Glow everywhere.** Glowing body text and glowing panels lose contrast and feel cheap. Fix: glow is for accents and hover states only; body stays matte.
4. **Effects over legibility.** Scanlines and grain sitting on paragraphs drag contrast under AA. Fix: overlays under content layers, 3-4% opacity, verified pairs.
5. **Glitch loops and flicker.** Continuous glitch animation risks photosensitive responses and reads as broken. Fix: 2-frame jitter on hover/focus only, no loops, reduced-motion kill switch ([references/implementation-examples.md](references/implementation-examples.md)).

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
