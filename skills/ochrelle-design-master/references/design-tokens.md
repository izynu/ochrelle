# Design Tokens

Tokens are the single source of truth for visible decisions. They make the art direction
portable, enforce consistency, and are the unit of review ("is this value intentional?").

## Token architecture

Three layers, each consuming only the layer above it:

1. **Primitive** (raw): named values with no opinion. `--color-violet-600: #7c3aed;`
   Never used directly in components.
2. **Semantic** (decision): what a value *means* in this product.
   `--color-bg: var(--color-violet-950);` Components consume only these.
3. **Component** (binding): semantic tokens scoped to a component and its variants.
   `--button-primary-bg: var(--color-action);`

Rules:

- A component must never reference a primitive directly; if it seems necessary, either a
  semantic token is missing or the design is drifting.
- Semantic layer is where themes (light/dark/contrast) swap values; component and markup
  layers stay untouched by theming.
- Number of tokens is bounded by the design, not by exceptions - every new token needs a
  reason a reviewer can verify.

## Naming conventions

Pattern: `--{category}-{concept}-{variant?}-{state?}`

- Categories: `color`, `space`, `radius`, `font`, `shadow`, `motion`, `z`.
- Concepts describe role, not appearance: `color-text-secondary` (not `color-gray-500` at
  semantic level), `space-inset-md`, `radius-card`.
- On-color pairs are explicit: every surface token that hosts text has a paired
  `on-` foreground token (`color-surface-raised` ↔ `color-on-surface-raised`).
- States appear in component tokens: `color-button-primary-bg-active`.
- Keep hyphen count predictable; sort mentally by category first, concept second.

## Complete example token set

A neutral, product-grade base (minimalist-leaning; style families adjust it below).

```css
:root {
  /* ---------- primitives (excerpt) ---------- */
  --violet-600: #7c3aed;
  --gray-0: #ffffff;
  --gray-50: #fafafa;
  --gray-100: #f4f4f5;
  --gray-300: #d4d4d8;
  --gray-500: #71717a;
  --gray-900: #18181b;
  --gray-950: #09090b;
  --red-600: #dc2626;

  /* ---------- semantic: color ---------- */
  --color-bg: var(--gray-50);
  --color-bg-emphasis: var(--gray-100);
  --color-surface: var(--gray-0);
  --color-surface-raised: var(--gray-0);
  --color-on-surface: var(--gray-900);          /* pairs with --color-surface */
  --color-on-surface-muted: var(--gray-500);
  --color-on-bg: var(--gray-900);               /* pairs with --color-bg */
  --color-border-subtle: var(--gray-300);
  --color-action: var(--violet-600);
  --color-on-action: var(--gray-0);             /* pairs with --color-action */
  --color-danger: var(--red-600);
  --color-on-danger: var(--gray-0);
  --color-focus-ring: var(--violet-600);

  /* ---------- semantic: space (4px base) ---------- */
  --space-1: 0.25rem;   /* 4  */
  --space-2: 0.5rem;    /* 8  */
  --space-3: 0.75rem;   /* 12 */
  --space-4: 1rem;      /* 16 */
  --space-6: 1.5rem;    /* 24 */
  --space-8: 2rem;      /* 32 */
  --space-12: 3rem;     /* 48 */
  --space-16: 4rem;     /* 64 */
  --space-inset-sm: var(--space-2);
  --space-inset-md: var(--space-4);
  --space-inset-lg: var(--space-6);
  --space-stack-md: var(--space-3);

  /* ---------- semantic: radius ---------- */
  --radius-none: 0;
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
  --radius-pill: 9999px;

  /* ---------- semantic: typography ---------- */
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "JetBrains Mono", "SF Mono", monospace;
  --font-size-xs: 0.75rem;    /* 12 */
  --font-size-sm: 0.875rem;   /* 14 */
  --font-size-md: 1rem;       /* 16 body floor */
  --font-size-lg: 1.25rem;    /* 20 */
  --font-size-xl: 1.5rem;     /* 24 */
  --font-size-2xl: 2rem;      /* 32 */
  --font-size-3xl: 2.75rem;   /* 44 */
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --line-height-tight: 1.2;
  --line-height-body: 1.5;

  /* ---------- semantic: shadow / elevation ---------- */
  --shadow-0: none;
  --shadow-1: 0 1px 2px rgba(9, 9, 11, 0.08);
  --shadow-2: 0 2px 8px rgba(9, 9, 11, 0.10);
  --shadow-3: 0 8px 24px rgba(9, 9, 11, 0.14);
  --shadow-focus: 0 0 0 2px var(--color-bg), 0 0 0 4px var(--color-focus-ring);

  /* ---------- semantic: motion ---------- */
  --motion-duration-fast: 120ms;
  --motion-duration-base: 200ms;
  --motion-duration-slow: 350ms;
  --motion-ease-standard: cubic-bezier(0.2, 0, 0, 1);
  --motion-ease-entrance: cubic-bezier(0, 0, 0.2, 1);
  --motion-ease-exit: cubic-bezier(0.4, 0, 1, 1);
}

/* ---------- component layer (example: button) ---------- */
.button {
  background: var(--color-action);
  color: var(--color-on-action);
  padding: var(--space-inset-sm) var(--space-4);
  border-radius: var(--radius-md);
  font-size: var(--font-size-md);
  transition: background var(--motion-duration-fast) var(--motion-ease-standard);
}
.button:hover { background: var(--color-action-hover, --color-action); }
.button:active { transform: translateY(1px); }
.button:focus-visible { box-shadow: var(--shadow-focus); outline: none; }
.button:disabled { opacity: 0.5; cursor: not-allowed; }

@media (prefers-reduced-motion: reduce) {
  .button { transition: none; }
  .button:active { transform: none; }
}
```

