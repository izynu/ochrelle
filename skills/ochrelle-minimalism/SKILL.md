---
name: ochrelle-minimalism
description: Art direction and implementation skill for minimalism grounded in Swiss/International Typographic Style - hierarchy through typography and whitespace, grid discipline, restrained palette with one accent, and honest affordances. Use when a project calls for minimal, Swiss, clean, spacious, functional, or Scandinavian-modern design; when building SaaS dashboards, documentation sites, enterprise tools, professional portfolios, or product pages; or when a user mentions whitespace-driven layouts, type-led hierarchy, grid systems, or "less but better".
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: typographic-expressive
---

# Minimalism (Swiss-Grounded)

## Definition

Minimalism is a discipline of **deliberate reduction**: the interface keeps only elements that carry information or function, and then makes those elements work harder. Hierarchy is produced by typography (scale, weight, position) instead of decoration; space is treated as active material that groups and separates; the palette is neutral with at most one accent.

The critical distinction: **minimalism ≠ empty, and minimalism ≠ decorated-down.**

| | Real minimalism | "Decorated-down" / lazy emptiness |
|---|---|---|
| Whitespace | Rhythmical, on a spacing scale, doing grouping work | Arbitrary gaps left because nothing was designed |
| Hierarchy | Strong, achieved via type scale & weight | Weak; everything equally faint |
| Affordances | Explicit - links underlined, buttons bordered/filled, disabled states visible | Links look like plain text, buttons are "subtle" ghosts nobody clicks |
| Contrast | High (black on white heritage) | Tiny gray-on-white captions below 4.5:1 |
| Grid | Strict, alignment is sacred | Loose, "airy" used as an excuse |

Removing ornament is the easy half. The hard half - and the actual style - is making each remaining element carry enough weight (visual and functional) that the page still orients, explains, and acts. If users can't tell what is clickable, that is not minimalism; it is a failure with good PR.

## Philosophy

1. **Less, but better.** Dieter Rams' formulation is the operating principle: reduction is only justified when what remains is *better* - clearer, faster, more obvious.
2. **Typography does the work.** A minimal interface is a typographic hierarchy wearing an interface. Size jumps (e.g. 16 → 24 → 40 → 64px), weight contrast (400 vs 600/700), and flush-left ragged-right composition create order.
3. **Whitespace is structure.** Space on an 8px rhythm groups related elements closer (proximity) and separates unrelated ones farther. In minimalism, whitespace replaces the borders, boxes, and dividers other styles lean on.
4. **One voice, one accent.** Neutral ground (white/off-white/near-black), ink text, and a single accent reserved for the one action or state that matters most. The accent's scarcity is what gives it power.
5. **Honesty of affordance.** Every interactive element must look interactive to a first-time visitor, without hover. Underlines stay. Disabled states stay visible. This is a Swiss value too - objectivity before aesthetics.

## Brief historical context (verifiable)

