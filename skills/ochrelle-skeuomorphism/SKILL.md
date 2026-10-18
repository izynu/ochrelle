---
name: ochrelle-skeuomorphism
description: Applies skeuomorphic UI design - realistic materials, layered gradients, multi-layer shadows, inset highlights, and texture - when a task calls for tactile, physical interfaces such as music apps, audio hardware panels, games, luxury brands, or immersive storytelling. Use when the user mentions skeuomorphism, realistic UI, textured controls, physical metaphors, leather/wood/metal surfaces, or retro-apple style interfaces.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: material-styles
---

# Skeuomorphism

## Definition

Skeuomorphism is a UI style in which digital objects deliberately imitate their real-world counterparts: buttons look pressable like machined keys, sliders look like faders on a mixing console, and surfaces carry the materials - brushed metal, leather, wood grain, stitched fabric, glass - of physical objects. Depth is produced with realistic lighting: layered gradients (4–8 stops), multi-layer box-shadows, inset highlights along lit edges, and fine texture such as noise or grain.

## Design Philosophy

- **The interface is an object.** Screens are treated as physical devices: controls have weight, travel, and a light source. Affordance is literal - if it looks like a knob, you turn it.
- **Materials carry meaning.** A leather-stitched binding suggests a notebook; a brushed-metal panel suggests precision hardware; felt suggests a game table. Materials are chosen to reinforce what the control does, not for decoration alone.
- **Realism through craft, not photographs.** Surfaces are built from CSS/SVG: multi-stop gradients, layered shadows, inset edge highlights, and subtle noise. Photographic bitmaps are a last resort because they do not scale or theme.
- **One light source.** Highlights sit top/left, shadows bottom/right, consistently across every surface - the way a real desk lamp would light a device.

## How It Differs From Similar Styles

| Style | Core idea | Contrast with skeuomorphism |
|---|---|---|
| **Neumorphism** | Soft monochrome embossing on one flat color | Neumorphism abstracts the material away (one surface, dual soft shadows); skeuomorphism celebrates distinct materials with color, texture, and hard specular highlights. Neumorphism is whispering; skeuomorphism is sculpting. |
| **Flat / Minimal** | No depth cues at all | Flat removes shadows, gradients, and texture; skeuomorphism makes them the primary communication channel. |
| **Claymorphism** | Playful chunky pastel 3D | Claymorphism is stylized and toy-like; skeuomorphism aims for believable realism of specific materials. |

## Historical Context (brief, factual)

Skeuomorphic interface design was prominent in consumer software of the late 2000s and early 2010s, most visibly in early versions of iOS, where apps imitated physical objects (stitched leather calendars, felt game tables, metal voice-memo cases). The industry broadly moved toward flat design in the mid-2010s, and skeuomorphism since survives as a deliberate, targeted choice rather than a platform default.

## When To Use

- **Music and audio products**: mixers, transport controls, tuners, drum pads - physical metaphors map 1:1 to what musicians already know (piano-key keyboards, hardware-style transport bars).
- **Games and playful products**: inventory screens, slot machines, card tables, arcade cabs.
- **Premium / luxury brands**: watch faces, whiskey and coffee labels, leather-goods commerce - material realism signals craft and price.
- **Immersive storytelling and education**: dioramas, museums, cockpit dashboards, science simulations where a physical analogy teaches the interaction.
- **Hardware companion apps**: when the app mirrors a real device the user owns, matching its materials reduces learning cost.

## When NOT To Use

- **Dense data tools**: trading dashboards, analytics tables, IDEs - texture competes with data; use flat or modern dark UIs instead.
- **High-volume enterprise forms**: reading speed and scanability beat tactility.
- **Accessibility-critical contexts**: low-vision users need maximum contrast; heavy texture and mid-tone materials make guaranteed contrast difficult.
- **Performance-limited environments**: many layered gradients, large blurs, and texture tiles add paint and memory cost on cheap devices.
- **Modern SaaS defaults**: if the product has no narrative reason for physical metaphor, the style reads as costume.

## Quick Art-Direction Summary

