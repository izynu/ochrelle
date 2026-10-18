---
name: ochrelle-y2k
description: Art direction and implementation skill for Y2K design, the 1997-2004 dot-com futurism aesthetic of translucent candy plastics, chrome and metallic gradients, gel and bubble buttons, lens flares, silver hi-tech whites, and millennium optimism. Covers iMac G3 color culture, Aqua-era gel materials, and T9-phone LCD moods. Use when a project calls for y2k, retro-futurist, millennium, bubblegum tech, chrome, bubbly, or dot-com era design; when building music and rave event pages, fashion drops, Gen Z portfolios, games, stickers and merch, or themed landing pages; or when a user mentions bubble buttons, lens flares, iMac colors, or turn-of-the-millennium tech vibes.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: thematic-genres
---

# Y2K Design

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Y2K design is the interface language of turn-of-the-millennium tech optimism (roughly 1997 to 2004): translucent candy plastics, chrome and silver gradients, gel and bubble buttons, lens flares, and friendly digital readouts. It believed the future was glossy, colorful, and consumer-friendly: the iMac era answering corporate beige.

It is not skeuomorphism proper (leather and wood imitation), not Frutiger Aero (the 2004-2013 glossy-nature successor), and not vaporwave (ironic 80s nostalgia). Y2K is sincere futurism with candy materials.

| | Real Y2K system | Lazy version |
|---|---|---|
| Materials | 2-3 tokenized recipes: chrome, gel, translucent plastic | A different gradient on every element |
| Color | Silver/white base + 2-3 candy accents | Rainbow soup, every hue at once |
| Glow | Lens flares and speculars as single accents | Flares on every corner, glow on text |
| Type | Clean rounded/extended sans, generous tracking | Script fonts, warped text, low contrast |
| Depth | Gel highlights + soft drops, consistent light source | Random bevels and emboss everywhere |
| Result | Nostalgic but legible and fast | A MySpace page that fails WCAG |

If a page needs more than three gradient recipes, it has stopped being Y2K and started being noise.

## Philosophy

1. **Optimism is the brief.** The future is friendly, consumer-grade, and fun. Nothing menacing, nothing industrial: Y2K chrome smiles.
2. **Materials are physical but digital.** Translucent plastic, gel, and chrome: each is a tokenized CSS recipe with one light source, not an improvised gradient per element.
3. **Candy on silver.** The palette is hi-tech whites and silvers carrying 2-3 candy accents (bondi blue, bubblegum, lime). Base is calm, accents pop.
4. **Curvature and glow signal "digital".** Pills, bubbles, rounded plastics, specular highlights: the geometry says technology is approachable.
5. **One hero effect per view.** A lens flare, a chrome wordmark, or a gel shimmer: the single exclamation mark. Restraint is what separates homage from pastiche.
6. **Nostalgia never overrides usability.** 16px body floor, 4.5:1 text pairs, real focus states: the revival must ship accessible UI, not a screenshot.

## Brief historical context (verifiable)

- **iMac G3** launched May 1998: Jony Ive's translucent Bondi Blue plastic; more candy colors (blueberry, strawberry, tangerine, lime, grape) followed in 1999. It is the object that defined the era's material palette.
- **Nokia's early-2000s phones** (the 3310 arrived in 2000) normalized friendly consumer tech: monochrome silver-on-dark LCDs, T9 texting, tactile curves.
- **Mac OS X Aqua** (announced 2000) formalized the gel/bubble button look with its candy-colored, high-gloss controls; **Windows XP's Luna theme** (2001) carried the blue/green gradient mood to the mainstream PC.
- The period's **dot-com optimism** (1995-2000 boom) is the emotional source: silver surfaces, blue skies, and chrome everything promised a frictionless digital future.
- The aesthetic was **revived on TikTok and in fashion** from around 2019-2022, bringing the vocabulary back to event pages, merch, and Gen Z brands.

## When to use / when NOT

**Use for:**
- Music events, raves, and festival pages: the chrome-and-candy energy is native.
- Fashion drops, merch, stickers, and Gen Z brand moments built on revival culture.
- Portfolios and landing pages that want a strong, joyful period identity.
- Games and playful apps themed on early-2000s tech.
- One-off campaign sites where nostalgia *is* the message.

**Do NOT use for:**
- Banking, healthcare, government, or anything where trust must read as calm competence.
- Dense B2B SaaS and data tools: gel materials and glows tax sustained scanning.
- Long-form reading products: decorative surfaces fight text.
- Products that need dark-mode-first ergonomics: Y2K is a light-material system at heart.
- Brands whose guidelines forbid playful decoration.

## Quick art-direction token sketch

