# Accessibility and Quality

Two responsibilities live here: the **accessibility gate** (WCAG 2.2 Level AA is the
Ochrelle default target) and the **anti-generic-design review rubric**. Both are mandatory
in the master workflow (Steps 5 and 6).

## Accessibility gate

Normative authority: the W3C Web Content Accessibility Guidelines (WCAG) 2.2. This file is
a working checklist, not a substitute for the specification.

### Structure and semantics

- Use semantic HTML: one `h1` per view, logical heading order, `nav`/`main`/`footer`
  landmarks, real `<button>`/`<a>` elements for their real purposes.
- Native elements first. A native `<button>` carries keyboard support, focus, and role for
  free; a `div` with a click handler carries none of them.
- Form controls have programmatically associated labels (`<label for>` or wrapping).
- ARIA restraint principle: add ARIA only when HTML cannot express the semantics, and
  never use ARIA to "fix" a wrong element - replace the element instead. The first rule
  of ARIA is not to use ARIA if a native equivalent exists.

### Keyboard and focus

- All functionality operable by keyboard alone, in a sensible tab order.
- Visible focus indicators on every focusable element: not removed, and not relying on a
  subtle color shift alone. Minimum viable indicator: 2px outline offset from the control,
  ≥ 3:1 contrast against adjacent colors.
- No keyboard traps; dialogs return focus to the trigger on close and trap focus while open.
- Skip-to-content link for repeated navigation.

### Contrast and color

- Text contrast ≥ **4.5:1** against its background; large text (≥ 24px regular, or ≥ 18.66px
  bold) ≥ **3:1**. Measure the real rendered pairs, including placeholder and disabled text
  (note: WCAG exempts disabled controls from minimums, but users still read them - keep
  them as readable as practical).
- Non-text UI indicators (borders, icons, focus rings, chart elements) ≥ 3:1 against
  adjacent colors.
- **No meaning by color alone**: pair color with text, icon, or pattern (error states get
  an icon + message, not just red).
- Style-specific trap: neumorphism's fg≈bg palette and glassmorphism's variable backdrop
  must be solved with on-color token pairs and solid fallbacks, not good intentions.

### States and targets

- Every interactive element implements the full state matrix
  (`references/component-patterns.md`): default / hover / active / focus / disabled, plus
  loading / error where applicable - each visually distinct and announced where relevant.
- Target size: WCAG 2.2 sets a **24×24 CSS px minimum** (with defined exceptions); Ochrelle
  recommends **44px** for primary touch targets.
- Alternatives to dragging: any dragging action (sliders, reordering, drawing paths) has a
  click/tap or keyboard equivalent (WCAG 2.2 target: dragging movements).

### Motion, display modes, and zoom

- `prefers-reduced-motion: reduce`: disable non-essential motion (parallax, autoplay
  transforms, decorative animation); keep essential transitions short and opacity-based.
- `forced-colors: active`: verify the UI remains usable with the system palette (borders
  and focus indicators survive; images and icons that carry meaning get
  `forced-color-adjust` care - use sparingly and deliberately).
- Zoom/reflow: content usable at 400% zoom / 320 CSS px width without two-dimensional
  scrolling or loss of function.

### Typography and content

- Body text ≥ 16px with line-height ≥ 1.5; paragraph width ~45–75 characters; line
  length and spacing not set via unreadably small or tightly cramped styles.
- Text as text (selectable, scalable), not text-in-images; images that carry information
  have meaningful `alt` text, decorative ones get empty `alt`.
- Page titles and form errors are explicit, in text, near the thing they describe.

### Verification honesty

Automated tools (linters, contrast checkers, axe-class scanners) catch only part of
accessibility issues - typically missing names, obvious contrast failures, and structural
errors. They do **not** reliably catch: poor focus order, confusing labels, keyboard traps
in composite widgets, motion discomfort, or cognitive overload. Therefore:

1. Run automated checks on every change.
2. Manually walk the primary flows with keyboard only.
3. Spot-check a screen reader on anything beyond links, buttons, and simple forms.
4. Report what was actually verified, and how.

---

## Anti-generic-design review rubric

Rate each dimension 1–5 against the documented anchors. The rubric exists to catch the
"generic AI look": default blue/purple gradients, uniform card rows, same-everywhere
rounded corners, emoji-as-illustration, interchangeable SaaS template layouts, and
decorative effects applied without intent.

**Scale anchors:**

- **5** - Exemplary; could be published as reference for this dimension.
- **4** - Strong; minor polish items only.
- **3** - Competent; correct but not memorable; the "safe default" zone.
- **2** - Weak; noticeable problems; must be fixed or explicitly accepted with reason.
- **1** - Failure; actively harms the product.

| # | Dimension | Question | What 5 looks like | What 1 looks like |
|---|---|---|---|---|
| 1 | Art direction | Is there a stated direction, and does the work follow it? | One-sentence direction governs every visible choice | No direction; framework defaults everywhere |
| 2 | Distinctiveness | Would a knowledgeable viewer recognize this as *this* product? | Memorable, owned identity without gimmicks | Interchangeable template indistinguishable from a thousand others |
| 3 | Hierarchy | Is importance unambiguous on every view? | Three clear ranks; eye lands where intended first | Flat sameness or noise; no entry point |
| 4 | Typography | Are type choices deliberate, readable, and consistent? | Distinct pairing or scale; real content rhythm | Single default font, no scale, cramped or huge walls of text |
| 5 | Composition | Grid, alignment, and spacing doing real work? | Strict system; whitespace shapes attention | Arbitrary offsets, crowded edges, misaligned groups |
| 6 | Style fidelity | If a named style is claimed, is it executed correctly? | Characteristic features present, tokens consistent with the style family | Named style applied as surface ornament (e.g. "glassmorphism" = one blur, nothing else) |
| 7 | Restraint | Is expressiveness budgeted where it pays? | Expression at hero/empty/illustration moments; calm working surfaces | Effects on every element; chrome competes with content |
| 8 | Functionality | Do components fully work: states, errors, edge cases? | Complete state matrices; empty/loading/error designed | Buttons with no disabled state; no thought for failure |
| 9 | Accessibility | Does it pass the gate above? | AA verified with method documented; inclusive defaults | Contrast failures, keyboard-inaccessible controls, motion ignored |
| 10 | Responsiveness | Does it hold from 320px to wide desktop? | Deliberate layout per breakpoint; collapse order planned | Desktop shrunk; broken mobile; overflow bugs |
| 11 | Maintainability | Can a team extend this without rework? | Tokens documented; components variant-driven | Hard-coded values; one-off hacks per screen |

**Verdict rules:**

- Every dimension is rated honestly; **3 is the median**, not a participation grade.
- Any dimension at **2 or below** requires a fix or a written, explicit acceptance with
  justification (e.g. "maintainability 2 accepted: one-off campaign page, lifetime < 1 month").
- **Capping rule: a critical accessibility or usability failure (dimension 9 rated 1, or
  any AA-blocking defect) caps the overall verdict at FAIL regardless of all other scores.**
- Overall verdict:
  - **PASS** - all dimensions ≥ 4, none capped.
  - **PASS WITH NOTES** - all dimensions ≥ 3, or ≥ 2 with documented acceptances.
  - **FAIL** - any dimension at 1, any critical accessibility/usability failure, or
    undocumented 2s.
- Process: rate → fix highest-impact failures → re-rate once → report scores and verdict
  in the Step 7 report.
