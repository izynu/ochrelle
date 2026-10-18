---
name: ochrelle-claymorphism
description: Applies claymorphism design - chunky pastel 3D elements with large radii, double shadows (colored outer drop plus inset light/dark pair), and springy squash-and-stretch motion - for playful, friendly products like children's education apps, onboarding flows, casual games, and creative tools. Use when the user mentions claymorphism, clay or candy UI, puffy 3D elements, bubbly pastel design, or toy-like interfaces.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: material-styles
---

# Claymorphism

## Definition

Claymorphism renders UI elements as **soft, puffy clay objects**: chunky rounded shapes (16–28px radii), a pastel palette, and a signature **double shadow** - a soft colored drop shadow beneath the element plus an inset pair (light from one corner, dark from the other) that makes the surface look inflated, like something molded from modeling clay. Motion is springy: elements squash on press and pop back with overshoot.

## Design Philosophy

- **Everything is inflated, nothing is flat.** Even the humblest chip looks air-filled: a colored drop shadow lifts it, inset shadows puff it.
- **Color is joyful but disciplined.** Pastels dominate; one saturated accent drives actions. The outer shadow is tinted with the element's own hue - this "colored shadow" is what makes clay feel dimensional rather than merely rounded.
- **Personality through physics.** Squash on press, spring on release. The interface behaves like a satisfying toy; feedback is physical and cheerful.
- **Friendly by default, serious by choice.** Clay can stay calm (neutral pastels, subtle motion) when a dense area demands it - the style scales its energy.

## How It Differs From Similar Styles

| Style | Core idea | Contrast with claymorphism |
|---|---|---|
| **Neumorphism** | Monochrome embossing on one flat surface; dual soft gray shadows | Neumorphism is tone-on-tone with almost no color and no bounce; claymorphism is color-led with saturated pastels, tinted outer shadows, and springy overshoot. Clay keeps visible boundaries (colored drop shadows), which is exactly the contrast neumorphism lacks. |
| **Skeuomorphism** | Realistic materials (metal, leather, wood) | Clay is stylized and toy-like - it imitates no real material, it imitates a *category of feel* (soft vinyl, modeling clay). No texture, no engraved labels. |
| **Flat with rounded corners** | Solid fills, no inflation | Without the inset light/dark pair and tinted drop shadow, a rounded button is just flat; the double shadow signature is the style's proof. |
| **Glassmorphism** | Translucent frost over content | Clay is fully opaque and content-positive; it never blurs or reveals what's behind. |

## Historical Context (brief, factual)

Claymorphism emerged around 2021 in the design community, riding the popularity of soft 3D "clay render" illustration styles, and spread through product UI for children's and lifestyle apps. It remains a deliberate brand choice rather than a platform default.

## When To Use

- **Children's education apps**: big targets, forgiving shapes, cheerful feedback.
- **Onboarding and empty states**: a friendly first-run experience where personality reduces anxiety.
- **Casual games and playful consumer apps**: pet care, mood journals, habit trackers, cooking timers.
- **Creative tools with a light heart**: sticker makers, kids' drawing apps, community platforms for teens.
- **Brand moments inside calmer products**: a clay onboarding card system inside an otherwise standard app.

## When NOT To Use

- **Formal corporate, legal, medical, and finance surfaces**: trust signals come from restraint; clay reads as unserious there.
- **Data-critical dashboards**: charts and tables need quiet containers; use flat or modern minimal systems for the data layer.
- **High-density productivity**: dense lists and toolbars lose an hour of screen real estate to inflation.
- **Accessibility-first text-heavy flows**: large decorative shadows and heavy type reduce text real estate; keep reading surfaces calm.
- **Dark-mode-first products**: the pastel system is light-biased; a dark clay variant needs careful re-tuning and is rarely worth it.

## Quick Art-Direction Summary

- Canvas: light pastel tint, never pure white (e.g. `#F4F1FA` lavender-tinged, `#FDF2EC` peach-tinged).
- Palette: pastels - baby blue `#A8D8EA`, mint `#B8E6C9`, peach `#FFD3B6`, lilac `#E6DFFA`; accent violet `#7C3AED` or coral `#FF6B6B`.
- Radii: 16–28px standard; 32px+ for hero cards; full pills for buttons and chips.
- Double shadow signature: outer `0 8px 24px rgba(primary, 0.35)` + inset `inset -4px -4px 8px rgba(0,0,0,0.08), inset 4px 4px 8px rgba(255,255,255,0.6)`.
- Borders: optional 0 or 3px solid in a deepened element hue (3px for kid-facing targets, 0 for editorial calm).
- Type: rounded friendly sans (e.g. Baloo-style, Nunito, Quicksand class); dark plum/charcoal ink `#332F3A`.
- Motion: springy cubic-bezier(0.34, 1.56, 0.64, 1) for hover/pop; squash to scale(0.92–0.96) on press.
- Depth: flat → lifted → popped, three levels; shadow color = element hue at 25–40% alpha.

