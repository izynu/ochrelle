---
name: ochrelle-hand-drawn
description: "Art direction and implementation skill for hand-drawn sketchbook UI: wobbly hand-inked borders, doodle arrows and underlines, paper and grid-paper textures, marker highlights, comic thought bubbles, and casual humanist type paired with handwriting accents. The look of a well-kept notebook, not clip-art randomness, with one ink weight and systematic wobble. Use for education platforms, kids tools, creative apps, onboarding and how-to guides, workshop brands, and indie products selling warmth and approachability, or when a user mentions sketchy, doodle, hand-drawn, sketchbook, notebook, whiteboard, comic, cartoon, marker, scrapbook, or playful-drawn aesthetics. Includes sketch-safe palettes with verified contrast, wobbly-but-visible focus states, and reduced-motion handling."
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: material-styles
---

# Hand Drawn

Hand Drawn makes an interface feel like a page from an active sketchbook: ink lines that wobble because a hand drew them, marker highlights that smear slightly, doodle arrows that point at real things, and handwriting that annotates instead of narrates. The warmth is engineered - every imperfection is a repeatable token, so the charm survives a design system.

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

The style is "drawn by a person who cares", executed as a system: one ink color, a small set of line weights, consistent wobble, paper grounds, and handwriting used only as an accent voice.

| | Real hand-drawn system | Lazy sketch theme |
|---|---|---|
| Line weight | 2-3px family, consistent everywhere | Every element a different stroke |
| Wobble | One repeating pattern (border-radius trick or SVG) | Random per element, never repeats |
| Handwriting | Accents only: labels, notes, ≤ short strings | Body copy in script at 14px |
| States | Drawn check/cross glyphs + text | Color-only feedback |
| Read of | "A person made this carefully" | "A font pack was installed" |

What it is NOT: not Comic Sans on everything, not crayon textures over unreadable text, and not permission to skip standard structure. The page still has landmarks, labels, real focus states, and AA contrast; the drawing is a material applied on top of a sound interface.

## Philosophy

1. **Imperfection is systematic.** The wobble, the ink bleed, the slight rotation are tokens, not accidents. The same border pattern appears on every card; variation comes from a fixed set, not random output.
2. **Paper first.** Ground is warm paper, often with faint grid or ruled lines. Ink sits on paper; nothing floats on flat white voids.
3. **Handwriting accents, never narrates.** Script faces carry short annotations, hints, and margin notes at generous sizes; body copy stays in a humanist sans at 16px+.
4. **Annotations are content.** A doodle arrow exists because it points at a real element; an underline emphasizes a real phrase. Decorative doodles are aria-hidden and removable without losing meaning.
5. **Warmth through generosity.** Big targets, forgiving states, playful (but instant) feedback, and encouraging copy - the ergonomics must deliver the approachability the style promises.

## Brief historical context (verifiable)

- **Comic Sans MS (1994):** Vincent Connare designed it at Microsoft for speech bubbles in Microsoft Bob; it became the most recognized (and most misused) casual face, proof that casual type needs discipline.
- **Balsamiq Mockups (2008, founded by Giacomo "Peldi" Guilizzoni):** made deliberately sketchy wireframes an industry-standard deliverable, building on paper-prototyping practice (Carolyn Snyder, "Paper Prototyping", 2003).
- **xkcd (Randall Munroe, 2005 onward):** the web's canonical stick-figure hand-drawn idiom; matplotlib even shipped a built-in `plt.xkcd()` sketch style in version 1.3 (2013).
- **Sketchnoting (Mike Rohde, "The Sketchnote Handbook", Peachpit Press, 2012):** popularized marker highlights, arrows, and hand lettering as a note-taking practice the style borrows directly from.

## When to use / when NOT

**Use for:**
- Education platforms, courseware, kids tools, and anything teaching a skill step by step.
- Creative apps, workshop and community brands, indie products selling warmth and approachability.
- Onboarding, how-to guides, and documentation walkthroughs where encouragement matters.

**Do NOT use for:**
- Banking, medical, legal, or government products: audiences read sketchiness as unfinished, not friendly.
- Dense data tools and dashboards: wobble fights alignment and scanability.
- Luxury or premium-positioned brands: the notebook idiom undercuts price justification.
- Products with strict accessibility certification needs that cannot afford the extra state-design care this style requires.

## Quick art-direction token sketch

- `--paper: #FFFCF2` warm ground; optional grid lines via repeating gradients at very low contrast (decorative only).
- `--ink: #33302A` warm soft-black for text, borders, and doodles - 12.8:1 on paper. Pure `#000` reads cold; keep the warmth.
- `--ink-soft: #5A544A` secondary text, 7.3:1 on paper.
- `--highlight: #FFE45C` marker yellow with ink text at 10.3:1; `--coral: #FF8A75` (5.7:1 with ink), `--sky: #8FC7F2` (7.3:1), `--leaf: #B9E4A8` (9.2:1) as marker fills.
- Errors as text first: `#8A2E1F` on paper, 8.2:1; success `#1F5C3D`, 7.7:1.
- Spacing: 4 / 8 / 12 / 16 / 24 / 40 / 64; cards breathe 24px; page gutter 24-40px.
- Type: humanist sans body (16-17px, weight 500), handwriting accents (Caveat, Patrick Hand, or Shantell Sans class) at 20px+ for short strings; display can be a chunky sans 700-800.
- Radius: the wobbly pill - asymmetric border-radius values (e.g. `255px 15px 225px 15px / 15px 225px 15px 255px`) on cards and buttons.
- Shadows: none or one soft offset `0 2px 0 rgba(51, 48, 42, 0.15)`; depth comes from ink outlines, not blur.
- Motion: 150-250ms ease-out; hover rotate ±1-2deg; doodle "draw-in" via dash offset only on load and only once.

