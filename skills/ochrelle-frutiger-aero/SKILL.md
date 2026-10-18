---
name: ochrelle-frutiger-aero
description: Applies the Frutiger Aero aesthetic, the glossy translucent consumer-tech look of roughly 2004 to 2013, to interfaces and marketing pages. Frutiger Aero fuses aqua gel buttons, glass reflections, water droplets, bubbles, fish and sky-and-grass nature imagery with clean technology, drawn from the Windows Vista/7 Aero glass era and Mac OS X Aqua, with humanist sans typography and skeuomorphic-lite shine. Use this skill when the user mentions Frutiger Aero, Aero glass, aqua UI, gel buttons, glossy web 2.0 shine, translucent gloss, nature-tech branding, or a mid-2000s revival for music players, throwback marketing sites, retro-future brand pages, kiosk screens or product microsites. It is not for dense data tools, enterprise forms or products that need a neutral, contemporary surface.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: period-aesthetics
---

# Frutiger Aero

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Frutiger Aero is the consumer-technology aesthetic of roughly 2004 to 2013: glassy translucent panels over bright sky-and-water scenes, aqua "gel" buttons with specular highlights, water droplets on leaves, bubbles and tropical fish drifting behind interfaces, glossy white plastic hardware, humanist sans-serif type, and an overarching mood that nature and technology had finally reconciled. Surfaces are glossy but interfaces are still legible and friendly; shine is a material statement, not a decorative afterthought. It is NOT glassmorphism as practiced in 2020s app UI. Modern glassmorphism is a neutral depth system (blur, tint, hairline borders) applied to any content; Frutiger Aero is a themed world: the background is always a nature scene or a bright cyan sky, shine is exaggerated and optimistic, and skeuomorphic affordances (pressable gel, droplets, embossed text) are welcome. It is also not Y2K cyber chrome: Frutiger Aero is the clean, eco-optimist successor to Y2K's metallic futurism.

| Signal | Real Frutiger Aero | Lazy imitation |
|---|---|---|
| Background | Composed scene: sky gradient, water, grass, bubbles, sometimes a fish | Flat saturated blue rectangle with no depth or subject |
| Buttons | Gel/aqua: vertical white-to-color gradient, top specular dot, 1px bright rim, visible press | Plain saturated fill with a plain border |
| Glass | Translucent white panel with real blur over the scene, bright top sheen line | 10% white fill over flat color, no blur, no sheen |
| Nature | Present as subject (leaf droplet, grass band, fish, sky) and theme (eco, clean) | Absent; "glossy" does all the work |
| Mood and type | Optimistic, humanist sans (Frutiger lineage: Segoe UI, Myriad), crisp dark ink | Generic "shiny", default font, low-contrast grey |

## Philosophy

1. **Nature and technology are co-stars.** Every screen pairs a natural subject (sky, water, grass, leaf, fish) with a technological surface (glass, gel, glossy white). Neither appears alone; the pairing is the entire message.
2. **Shine communicates material, not luxury.** The specular highlight says "this is glass", "this is gel", "this is polished plastic". If a highlight does not identify a material, delete it.
3. **Bright, airy, uncluttered.** Large fields of sky-tinted light, generous spacing, few elements per screen. Frutiger Aero is the opposite of dark mode: it is a sunny operating system.
4. **Optimism is the brief.** No grunge, no irony, no dread. Text is welcoming, imagery is utopian, motion is smooth and buoyant; even error states stay calm and aquatic.
5. **Depth and legibility are non-negotiable.** Glass blurs what is actually behind it, gel buttons visibly depress, layers stack in one elevation order, and text sits on light glass with dark ink; any surface where body text drops below 4.5:1 contrast is redesigned, not defended.

## Brief historical context (verifiable)

