---
name: ochrelle-editorial-design
description: Art direction and implementation skill for editorial design - magazine and newspaper craft translated to the web. Dominant headline typography, deck and subhead hierarchy, kickers and bylines, pull quotes, drop caps, baseline-grid rhythm, asymmetric grids, disciplined 60-75 character measure, figure captions, and folios. Think The New York Times, The Gentlewoman, Monocle. Use for blogs, digital magazines, essays, press pages, newsrooms, newsletters, and story-driven product marketing. Trigger words include editorial, magazine, newspaper, article, longform, journal, masthead, broadsheet, newsprint, typography-led.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: typographic-expressive
---

# Editorial Design

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Editorial design is the grammar of print journalism applied to screens: one dominant headline voice, a strict hierarchy of kicker, headline, deck, body, and caption, hairline rules, folios, and a body measure held between 60 and 75 characters. Authority comes from typography and structure, not from decoration.

What it is NOT: it is not "big serif font" bolted onto a centered template, and it is not a dashboard of identical cards. If every block is centered and equally weighted, it is a template wearing a masthead.

| | Real editorial design | Lazy "blog theme" |
|---|---|---|
| Hierarchy | Kicker / headline / deck / byline / body / caption, each a distinct voice | One heading style, bolded randomly |
| Measure | 60-75ch body, 45-55ch decks and captions | Full-bleed 120ch paragraph walls |
| Grid | Asymmetric multi-column print grid, visible hairlines | Centered 720px column, nothing else |
| Type | Serif text voice + deliberate display voice, tight family | Five Google Fonts that fight |
| Detail | Drop caps, pull quotes, figure captions, folios | Stock "share" buttons between paragraphs |
| Result | Reads like a publication | Reads like a theme demo |

## Philosophy

1. **Type is the layout.** The grid exists to serve letterforms. Size, weight, and position carry hierarchy; color boxes and icon rows do not.
2. **Hierarchy is grammar.** Kicker tells you where you are, headline tells you what happened, deck frames it, byline signs it, body proves it, caption credits it. Each has one fixed typographic form.
3. **Measure before width.** Nothing is placed wider than its voice allows: body 60-75ch, decks and captions 45-55ch, headlines as wide as their rank permits.
4. **Rules and space are structure.** Hairlines group and separate like margins in a broadsheet; folios and section marks tell readers where they are without chrome.
5. **Restraint signals authority.** One accent color, used sparingly, reads as institutional confidence. Decoration reads as insecurity.
6. **Images are evidence.** Every figure gets a caption and a credit; an uncaptioned image is decoration, not journalism.

## Brief historical context (verifiable)

- The New York Times printed its first issue in 1851 and adopted the slogan "All the News That's Fit to Print" in 1896 under Adolph Ochs; its newsroom faces are drawn versions of Cheltenham (headlines), Imperial (body), and Franklin Gothic (sans).
- Jan Tschichold wrote the Penguin Composition Rules while at Penguin Books (1947-1949), standardizing composition for mass-market paperbacks - an early typographic design system.
- Josef Müller-Brockmann codified the Swiss grid in the journal *Neue Grafik* (founded 1958) and the book *Grid Systems in Graphic Design* (1981).
- Robert Bringhurst's *The Elements of Typographic Style* (1992) fixed the classic measure guidance: 45-75 characters per line for single-column work.
- The Guardian's 2005 Berliner-format redesign under creative director Mark Porter showed how grid discipline and web-era flexibility could share one system.

## When to use / when NOT

**Use for:**
- Blogs, digital magazines, essays, and newsletters - the native habitat.
- Press pages, newsrooms, and annual reports - authority is the product.
- Story-driven product marketing (case studies, founder letters, changelogs with a voice).
- Writer and photographer portfolios where the work is text and image.

**Do NOT use for:**
- Data-dense dashboards, admin consoles, checkout flows - scanning beats reading there.
- Youth-culture drops, party brands, gaming - editorial restraint will read as dull.
- Immersive campaign pages built around motion and full-bleed video.
- Apps whose primary screen is a table, map, or chat stream.

## Quick art-direction token sketch

- `--bg: #FAF7F0` (warm ivory, ink on it: 16.3:1); `--card: #FFFFFF` for raised matter.
- `--ink: #1A1A1A` body and headline text; `--muted: #565650` for captions, decks, metadata (6.9:1 on ivory).
- `--accent: #8C1D1D` deep editorial red (8.5:1 as text on ivory; white on it: 9.1:1) - links in body, kickers, small flags. One accent only.
- `--rule: #D6CFBF` hairlines and column rules; `1px` everywhere, `2px` under the masthead.
- Spacing: baseline rhythm on a 4px unit; body blocks `1.5rem` apart; sections `4rem` apart; asymmetric gutters (wide outer margin, narrow inner).
- Type: serif text voice (Source Serif-class) 400/600; display voice for headlines, `clamp(2.25rem, 5vw, 3.75rem)`; decks `1.25rem/1.5` muted; captions `0.8125rem` muted.
- Radius: 0. Shadows: none on the page; modals may use `0 8px 24px rgba(26, 26, 26, 0.12)`.
- Motion: `160ms ease-out` for hover states; links swap underline weight, not layout. Reduced motion kills all transforms.

