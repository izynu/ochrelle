---
name: ochrelle-art-deco
description: "Art direction and implementation skill for Art Deco, the 1920s-30s style of geometric luxury: symmetrical stepped forms, sunburst fans, ziggurat corners, sharp rectilinear frames, double hairline rules, and a jewel palette of ivory, near-black, metallic gold, emerald, midnight blue, and oxblood. Use for boutique hotels and cocktail bars, tasting rooms and patisseries, theater and cinema sites, jewelry, perfume and spirits brands, wedding and event invitations, and museum exhibition pages. Trigger words include art deco, deco, gatsby, roaring twenties, jazz age, speakeasy, gold geometric, marquee, or cinema palace."
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: period-aesthetics
---

# Art Deco

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Art Deco on screen is architecture applied to interface: everything symmetrical, everything stepped, everything framed. Ivory ground, near-black structure, metallic gold drawn as line (not paint), jewel-tone panels, and display type set like a marquee. Elegance comes from geometry and edge control, never from blur or gradient.

What it is NOT: it is not gold-gradient "bling", not a cursive wedding font, and not Great Gatsby clip art. Confetti and feathers are a party theme; deco is a building system of steps, fans, chevrons, and frames.

| | Real Art Deco | Lazy "gatsby" theme |
|---|---|---|
| Gold | Thin metallic lines and small fills | Big gold gradients everywhere |
| Type | Geometric marquee display + geometric sans | Cursive script with gold gradient |
| Shape | Steps, fans, chevrons, ziggurat corners | Random circles and confetti PNGs |
| Layout | Symmetrical, centered, framed like a facade | Uneven blog grid |
| Color | Ivory + near-black + gold + 2 jewel tones max | Rainbow metallics |
| Result | Reads as a 1930s facade | Reads as a New Year flyer |

## Philosophy

1. **Symmetry is the skeleton.** Center axes, mirrored frames, balanced masses. Asymmetry belongs to the deco poster, not to the interface; a page that lists left-heavy is broken deco.
2. **Geometry is the ornament.** Every decoration is constructed: sunburst fans, stepped ziggurat corners, chevron bands, concentric arcs. Nothing organic, nothing freeform.
3. **Luxury is edge control.** Double hairlines, stepped frames, and precise spacing signal craft. Gradients and glows signal plastic; gold is drawn as a 1-2px line or a flat small fill.
4. **Jewel discipline.** Ivory and near-black carry the page; gold carries the accents; at most two jewel tones (emerald, midnight, oxblood) appear per view. More color collapses the ledger.
5. **Type is architecture.** Display faces are tall, stepped, and geometric like the buildings; body text stays quiet and geometric so the display can be loud.
6. **Motion is machinery.** Even, cadenced transitions (180ms), like elevator doors and clock mechanisms. Nothing bounces.

## Brief historical context (verifiable)

- The style takes its name from the 1925 Paris exhibition, the Exposition Internationale des Arts Decoratifs et Industriels Modernes; the shorthand "Art Deco" was popularized retrospectively in the 1960s, notably by historian Bevis Hillier's 1968 book on the 1920s and 1930s style.
- New York's 1916 Zoning Resolution forced the stepped "wedding cake" massing that became deco's skyline signature; the Chrysler Building (completed 1930, architect William Van Alen) is the canonical example, briefly the world's tallest building until the Empire State Building (1931).
- **Broadway**, drawn by Morris Fuller Benton for American Type Founders and released in 1928, is the loud geometric display face of theater marquees and 1930s poster work.
- Poster artist Cassandre (Adolphe Mouron Cassandre) defined deco graphic rigor in works such as the Normandie poster (1935): bold geometry, tight palettes, monumental scale.

## When to use / when NOT

**Use for:**
- Boutique hotels, cocktail bars, speakeasies, tasting rooms - the facade metaphor is native.
- Theaters, cinemas, concert halls, museum and exhibition pages.
- Jewelry, perfume, spirits, watches, patisserie - crafted luxury with a story.
- Wedding and event invitations, launch parties, gala microsites - any brand promising engineered glamour.

**Do NOT use for:**
- Developer tools, fintech dashboards, admin consoles - marquee type kills dense data.
- Kids products, sports, casual fast food - the register is wrong.
- Healthcare and government - ornament here reads as unserious.
- Dark-mode reading products - the ivory ground is structural to this system.

## Quick art-direction token sketch

- `--bg: #F2EBDA` (ivory; near-black ink on it: 14.1:1) with `--card: #FBF7EC` raised panels.
- `--ink: #211D16` warm near-black for text and frames; `--muted: #6E6353` for secondary text (5.0:1 on ivory).
- `--gold-line: #D4AF37` metallic gold for rules, ornament, and text only on dark grounds (8.0:1 on ink, 6.8:1 on midnight); `--gold-text: #7E5E10` deep gold reserved for small text on ivory (5.1:1).
- Jewel panels: `--emerald: #1D5C4D` (ivory text 7.3:1), `--midnight: #1F2A44` (ivory 13.3:1, gold 6.8:1), `--oxblood: #6B2230` (ivory 10.3:1); `--champagne: #E2D3A8` bands (ink 11.3:1).
- Spacing: 8 / 16 / 24 / 40 / 64 / 96 with symmetric page gutters (equal left/right, always).
- Type: marquee display (Limelight/Broadway class) `clamp(2.25rem, 5vw, 4rem)`; geometric sans body `1rem/1.7`; tracked uppercase labels `0.18em`.
- Radius: 0. Frames: 1px ink double-rule system (`border` + `box-shadow: 0 0 0 1px` with 3px gap) and stepped corners via clip-path.
- Shadows: none on the page - elevation is drawn with gold lines and stepped frames, not blur. Modals: `0 24px 48px rgba(33, 29, 22, 0.25)` maximum.
- Motion: `180ms ease-out`, even and mechanical; no springs, no bounce.