- The typeface **Frutiger** was designed by Swiss type designer **Adrian Frutiger** and released in **1976**, originally commissioned for wayfinding signage at **Charles de Gaulle Airport** in Paris. Its humanist clarity seeded the era's UI fonts: **Segoe UI** (Microsoft, shipped with Windows Vista in **2007**) and **Myriad** (used across Apple's product line through the 2000s).
- **Apple** shipped the **Aqua** interface with **Mac OS X 10.0 in March 2001**, introducing glossy "gel" buttons, pinstripes and water imagery that mainstreamed aquatic shine; the same year, **Microsoft's Windows XP** shipped with the **"Bliss" wallpaper**, a photograph by **Charles O'Rear** of green hills under a bright sky, arguably the most-seen nature image in computing history.
- **Windows Vista (2007)** and **Windows 7 (2009)** shipped the **Aero glass** window treatment: translucent, blurred, light-catching window frames that named the era's look.
- Glossy hardware pushed the same language offline: Apple's **iPod** line (from 2001), **Nintendo's Wii (2006)** and DS handhelds, and mid-2000s feature phones all favored white or translucent plastic with blue water-clean cues.
- The name **"Frutiger Aero"** was coined retrospectively around **2017** by the online archiving community **Y2K Aesthetic Institute**; the style never carried that name while it was current, and it surged back into fashion in the early 2020s as nostalgia design.

## When to use / when NOT

**Use for:**

- Music players and audio apps where the "living water" mood fits playback UI (transport, progress, album art glass).
- Throwback marketing pages, anniversary microsites and era-nostalgia campaigns aimed at audiences who grew up with Vista/7 and the Wii.
- Retro-future branding for consumer goods that want clean-eco optimism: sustainability landing pages, wellness tech, smart-home kiosks.
- Product configurators, kiosk screens and creative portfolios where bright, touchable, period-craft surfaces guide or delight users.

**Do NOT use for:**

- Dense data tools, trading dashboards, IDEs and admin tables; glass and gloss tax scanning speed.
- Accessibility-critical government, health or emergency interfaces; the translucent system is hard to guarantee under every background.
- Enterprise forms with high field counts; input affordance gets noisy under shine.
- Products whose brand is austere, brutalist or editorial, and long-form reading apps: light-sky palettes and shine tire the eye across hours of text.

## Quick art-direction token sketch

```css
:root {
  /* Sky-tinted light theme - the canonical Frutiger Aero surface */
  --bg: #F0FAFD;            /* sky-tinted near-white */
  --bg-scene-top: #BDE9F7;  --bg-scene-bottom: #6FC7E9;  /* scene sky band */
  --ink: #0C3B4A;           /* deep marine ink, 11.38:1 on --bg */
  --ink-soft: #33667A;      /* secondary text, 5.96:1 on --bg */
  --accent: #0A7099;        /* deep aqua, 5.22:1 on --bg, white on it 5.54:1 */
  --accent-bright: #0F9AD1; /* decorative or large text only, white 3.20:1 */
  --gel-top: #9FE8FA;       /* gel highlight, ink on it 8.85:1 */
  --gel-bottom: #0A6FA6;    /* gel base, white on it 5.47:1 */
  --glass: rgba(255, 255, 255, 0.62);
  --glass-border: rgba(255, 255, 255, 0.85);
  --grass: #7EC13F;         /* decorative band only */
}
```

- Spacing scale: 4, 8, 12, 16, 24, 32, 48, 64px; airy is correct, 16px minimum card padding, 24px for heroes.
- Type scale: 14 / 16 / 20 / 28 / 40px; humanist sans stack `Segoe UI, Frutiger, Myriad Pro, system-ui, sans-serif`; body 400-500, headings 600.
- Radius 12-18px cards and pills for gel buttons; shadows soft and low (`0 6px 16px rgba(10, 60, 80, 0.18)` plus an `inset 0 1px 0 rgba(255, 255, 255, 0.8)` sheen), never hard black.
- Motion: 180ms hover, 240ms press, ease-out; ambient float loops 8-16s and must pause under reduced motion.

## Component guidance summary