- **Swiss Style / International Typographic Style** emerged in Switzerland in the **1950s** among designers such as Josef Müller-Brockmann, Max Bill, and Armin Hofmann. Hallmarks: mathematical grids (Müller-Brockmann's *Grid Systems in Graphic Design*, 1961), sans-serif type (Helvetica, designed 1957 in Münchenstein), flush-left ragged-right setting, objective photography, and a rejection of illustration-driven advertising.
- **Dieter Rams** led Braun's product design from the 1950s–90s under the principle "Weniger, aber besser" ("less, but better"); his ten principles of good design are widely cited as ancestry for both minimal product design and Apple's hardware/software language in the 2000s.
- The web inherited both strands: **grid systems** (12-column layouts became standard practice) and **type-led flat design** (the mid-2010s "flat" wave was partly minimalism's constraints going mainstream).

## When to use / when NOT

**Use for:**
- SaaS dashboards, admin panels, enterprise tools - density of function rewards reduction elsewhere.
- Documentation sites, developer tools, changelogs - reading-first surfaces.
- Professional services, consulting, architecture/firm portfolios - competence signaled through restraint.
- Product pages and pricing pages where one decision (sign up, buy) should dominate.
- Anything where task efficiency and scan speed outrank brand theatre.

**Do NOT use for:**
- Entertainment, events, youth-culture brands, music - the energy won't match (that's maximalism's job).
- E-commerce catalogs with hundreds of SKUs - image-forward density serves shoppers better.
- Kids' products, playful brands - restraint reads as sterile.
- Landing pages that need to explain a novel, complex concept with few words - you'll need editorial illustration or diagram systems, which this style rationing may starve.

## Quick art-direction token sketch

- `--bg: #FFFFFF` (or warm `#FAFAF7`); `--ink: #111111` (never pure #000 on #FFF for body - #111111 is a touch softer at ~19:1); muted text `#5F6368` (6.0:1 on white); the absolute lightness floor is `#767676` (4.54:1).
- `--accent: one` saturated color (e.g. `#2563EB` blue or `#0F766E` teal) - used for primary actions, active states, and focus; nowhere else.
- Spacing scale: **8 / 16 / 24 / 48 / 96** (doubles create rhythm: intra-component 8–16, section 48, hero 96).
- Type: one sans family (e.g. Inter/IBM Plex Sans/Söhne-class), scale `16 / 18 / 24 / 32 / 48 / 64+`, weights 400 / 600 only (700 reserved for the single loudest element).
- Radius: small and consistent - `4–8px` (or 0 for a stricter Swiss read); one value system-wide.
- Shadows: none or a single hairline `0 1px 2px rgba(0,0,0,0.06)` + `1px` border `#E5E7EB` for elevation; depth prefers borders over blur.
- Prose measure: `60–68ch`; content max-width `~1040px` (dashboards) on a 12-column grid.
- Motion: micro-interactions **150–250ms**, `ease-out`; nothing bounces, nothing flies.

## Component guidance summary

**What shines:** typography-led heroes, tables and data lists (minimalism's grid heritage loves tabular structure), forms with clear labels and single-column flow, documentation/prose layouts, nav bars as plain horizontal lists, pricing cards separated by hairlines instead of shadow boxes.

**What stays restrained:** everything - but especially ornament (no decorative illustration clusters, no gradient washes), color (one accent, semantic colors only for status), and motion (opacity/1–2px translates; no parallax). Complexity is handled by **progressive disclosure** (collapsible sections, step-by-step flows, secondary actions behind overflow menus) rather than by shrinking everything to fit.

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Canonical CSS recipe

```css
/* The minimalism contract in 20 lines: rhythm, hairlines, one accent, honest affordances */
:root {
  --bg: #ffffff; --ink: #111111; --muted: #5f6368;
  --line: #e5e7eb; --accent: #2563eb;
  --s1: 8px; --s2: 16px; --s3: 24px; --s4: 48px; --s5: 96px;
  --dur: 200ms; --ease: ease-out;
}
.btn-primary {
  background: var(--ink); color: #fff;
  border: 1px solid var(--ink); border-radius: 6px;
  padding: 10px 20px; font: 500 1rem/1.2 inherit;
  transition: background-color var(--dur) var(--ease);
}
.btn-primary:hover { background: #000; }
.btn-primary:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.btn-primary:disabled { background: var(--line); border-color: var(--line); color: var(--muted); cursor: not-allowed; }

a { color: inherit; text-decoration: underline; text-underline-offset: 0.15em;
    text-decoration-color: var(--line); transition: text-decoration-color var(--dur) var(--ease); }
a:hover { text-decoration-color: var(--ink); }
.card { border: 1px solid var(--line); border-radius: 6px; padding: var(--s3); }
```

## Accessibility notes (mandatory)

- **Contrast floor:** body ≥4.5:1 (WCAG 1.4.3). The most common minimalism failure is "subtle" gray text - anything lighter than `#767676` (4.54:1) on white fails; `#5F6368` (6.0:1) is the practical muted default, `#6B7280` (4.8:1) the last acceptable step. Never place body text below 16px, and never at `#9CA3AF` (2.5:1) or lighter.
- **Affordance without hover:** links underlined (or clearly boxed); if you de-underline links in prose, the de-decoration must still pass "distinguishable without color" - in practice, keep the underline. This is the style's #1 accessibility contract.
- **Disabled visibility:** disabled buttons use solid light fill + mid-gray text (≥4.5:1 where text is meaningful) + `cursor: not-allowed`; they must be recognizably disabled at a glance, not merely faint.
- **Focus:** 2px solid accent outline, `offset: 2px`, on every interactive element - the accent's second job.
- **Motion:** 150–250ms transitions respect `prefers-reduced-motion: reduce` (transitions drop to 0ms; nothing functional depends on motion).
- **Whitespace ≠ offscreen:** generous spacing must not push primary actions below the fold on mobile; the rhythm adapts (96→48), it doesn't just compress.

## Top-5 failure modes

1. **Invisible affordances** - de-underlined gray links, ghost buttons, hover-only hints. Fix: underline + hover-darken pattern in [references/style-guide.md](references/style-guide.md).
2. **Faint text epidemic** - 13px `#9CA3AF` captions everywhere. Fix: the contrast floor and muted-token ladder in [references/quality-checklist.md](references/quality-checklist.md).
3. **Whitespace without rhythm** - arbitrary 27px gaps; spacing that doesn't group. Fix: the 8/16/24/48/96 scale and proximity rules.
4. **Hierarchy collapse** - everything 400-weight 16px, or 12 equally-styled cards. Fix: type scale + "one loudest element per viewport" rule in [references/implementation-examples.md](references/implementation-examples.md).
5. **Accent dilution** - the accent used on links, icons, badges, and charts until nothing reads as primary. Fix: accent budget (≤3 uses per viewport).

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
