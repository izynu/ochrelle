# Universal Design Principles

Style-agnostic principles that hold across all ten Ochrelle specialists. Every style-
specific decision must survive these. Each principle includes a violation → fix example.

## 1. Hierarchy

The most important element on a screen must be the first thing perceived. Build hierarchy
with at most three ranks per view (primary / secondary / tertiary) expressed through size,
weight, color, and position - not through decoration alone.

**Violation → fix**: A pricing page where the three plans are identical cards and the
recommended plan differs only by a thin border → make the recommended plan physically
dominant (larger card, filled treatment, explicit "Recommended" label in text, not only color).

## 2. Contrast

Contrast is both an accessibility requirement (ratios, see
`references/accessibility-and-quality.md`) and a compositional device: focal elements
should differ from their surroundings in at least one strong dimension - value, size,
color, or shape.

**Violation → fix**: A hero headline at the same size and weight as body copy → scale the
headline to a distinct type-scale step and add weight or value separation.

## 3. Alignment

Nothing is placed arbitrarily. Every element aligns to a shared edge, center, or grid
line. Consistent alignment is invisible when present and instantly amateur when absent.

**Violation → fix**: Card content with icon, title, and body each starting at slightly
different x-offsets → define one padding token for card interiors and align icon, title,
and body to it.

## 4. Proximity

Elements that belong together sit together. Spacing is the cheapest grouping signal and
must be systematic: related items get small gaps; groups get large gaps. If two groups
are closer to each other than items are within a group, the layout lies.

**Violation → fix**: A form where the label of field 3 is visually closer to field 2 than
to field 3 → bind each label to its field with a small fixed gap and increase inter-field
spacing to the next spacing token.

## 5. Repetition

Repetition builds identity and predictability. The same kind of thing (buttons, cards,
section headers) looks the same kind of way everywhere. Variation must be systematic -
defined as tokens or variants - not improvised per screen.

**Violation → fix**: Four screens using four different corner radii on their primary
buttons → collapse to one `--radius-md` button token and use it everywhere.

## 6. Whitespace as content

Whitespace is an active design material, not leftover space. It directs attention, groups
content, and signals confidence. Give primary content breathing room; cramped whitespace
around a focal element weakens it.

**Violation → fix**: A hero where headline, subline, CTA, and badges are stacked with
uniform 8px gaps → increase spacing between functional groups (headline block → CTA) to
a larger token and remove the badges unless they carry information.

## 7. Affordance honesty

How something looks must truthfully signal how it behaves. Things that look clickable are
clickable; things that are not clickable do not look it. Styles that flatten affordances
(everything looks like a card; nothing looks pressable) force users to discover behavior
by trial.

**Violation → fix**: A neumorphic panel that looks identical to the neumorphic button next
to it → differentiate interactive elements with a pressed/raised state system, an explicit
control shape (e.g. pill), and, where needed, an icon or label convention.

## 8. Consistency with variation

Users build a mental model from repeated patterns; deliberate variation provides emphasis
and freshness. The rule: **be consistent in structure, selective in emphasis**. Vary color,
imagery, and illustration; keep navigation, controls, spacing, and interaction behavior
stable.

**Violation → fix**: Each page of an app inventing a different header layout → define one
page-header component with optional slots and reuse it, varying only the page title and
actions.

## 9. Content-first design

Design from the content outward: put real (or rigorously realistic) content into the
layout early. Layout decisions made against placeholder content are guesses; content has
length, rhythm, and edge cases that shapes what the layout must do.

**Violation → fix**: A three-column feature grid designed against three fictional one-line
blurbs, which breaks when real copy runs four lines → design with realistic lengths up
front, define min-heights, and decide wrap/ellipses behavior per content type.

## 10. Intentional vs accidental design

Every visible decision should be attributable to a reason: brand, audience, content, or
principle. "It looked nice" or "the framework does it this way" is accidental design. A
direction is intentional when you can state what it communicates, why it fits the product,
and what you rejected.

**Violation → fix**: A dashboard using glassmorphism because the template shipped with it →
either justify the material (media-rich background, floating chrome that must adapt) or
replace it with a conventional solid surface; record the decision.

## Applying the principles

- During Step 2 (art direction), write how the chosen style will honor each principle.
- During Step 5 (anti-generic review), each principle doubles as a review lens: ask
  "where does this layout lie about grouping, hierarchy, or behavior?"
- When a style conflicts with a principle (e.g. maximalism vs restraint on working
  surfaces), scope the style away from the conflicting surface rather than abandoning
  either blindly.
