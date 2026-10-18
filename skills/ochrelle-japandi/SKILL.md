---
name: ochrelle-japandi
description: Art direction and implementation skill for Japandi, the fusion of Japanese wabi-sabi and Scandinavian hygge that spread through interior and product design in the 2010s. Muted naturals such as warm beige, clay, moss, and charcoal, low-contrast yet AA-safe layering, generous negative space, matte natural textures like linen and wood, asymmetric balance, and quiet craft restraint. Use for wellness and mindfulness apps, hospitality and booking sites, portfolios, calm productivity tools, skincare and tea brands, and boutique hotels. Trigger words include japandi, wabi-sabi, zen, hygge, organic, calm, mindful, quiet luxury, natural, minimal warmth.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: typographic-expressive
---

# Japandi

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Japandi is the quiet fusion of Japanese wabi-sabi (beauty in imperfection, impermanence, restraint) and Scandinavian hygge (warmth, comfort, care). On screen it means warm beige grounds instead of white, charcoal instead of black, matte textures instead of gloss, asymmetric balance instead of mirrored grids, and enough negative space that every element earns its place.

What it is NOT: it is not sterile minimalism with gray-on-gray text, not "add a bamboo photo", and not low-contrast aesthetics that fail WCAG. Calm that is illegible is broken.

| | Real Japandi | Lazy "zen minimal" |
|---|---|---|
| Ground | Warm beige `#F2EDE3`, layered off-whites | Pure white, cold gray |
| Ink | Soft charcoal `#2E2C28` (11.9:1) | Thin gray text at 2.8:1 |
| Texture | Matte linen, paper grain, wood grain | Glassy gradients and gloss |
| Balance | Asymmetric, weighted like ikebana | Perfectly mirrored 3-column rows |
| Detail | Visible craft: stitch, joinery, grain | Blank surfaces with nothing to hold |
| Result | Warm, quiet, alive | Cold, empty, flat |

## Philosophy

1. **Quiet is loud enough.** The style's confidence comes from restraint: fewer elements, softer edges, muted tone. If it needs decoration to feel designed, it has already failed.
2. **Imperfection is texture.** Wabi-sabi lets materials show themselves: paper grain, linen weave, brush-like rules, hand-set asymmetry. Perfection reads as machine; texture reads as care.
3. **Warmth is structural.** Hygge is engineered with warm grounds, soft radii, and gentle shadows, not with gradients or rounded-everything creep.
4. **Asymmetry balances.** Compositions weight to one side the way ikebana does: one mass, one void, one line. Negative space is a component, budgeted like any other.
5. **Contrast is earned.** The palette is low-chroma, never low-legibility: muted text colors are chosen to pass AA, and layering does the subtle work color cannot.

## Brief historical context (verifiable)

- The dialogue is old: mid-century Scandinavian designers such as Finn Juhl and Hans Wegner openly absorbed Japanese joinery, proportion, and material honesty into Danish modern furniture.
- **Wabi-sabi** stems from Japanese tea-culture aesthetics that prize imperfection, impermanence, and incompleteness; it entered Western design vocabulary through late-20th-century writing on Japanese arts.
- **Hygge**, the Danish and Norwegian concept of cozy conviviality, became a global lifestyle and interiors keyword during the 2010s publishing wave.
- The compound term **Japandi** itself surfaced as an interiors label in the mid-2010s and became a headline trend in 2020, when design media consolidated it as the year's dominant "calm" style.
- Its web translation rides the same wave as slow, calm digital products: muted palettes, serif-and-sans pairings, and photography of matte natural materials.

## When to use / when NOT

**Use for:**
- Wellness, meditation, and mindfulness apps where calm is the product.
- Hospitality: boutique hotels, onsen/spa booking, tea and coffee houses, restaurants with craft kitchens.
- Skincare, ceramics, stationery, and furniture brands selling material honesty.
- Portfolios for photographers, makers, and studios with tactile work.
- Calm productivity tools (journaling, focus timers, notes) and slow editorial sites.

**Do NOT use for:**
- Trading, analytics, or security dashboards - density and instant scanning beat calm.
- Youth hype drops, gaming, sports - the energy is wrong.
- Emergency, alert-heavy, or safety-critical interfaces - calm must never mute urgency.
- Brands whose identity is loud, maximal, or neon - this style will read as off-brand silence.

## Quick art-direction token sketch

- `--bg: #F2EDE3` (warm beige; charcoal ink on it: 11.9:1) and `--card: #FAF7F1` for raised layers.
- `--ink: #2E2C28` soft charcoal; `--muted: #6A655C` for secondary text (5.0:1 on beige, 5.4:1 on cards).
- `--clay: #96614A` (white text on it: 5.1:1) for primary actions and accents; `--moss: #67714E` (white text: 5.2:1) for confirmations and tags; `--line: #D9D0C0` hairlines.
- `--charcoal: #3B3833` inverted surfaces with `#F2EDE3` text (10.0:1) for footers and immersive panels.
- Spacing: 8 / 16 / 24 / 40 / 64 / 96 / 128 - the most generous scale in the library; a section needs 96px of air to breathe.
- Type: quiet pairing - light-contrast serif or refined sans for display (300-500 weight, `clamp(2rem, 4.5vw, 3.25rem)`), `1.0625rem/1.75` body, tracked uppercase micro-labels.
- Radius: 2-4px on components (soft, not soft-everything); images may take 4px or full bleed.
- Shadows: rare and diffuse - `0 8px 24px rgba(46, 44, 40, 0.08)` for overlays and lifted cards only.
- Motion: `220ms ease-out`, gentle and short; fades under 8% translate distance; nothing springs.

