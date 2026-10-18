# Research Methodology

How Ochrelle contributors research and verify design claims. The repo's credibility rests
on every claim being standard, verifiable knowledge with a traceable source.

## Source hierarchy (read in this order)

1. **Platform human-interface guidelines** - Apple Human Interface Guidelines (including
   its Liquid Glass and spatial design documentation), Google Material Design guidance,
   Microsoft Fluent design guidance. These are the definitive sources for what a
   platform's named systems (e.g. Liquid Glass) actually are.
2. **W3C / WHATWG standards** - WCAG 2.2 for accessibility, HTML Living Standard for
   semantics, CSS specifications (Filter Effects for `backdrop-filter`, CSS Color Adjust
   for `forced-colors`, Media Queries for `prefers-reduced-motion`).
3. **MDN Web Docs** - practical, browser-accurate documentation for CSS/HTML/ARIA
   features, support, and caveats.
4. **Named-body publications** - W3C WAI tutorials, WebAIM articles, Nielsen Norman Group
   research summaries. Cite the organization and the specific page, not a paraphrase of
   "studies show".
5. **Practitioner literature** - established books and essays (e.g. canonical Swiss
   design writing, "Don't Make Me Think"-class UX literature) for principles. Use for
   grounding principles; verify any *numbers* separately.
6. **Community writing** - blogs, design-tool docs, trend posts. Useful for orientation
   and vocabulary; **never sufficient alone** for a factual claim. Cross-check against
   tiers 1–4 before anything from here enters Ochrelle files.

## Verifying a claim

- **Definitions** (what a style/system *is*): must trace to tier 1–2 sources, or to
  multiple independent tier 3+ sources in agreement. Style names with a single origin
  (e.g. neumorphism from community writing, Liquid Glass from Apple) trace to that origin.
- **Numbers** (contrast ratios, target sizes, timing thresholds): must match the current
  normative document text - WCAG 2.2 for 4.5:1 / 3:1 / 24px targets, the CSS spec or
  MDN for durations and media queries. Re-read the spec; do not trust summaries,
  including this file's.
- **Compatibility/performance claims** ("backdrop-filter is expensive"): verify against
  MDN/can i use for support, and frame performance statements as engineering guidance
  with reasoning, not as benchmarks.
- **Attributed ideas** (Fitts's law, Miller-era chunking claims, Gestalt principles):
  attribute to the source literature by name; never attach invented dates, sample sizes,
  or precise statistics.
- If two sources disagree, record both with dates and prefer the normative or more
  recent one; if unverifiable, the claim does not ship.

## Source catalog

Maintain a catalog entry for every source that materially shaped a file:

| Field | Rule |
|---|---|
| URL | Direct link to the page, not the domain |
| Title | As published |
| Publisher | Organization or author |
| Key finding | One sentence: what this source established for our file |
| Verification date | ISO date (YYYY-MM-DD) of your last read-through |
| Status | `current` / `stale - recheck due` / `superseded (by <link>)` |

Example entry (illustrative format - fill with your own verification when you do it):

```
URL: https://www.w3.org/TR/WCAG22/
Title: Web Content Accessibility Guidelines (WCAG) 2.2
Publisher: W3C
Key finding: AA text contrast 4.5:1 (3:1 large text); minimum target size 24x24 CSS px;
  dragging movements need a non-drag alternative.
Verification date: YYYY-MM-DD
Status: current
```

Store catalogs alongside the skill that depends on them (e.g.
`ochrelle-liquid-glass/` keeps its Apple HIG catalog) so each specialist owns its sources.

## Avoiding invented citations

- Never generate a citation from memory. If you cannot produce a real URL you have
  actually consulted, write the claim **without** citation and mark it
  `needs-source`, or omit it.
- Never fabricate statistics, benchmarks, survey numbers, or dates. "Generous spacing
  improves scanability" needs no number; do not add one.
- Distinguish in text between: *verified with source*, *general standard practice*, and
  *working assumption*. Readers must know which is which.

## Refresh cadence

| Content | Cadence |
|---|---|
| WCAG / normative-spec references | On new spec versions, and at least yearly re-verify |
| Platform HIG (Apple/Material/Fluent, incl. Liquid Glass) | At each major platform announcement; re-verify before any task that cites it |
| MDN-backed compatibility/performance notes | Every 6 months or on use |
| Style trend statuses (what's current/faded) | Yearly; trend claims must be dated in text |
| This skill's files | Re-verify `Verification date` fields quarterly; update statuses |

When a source goes stale: update or rewrite the dependent claim in the same change that
updates the catalog - a stale catalog entry with a live claim is treated as an error in
review.