## Dark mode strategy

- Strategy choice: **semantic remap** (recommended) - same semantic token names, swapped
  values under `@media (prefers-color-scheme: dark)` and/or a `[data-theme="dark"]`
  attribute hook. Components never know a theme switch happened.
- Invert lightness, not hue relationships: dark backgrounds get desaturated light tints;
  brand accents usually lighten one step for contrast.
- Never hard-code black/white in components; elevation is expressed with **surface
  lightness steps** plus subtle borders in dark mode (shadows read poorly on dark), e.g.
  `--color-surface-raised` = a lighter dark gray rather than a bigger shadow.
- Verify every `on-*` pair in both themes at 4.5:1 (3:1 for large text and UI indicators).
- Respect `color-scheme: light dark` so platform chrome (scrollbars, form controls) matches.

## How tokens differ per style family

The architecture is identical; the *values* and *which layers carry expression* change:

| Family | Typical signature in tokens |
|---|---|
| Minimalism | Neutral palette + one accent; `--radius` from `0–8px`; `--shadow-0/1` only; generous `space` scale; type scale does the expressiveness |
| Neumorphism | Single base surface tone; two-direction shadow tokens (light top-left, dark bottom-right); `on-surface` pair must be a deliberate contrast decision |
| Glassmorphism | `color-surface-glass` (rgba), `--blur-glass` (e.g. `16px`), 1px translucent `color-border-glass`; solid fallback tokens defined in parallel |
| Claymorphism | Saturated tinted surfaces; double-shadow token (`inset` + large soft drop); large radii (`16–24px+`) |
| Brutalism | `--radius-none`; `--shadow` = hard offset (e.g. `4px 4px 0 black`); 2–3px border-width token; raw system font stack allowed as a deliberate choice |
| Maximalism | Extended accent hue set; pattern/texture tokens; strict grid + spacing tokens carry the legibility burden |
| Skeuomorphism | Texture asset tokens; multi-layer shadow tokens per material; dimension tokens (bevel widths, knob sizes) |
| Liquid Glass (web approx.) | Platform-provided material where available; approximation tokens labeled `--liquid-glass-approx-*` with explicit fallbacks |
| Bento grid | Layout tokens: `--bento-gap`, `--bento-cell-min`, span sizes - combined with whichever visual family above |
| Spatial UI | Depth tokens: `--z-scene/-content/-chrome`; environment-aware material tokens; motion tokens tuned for comfort |

Wherever a style's signature conflicts with AA contrast (neumorphism, glassmorphism on
busy backdrops), the token set must include the remediation token (high-contrast variant,
solid fallback) as a first-class member - not as a per-component hack.
