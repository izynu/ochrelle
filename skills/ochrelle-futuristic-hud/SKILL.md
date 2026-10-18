---
name: ochrelle-futuristic-hud
description: "Art direction and implementation skill for futuristic HUD (heads-up display) interfaces: translucent data panels over near-black space, cyan and amber instrument text, chamfered corner brackets, corner reticles, radar sweeps, scanlines, monospace telemetry readouts, and status colors that behave like avionics. Glow is decoration only, every essential text pairing passes 4.5 to 1 without it. Use for robotics and drone dashboards, sci-fi games and fan tools, telemetry and mission-control pages, launch event sites, cyberpunk events, and concept UI explorations. Trigger words include HUD, heads up display, sci-fi, cyberpunk, telemetry, avionics, holographic, targeting, mission control, or space UI."
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: thematic-genres
---

# Futuristic HUD

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

The futuristic HUD style treats the screen as an instrument canopy over a dark world: data panels with chamfered corners, corner brackets framing targets, monospace telemetry, radar sweeps, and a strict instrument palette of cyan on near-black with amber and red reserved for meaning. The UI talks like avionics - terse labels, live numbers, clear states.

What it is NOT: it is not neon soup. If everything glows, nothing is an instrument; if text fails contrast, it is not a HUD, it is a screensaver.

| | Real HUD art direction | Lazy neon sci-fi |
|---|---|---|
| Ground | Near-black `#05080D` with faint grid | Purple gradient with stars PNG |
| Text | Cyan `#7FE9FF` at 14.3:1, monospace data | Glowing white-on-blue at 2:1 |
| Color | Cyan + amber + red = status meaning | Every hue at full saturation |
| Glow | 1-2px decorative halo on chrome only | Blur glow on all text |
| Shape | Chamfered panels, corner brackets | Rounded translucent blobs |
| Result | Reads as an instrument | Reads as a screensaver |

## Philosophy

1. **The frame is the style.** Chamfered panels, bracket corners, and hairline grid do the art direction; content lives inside the instrument.
2. **Data is the decoration.** Telemetry, coordinates, and status codes are the ornament. A HUD with real numbers needs no confetti.
3. **Color means status.** Cyan is nominal information, amber is caution, red is alert, green is confirmed. Color never appears without meaning attached.
4. **Glow is light, not paint.** A 1-2px same-color halo on chrome and headers only; every text pairing passes 4.5:1 with the glow switched off entirely.
5. **Motion is telemetry.** Sweeps and scans are continuous, slow, and pausable; state changes snap in 200ms. Instruments do not bounce.
6. **Density with hierarchy.** HUDs are dense but gridded: every glyph occupies a slot, and the primary reading path is unambiguous.

## Brief historical context (verifiable)

- Production fighter aircraft HUDs - monochrome green/amber line symbology projected onto a combiner glass, speed and altitude as tape ladders - matured through the 1970s with fighters such as the F-16, and set the real-world visual grammar the genre borrows.
- Films *Alien* (1979) and *Blade Runner* (1982) established CRT-glow data surfaces and dense screens of readouts as science-fiction canon.
- *Minority Report* (2002) made translucent, gesture-driven data layers the modern default; its interface imagery was developed with MIT researcher John Underkoffler, whose lab work later became the g-speak platform.
- *Iron Man* (2008) codified the cyan holographic workshop HUD around the J.A.R.V.I.S. assistant, the single most imitated reference in product and motion design.
- Games proved the diegetic variant: *Metroid Prime* (2002) rendered the HUD as helmet glass, and *Dead Space* (2008) integrated the entire interface into the character's suit - both staples of HUD design talks since.

## When to use / when NOT

**Use for:**
- Robotics, drone, and IoT dashboards where telemetry is the content.
- Sci-fi games, fan tools, and ARG/event sites that want diegetic chrome.
- Launch events, product reveals, mission-control-style live pages.
- Cyberpunk club and event branding, night-mode kiosks.
- Concept UI explorations and portfolio pieces demonstrating state systems.

**Do NOT use for:**
- Long-form reading products, docs, legal - scanline density taxes reading.
- Healthcare and safety-critical control surfaces - style must not dress urgency down.
- E-commerce checkout and everyday productivity apps - the chrome outweighs the task.
- Kids products - the palette and density are not child-legible.

## Quick art-direction token sketch

- `--bg: #05080D` near-black blue; `--panel: #0B141F` instrument panels; `--grid: #12202E` hairline grid (decorative).
- `--hud: #7FE9FF` primary cyan text (14.3:1 on bg, 13.2:1 on panels); `--bright: #EAF6FF` for emphasis (18.3:1); `--dim: #8AA3B8` secondary (7.7:1, 7.1:1).
- Status: `--amber: #FFC069` caution (12.4:1), `--alert: #FF7B72` alert (8.0:1), `--ok: #6EE7A0` confirmed (12.0:1 on panel).
- `--fill: #19C8DE` solid cyan action fill with `#05080D` text (9.9:1) - the one bright surface, used for primary actions.
- Spacing: 8 / 16 / 24 / 40 / 64; panels pad 16-24px; gutters 24px; the grid (8px cell) aligns every glyph.
- Type: monospace for all data (`ui-monospace` stack), squared/condensed sans for labels; labels uppercase tracked `0.08em`; body `0.9375rem/1.6` (15px floor - HUDs are instruments, not novels).
- Shape: radius 0-2px; chamfered corners via `clip-path` (12px cuts on opposite corners); corner brackets drawn with `::before`/`::after` borders.
- Glow: `0 0 12px rgba(127, 233, 255, 0.35)` on panel borders and headings only; never on body text; contrast never depends on it.
- Motion: `200ms ease-out` for state changes; continuous sweeps (radar 4s linear, scan 6s) paused on hover/focus and killed by `prefers-reduced-motion`.

