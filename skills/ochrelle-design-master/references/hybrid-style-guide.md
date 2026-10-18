# Hybrid Style Guide

How to combine the ten Ochrelle approaches into one coherent design instead of a
competing-styles collage.

## Roles: primary and secondary

- **Primary direction** (exactly one): owns the visual language - palette, surfaces,
  radii, shadows, typography, motion feel. Every surface inherits it by default.
- **Secondary techniques** (at most two): borrowed patterns that *strengthen* the primary.
  They appear where they add function (organizing content, teaching interaction, adding
  depth) and are re-skinned in the primary's language.
- Test for a legitimate secondary: "If I removed it, would the design lose function or
  clarity?" If the answer is "no, only decoration", it does not ship.

## Material budget

**At most 2 expressive materials per surface** (a "surface" = a coherent screen region:
a page, a panel, a sheet). Count as expressive materials: glass blur, neumorphic
embossing, clay inflation + double shadow, heavy skeuomorphic texture, brutalist hard
offset shadow system, dense maximalist patterning. Neutral things - flat fills, standard
borders, plain elevation shadows - are free.

Examples of legal budget use:

- Landing page: glass header (1) + flat content (0) = fine.
- Dashboard: bento layout (not a material) + flat cards (0) = fine.
- Media player: glass panel (1) + skeuomorphic knob (1) = at budget; nothing else.
- Settings page: flat (0), always.

When over budget: demote or cut. Usually the older, less load-bearing material goes.

## Hierarchy rules for hybrids

1. The primary direction defines the **hierarchy mechanism** (minimalism: scale and
   whitespace; maximalism: color and placement; brutalism: weight and position).
   Secondary techniques must use that same mechanism, not introduce a rival one.
2. One material owns each **layer**: e.g. glass for floating chrome, flat for content,
   never glass over clay on the same z-position.
3. Interaction language stays unified: one focus-ring style, one pressed-state logic,
   one motion feel (durations/easings from the shared motion tokens) - regardless of
   which material an element wears.
4. Contrast treatment is global: every text/background pair is evaluated against AA no
   matter which material it sits on.

## What never combines

- **Neumorphism + glassmorphism** - two incompatible light models (single-source soft
  light vs transmitted/blurred light) on the same surfaces reads as a rendering bug.
- **Brutalism + claymorphism** - opposed value systems: raw/honest vs soft/tactile.
- **Skeuomorphism + brutalism** - opposed philosophies of finish: crafted surfaces vs
  exposed rawness.
- **Maximalism + minimalism as co-equal directions** - pick one as primary; the other
  can exist only as a scoped zone (e.g. a loud hero in an otherwise quiet product).
- **Liquid Glass (web approximation) + generic glassmorphism** - pick one material
  story; two glass systems with different behaviors is incoherent.
- Any combination that pushes a surface past the material budget.

## Worked combination examples

### 1. Minimalist Bento analytics dashboard

Primary: `ochrelle-minimalism` (visual). Secondary: `ochrelle-bento-grid` (layout).
Rationale: daily-use data product; content-first; bento organizes heterogeneous KPI
modules without adding visual noise.

```css
:root {
  --color-bg: #fafafa; --color-surface: #ffffff;
  --color-on-surface: #18181b; --color-on-surface-muted: #71717a;
  --color-action: #4f46e5; --color-on-action: #ffffff;
  --color-border-subtle: #e4e4e7;
  --bento-gap: 1rem; --bento-cell-min: 240px; --radius-card: 0.75rem;
  --shadow-1: 0 1px 2px rgba(9, 9, 11, 0.06);
  --motion-duration-base: 200ms;
}
/* Neutral card: flat, bordered, no expressive material - budget spent on layout. */
.bento-card { background: var(--color-surface); border: 1px solid var(--color-border-subtle);
  border-radius: var(--radius-card); box-shadow: var(--shadow-1); padding: 1.25rem; }
/* One hero KPI earns hierarchy via span + type scale, not decoration. */
.bento-card--hero { grid-column: span 2; font-size: 2rem; }
```

### 2. Glass materials over a conventional readable UI (music/podcast player)

Primary: conventional readable UI (neutral tokens). Secondary: glassmorphism on *floating
chrome only*. Rationale: content (album art, waveform) is rich and variable behind
chrome; solid chrome would cover it, glass adapts; readability is preserved by keeping
body surfaces opaque.

```css
:root {
  --color-bg: #0a0a0f; --color-on-bg: #f4f4f5;
  --color-surface: #17171d; --color-on-surface: #f4f4f5;
  /* Material 1 of 1: glass, floating chrome only */
  --color-surface-glass: rgba(23, 23, 29, 0.55);
  --color-border-glass: rgba(255, 255, 255, 0.12);
  --blur-glass: 16px;
  --color-focus-ring: #a5b4fc;
}
.chrome-bar { background: var(--color-surface-glass);
  backdrop-filter: blur(var(--blur-glass)); -webkit-backdrop-filter: blur(var(--blur-glass));
  border: 1px solid var(--color-border-glass); }
.content-body { background: var(--color-surface); } /* opaque: text safety */
@supports not (backdrop-filter: blur(1px)) {
  .chrome-bar { background: var(--color-surface); } /* solid fallback */
}
```

### 3. Skeuomorphic hero control inside a conventional tool (dj/recorder app)

Primary: conventional neutral UI. Secondary: skeuomorphism on *one* teaching control -
the crossfader - where physical familiarity aids comprehension. Rationale: the metaphor
carries meaning exactly once; everything else stays fast and calm.

```css
:root {
  --color-bg: #f4f4f5; --color-surface: #ffffff; --color-on-surface: #18181b;
  --color-action: #18181b; --color-on-action: #fafafa;
  --radius-md: 0.5rem;
  /* Material 1 of 1: skeuomorphic fader track + cap */
  --skeu-track: linear-gradient(#d4d4d8, #f4f4f5 45%, #a1a1aa);
  --skeu-cap: linear-gradient(#fafafa, #d4d4d8);
  --skeu-cap-shadow: 0 2px 4px rgba(9,9,11,.35), inset 0 1px 0 #fff;
}
.fader-track { background: var(--skeu-track); border-radius: 9999px; height: 12px; }
.fader-cap  { background: var(--skeu-cap); border-radius: 6px; box-shadow: var(--skeu-cap-shadow); }
/* Keyboard equivalence is mandatory for the physical metaphor: */
.fader:focus-visible { outline: 3px solid var(--color-action); outline-offset: 4px; }
```

## Review checklist for hybrids

- Exactly one primary direction stated, secondaries justified by function.
- Material budget respected per surface; count them explicitly.
- One hierarchy mechanism, one interaction language, one motion feel across materials.
- No pairing from the "never combines" list.
- Every material has a fallback (no-blur, no-texture, reduced-motion) that preserves AA.