## Component guidance summary

| Component | Editorial treatment |
|---|---|
| Headline block | Kicker (tracked caps, accent), headline (display serif), deck (muted, 45-55ch), byline rule |
| Article body | Single 60-75ch column, drop cap on opening paragraph, crossheads every ~300 words |
| Pull quotes | Oversized serif, hairlines above and below, sits in a wider margin column |
| Figures | Full grid-width image, caption + credit line beneath, `figure`/`figcaption` |
| Buttons | Quiet: ink outline or solid ink fill, no radius, no gradient; action verbs only |
| Nav | Masthead bar: wordmark centered or left, date/folio line, section nav in tracked caps, 2px bottom rule |
| Forms | Underlined inputs, uppercase micro-labels, inline validation in accent red |

## Canonical CSS recipe

```css
:root {
  --bg: #FAF7F0;
  --card: #FFFFFF;
  --ink: #1A1A1A;      /* 16.3:1 on bg */
  --muted: #565650;    /* 6.9:1 on bg */
  --accent: #8C1D1D;   /* 8.5:1 on bg; white on it 9.1:1 */
  --rule: #D6CFBF;
  --measure: 68ch;
  --quick: 160ms ease-out;
}
.article {
  max-width: var(--measure);
  margin: 0 auto;
  font: 400 1.125rem/1.7 Georgia, "Times New Roman", serif;
}
.kicker {
  font: 600 0.8125rem/1 "Helvetica Neue", Arial, sans-serif;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--accent);
}
.article h1 {
  font: 700 clamp(2.25rem, 5vw, 3.75rem)/1.08 var(--font-display, Georgia, serif);
  letter-spacing: -0.01em;
  margin: 0.5rem 0 1rem;
}
.deck { font: 400 1.25rem/1.5 var(--font-text, Georgia, serif); color: var(--muted); max-width: 52ch; }
.article p + p { margin-top: 1.5rem; }
.article > p:first-of-type::first-letter {
  float: left;
  font: 700 3.4em/0.8 var(--font-display, Georgia, serif);
  padding: 0.08em 0.12em 0 0;
}
.pullquote {
  border-block: 1px solid var(--rule);
  margin: 2.5rem 0;
  padding: 1.5rem 0;
  font: 600 italic 1.5rem/1.4 var(--font-display, Georgia, serif);
  max-width: 45ch;
}
.btn-ink {
  font: 600 0.875rem/1 "Helvetica Neue", Arial, sans-serif;
  letter-spacing: 0.04em;
  color: #FFFFFF;
  background: var(--ink);
  border: 1px solid var(--ink);
  border-radius: 0;
  padding: 0.875rem 1.5rem;
  min-height: 44px;
  transition: background var(--quick);
}
.btn-ink:hover { background: var(--accent); border-color: var(--accent); }
.btn-ink:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }
```

## Accessibility notes (mandatory)

- **Contrast:** body text `#1A1A1A` on ivory is 16.3:1; muted `#565650` is 6.9:1 and reserved for decks, captions, and metadata - never for body copy. Accent red text (8.5:1) passes AA at any size; it also passes AAA for large text.
- **Links:** underlined by default (1px offset `0.12em`), turning 2px and accent-colored on hover. Never rely on color alone.
- **Focus:** `outline: 2px solid var(--accent); outline-offset: 3px` on every interactive element (WCAG 2.4.11); the ring is thin because the style is thin, but it is always present.
- **Drop caps** are decorative floats: wrap the logical first letter in real text, never an image glyph; verify screen readers read the sentence intact.
- **Pull quotes** marked with `figure` + `blockquote` semantics; never duplicate the same sentence twice in the DOM without `aria-hidden` on one instance.
- **Motion:** 160ms hovers only; respect `prefers-reduced-motion: reduce` by removing transforms and sticky reveal effects.
- **Measure and zoom:** 60-75ch holds at 200% zoom because the column is character-based, not pixel-based; verify at 1280px and 360px.

## Top-5 failure modes

1. **Centered template drift** - everything centered, hierarchy erased. Fix: rebuild on the asymmetric print grid in [references/style-guide.md](references/style-guide.md), section 7.
2. **Measure creep** - paragraphs running 90-120 characters wide. Fix: enforce `--measure: 68ch` on the body column and 45-55ch on decks and captions.
3. **Font zoo** - three serif families plus a sans that never appears twice. Fix: exactly one text serif, one display voice, one sans for labels; the pairing rules are in [references/implementation-examples.md](references/implementation-examples.md).
4. **Captionless figures** - images floating without context or credit. Fix: every image ships as `figure` + `figcaption` with photographer or source.
5. **Hierarchy by color box** - section titles as filled banners instead of type. Fix: hierarchy lives in size, weight, and rules; the state matrix for the few interactive elements is in [references/quality-checklist.md](references/quality-checklist.md).

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