## Component-Level Guidance Summary

- **Shine here**: primary CTAs, onboarding cards, badges and achievement chips, avatars, toggle switches, quiz/choice buttons, progress pills, mascots and icon tiles.
- **Stay restrained**: form fields (pastel-washed solid fills, minimal inflation), list rows (flat pastel rows with soft separators), data displays (plain cards, no bounce).
- **Never**: inflate dense tables or long-form text containers; put two saturated accents in one component; animate entrance springs on containers holding text users are reading.

## Canonical CSS Recipe

```css
/* The clay signature: tinted drop + inset puff pair */
.clay {
  background: linear-gradient(180deg, #b79bff, #9a6bff);
  color: #ffffff;
  border-radius: 20px;
  border: 0;
  padding: 14px 26px;
  box-shadow:
    0 8px 24px rgba(124, 92, 255, 0.35),                  /* outer soft drop, tinted */
    inset -4px -4px 8px rgba(0, 0, 0, 0.08),              /* bottom-right dip */
    inset 4px 4px 8px rgba(255, 255, 255, 0.6);           /* top-left puff */
  transition: transform 240ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
.clay:active {
  transform: scale(0.94);               /* squash */
  transition-duration: 100ms;
}
```

## Reference Files

- [references/style-guide.md](references/style-guide.md) - full art direction: pastel systems, double-shadow recipes, states, motion, responsive rules.
- [references/implementation-examples.md](references/implementation-examples.md) - runnable component set (button, card, input, toggle, badge) plus advanced recipes and failure-mode fixes.
- [references/quality-checklist.md](references/quality-checklist.md) - verifiable pre-delivery checklist.

## Accessibility Notes (claymorphism-specific)

- **Pastel-on-pastel fails contrast by default - test everything.** Ink is dark plum `#332F3A` on light pastels; white text only on saturated accent fills; verify 4.5:1 body / 3:1 large against the actual gradient ends, not the mid-tone.
- **State must be dual-coded.** Clay motion is charming but not semantic: pair pressed/selected states with color/fill/icon changes (checkmark appears, fill deepens) so state survives without perceiving the squash.
- **Never remove focus outlines for cuteness.** Use a thick (3px) high-contrast ring - dark ink ring on pastels, white ring on saturated fills - with 2px offset; clay's soft shadows will otherwise swallow thin rings.
- **Respect `prefers-reduced-motion`**: remove spring/overshoot and squash transforms entirely; keep color/shadow state changes. Springs and bounces are the style's signature but must degrade to instant state flips.
- **Motion restraint where it matters**: no entrance springs on containers with body text; limit springy motion to controls and small decorative elements to avoid vestibular triggers and reading disruption.
- **Touch targets**: chunky shapes invite small pads - enforce ≥44×44px (≥48px in kids' products) with ≥12px gaps; the 3px borders and big radii must not visually merge adjacent targets.
- **Error states stay calm**: a saturated red on pastels screams; use a deepened berry `#C6426B` rim + icon + text so errors are legible without clashing with the palette.

## Failure Modes Summary (top 5)

1. **Shadow soup** - every element gets large tinted drops in different hues; the page vibrates and nothing has hierarchy. Fix: one shadow scale, shadows tinted by each element's own hue, drops only on the lifted tier.
2. **Pastel-on-pastel contrast failure** - light text on light clay; fix with the dark-ink floor and contrast checks against gradient ends.
3. **Spring everything** - overshoot on lists, inputs, and modals makes the product feel broken and triggers vestibular issues; springs belong to controls only, with reduced-motion opt-out.
4. **Inflated data** - clay treatment on tables/dense lists destroys scanability; keep data areas calm and reserve clay for chrome and moments.
5. **Radius chaos** - 12px chips next to 40px cards with no system; fix with a 3-step radius scale (16/24/32) applied consistently.

For the full verifiable list, see [references/quality-checklist.md](references/quality-checklist.md).
