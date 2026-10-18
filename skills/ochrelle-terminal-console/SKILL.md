---
name: ochrelle-terminal-console
description: "Art direction and implementation skill for text-first terminal and console UI: monospace grids, box-drawing frames, tiling panes, status bars, prompt symbols, and phosphor-green or amber type on near-black grounds. Grounded in 1970s CRT video terminals, BIOS and DOS text modes, and TUI conventions from tmux, vim, and htop. Use when building developer tools, CLI companions, log viewers, status dashboards, terminal emulators, package manager UIs, or engineering-first products, or when a user mentions terminal, console, TUI, command line, phosphor, CRT, monospace, hacker aesthetic, retro computer, or tmux-style layout. Includes accessibility-safe phosphor palettes, inverse-video interaction states, live log regions, and reduced-motion-safe animation."
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: typographic-expressive
---

# Terminal Console

Terminal Console brings text-mode discipline to the browser: every element sits on a monospace cell grid, panels are framed with box-drawing borders, hierarchy comes from brightness and position instead of size and shadow, and the interface answers like a machine: instantly. It is the aesthetic of the VT100, the DOS prompt, and the tmux status bar, rebuilt as an accessible web design system.

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

A terminal console UI is a composition of text cells: fixed-width type, character-aligned columns, bordered panes, inverse-video states, and a persistent status line. Structure is drawn, not implied. The real thing is engineered; the lazy thing is a dark page with green text.

| | Real terminal console | Lazy "hacker page" |
|---|---|---|
| Grid | Every column aligns to the mono cell rhythm | Text wraps wherever it wraps |
| Frames | Box-drawing or 1px borders on every pane | Floating blocks, no frames |
| Color | One phosphor hue + status colors, brightness = hierarchy | Green, amber, cyan, and red all shouting at once |
| Type | Monospace everywhere structure exists; 16px body floor | 12px monospace walls of text |
| States | Inverse video, instant | CSS glow soup, blurry text-shadow on glyphs |
| Read of | "This tool is real and maintained" | "This is a themed landing page" |

What it is NOT: not an unstyled HTML document, not a photo of a CRT with a bezel and glass reflections bolted onto a normal site, and not license to put text-shadows on body copy. The CRT look lives in the palette and the grid, never in blurring the glyphs.

## Philosophy

1. **Grid before chrome.** Alignment is the aesthetic. Before adding any decoration, everything must line up on the monospace cell rhythm; a misaligned console is broken, not styled.
2. **Monospace is law for structure.** Numbers, labels, tables, logs, and code are monospace. Body prose may stay sans, but if a page is mostly prose, this is the wrong style.
3. **Brightness is hierarchy.** Phosphor displays had one hue and many brightnesses. Use the same trick: bright for active and important, mid for body, dim for secondary. Size changes less; tone changes more.
4. **The machine speaks plainly.** Status lines, prompt symbols (`$`, `>`, `[ok]`, `[fail]`), and explicit text labels are honest. Never hide state behind icon-only gestures; a console says what it does.
5. **Keyboard first, pointer second.** TUIs are keyboard-native. Full tab order, visible focus, and shortcuts are part of the style, not an add-on.
6. **Color is information.** A color change means something changed. Green = ok, amber = warn, red = fail, and nothing else. If a color carries no state, it should not exist.

## Brief historical context (verifiable)

- **DEC VT100 (1978):** Digital Equipment Corporation's video terminal standardized the 80x24 cell grid and became the reference for ANSI-compatible text terminals.
- **ECMA-48 (1976) / ANSI X3.64 (1979):** the escape-code standards that defined SGR attributes, including inverse video and the color codes modern terminal palettes still inherit.
- **Phosphor heritage:** green P1 phosphor dominated early video terminals; amber (long-persistence P3) displays spread through the late 1970s and early 1980s, marketed as easier on the eyes during long sessions.
- **IBM PC (1981):** shipped with an 80x25 text mode serviced by the BIOS; DOS applications and shareware UIs made 80x25 the de facto layout frame.
- **xterm (1984):** born with the X Window System and still the reference for terminal color scheme design (its green/amber defaults anchor most palettes).
- **Vim (1991, Bram Moolenaar), htop (2004, Hisham Muhammad), tmux (2007, Nicholas Marriott):** the TUI canon; their status bars, pane splits, and shortcut conventions are the idioms users expect. Modern developer tooling (CI logs, cloud consoles) adopted the same look as a trust signal.

