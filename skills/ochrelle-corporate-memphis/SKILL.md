---
name: ochrelle-corporate-memphis
description: Applies Corporate Memphis, the flat vector illustration style also known as Alegria that Big Tech illustration systems popularized from 2017 onward, to product and marketing surfaces. The style uses simplified human figures with disproportionate flexible limbs and tiny heads, flat saturated-but-muted color fills, geometric plant and furniture props, and a relentlessly optimistic mood. Use this skill when the user mentions Corporate Memphis, Alegria, flat illustration, big tech art style, tech company illustrations, bendy characters, or asks for onboarding illustrations, HR and internal tool visuals, empty states, community pages, benefits explainers or friendly SaaS marketing. It is not for premium brands, editorial storytelling, or products that need photorealistic or emotionally complex imagery.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: material-styles
---

# Corporate Memphis

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Corporate Memphis is a flat vector illustration style in which human figures are drawn as smooth, simplified shapes with exaggerated proportions: small heads, wide torsos, and long, rubbery, bendable limbs that bend where elbows and knees would not. Figures float or loll through geometric scenes: flat color blocks, abstract plants, pastel furniture, and objects that curve softly instead of obeying perspective. The palette is saturated but muted, the mood is uniformly upbeat, and the UI chrome around the illustrations stays plain and functional.

It is NOT generic flat design. Flat design (post-2013) is a UI style: it removes skeuomorphism from buttons and icons while keeping realistic proportions. Corporate Memphis is an illustration system: it reshapes the human body itself and ships it at scale. It is also NOT character animation for storytelling; the figures are scenery for empty states and hero panels, not protagonists with arcs.

| Signal | Real Corporate Memphis | Lazy imitation |
|---|---|---|
| Figures | 2-4 asymmetric poses, limbs bend playfully, heads tiny, skin in stylized hues (including blue/green) | One stiff symmetrical stick figure with a photoreal head |
| Palette | 4-6 muted-saturated fills, one dominant, warm paper background | Full rainbow, or two grays and a logo blue |
| Props | Geometric plants, curved furniture, floating abstract shapes | Stock photo cutouts or detailed icon clutter |
| UI pairing | Plain, high-contrast chrome; illustration lives in dedicated slots | Illustration styles bleeding into controls and text |
| Mood | Casual, communal, mildly playful | Corporate-serious or sarcastic (either breaks the system) |
| Consistency | One limb language and one fill set across every scene | Each illustration in a different style |

## Philosophy

1. **The body is elastic.** Limbs stretch, loop and drape; heads are 1:5 to 1:7 of figure height. The distortion is the charm, and it must be consistent: every figure in a product shares the same anatomy rules.
2. **Flat is a contract.** No gradients on figures, no shadows under feet unless the scene needs grounding, no outlines heavier than 2px, no texture. Depth comes from layering flat shapes, not rendering.
3. **Muted saturation, warm ground.** Fills sit at 60-80% saturation with warm background paper; the combination reads "friendly" where pure primaries read "children's product" and pastels read "baby product".
4. **Illustration has slots.** Characters appear in defined places: hero panels, empty states, onboarding steps, 404 pages. They never decorate forms, tables or navigation; those stay typographic and plain.
5. **Optimism by default, honesty by design.** The style's uniform cheer is its strength and its failure mode; use it for genuine community and productivity moments, and pair it with real, concrete copy so it does not feel like flavored air.
6. **Consistency beats brilliance.** A mediocre figure drawn in the same limb language as every other figure is on-brand; a brilliant figure in a new style is off-brand.

## Brief historical context (verifiable)