- `--bg: #EAF2FB` ice; `--surface: rgba(255,255,255,0.72)` translucent plastic panels; `--ink: #14213D` navy (14.14:1 on ice, 15.97:1 with white on it).
- `--gel-blue: #1B6CA8` for text-bearing fills (white label 5.59:1); `--bondi: #2FA8C9` decorative only; `--bubble: #FF8FD3` (navy ink 7.70:1); `--sun: #FFD166` (navy ink 11.08:1); `--ice-tint: #BFE7FA` (navy ink 12.19:1).
- Chrome recipe: `linear-gradient(180deg, #F8FAFC 0%, #C9D3E0 45%, #8E9BAE 100%)` for bars, bezels, wordmarks.
- Gel recipe: candy `linear-gradient(180deg, #7CC4F5, #1B6CA8)` + top inner white highlight + soft drop shadow `0 6px 14px rgba(20,33,61,0.25)`.
- Radius: pills for buttons/tabs (999px), 12-16px for panels; corners are soft, never sharp.
- Shadows: soft drops only (`0 6px 14px rgba(20,33,61,0.25)`); inner white highlights carry the "gel" read.
- Type: rounded or extended techno sans (Eurostile-like) for display with wide tracking; clean sans for body; 16px floor.
- Spacing: 8 / 16 / 24 / 40 / 64; airy, floating layouts.
- Motion: 150-250ms `ease-out`; gentle bounce allowed on toggles (one overshoot); shimmer sweeps 1.2s+ and die under reduced motion.

## Component guidance summary

- **Buttons:** gel pills: candy vertical gradient, inner top highlight, soft drop; navy or white label per contrast table; pressed state sinks (inset shadow).
- **Cards:** translucent white panels (`rgba(255,255,255,0.72)`) over tinted scenes, 1px white borders, soft shadows; content sits on solid white islands when the scene is busy.
- **Forms:** white inputs with 1-2px silver borders and rounded corners; focus = 2px `--gel-blue` ring with offset; errors in a deep red with text, never color alone.
- **Nav:** silver gradient bar or pill tab strip; active tab is the gel pill; icon + label, 44px targets.
- **Hero:** chrome wordmark (gradient text) or one lens flare over a sky-tinted scene; headline stays plain navy for legibility.
- **What stays restrained:** body copy (plain navy, 16px/1.6), tables (solid white, silver hairlines), iconography (rounded outline sets, 2px strokes).

## Canonical CSS recipe

```css
/* Y2K tokens + the gel button that defines the style */
:root {
  --bg: #EAF2FB;
  --ink: #14213D;
  --gel-blue: #1B6CA8;      /* white label 5.59:1 */
  --gel-blue-deep: #144E7C; /* pressed / hover step */
  --bubble: #FF8FD3;        /* navy ink 7.70:1 */
  --shadow-soft: 0 6px 14px rgba(20, 33, 61, 0.25);
  --ease-out: cubic-bezier(0.22, 0.61, 0.36, 1);
}
.btn-gel {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 12px 28px;
  border: 1px solid #144E7C;
  border-radius: 999px;
  background: linear-gradient(180deg, #7CC4F5 0%, #1B6CA8 100%);
  color: #FFFFFF;                          /* 5.59:1 on the darker stops */
  font: 600 1rem/1 system-ui, sans-serif;
  cursor: pointer;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.85),   /* the gel highlight */
    inset 0 -6px 10px rgba(20, 33, 61, 0.18),  /* bottom depth */
    var(--shadow-soft);
  transition: transform 200ms var(--ease-out), box-shadow 200ms var(--ease-out);
}
.btn-gel:hover  { transform: translateY(-1px); }
.btn-gel:active {
  transform: translateY(1px);
  box-shadow: inset 0 2px 6px rgba(20, 33, 61, 0.35);   /* sinks into the gel */
}
.btn-gel:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.btn-gel:disabled {
  background: linear-gradient(180deg, #D7DEE8, #AEB9C9);
  color: #3D4A63;                          /* ~5.6:1 on the darker stop */
  box-shadow: none; cursor: not-allowed;
}
```

## Accessibility notes (mandatory)

- **Contrast:** body 4.5:1, large 3:1 (WCAG 1.4.3). The Y2K trap is white or pale text on gel gradients: white on a light-blue gel stop can fall under 3:1. Use white only on `#1B6CA8`-grade fills (5.59:1), navy on candy tints, and *measure the lightest stop* of any gradient behind text.
- **Chrome text:** gradient-filled wordmarks are display-size only; their darkest stop must still clear 3:1 against the background, or keep the wordmark decorative and repeat the message in plain text.
- **Focus:** `outline: 2px solid var(--ink); outline-offset: 3px` on every control; glow is never a focus substitute (WCAG 2.4.7, 2.4.11).
- **Translucent panels:** text sits on a solid or near-solid island; verify contrast against the *composite* of panel over scene, not against the panel color alone.
- **Motion and flash:** lens flares and shimmer sweeps must be static or slow; nothing flashes more than 3 times per second (WCAG 2.3.1), and `prefers-reduced-motion: reduce` freezes shimmer/flare animations.
- **Targets:** 44x44px minimum; gel gloss is not a padding excuse.

## Top-5 failure modes

1. **Gradient soup.** Five different gradients per view read as noise, not material. Fix: three tokenized recipes (chrome, gel, plastic) from [references/style-guide.md](references/style-guide.md); everything else is flat.
2. **Lens flares over text.** A flare is a single accent, never overlaid on copy, and never repeated per section. Fix: one static `aria-hidden` flare per page, clear of text.
3. **White text on light gel.** Fails contrast on the light stops. Fix: white labels only on `#1B6CA8`-grade fills; navy on candy; measure the lightest stop.
4. **Chrome at reading size.** Gradient text under 24px is illegible and usually fails contrast. Fix: chrome for display only; body stays plain navy.
5. **Animation everything.** Shimmer loops, pulsing glows, animated flares: inaccessible and heavy. Fix: static effects, one optional slow sweep, killed by `prefers-reduced-motion` ([references/implementation-examples.md](references/implementation-examples.md)).

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