## When to use / when NOT

**Use for:**
- Developer tools, log viewers, CI/build dashboards, API explorers, and observability products.
- CLI companion sites, package manager docs, and engineering-first SaaS.
- Status pages and ops dashboards where density and scanability beat decoration.
- Any brand that wants to signal "built by engineers, for engineers".

**Do NOT use for:**
- Long-form reading products: monospace body text fatigues fast at length.
- Consumer marketing, luxury, or photography-led brands: the metaphor reads technical, not premium.
- Non-technical audiences who will read the dark screen with green text as "hacker cosplay" rather than competence.

## Quick art-direction token sketch

- `--bg: #0A0F0A` (green theme) or `#140D04` (amber theme); near-black with a phosphor tint.
- `--ink: #A8F0BC` body text, 14.6:1 on `--bg`; amber theme body `#FFD9A0`, 14.4:1.
- `--bright: #33FF77` active/labels, 14.5:1 on bg; `--dim: #6FA57E` secondary, 6.8:1 on bg (still AA).
- `--line: #4A7D58` component borders, 4.0:1 on bg (passes WCAG 1.4.11 non-text 3:1); `--hairline: #1F3526` decorative only. Status: `--warn: #FFB454` (11.0:1), `--error: #FF6B66` (7.0:1).
- Spacing scale: 4 / 8 / 12 / 16 / 24 based on the cell; pane padding 12-16px; gutter 16-24px.
- Type: monospace stack only (`ui-monospace, "SF Mono", Menlo, Consolas, monospace`); body 16px, labels 13px uppercase with 0.08em tracking; line-height 1.5.
- Radius: 0-2px max. Shadows: none. Glow only as decoration on non-text surfaces.
- Motion: 0-80ms instant state changes; cursor blink 1s steps; spinner 100ms/frame; all killed under reduced motion.

## Component guidance summary

- **Buttons:** bracketed or bordered mono labels; hover = inverse video (bg and ink swap); active = brighter inverse, instant. The `[ Deploy ]` bracket is the signature.
- **Cards/panes:** 1px bordered boxes with a one-line uppercase title bar and a hairline divider; content sits on a strict column grid; optional corner glyphs (`+`) at frame joints.
- **Forms:** prompt-line inputs: `> ` prefix, bottom-border only, caret in `--bright`; labels as uppercase mono above; errors as `[!] message` lines in `--error`.
- **Nav:** tmux-style status bar: left = brand/session, center or right = items, current item rendered as inverse-video block; bottom-anchored bars are idiomatic. Tables/logs: zebra via panel tone, timestamps in `--dim`, severity as text tags (`[ok]`, `[warn]`, `[fail]`), never color alone.

## Canonical CSS recipe