## Component guidance summary

| Component | Japandi treatment |
|---|---|
| Buttons | Clay or moss fill, off-white text, 4px radius, no border; ghost buttons use 1px line border |
| Cards | Off-white card on beige ground, 1px `--line` border, no shadow; one may lift with the diffuse shadow |
| Forms | Off-white inputs, 1px `--line` borders, focus moves to a 2px charcoal line; labels float small and quiet |
| Nav | Transparent on beige, tracked micro-label links, charcoal text; a single hairline under the masthead |
| Imagery | Matte photography of natural materials (linen, wood, stone, ceramic), warm-graded, asymmetric crops |
| Iconography | 1.5px stroke line icons in charcoal, 20px grid, used sparingly |

## Canonical CSS recipe

```css
:root {
  --bg: #F2EDE3;        /* 11.9:1 with ink */
  --card: #FAF7F1;      /* 13.0:1 with ink */
  --ink: #2E2C28;       /* 11.9:1 on bg */
  --muted: #6A655C;     /* 5.0:1 on bg, 5.4:1 on card */
  --clay: #96614A;      /* white text on it: 5.1:1 */
  --moss: #67714E;      /* white text on it: 5.2:1 */
  --line: #D9D0C0;
  --charcoal: #3B3833;  /* bg text on it: 10.0:1 */
  --radius: 4px;
  --calm: 220ms ease-out;
}
.btn-calm {
  font: 500 0.9375rem/1 system-ui, sans-serif;
  letter-spacing: 0.02em;
  color: #FAF7F1;
  background: var(--clay);
  border: 0;
  border-radius: var(--radius);
  padding: 0.875rem 1.75rem;
  min-height: 44px;
  transition: background var(--calm), transform var(--calm);
}
.btn-calm:hover { background: #85543F; }
.btn-calm:active { transform: translateY(1px); }
.btn-calm:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.card-calm {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 24px;
}
.card-calm h2 {
  font: 500 1.375rem/1.3 var(--font-display, Georgia, serif);
  color: var(--ink);
}
.card-calm p { color: var(--muted); margin-top: 8px; }
.rule-calm {
  border: 0;
  border-top: 1px solid var(--line);
  margin: 64px 0;
}
```

## Accessibility notes (mandatory)

- **The low-contrast trap:** Japandi looks quiet but ships loud legibility. Body text is `#2E2C28` (11.9:1 on beige); the lightest permitted text is `--muted #6A655C` at 5.0:1, reserved for secondary copy. Nothing grayer ships, ever.
- **Buttons:** white/off-white text on clay (5.1:1) or moss (5.2:1) passes AA body contrast; hover states darken the fill (`#85543F`), never lighten it.
- **Focus:** `outline: 2px solid var(--ink); outline-offset: 3px` on every interactive element; on charcoal surfaces the outline flips to `#F2EDE3` (WCAG 2.4.11). Focus must remain visible against the beige ground: 2px charcoal passes 3:1 everywhere on this palette.
- **Negative space is not emptiness for screen readers:** landmarks (`header`, `nav[aria-label]`, `main`, `footer`) and a real heading outline carry the structure the eye gets from whitespace.
- **Motion:** 220ms fades and 8px-or-less translations only; `prefers-reduced-motion: reduce` collapses them to instant states.
- **Targets:** 44px minimum on buttons, nav links, and list rows; generous padding is the style's native target-size strategy.
- **Imagery:** matte photography needs alt text that names the material and moment ("Linen cushion on oak bench in morning light"), never "aesthetic photo".

## Top-5 failure modes

1. **Gray-on-gray legibility failure** - muted text at 3:1 "because calm". Fix: `--muted` is the floor at 5.0:1; the pair audit table is in [references/quality-checklist.md](references/quality-checklist.md).
2. **Sterile white drift** - pure white ground, cold gray ink, blue links: minimalism, not Japandi. Fix: the warm token set (beige, card, charcoal, clay) from [references/style-guide.md](references/style-guide.md).
3. **Symmetric template reuse** - three identical centered columns. Fix: asymmetric composition rules (one mass, one void, one line) in section 7 of the style guide.
4. **Gradient and gloss creep** - glassy buttons and gradient heroes destroy the matte premise. Fix: flat fills, 1px lines, diffuse shadow only on overlays.
5. **Zen cliches as design** - stock lotus photos, bamboo borders, enso SVGs everywhere. Fix: one material texture per view, real photography of the actual product or space; icon restraint rules in [references/implementation-examples.md](references/implementation-examples.md).

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