- **Buttons**: gel pills with vertical white-to-aqua gradient, 1px bright rim, top specular highlight, press = gradient compresses and button dips 1px. Primary is deep aqua gel; secondary is a translucent glass pill.
- **Cards**: glass panels (blur 10-16px) over the scene, bright 1px top rim, soft aqua drop shadow, marine ink text inside.
- **Forms**: fields are near-opaque white glass (fill 0.85+) so text contrast is deterministic; 2px aqua focus ring; labels always visible.
- **Nav**: floating glass bar, pill links, active link gets a small gel capsule; the blurred scene behind it must stay calm.
- **Progress, meters, icons**: gel channels with glossy fill (playback and capacity meters are the style's signature moment); icons rounded and glossy, 2px-max strokes, never flat line icons from dark UI kits.

## Canonical CSS recipe

```css
:root {
  --bg: #F0FAFD;
  --ink: #0C3B4A;
  --ink-soft: #33667A;
  --accent: #0A7099;
  --gel-top: #9FE8FA;
  --gel-bottom: #0A6FA6;
  --glass: rgba(255, 255, 255, 0.62);
  --glass-border: rgba(255, 255, 255, 0.85);
  --sheen: inset 0 1px 0 rgba(255, 255, 255, 0.8);
  --ease-out: cubic-bezier(0.22, 0.61, 0.36, 1);
}

.aero-gel-button {
  padding: 12px 28px;
  border: 1px solid rgba(255, 255, 255, 0.85);
  border-radius: 999px;
  background: linear-gradient(180deg, var(--gel-top) 0%, #4FBFE4 38%, var(--gel-bottom) 100%);
  box-shadow: var(--sheen), 0 3px 6px rgba(10, 90, 130, 0.35), 0 8px 18px rgba(10, 60, 80, 0.22);
  color: #ffffff;
  font: 600 16px/1 "Segoe UI", "Frutiger", "Myriad Pro", system-ui, sans-serif;
  text-shadow: 0 1px 1px rgba(6, 55, 75, 0.45);
  transition: transform 240ms var(--ease-out), box-shadow 240ms var(--ease-out);
}
.aero-gel-button:hover { transform: translateY(-1px); }
.aero-gel-button:active {
  transform: translateY(1px);
  box-shadow: inset 0 2px 6px rgba(6, 55, 75, 0.5), 0 2px 4px rgba(10, 60, 80, 0.25);
}

.aero-glass-card {
  position: relative;
  padding: 24px;
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  background: var(--glass);
  -webkit-backdrop-filter: blur(14px) saturate(150%);
  backdrop-filter: blur(14px) saturate(150%);
  box-shadow: var(--sheen), 0 6px 16px rgba(10, 60, 80, 0.18);
  color: var(--ink);
}
.aero-glass-card::after {  /* glossy top reflection band */
  content: "";
  position: absolute;
  inset: 1px 1px auto 1px;
  height: 42%;
  border-radius: 15px 15px 40% 40% / 15px 15px 18px 18px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.55), rgba(255, 255, 255, 0));
  pointer-events: none;
}
```

## Accessibility notes

- **Contrast floor**: body text 4.5:1 minimum against the busiest region that can scroll behind the glass, not the average. Ink `#0C3B4A` on the glass plate computes 11.38:1 on `--bg`; re-verify over the most saturated scene region. White on the gel base `#0A6FA6` computes 5.47:1; bright aqua `#0F9AD1` (white 3.20:1) is reserved for 24px+ bold text or non-text decoration per WCAG 2.2 AA large-text rules.
- **Non-text contrast**: button rims, focus rings and progress fills must reach 3:1 against adjacent colors (WCAG 2.2, 1.4.11). Test the rim against both the gel gradient and the scene behind it.
- **Focus-visible**: never rely on the sheen alone. Use `outline: 3px solid #0A7099; outline-offset: 2px` on all controls; the aqua holds 3:1 against the light plate and the marine ink.
- **prefers-reduced-motion**: freeze bubble drift, droplet shimmer and gel hover lifts; keep only opacity fades at 150ms. Ambient loops (bubbles, fish) must stop entirely.
- **Transparency fallbacks**: honor `prefers-reduced-transparency` and `@supports not (backdrop-filter: blur(1px))` by swapping `--glass` to a solid `rgba(255, 255, 255, 0.95)` plate with the same ink and no layout shift; never raw text-on-scene as the fallback.

## Top-5 failure modes

1. **Gloss over flat color.** A gel button or glass card on a plain saturated blue reads as clip-art. Fix: build a real scene (sky gradient, grass band, at least two natural subjects) before placing any shine.
2. **Text on translucent glass over busy scenes.** Contrast collapses the moment a fish or dark cloud scrolls behind. Fix: inputs and body-text areas use 0.85+ white fill, captions get a scrim, verify worst-case contrast per WCAG 2.2 AA.
3. **Highlight direction chaos.** Specular dots top-left on one button and bottom-right on the next destroys the "one sun" illusion. Fix: a single light source top-center, enforced in a shared gradient token.
4. **Everything shines.** Glossing every surface produces an oil-slick page. Fix: one hero material per region (gel for actions, glass for containers), flat white for supporting chrome.
5. **Dropping the nature layer.** Removing fish, droplets and grass leaves "generic glossy blue", which is a different, worse style. Fix: budget at least one natural subject and one eco cue per view, marked `aria-hidden` as decoration.

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