```css
:root {
  --bg: #0A0F0A;
  --panel: #101812;
  --ink: #A8F0BC;      /* 14.6:1 on bg */
  --bright: #33FF77;   /* 14.5:1 on bg - labels, active */
  --dim: #6FA57E;      /* 6.8:1 on bg - secondary */
  --line: #4A7D58;     /* 4.0:1 on bg - functional borders */
  --hairline: #1F3526; /* decorative rules only */
  --warn: #FFB454;     /* 11.0:1 */
  --error: #FF6B66;    /* 7.0:1 */
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, "DejaVu Sans Mono", monospace;
}
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font: 16px/1.5 var(--font-mono);
}

/* Pane: a framed text-mode panel with a title bar */
.pane { border: 1px solid var(--line); background: var(--panel); }
.pane-title {
  padding: 6px 12px;
  border-bottom: 1px solid var(--hairline);
  color: var(--bright);
  font-size: 13px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

/* Button: bracket label + inverse-video hover, instant feedback */
.btn {
  font: inherit;
  color: var(--ink);
  background: transparent;
  border: 1px solid var(--line);
  padding: 8px 14px;
}
.btn::before { content: "[ "; color: var(--dim); }
.btn::after  { content: " ]"; color: var(--dim); }
.btn:hover { background: var(--ink); color: var(--bg); }
.btn:hover::before, .btn:hover::after { color: inherit; }
.btn:active { background: var(--bright); color: var(--bg); transition: none; }
.btn:focus-visible { outline: 2px solid var(--bright); outline-offset: 2px; }
.btn:disabled { color: var(--dim); border-color: var(--hairline); cursor: not-allowed; }

/* Status bar nav: tmux-style, current item is inverse video */
.statusbar {
  display: flex; gap: 4px; align-items: stretch;
  padding: 4px 12px;
  border-top: 1px solid var(--line);
  background: var(--panel);
  font-size: 13px;
}
.statusbar a { color: var(--dim); text-decoration: none; padding: 4px 10px; }
.statusbar a:hover { color: var(--bright); }
.statusbar a[aria-current="page"] { background: var(--bright); color: var(--bg); }
.statusbar a:focus-visible { outline: 2px solid var(--bright); outline-offset: -2px; }
```

## Accessibility notes (mandatory)

- **Contrast floor:** body text `#A8F0BC` on `#0A0F0A` is 14.6:1; even dimmed secondary `#6FA57E` is 6.8:1, so WCAG 2.2 AA (4.5:1) holds everywhere. Never darken text below the dim token to fake hierarchy; use position and the dim tone only.
- **Glow discipline:** phosphor glow is simulated, if at all, with `box-shadow` on non-text containers or a separate decorative layer. `text-shadow` blurs glyphs and is banned on anything readable. The readable color must pass 4.5:1 without any glow.
- **Focus:** 2px solid `--bright` outline with 2px offset on every focusable element; in inverse-video states the outline flips to `--bg` on bright fills (WCAG 2.4.11; never `outline: none`). Interactive targets stay at least 44x44px.
- **Live regions:** log panes use `aria-live="polite"` (or `off` for high-rate streams) with a visible Pause control; cap announced rows so screen readers are not flooded.
- **Motion:** cursor blink, spinner frames, and any scanline drift stop under `prefers-reduced-motion: reduce`. CRT flicker filters are banned outright: they are a vestibular trigger and cost contrast.
- **Keyboard parity:** shortcuts documented in a visible help pane; every icon-adjacent action carries a text label.

## Top-5 failure modes

1. **Glow on glyphs** - `text-shadow` on body copy turns AA text into mush. Fix: glow only on container edges via `box-shadow`, never on text; verify 4.5:1 on the plain colors.
2. **Classic neon green as body text** - `#33FF33` walls of text vibrate and tire the eye. Fix: body `#A8F0BC`, reserve `--bright` for labels, active states, and the caret.
3. **Phosphor salad** - green, amber, and cyan on one screen reads as a theme shop, not a terminal. Fix: one hue per product plus the fixed status colors; run the palette gate in [references/quality-checklist.md](references/quality-checklist.md).
4. **Flicker filter everywhere** - CRT scanline/flicker overlays over text are an accessibility fail. Fix: if used at all, they go on empty decorative regions, under 4% opacity, and off under reduced motion.
5. **Unstyled-page drift** - ragged gutters, no status bar, mixed border weights: it reads as a broken dark page. Fix: the ch-based grid, pane frame system, and state matrix in [references/style-guide.md](references/style-guide.md).

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