- Base materials: warm off-whites, brushed greys, walnut browns, oxblood leather tones; accent via machined brass/copper or signal red/green LEDs.
- Gradients: 4–8 stops per surface, angled 160–200deg to sell curvature.
- Shadows: 3+ layers per elevated surface - contact shadow, ambient shadow, cast shadow.
- Highlights: 1px inset top edge `inset 0 1px 0 rgba(255,255,255,.55)`.
- Texture: SVG `feTurbulence` noise at 2–5% opacity; never above ~8%.
- Radii: 6–14px for hardware parts; pills for keys and LEDs.
- Typography: engraved/letterpress text via dual text-shadows; dark slate `#2B2B2B` on light metal.
- Press state: `scale(0.97)` with faster duration (~100–140ms) than release.
- Light source: top-left, everywhere, without exception.

## Component-Level Guidance Summary

- **Shine here**: buttons/keys, sliders and faders, knobs/dials, toggle switches, transport controls, badges, on/off LEDs, panel headers with material bands.
- **Stay restrained**: body text containers, tables, lists, forms with many fields - keep these on quiet, near-flat surfaces so content dominates; reserve realism for the controls.
- **Never**: put texture behind small body text, or stack a second material inside an already busy one.

## Canonical CSS Recipe

```css
/* Machined skeuomorphic key - the canonical element */
.skeuo-key {
  padding: 12px 22px;
  border-radius: 10px;
  border: 1px solid #6d6d70;
  background: linear-gradient(
    180deg,
    #fdfdfd 0%,
    #ececee 22%,
    #cfcfd4 55%,
    #b9b9c0 78%,
    #a3a3ac 100%
  );
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.85),   /* lit top bevel   */
    inset 0 -2px 3px rgba(0, 0, 0, 0.25),      /* dark lower lip  */
    0 1px 0 rgba(255, 255, 255, 0.4),          /* reflected light */
    0 2px 4px rgba(0, 0, 0, 0.35),             /* contact shadow  */
    0 6px 12px rgba(0, 0, 0, 0.25);            /* ambient shadow  */
  color: #2b2b2b;
  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.6);
}
.skeuo-key:active {
  transform: scale(0.97) translateY(1px);
  transition-duration: 90ms;                  /* press is faster */
  box-shadow:
    inset 0 2px 5px rgba(0, 0, 0, 0.45),
    inset 0 1px 0 rgba(255, 255, 255, 0.3),
    0 1px 2px rgba(0, 0, 0, 0.3);
}
```

## Reference Files

- [references/style-guide.md](references/style-guide.md) - full art direction: palettes, materials, lighting, motion, responsive rules.
- [references/implementation-examples.md](references/implementation-examples.md) - runnable component set (button, card, input, toggle, fader) plus advanced recipes and failure-mode fixes.
- [references/quality-checklist.md](references/quality-checklist.md) - verifiable pre-delivery checklist.

## Accessibility Notes (skeuomorphism-specific)

- **Contrast must be measured on the textured surface, not the palette.** Noise and grain darken perceived backgrounds; verify body text still reaches the project's WCAG target (typically 4.5:1) against the worst region of the texture, and keep texture opacity ≤5% behind text.
- **Never remove the focus outline to preserve realism.** Replace it: `outline: 3px solid` in an accent color with a 2px offset so it reads on metal; skeuomorphic chrome makes default focus rings easy to lose - compensate.
- **Press affordance needs a non-color cue**: scale/travel motion (0.97) so state is not communicated by shading alone (color-blindness safe).
- **Texture is decoration - mark it as such** with `aria-hidden="true"` on decorative texture/gradient layers, and never encode information in material choice alone (a "wood" tab vs "metal" tab must also differ in label).
- **Respect `prefers-reduced-motion`**: replace spring/bounce releases with instant state changes.
- **Texture `background-image` must not break text selection readability**: keep `text-shadow` subtle (≤1px offset) so glyphs stay crisp.

## Failure Modes Summary (top 5)

1. **Texture overuse** - noise above ~8% opacity or texture behind body text destroys legibility; keep grain whisper-quiet (see quality-checklist).
2. **Inconsistent light source** - highlights bottom-right on one card and top-left on the next breaks the physical illusion entirely.
3. **Gradient banding / too few stops** - 2–3 stop gradients look flat and cheap; skeuomorphic surfaces need 4–8 stops to read as curvature.
4. **Ornament without metaphor** - applying leather to a settings page reads as kitsch; every material must justify itself through function.
5. **Lost focus/disabled states** - realism chrome swallows focus rings and disabled buttons look identical to idle ones; always design explicit states.

For the full verifiable list, see [references/quality-checklist.md](references/quality-checklist.md).