## Component guidance summary

| Component | Deco treatment |
|---|---|
| Buttons | Rectangles, midnight or emerald fill, ivory or gold text, gold hairline inset; hover steps the border, never rounds it |
| Cards | Ivory panels with double hairline frame and stepped corner; one jewel header band |
| Forms | Card-ground inputs with 1px ink underline, gold focus line, tracked uppercase labels |
| Nav | Centered masthead: wordmark, sunburst divider, tracked links; 1px + 3px + 1px rule beneath |
| Ornament | Sunburst fans, chevron bands, stepped corners - all `aria-hidden`, all constructed from the two geometry tokens |
| Badges | Champagne ovals with ink text and 1px ink frame; rotated at most 2deg |

## Canonical CSS recipe

```css
:root {
  --bg: #F2EBDA;         /* ivory, ink 14.1:1 */
  --card: #FBF7EC;
  --ink: #211D16;
  --muted: #6E6353;      /* 5.0:1 on bg */
  --gold-line: #D4AF37;  /* on ink 8.0:1, on midnight 6.8:1 */
  --gold-text: #7E5E10;  /* on ivory 5.1:1 */
  --emerald: #1D5C4D;    /* ivory text 7.3:1 */
  --midnight: #1F2A44;   /* ivory 13.3:1 */
  --oxblood: #6B2230;    /* ivory 10.3:1 */
  --champagne: #E2D3A8;  /* ink 11.3:1 */
  --step: 180ms ease-out;
}
.btn-deco {
  font: 600 0.875rem/1 "Josefin Sans", "Futura", system-ui, sans-serif;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--card);
  background: var(--midnight);
  border: 1px solid var(--gold-line);
  box-shadow: inset 0 0 0 3px var(--midnight), inset 0 0 0 4px var(--gold-line);
  border-radius: 0;
  padding: 1rem 2rem;
  min-height: 44px;
  transition: background var(--step);
}
.btn-deco:hover { background: var(--emerald); }
.btn-deco:active { background: var(--oxblood); }
.btn-deco:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }
.card-deco {
  position: relative;
  max-width: 36rem;
  margin: 3rem auto;
  padding: 24px;
  background: var(--card);
  border: 1px solid var(--ink);
  box-shadow: 0 0 0 4px var(--card), 0 0 0 5px var(--ink);
  border-radius: 0;
}
.card-deco::before {                    /* stepped ziggurat corner */
  content: "";
  position: absolute; top: 0; right: 0;
  width: 40px; height: 40px;
  background:
    linear-gradient(var(--gold-line), var(--gold-line)) 0 0 / 40px 8px no-repeat,
    linear-gradient(var(--gold-line), var(--gold-line)) 0 0 / 24px 16px no-repeat,
    linear-gradient(var(--gold-line), var(--gold-line)) 0 0 / 8px 40px no-repeat;
}
.sunburst {                              /* half-fan divider, decorative */
  width: 96px; height: 48px;
  margin: 0 auto;
  background: repeating-conic-gradient(from 270deg at 50% 100%,
    var(--gold-line) 0deg 2deg, transparent 2deg 10deg);
  border-bottom: 1px solid var(--ink);
}
```

## Accessibility notes (mandatory)

- **The gold trap:** metallic gold `#D4AF37` text on ivory is about 3.0:1 and fails. Gold as text lives only on ink or midnight grounds (8.0:1, 6.8:1); on ivory, gold text deepens to `#7E5E10` (5.1:1) and gold as `--gold-line` is decorative only.
- **Contrast:** body text `#211D16` on ivory is 14.1:1; muted `#6E6353` (5.0:1) is the lightest permitted text. Jewel panels carry ivory text only (all pass AA, see the table in [references/quality-checklist.md](references/quality-checklist.md)).
- **Focus:** `outline: 2px solid var(--ink); outline-offset: 3px` on ivory grounds; on midnight or emerald panels the outline flips to `#FBF7EC` (WCAG 2.4.11). The inset gold hairline is decoration, never the focus indicator.
- **Ornament discipline:** fans, chevrons, and stepped corners are `aria-hidden="true"`; no text over a fan or chevron band - text sits on flat ivory, card, or jewel ground.
- **Motion:** 180ms mechanical transitions only; `prefers-reduced-motion: reduce` collapses them to instant states.
- **Targets:** 44px minimum; squared buttons get generous padding so the geometry never shrinks the hit area.

## Top-5 failure modes

1. **Gold text on ivory** - metallic gold at 3.0:1 everywhere. Fix: gold text on dark grounds only; on ivory use `--gold-text #7E5E10`; the audit table is in [references/quality-checklist.md](references/quality-checklist.md).
2. **Bling gradient creep** - gold gradients, shiny 3D text, glow. Fix: gold is a 1-2px line or flat small fill; if it shines, it is wrong; rules in [references/style-guide.md](references/style-guide.md).
3. **Ornament inflation** - sunbursts behind headings, chevrons on every card. Fix: one fan per view, ornament only in dedicated bands and corners, always `aria-hidden`; composition rules in [references/style-guide.md](references/style-guide.md).
4. **Radius creep** - rounded buttons and pill chips. Fix: radius 0 everywhere; a deco curve is a constructed arc (fan, arch), not a CSS `border-radius`.
5. **Script-font substitution** - cursive script standing in for deco display. Fix: geometric marquee faces only (Broadway/Limelight class), geometric sans for everything else; pairing in [references/implementation-examples.md](references/implementation-examples.md).

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