## Component guidance summary

- **Buttons:** marker-outlined pills with the wobbly radius; hover lifts and rotates -1deg; active presses flat; check/cross glyphs for toggle outcomes; never color-only.
- **Cards:** paper panels with ink outline, optional washi-tape strip (rotated translucent rect, aria-hidden) on a corner; thought-bubble variant for tips.
- **Forms:** ruled-line inputs (2px ink bottom border, slight -0.5deg skew), handwriting hint text under fields; error state adds a hand-drawn circle glyph and text.
- **Nav:** folder-tab nav or a horizontal list where the current item gets a scribble underline (SVG path, aria-hidden) plus `aria-current="page"`.
- **Highlights:** `<mark>` styled as marker smear behind real text; never place highlight behind text to fix a contrast problem.

## Canonical CSS recipe

```css
:root {
  --paper: #FFFCF2;
  --ink: #33302A;      /* 12.8:1 on paper */
  --ink-soft: #5A544A; /* 7.3:1 on paper */
  --highlight: #FFE45C;/* ink on it: 10.3:1 */
  --coral: #FF8A75;    /* ink on it: 5.7:1 */
  --error: #8A2E1F;    /* 8.2:1 on paper */
  --radius-wobble: 255px 15px 225px 15px / 15px 225px 15px 255px;
  --font-body: "Comic Neue", "Trebuchet MS", "Segoe UI", sans-serif;
  --font-hand: "Caveat", "Patrick Hand", "Segoe Print", cursive;
  --dur: 200ms;
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
}
body {
  margin: 0;
  background:
    repeating-linear-gradient(0deg, transparent 0 31px, rgba(51, 48, 42, 0.06) 31px 32px),
    var(--paper);
  color: var(--ink);
  font: 500 17px/1.6 var(--font-body);
}

/* Button: marker-outlined pill */
.btn {
  font: 700 1rem var(--font-body);
  color: var(--ink);
  background: var(--highlight);
  border: 3px solid var(--ink);
  border-radius: var(--radius-wobble);
  padding: 12px 24px;
  cursor: pointer;
  transition: transform var(--dur) var(--ease-out);
}
.btn:hover { transform: rotate(-1deg) translateY(-2px); }
.btn:active { transform: translateY(1px); }
.btn:focus-visible { outline: 3px dashed var(--ink); outline-offset: 4px; }

/* Card: paper panel with ink outline */
.card {
  border: 3px solid var(--ink);
  border-radius: var(--radius-wobble);
  background: var(--paper);
  padding: 24px;
  position: relative;
}
.card-note { font: 400 1.35rem/1.3 var(--font-hand); color: var(--ink-soft); }

/* Ruled input with handwriting hint */
.field input {
  font: 500 17px var(--font-body);
  color: var(--ink);
  background: transparent;
  border: 0;
  border-bottom: 2px solid var(--ink);
  padding: 8px 4px;
  width: 100%;
}
.field input:focus-visible { outline: 3px dashed var(--ink); outline-offset: 4px; }
.field-hint { font: 400 1.25rem var(--font-hand); color: var(--ink-soft); margin-top: 4px; }
.field-error { color: var(--error); font-weight: 700; }

/* Marker highlight behind real text */
mark { background: var(--highlight); color: var(--ink); padding: 0 4px; }

@media (prefers-reduced-motion: reduce) {
  .btn, .card { transition: none; }
  .btn:hover { transform: none; }
}
```

## Accessibility notes (mandatory)

- **Contrast:** body ink `#33302A` on paper is 12.8:1; ink on every marker fill passes AA (10.3 / 7.3 / 5.7:1). Coral is a large-text-and-graphics fill only; never set light text on markers. Grid/rule lines are ≤6% alpha and purely decorative, behind an optional solid-text island if busy backgrounds appear.
- **Handwriting legibility:** script faces are for accents only, 20px+ , short strings, never body copy, never all-caps (most script faces have no true caps rhythm). Long-form reading uses the humanist sans at 16px minimum.
- **Focus:** 3px dashed ink outline with 4px offset on every focusable element - the dashed style reads as "sketchy" while exceeding the WCAG 2.4.11 contrast intent (ink vs paper is 12.8:1).
- **Motion:** hover rotations are tiny (1-2deg) and never the sole feedback; draw-in animations fire once on load and stop entirely under `prefers-reduced-motion: reduce`.
- **States are dual-coded:** correct/incorrect pairs a drawn check/cross glyph and a text word with the color; marker highlights never replace emphasis semantics (keep `<strong>`/`<em>`).
- **Doodles:** all arrows, tape strips, and scribbles are `aria-hidden="true"` with `alt=""`; the content they point to is reachable by screen readers in DOM order.

## Top-5 failure modes

1. **Script body copy** - handwriting at 15px for paragraphs fails legibility and looks amateur. Fix: sans for reading, script for accents at 20px+; enforce with a lint on `font-family` usage.
2. **Random wobble** - five different radius patterns reads as bugs. Fix: one `--radius-wobble` token (plus one small variant) used everywhere, per [references/style-guide.md](references/style-guide.md).
3. **Rainbow markers** - every section a new marker color collapses the system. Fix: 3-4 accent fills max, one per meaning; run the palette gate in [references/quality-checklist.md](references/quality-checklist.md).
4. **Color-only feedback** - red border "because it looks drawn". Fix: every state pairs glyph + text word + color; see the state matrix in [references/implementation-examples.md](references/implementation-examples.md).
5. **Doodle overload** - arrows, stars, and tape on every corner taxes scanning. Fix: one annotation voice per section; doodles must point at real content or be deleted.

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
