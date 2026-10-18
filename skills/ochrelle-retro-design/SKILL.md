---
name: ochrelle-retro-design
description: Art direction and implementation skill for retro Americana design - mid-century 1950s-1960s diner and populuxe graphics fused with 1970s warmth. Googie shapes and starbursts, halftone dots, vintage badge seals, groovy rounded display type, and a warm palette of cream, burnt orange, mustard, avocado, and brown. Use for cafes, diners, bakeries, breweries and taprooms, record and vinyl stores, barbershops, food packaging, event posters, and any brand selling warmth, nostalgia, and craft. Trigger words include retro, vintage, mid-century, fifties, sixties, seventies, googie, diner, populuxe, groovy, nostalgic, Americana.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: period-aesthetics
---

# Retro Design (Mid-Century Americana & 1970s Warmth)

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Retro design here means the commercial graphic language of mid-century American storefronts and print, carried forward to the web: menu boards, badge seals, starburst price flags, halftone screens, and groovy rounded type, warmed into the 1970s palette. It is optimistic, tactile, and a little theatrical - the design equivalent of a neon "OPEN" sign.

What it is NOT: it is not "anything older than 2000", not a sepia photo filter on a default template, and not kitsch by accident. Random serif fonts plus a paper texture is a costume, not a style.

| | Real retro art direction | Lazy "vintage" theme |
|---|---|---|
| Type | Groovy rounded display face + sturdy text face, tight pair | Times New Roman with a drop shadow |
| Color | 1 warm ground + 3-4 period fills, disciplined | Sepia wash over stock blue links |
| Ornament | Starbursts, badges, dots used as structure | Clip-art apron emoji in the header |
| Texture | Halftone screens and print grain, deliberate | "paper_texture_final_v2.jpg" at 40% opacity |
| Layout | Menu-board logic: blocks, rows, dotted leaders | Centered hero, three feature cards |
| Result | Reads as one hand, one era, one place | Reads as a template wearing a costume |

## Philosophy

1. **Print is the material.** The reference is ink on coated paper and enamel on steel: flat spot colors, halftone screens, crisp rules. Screens imitate the artifacts of print (dot gain, misregistration) only as deliberate choices.
2. **Shapes sell optimism.** Boomerang angles, porthole windows, starbursts: googie geometry is the emotional core. Use it where attention is earned (badges, CTAs, section marks), not sprayed everywhere.
3. **A warm palette with discipline.** Cream ground, warm brown ink, and at most four period fills (burnt orange, mustard, avocado, cherry). The moment a cool gray or a pure `#0000FF` appears, the era collapses.
4. **Nostalgia is a tone, not a costume.** The goal is "this place has been here forever and cares", not a museum diorama. Modern usability (real forms, fast loads, visible focus) is part of the fiction's credibility.
5. **The badge is composition.** Seal, burst, and oval shapes organize hierarchy the way a menu board does: today's special gets the starburst; the house rules get the plaque.

## Brief historical context (verifiable)

- **Googie** architecture is named for Googie's coffee shop in Los Angeles, designed by John Lautner in 1949; the name was coined as a jab in a 1952 House & Home article by Douglas Haskell. Angled roofs, boomerangs, starbursts, and cantilevered signs defined it.
- **Populuxe**, the name historians use for the exuberant 1950s-60s consumer aesthetic, comes from Thomas Hine's 1986 book *Populuxe*.
- Roadside Americana built the graphic kit this skill uses: porcelain-enamel and neon signs, diner menu boards, and starburst price flags. The LAX Theme Building (opened 1961) is a surviving googie landmark.
- **Cooper Black**, drawn by Oswald Bruce Cooper and released in 1922, became an inescapable display face of 1970s album covers and grocery branding - the canonical "groovy warm" voice.
- Avocado green and harvest gold became appliance and kitchen staples across the 1970s; pairing them with cream, brown, and burnt orange reads instantly as that decade.

## When to use / when NOT

**Use for:**
- Cafes, diners, bakeries, ice cream shops - menu-board layouts and badge CTAs are native here.
- Breweries, taprooms, pizzerias, BBQ joints - label and packaging DNA translates directly to web.
- Record and vinyl stores, barbershops, bowling alleys, drive-ins, retro arcades.
- Event posters, food festivals, merch drops - the poster grammar (burst, badge, big type) carries.
- Any brand whose promise is warmth, craft, and nostalgia rather than speed and novelty.

**Do NOT use for:**
- Fintech, healthcare, insurance, government - period type undermines trust in critical information.
- Data-dense dashboards and admin tools - menu-board layouts cannot carry 40 columns of table.
- Luxury and high fashion - retro warmth reads as friendly, not exclusive.
- Dark-mode developer tools - the cream ground is the style's spine; without it the system breaks.

## Quick art-direction token sketch

- `--bg: #F7EFD9` (cream ground; brown ink on it: 11.7:1) and `--paper: #FFFDF5` for raised cards.
- `--ink: #3D2B1F` (warm brown, not black) - body text, rules, outlines.
- `--accent: #AD4E1A` (burnt orange; cream text on it: 5.4:1) - CTAs, starburst fills, active states.
- `--mustard: #D9A404` (ink text on it: 5.9:1), `--avocado: #6B7C33` (cream text: 4.6:1), `--cherry: #A32E2E` (cream text: 7.0:1) - section fills and badges.
- `--muted: #6B5138` for secondary text (6.4:1 on cream).
- Spacing scale: 4 / 8 / 16 / 24 / 40 / 64 / 96 - menu boards are generous with rows, tight within blocks.
- Type scale: display `clamp(2.5rem, 6vw, 4.5rem)` weight 700-800 rounded; h2 `2rem`; body `1rem/1.6`; labels `0.8125rem` uppercase, tracked `0.08em`.
- Radius: `10px` on panels, `999px` on pills and badge ovals - soft, never razor-sharp, never bubbly 24px.
- Shadows: minimal and warm - `0 2px 0 rgba(61, 43, 31, 0.25)` as a letterpress hint; no blur stacks.
- Motion: `180ms ease-out`; hovers lift 1-2px; starbursts rotate on hover only. Respect `prefers-reduced-motion`.

