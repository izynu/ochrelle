---
name: ochrelle-memphis-design
description: Art direction and implementation skill for Memphis Design, the postmodern language born with the Memphis Milano group in 1981. Squiggles, zigzags, terrazzo speckle, clashing pastels against bright primaries, black-and-white stripes, asymmetric geometry, and chunky black outlines that refuse functionalist seriousness. Use for creative tools, music and club culture, party and event brands, youth products, sticker and merch shops, portfolio experiments, and anywhere deliberate play beats corporate calm. Trigger words include Memphis, postmodern, eighties, Milano, squiggle, terrazzo, zigzag, playful, anti-minimal, retro-futurist.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: period-aesthetics
---

# Memphis Design

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Memphis design is organized mischief: flat pastel and primary fills, chunky black outlines, speckled terrazzo, zigzag and squiggle motifs, and geometry that ignores both the grid and gravity. It is anti-functional on purpose - but the interface underneath must be ruthlessly functional. The play is in the art direction; the usability is non-negotiable.

What it is NOT: it is not "random 80s colors everywhere", not a pastel gradient festival, and not an excuse to drop contrast or skip states. Chaos without the ink referee is just a broken stylesheet.

| | Real Memphis art direction | Lazy "80s party" theme |
|---|---|---|
| Color | 5-fill palette disciplined by black outlines | Unlimited gradients, white text on pastels |
| Pattern | Terrazzo, stripes, zigzags as structured bands | Patterns behind body text everywhere |
| Geometry | Asymmetric but anchored compositions | Everything rotated 15deg for no reason |
| Line | Chunky 3px ink outline on every shape | No outlines, soft shadows, blur |
| Motion | One overshoot bounce on purpose | Infinite floating animations |
| Result | Playful and precise | Playful and unusable |

## Philosophy

1. **Play is a design decision.** Every squiggle and clash is chosen and placed like a compositor places type. Randomness is the one thing Memphis is not.
2. **Black ink is the referee.** 3px outlines, black text, black shadows: the constant ink line is what lets five clashing fills share one page without visual noise.
3. **Pattern is a material.** Terrazzo, stripes, and zigzags are construction materials with placement rules - bands, borders, and fills - never background washes under text.
4. **Asymmetry needs an anchor.** Rotated cards and off-grid shapes orbit one solid, aligned element (a headline block, a nav bar) so the page reads as composed, not spilled.
5. **Fun must stay usable.** AA contrast, visible focus, 44px targets, reduced-motion fallbacks. The joke is never at the user's expense.

## Brief historical context (verifiable)

- The Memphis group was founded in Milan by Ettore Sottsass; conceived in late 1980 and unveiled to the press and public at the September 1981 Milan furniture fair. It is named, by the group's own telling, from repeated plays of Bob Dylan's "Stuck Inside of Mobile with the Memphis Blues Again".
- Sottsass's **Carlton** room divider and **Casablanca** sideboard (both 1981) are the movement's signature pieces: laminate, bright laminate patterns, and deliberately "bad" postmodern silhouettes.
- Designer **Nathalie Du Pasquier** and **George Sowden** created many of the group's defining patterns and decorated surfaces.
- Fashion designer **Karl Lagerfeld** fitted out his Monte Carlo apartment with Memphis pieces in the early 1980s; **David Bowie** was a major collector, and his Memphis holdings sold in the 2016 sale of his estate's art collection.
- Sottsass left the group in 1985; Memphis wound down around 1988, but its patterns colonized 1980s visual culture (TV graphics, cartoons, product packaging) and keep resurfacing in youth-brand design.

## When to use / when NOT

**Use for:**
- Creative tools, design-community products, portfolio experiments - audiences that get the joke.
- Music culture: label sites, festival and club promoters, vinyl merch, band stores.
- Party and event brands, invitations, ticketing for playful formats.
- Youth products, sticker packs, merch drops, indie games.
- Campaign pages that need to signal "we are not a bank" within one second.

**Do NOT use for:**
- Banking, insurance, healthcare, government - trust requires calm.
- Enterprise B2B dashboards and long data tables - patterns and asymmetry tax scanning.
- Luxury brands - Memphis is laminate, not lacquer; it undercuts premium cues.
- Continuous-reading products (news readers, documentation portals) - the style fights sustained reading.

## Quick art-direction token sketch

- `--bg: #FFF9EF` warm white ground; `--ink: #101010` near-black (18.2:1 on bg).
- The five-fill palette, **ink text on every fill**: `--yellow: #FFD23F` (13.2:1), `--lilac: #C9B1F5` (10.1:1), `--coral: #FF6B5B` (6.8:1), `--teal: #0FA3A3` (6.2:1), `--blue: #4EA8DE` (7.2:1). White text only on the ink ground (19:1) - never on fills.
- Borders: `3px solid var(--ink)` on every interactive and raised element; 6px on feature cards.
- Radius: a chosen mix, not a default - `0` on outlined graphic blocks, `12px` on cards, `999px` on chips and pills.
- Shadows: hard offset only - `4px 4px 0 0 var(--ink)` on buttons, `6px 6px 0 0 var(--ink)` on cards; blur stays 0.
- Spacing scale: 8 / 16 / 24 / 40 / 64 / 96; bands and patterns need breathing room (40px around any pattern strip).
- Type: one chunky display face (800-900 weight, geometric or slab) for headlines; one clean sans for body `1rem/1.6`; labels uppercase `0.05em` tracked.
- Motion: `200ms cubic-bezier(0.34, 1.56, 0.64, 1)` - one overshoot on press and entrance; nothing loops infinitely.