- The style is most closely identified with **Alegria**, the illustration system developed for **Facebook** around **2017** as part of its in-house brand illustration efforts; the system's simplified, elastic figures spread across Facebook's product surfaces in the following years.
- Throughout the late 2010s, major platform companies adopted similar systems: **Google**, **Airbnb**, **Slack**, **Uber** and **Mailchimp** each built large in-house illustration teams with recognizable flat-figure languages during this period.
- The nickname **"Corporate Memphis"** spread online around **2020** as a half-affectionate, half-critical label for the style's ubiquity in tech marketing; the related term **"Flat Art"** and the critique idiom "weird little guys" circulated in the same discussion.
- The style's roots are commonly traced to **Pablo Delcan**'s 2010s editorial work and to mid-century modernist illustration (flat shapes, exaggerated figures) filtered through vector tooling; designers also cite **Jean Jullien**'s playful line-and-fill figures as an influence.
- By the early 2020s the style was widely criticized for sameness and for sanitizing the companies using it; several platform brands (including Facebook/Meta's marketing and others) visibly diversified their illustration systems in response.

## When to use / when NOT

**Use for:**

- Onboarding illustrations: step-by-step flows where a friendly figure reduces first-run anxiety.
- HR tools, internal portals and benefits explainers where warmth and non-threatening tone matter more than brand edge.
- Community pages, event pages and empty states (no data yet, no messages yet) that need human presence without photography.
- SaaS marketing heroes that promise ease and collaboration over power and precision.
- Products that need illustration at scale on a budget: one system, many scenes, cheap to produce and localize.

**Do NOT use for:**

- Premium, luxury or craft brands: the elastic figures undercut price positioning instantly.
- Serious domains (health crises, legal, finance risk, security incidents) where uniform cheer reads as tone-deaf.
- Editorial storytelling or journalism: the style's abstraction hides the specific human detail stories need.
- Products competing on visual craft (design tools, creative portfolios): the style signals template, not authorship.
- Accessibility-critical instructions: simplified figures are bad at showing precise physical actions; use diagrams or video.

## Quick art-direction token sketch

```css
:root {
  --bg: #FBF5EE;          /* warm paper, 13.15:1 with --ink */
  --ink: #2E2A26;         /* near-black warm ink */
  --ink-soft: #6B6259;    /* 5.52:1 on --bg, secondary text */
  --accent: #B5431A;      /* primary action, white on it 5.55:1, 5.13:1 on --bg */
  --accent-2: #20647A;    /* secondary action/links, white 6.63:1, 6.13:1 on --bg */
  --fig-orange: #F4A259;  /* illustration fills: decorative only */
  --fig-green: #7FB069;
  --fig-plum: #B08BBB;
  --fig-blue: #6C91BF;
  --fig-skin-1: #E8B08C;  /* stylized skin hues; non-realistic tones welcome */
  --fig-skin-2: #8C6D9C;
}
```

- Spacing: 4 / 8 / 12 / 16 / 24 / 40 / 64px; illustration slots get 24px+ padding so figures never touch text.
- Type: one friendly humanist sans (`Inter, "Segoe UI", system-ui, sans-serif`); 14 / 16 / 20 / 28 / 36px; headings 600-700, body 400.
- Radius: 10-14px cards and buttons (friendly but not toy-like); 6-8px chips; no pills and no sharp corners.
- Shadows: nearly none. Flat `0 1px 2px rgba(46, 42, 38, 0.08)` at most; illustrations carry zero shadows unless grounding is required.
- Motion: 200ms hover, 220ms step transitions, ease-out; illustration motion is limited to subtle limb sway or float loops (12s+) that stop under reduced motion.

## Component guidance summary

- **Buttons**: flat accent fills (`--accent`) with white 600-weight labels, 10px radius, hover darkens 6%, press darkens 10%; no gradients, no gloss.
- **Cards**: flat white or paper-tint panels, 1px `#E9E0D4` border, generous 24px padding; the illustration sits in a dedicated top slot of fixed height.
- **Forms**: plain fields, 1px `#C9BFB2` border, 4px radius, visible labels; focus is a 2px `--accent-2` ring; illustration never inside the form flow.
- **Nav**: flat bar or plain links, ink text, active link underlined with 3px `--accent` bar; no illustration in the nav.
- **Empty states**: the signature component: one figure doing a casual activity, one headline, one concrete action button.
- **Illustration slots**: fixed aspect boxes (3:2 hero, 1:1 empty state) with `aria-hidden="true"` on the figure and a real text alternative nearby.

## Canonical CSS recipe

```css
:root {
  --bg: #FBF5EE;
  --ink: #2E2A26;
  --ink-soft: #6B6259;
  --accent: #B5431A;
  --accent-2: #20647A;
  --border: #E9E0D4;
  --ease-out: cubic-bezier(0.22, 0.61, 0.36, 1);
}

.cm-button {
  padding: 12px 24px;
  border: 0;
  border-radius: 10px;
  background: var(--accent);
  color: #ffffff;
  font: 600 16px/1.2 inherit;
  font-family: inherit;
  cursor: pointer;
  transition: background-color 200ms var(--ease-out), transform 200ms var(--ease-out);
}
.cm-button:hover  { background: #9E3814; }  /* darkens, stays 4.5:1+ with white */
.cm-button:active { background: #8C3012; transform: translateY(1px); }
.cm-button:focus-visible { outline: 3px solid var(--accent-2); outline-offset: 2px; }
.cm-button:disabled { opacity: 0.5; cursor: not-allowed; }

.cm-card {
  max-width: 480px;
  padding: 24px;
  border: 1px solid var(--border);
  border-radius: 14px;
  background: #ffffff;
  color: var(--ink);
}
.cm-card-illustration {   /* dedicated, fixed slot: the figure lives here */
  height: 160px;
  margin: 0 0 16px;
  border-radius: 10px;
  background: var(--bg);
}

.cm-empty-title { margin: 0 0 8px; font-size: 20px; font-weight: 700; }
.cm-empty-body   { margin: 0 0 16px; color: var(--ink-soft); line-height: 1.5; }
```

## Accessibility notes

- **Illustrations are decorative**: figures and scenes get `aria-hidden="true"`; any meaning they carry (success, wait, error) is duplicated in adjacent text with real contrast. Never let an illustration be the only state indicator.
- **Contrast is computed in the UI layer, not the illustration layer**: body text 4.5:1 (`#2E2A26` on `#FBF5EE` is 13.15:1; `#6B6259` is 5.52:1) and large text 3:1. Illustration fills are exempt from text contrast because no text ever sits on them; keep it that way.
- **Buttons pass with white labels on `#B5431A` (5.55:1)**; hover/active shades stay above 4.5:1 with white. Links use `--accent-2` (`#20647A`, 6.13:1 on the paper background) and are underlined, since color alone is not enough (WCAG 2.2, 1.4.1).
- **Focus-visible**: `outline: 3px solid var(--accent-2); outline-offset: 2px` on every control; the style's flatness makes default rings disappear, so the ring is part of the design, not an override.
- **Skin-tone policy**: stylized non-realistic hues (blue, green, plum) are traditional in this system; if realistic tones are used, ship a documented mix across the set so no scene implies a single demographic.
- **prefers-reduced-motion**: limb sway, float loops and step transitions collapse to opacity fades at 150ms; nothing on screen moves continuously.
- **Empty-state honesty**: the cheerful figure must not mask an error. Failed loads get an explicit message and a retry control, never just a smiling illustration.

## Top-5 failure modes

1. **Style bleed into the UI.** Elastic limbs and muted fills creep into buttons, inputs and icons, producing a toy product. Fix: the illustration system and the UI system are separate token sets; controls use `--ink`/`--accent`/`--accent-2` only.
2. **The sameness trap.** Every screen uses the same lolling figure with a laptop, and users stop seeing the illustrations at all. Fix: maintain a pose library (min. 8 distinct poses) and a rule: no pose repeats within three consecutive screens.
3. **Cheer over substance.** A grinning figure next to "Payment failed" reads as mockery. Fix: reserve the style for neutral and positive moments; error and legal surfaces drop to typographic treatment.
4. **Rainbow drift.** New scenes add new hues until the palette is 20 colors. Fix: lock the 4-6 fill tokens; new scenes must compose from existing fills, and a lint-style audit counts hues per export.
5. **Floating figures, no ground.** Characters hover with no anchoring shape, and the layout looks unfinished. Fix: either add a soft geometric ground blob (10% tint of a figure fill) or commit to the float deliberately across every scene, never both in one product.

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