## Component guidance summary

| Component | HUD treatment |
|---|---|
| Buttons | Cyan fill `#19C8DE` with dark text, chamfered corners; ghost variant uses 1px cyan border |
| Panels | `#0B141F` with 1px cyan-tinted border, chamfer + corner brackets, monospace header row |
| Forms | Dark inputs, 1px cyan border, uppercase micro-labels, cyan focus bracket |
| Nav | Top bar with system name left, status readout right, hairline grid beneath |
| Telemetry | Monospace rows: label (dim), value (hud), unit (dim), status chip (amber/alert/ok) |
| Radar/scan | Decorative conic sweep or scanline bands, `aria-hidden`, pausable |

## Canonical CSS recipe

```css
:root {
  --bg: #05080D;
  --panel: #0B141F;
  --grid: #12202E;
  --hud: #7FE9FF;      /* 14.3:1 on bg */
  --bright: #EAF6FF;   /* 18.3:1 on bg */
  --dim: #8AA3B8;      /* 7.7:1 on bg */
  --amber: #FFC069;    /* caution */
  --alert: #FF7B72;    /* alert */
  --ok: #6EE7A0;       /* confirmed */
  --fill: #19C8DE;     /* action fill, dark text 9.9:1 */
  --glow: 0 0 12px rgba(127, 233, 255, 0.35);
  --quick: 200ms ease-out;
}
.btn-hud {
  font: 600 0.875rem/1 ui-monospace, "Cascadia Mono", Menlo, monospace;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #05080D;
  background: var(--fill);
  border: 1px solid var(--fill);
  clip-path: polygon(10px 0, 100% 0, 100% calc(100% - 10px), calc(100% - 10px) 100%, 0 100%, 0 10px);
  padding: 0.875rem 1.5rem;
  min-height: 44px;
  transition: background var(--quick), color var(--quick);
}
.btn-hud:hover { background: var(--hud); }
.btn-hud:active { background: #0FA5BC; }
.btn-hud:focus-visible { outline: 2px solid var(--hud); outline-offset: 3px; }
.panel-hud {
  position: relative;
  background: var(--panel);
  border: 1px solid #1E3A4C;
  padding: 16px 24px;
  clip-path: polygon(14px 0, 100% 0, 100% calc(100% - 14px), calc(100% - 14px) 100%, 0 100%, 0 14px);
}
.panel-hud > h2 {
  font: 600 0.8125rem/1.2 ui-monospace, Menlo, monospace;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--hud);
  border-bottom: 1px solid var(--grid);
  padding-bottom: 8px;
  text-shadow: 0 0 8px rgba(127, 233, 255, 0.4);  /* decorative halo, not load-bearing */
}
.panel-hud .row { display: flex; gap: 12px; padding: 8px 0;
                  font: 400 0.9375rem/1.5 ui-monospace, Menlo, monospace; }
.panel-hud .row .k { color: var(--dim); min-width: 10ch; }
.panel-hud .row .v { color: var(--hud); }
.scan-band {                       /* decorative scanlines, own band only */
  height: 16px;
  background: repeating-linear-gradient(180deg, var(--grid) 0 1px, transparent 1px 4px);
}
```

## Accessibility notes (mandatory)

- **Contrast without glow:** every text pairing passes on raw color, glow off: hud 14.3:1, bright 18.3:1, dim 7.7:1, amber 12.4:1, alert 8.0:1, ok 12.0:1 on their grounds. Text-shadow is a 1-2px halo on headers/chrome only; body text never glows.
- **Status is never color-only:** amber/alert/ok states always ship a text label (`CAUTION`, `ALERT`, `NOMINAL`) plus `role="status"` where they update live.
- **Focus:** `outline: 2px solid var(--hud); outline-offset: 3px` on dark grounds; on `--fill` cyan surfaces the outline flips to `#05080D` (WCAG 2.4.11). Chamfered corners never clip the focus ring: keep the outline offset larger than the chamfer.
- **Motion:** radar sweeps, scanlines, and blips are `aria-hidden` decoration, paused on hover and `:focus-within`, and fully removed by `prefers-reduced-motion: reduce`; interactive state changes stay at 200ms.
- **Targets:** 44px minimum; chamfers cut into the box, so pad generously inside the clip.
- **Live regions:** telemetry updates use `aria-live="polite"` on the value container, not the whole panel, to avoid screen-reader storms.

## Top-5 failure modes

1. **Glow-dependent contrast** - text readable only through its halo. Fix: measure every pair with glow off; halo only on headers and chrome, per the rules in [references/style-guide.md](references/style-guide.md).
2. **Neon soup** - magenta, lime, and orange at once. Fix: cyan + amber + alert + ok only; color = status meaning; the palette audit is in [references/quality-checklist.md](references/quality-checklist.md).
3. **Motion that never stops** - infinite sweeps, blinking cursors everywhere. Fix: continuous motion is decorative, pausable, and reduced-motion-safe; patterns in [references/implementation-examples.md](references/implementation-examples.md).
4. **Chamfer-clipped text and focus** - clip-path eats descenders and focus rings. Fix: pad 12-16px inside chamfers and keep outline offset ≥3px.
5. **Purple-gradient backdrop drift** - the lazy sci-fi tell. Fix: near-black ground plus hairline grid; glow lives on chrome only.

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