## Component guidance summary

| Component | Memphis treatment |
|---|---|
| Buttons | Coral or yellow fill, 3px ink border, hard 4px shadow; press slides onto the shadow |
| Cards | White or fill ground, 12px radius, 6px hard shadow, may rotate up to 2deg with one per section |
| Forms | White inputs, 3px ink border, 12px radius, chunky 3px focus outline offset 3px |
| Nav | Ink ground bar, white tracked links, one yellow "sticker" CTA - the page's anchor |
| Pattern bands | Terrazzo/stripe/zigzag strips 16-32px tall as section dividers, `aria-hidden` |
| Badges | Starburst or blob stickers pinned to corners, always outlined, max one per card |

## Canonical CSS recipe

```css
:root {
  --bg: #FFF9EF;
  --ink: #101010;        /* 18.2:1 on bg */
  --yellow: #FFD23F;     /* ink text 13.2:1 */
  --lilac: #C9B1F5;      /* ink text 10.1:1 */
  --coral: #FF6B5B;      /* ink text 6.8:1 */
  --teal: #0FA3A3;       /* ink text 6.2:1 */
  --blue: #4EA8DE;       /* ink text 7.2:1 */
  --bw: 3px;
  --radius: 12px;
  --bounce: 200ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
.btn-memphis {
  font: 800 1rem/1 system-ui, sans-serif;
  color: var(--ink);
  background: var(--coral);
  border: var(--bw) solid var(--ink);
  border-radius: 999px;
  padding: 0.75rem 1.5rem;
  min-height: 44px;
  box-shadow: 4px 4px 0 0 var(--ink);
  cursor: pointer;
  transition: transform var(--bounce), box-shadow var(--bounce);
}
.btn-memphis:hover { transform: translate(-1px, -1px); box-shadow: 5px 5px 0 0 var(--ink); }
.btn-memphis:active { transform: translate(2px, 2px); box-shadow: 2px 2px 0 0 var(--ink); }
.btn-memphis:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.card-memphis {
  background: #FFFFFF;
  border: 6px solid var(--ink);
  border-radius: var(--radius);
  box-shadow: 6px 6px 0 0 var(--ink);
  padding: 24px;
}
.stripe-band {
  height: 24px;
  background: repeating-linear-gradient(90deg, var(--ink) 0 12px, var(--bg) 12px 24px);
}
.terrazzo {
  height: 48px;
  background-color: #F3E9D2;
  background-image:
    radial-gradient(circle at 20% 40%, var(--coral) 0 5px, transparent 6px),
    radial-gradient(circle at 60% 20%, var(--teal) 0 4px, transparent 5px),
    radial-gradient(circle at 80% 70%, var(--yellow) 0 5px, transparent 6px),
    radial-gradient(circle at 35% 80%, var(--lilac) 0 4px, transparent 5px);
  background-size: 90px 60px;
}
```

## Accessibility notes (mandatory)

Memphis is the style most tempted to fail contrast; the rules below are the whole defense.

- **Text pairing rule:** ink `#101010` text on every fill (yellow 13.2:1, lilac 10.1:1, coral 6.8:1, teal 6.2:1, blue 7.2:1 - all pass AA). White text lives only on the ink ground (19:1). White on teal is 3.1:1 (large text only) and white on every other fill fails outright: do not use it.
- **Focus:** `outline: 3px solid var(--ink); outline-offset: 3px` everywhere; in the ink-ground nav, the outline is `#FFF9EF`. Rings are chunky because the borders are chunky (WCAG 2.4.11).
- **Patterns never host text.** Terrazzo, stripes, and squiggles are `aria-hidden` decorative bands; body text sits on flat white or flat fill only.
- **Rotation caps:** decorative elements rotate at most 2-3deg; interactive elements never rotate (hit target integrity at WCAG 2.5.8).
- **Motion:** the overshoot bounce is 200ms and fires on interaction only; infinite floaters are banned; `prefers-reduced-motion: reduce` removes transforms and loops entirely.
- **Targets:** 44px minimum on buttons, tabs, and nav links; hard shadows do not count toward the tap area.

## Top-5 failure modes

1. **White text on pastels** - the single most common Memphis collapse (white on lilac is about 2.0:1). Fix: ink text on every fill; white text only on ink; the audit table is in [references/quality-checklist.md](references/quality-checklist.md).
2. **Pattern under text** - terrazzo behind a paragraph. Fix: patterns live in dedicated `aria-hidden` bands with 40px clearance; composition rules in [references/style-guide.md](references/style-guide.md).
3. **Rotation anarchy** - everything tilted 8-15deg until nothing is clickable. Fix: 2-3deg cap on decoration, zero on interactive elements, one anchored axis-aligned block per section.
4. **Motion chaos** - infinite bouncing squiggles that never respect the user. Fix: one 200ms overshoot on interaction, no infinite loops, full reduced-motion fallback (recipe in [references/implementation-examples.md](references/implementation-examples.md)).
5. **Palette overflow** - seven fills, two gradients, no referee. Fix: hard ceiling of five flat fills + ink + ground; outlines on every raised shape; no gradients, no blur.

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