## Component guidance summary

| Component | Retro treatment |
|---|---|
| Buttons | Pill shape, burnt orange or cherry fill, cream text, 2px brown border, letterpress shadow; hover lifts 1px |
| Cards | Paper panels with 2px brown border and 10px radius; badge or burst pinned to a corner |
| Forms | Cream inputs with 2px brown borders, uppercase tracked labels, dotted leaders in summary rows |
| Nav | A menu-board bar: wordmark left, links as tracked uppercase "aisles", current page marked with a dot or underline rule |
| Imagery | Real photography, warm-graded; halftone dot screens on decorative bands only |
| Iconography | Chunky 2px stroke icons or filled period glyphs (arrows, forks, records); no thin line sets |

## Canonical CSS recipe

```css
:root {
  --bg: #F7EFD9;
  --paper: #FFFDF5;
  --ink: #3D2B1F;        /* 11.7:1 on cream */
  --accent: #AD4E1A;     /* cream text on it: 5.4:1 */
  --mustard: #D9A404;    /* ink text on it: 5.9:1 */
  --cherry: #A32E2E;     /* cream text on it: 7.0:1 */
  --muted: #6B5138;      /* 6.4:1 on cream */
  --radius: 10px;
  --press: 180ms ease-out;
}
.btn-retro {
  font: 700 1rem/1 system-ui, sans-serif;
  letter-spacing: 0.02em;
  color: #FFFDF5;
  background: var(--accent);
  border: 2px solid var(--ink);
  border-radius: 999px;
  padding: 0.75rem 1.5rem;
  min-height: 44px;
  box-shadow: 0 3px 0 rgba(61, 43, 31, 0.35);
  transition: transform var(--press), box-shadow var(--press);
}
.btn-retro:hover { transform: translateY(-2px); }
.btn-retro:active { transform: translateY(1px); box-shadow: 0 1px 0 rgba(61, 43, 31, 0.35); }
.btn-retro:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; }
.starburst {
  display: grid; place-items: center; width: 96px; height: 96px;
  background: var(--mustard); color: var(--ink);
  font: 800 0.875rem/1.1 system-ui, sans-serif; text-transform: uppercase;
  clip-path: polygon(50% 0%, 60% 13%, 75% 7%, 77% 23%, 93% 25%, 87% 40%, 100% 50%, 87% 60%, 93% 75%, 77% 77%, 75% 93%, 60% 87%, 50% 100%, 40% 87%, 25% 93%, 23% 77%, 7% 75%, 13% 60%, 0% 50%, 13% 40%, 7% 25%, 23% 23%, 25% 7%, 40% 13%);
}
.halftone-band {
  height: 24px;
  background-image: radial-gradient(circle, rgba(61, 43, 31, 0.4) 1.4px, transparent 1.6px);
  background-size: 8px 8px;
}
```

## Accessibility notes (mandatory)

Retro warmth never suspends WCAG 2.2 AA. The period palette is friendly to contrast if paired by rule:

- **Text pairing rule:** cream or white text only on burnt orange (5.4:1), avocado (4.6:1), cherry (7.0:1), and brown ink; brown ink text only on cream, paper, and mustard (5.9:1). Never white on mustard (~1.9:1) and never brown ink on burnt orange (~2.5:1).
- **Focus:** `outline: 3px solid var(--ink); outline-offset: 3px` on every interactive element (WCAG 2.4.11). The 2px component border is not a focus indicator.
- **Halftone and starburst discipline:** decorative screens sit behind nothing legible - no text over dots; the starburst's clip-path must not clip its own label (keep labels ≤ 3 short lines, min 0.875rem bold).
- **Reduced motion:** hover lifts, rotating bursts, and marquee specials collapse to static states under `prefers-reduced-motion: reduce`.
- **Targets:** pill buttons keep ≥ 44px height; nav links get full-height tap areas.
- **Links** in body copy are underlined (dotted or solid) - period styling never removes the affordance.

## Top-5 failure modes

1. **Sepia costume drift** - a gray template with a paper texture and a serif logo. Fix: commit to the token system (cream ground, brown ink, period fills) and the menu-board layout in [references/style-guide.md](references/style-guide.md).
2. **White text on mustard** (about 1.9:1) or brown text on burnt orange (about 2.5:1). Fix: follow the pairing rule above; the audit table is in [references/quality-checklist.md](references/quality-checklist.md).
3. **Ornament inflation** - five starbursts and four badges competing on one screen. Fix: one burst per view, one badge per card; ornaments mark hierarchy, they are not confetti.
4. **Texture over text** - halftone or grain screens laid under paragraphs, cutting legibility. Fix: decorative bands live in dedicated strips and section fills; text always sits on flat ground.
5. **Period fonts that fight** - three display faces plus a script. Fix: exactly one groovy display face, one workhorse text face, tracked uppercase labels for everything else; see the type section in [references/implementation-examples.md](references/implementation-examples.md).

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
