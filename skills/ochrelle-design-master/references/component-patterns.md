# Component Patterns

How core components are approached in **any** style. The visual family supplies the skin;
this file supplies the contract. Every interactive component gets the full state matrix;
every state must be visually distinct *and* programmatically expressed where applicable.

## Universal state matrix

| State | Visual requirement | Semantic requirement |
|---|---|---|
| Default | Resting appearance per style | Correct element/role, label |
| Hover | Clear but non-shifting change (color/border/shadow; no layout movement) | Optional tooltip/`title` only as supplement |
| Active (pressed) | Stronger change: press depth, darker fill, or offset shadow collapse | - |
| Focus | Visible focus ring, never `outline: none` without replacement | `:focus-visible` for pointer/mouse, `:focus` for keyboard paths |
| Disabled | Visually muted but ≥ practical readability; cursor change; no hover/active responses | `disabled` attribute or `aria-disabled` when it must stay focusable (see tooltips) |
| Loading | Replace label text with spinner + "Saving…"-style text or `aria-busy="true"`; keep width stable | `aria-live="polite"` region announces completion |
| Error | Message in text + icon + color; input border and message both change | `aria-invalid="true"`, message linked via `aria-describedby` |

## Buttons

- One primary style per view; secondary/tertiary (outline, ghost) clearly ranked.
- Preserve button width during loading (swap label with `aria-busy`, or min-width).
- Destructive actions: text label always ("Delete"), danger color as support.
- Icon-only buttons require `aria-label` and, ideally, visible text - icon-only is a
  last resort.
- Style notes: neumorphic buttons must keep a distinct pressed state; brutalist buttons
  keep their offset shadow collapsing on press (that *is* the affordance).

## Inputs and forms

- Label above the field (placeholder is not a label; if placeholders exist they show
  format examples, never essential info).
- Validation: on blur or submit, not on every keystroke; error text below the field,
  tied with `aria-describedby`; never color-only.
- Helper text is persistent, not hover-only.
- Required is stated in text or marked consistently with an explained symbol.
- Disabled vs read-only are distinct: disabled fields are skipped and unsubmitted,
  read-only fields remain readable and are submitted.

## Navigation

- Current location indicated with more than color: bold weight, marker, or text.
- Keyboard: logical tab order; dropdown/submenu items reachable and escapable with
  `Escape`; focus visible on every nav item.
- Persistent global navigation stays in the same position across views (repetition
  principle); mobile collapse (hamburger/drawer) must be keyboard- and screen-reader-operable,
  with focus trapped while open and returned on close.

## Cards

- A card is one unit of meaning; if it is clickable, the whole card is one target with
  one accessible name (stretch the link, don't nest interactive elements inside a link).
- Internal hierarchy: title → supporting text → meta; never more than one primary action.
- Bento variant: same grid gap token everywhere; cells that matter more earn larger
  spans, not louder colors.

## Dialogs

- Native `<dialog>` or equivalent; focus moves in on open, traps inside, returns to the
  trigger on close; `Escape` closes; background content is `inert`/`aria-hidden`.
- Every dialog has an accessible name (`aria-labelledby` pointing at its title).
- Non-modal popovers follow their platform semantics (`popover` attribute or equivalent).

## Menus

- Trigger is a real button with `aria-haspopup`/`aria-expanded`; items are menuitems in a
  container with the menu role, arrow-key navigable, `Escape` closes and restores focus.
- Never nest anything interactive inside menu items beyond the single action.
- Position must not cover the trigger; on small screens, convert to bottom sheets rather
  than tiny floating lists.

## Tooltips

- Supplement, never the only carrier of essential information (keyboard users on
  `:hover`-only tooltips lose it). Show on focus as well as hover; dismissible with
  `Escape`; not focusable themselves.
- Keep delays short and consistent; hide on scroll.

## Tables

- Real `<table>` with `<th>` + `scope` headers; caption or `aria-label` describing purpose.
- Sortable headers are buttons with `aria-sort`; row actions keyboard-reachable; sticky
  header for long tables.
- Dense data tables are the canonical "restrained surface": even in maximalist or clay
  directions, tables use flat or minimal treatment - legibility outranks expression.

## Loading, empty, and error states

Design all three for every major view; they are where generic products fall apart and
where expressive styles may spend personality budget.

- **Loading**: skeletons matching final layout (no spin-only global blocking); keep it
  under ~300ms of delay before showing to avoid flashes.
- **Empty**: state explains *why* it's empty and offers the *next action* ("No projects
  yet - create your first"); this is a legitimate expressiveness zone.
- **Error**: plain-language cause + concrete recovery action; never dead ends; retry
  affordance where retry makes sense.

## Restrained surfaces rule

Even in expressive styles, these stay visually calm: data tables, long forms, settings
panels, code/display areas, and anything users stare at for minutes. Expressiveness is
budgeted for: hero/landing moments, empty states, illustrations, onboarding, marketing
surfaces. If a working surface needs decoration to feel finished, the underlying
hierarchy or spacing is wrong - fix that instead.
