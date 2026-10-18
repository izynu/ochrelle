# Editorial Design - Quality Checklist

Ship gate for editorial design. Every item must pass before delivery.

---

## A. Art direction

1. **(gate)** One text serif, one display voice, one label sans - three families maximum, each with a fixed job.
2. **(gate)** Body measure is 60-75ch (`--measure`), decks and captions 45-55ch; no paragraph exceeds the measure at any breakpoint.
3. Hierarchy is typographic: kicker, headline, deck, byline, body, caption each have one fixed form and appear in that order on article pages.
4. Radius 0 on every component; hairlines are 1px `--rule`, structural rules are 2px `--ink`; shadows appear only on modals.
5. One accent color; kickers, links, and flags may use it; section headings never wear color fills.
6. The asymmetric grid is visible on desktop: body column plus margin column hosting pull quotes and marginalia.

## B. Components & states

7. **(gate)** Links, buttons, nav links, inputs, and pagination all define default, hover, `:focus-visible`, active, disabled (and current for nav/pagination) per style-guide section 8.
8. Body links are underlined by default and change thickness/color on hover; hover is never the only channel for meaning.
9. Disabled buttons use `#B9B4A6` fill with `#565650` text (4.6:1) - no opacity hacks.
10. Nav marks the current section with accent color plus a 2px underline (`aria-current="page"`).
11. Forms have persistent visible labels (placeholder is never the only label), `autocomplete` on identity fields, and `aria-invalid` + `aria-describedby` wiring for errors.
12. The accordion/toc (if used) wires `aria-expanded`/`aria-controls`, uses real `<button>` elements, and works with keyboard only.

## C. Accessibility

### Verified pair reference (computed WCAG ratios)

| Text | Fill | Ratio | Verdict |
|---|---|---|---|
| `#1A1A1A` ink | `#FAF7F0` ivory | 16.3:1 | ✓ body |
| `#1A1A1A` ink | `#FFFFFF` card | 17.4:1 | ✓ body |
| `#565650` muted | ivory | 6.9:1 | ✓ decks, captions, metadata |
| `#8C1D1D` accent | ivory | 8.5:1 | ✓ links, kickers |
| `#FFFFFF` white | `#8C1D1D` accent fill | 9.1:1 | ✓ solid buttons |
| `#FFFFFF` white | `#1A1A1A` ink fill | 17.4:1 | ✓ primary buttons |
| `#565650` muted | `#B9B4A6` disabled fill | 4.6:1 | ✓ disabled labels only |
| `#D6CFBF` rule | ivory | 1.4:1 | decorative only, never text |

13. **(gate)** All body text ≥4.5:1 (16.3:1 here); muted text is the lightest permitted and never used for body copy.
14. **(gate)** Focus visible everywhere: `outline: 2px solid var(--accent); outline-offset: 3px`; ring contrast ≥3:1 against adjacent surfaces.
15. Links are distinguishable without color (underline always present).
16. Every image is a `figure` with a `figcaption`; decorative images carry empty `alt`; credit lines identify the source.
17. Drop caps are real text (no image glyphs); screen readers read the opening sentence intact.
18. Pull quotes use `blockquote` semantics; duplicated display copy is `aria-hidden` on one instance.
19. `prefers-reduced-motion: reduce` collapses transitions and disables scroll-triggered reveals.
20. Headings follow one `h1` per article, `h2` crossheads in order; landmarks (`header`, `nav[aria-label]`, `main`, `article`) present.

## D. Performance

21. At most 3 font families with only used weights; webfonts subset with `font-display: swap`; italic and semibold loaded only if used.
22. Figures carry explicit `width`/`height` or `aspect-ratio`; below-the-fold images `loading="lazy"`.
23. No parallax, carousels, or scroll-jacking scripts; motion budget is a few CSS transitions.
24. Long articles paginate or lazy-load without shifting the reading column (no late-loading ads or embeds resizing text).

## E. Responsive

25. Article column stays 60-75ch from 360px to 2560px because the measure is ch-based; verify at 360, 768, 1280.
26. Margin notes and pull quotes fold into the flow below 1024px without orphaning near headings.
27. Masthead compresses: wordmark scales, nav stays reachable (horizontal scroll or list, not a mystery hamburger without a label).
28. Tap targets ≥44px on nav links, buttons, and toc rows; page works at 200% zoom with no clipped captions.

---

## 10-point pre-delivery pass

- [ ] 1. Read one full article at 100% zoom: measure, rhythm, and hierarchy hold for at least 5 paragraphs of reading.
- [ ] 2. Tab the page: focus ring (2px accent, offset) visible on every link, button, input; order follows the reading order.
- [ ] 3. Keyboard-test the toc/accordion: Enter toggles, focus stays sensible, one section open at a time.
- [ ] 4. Audit pairs against the C table; measure any pair not listed and record the ratio.
- [ ] 5. Unplug motion: reduced-motion users get instant states, no fades, no reveals.
- [ ] 6. Check every figure: caption sentence plus credit line present, image does not reflow the column when loading.
- [ ] 7. Count families and weights in the shipped CSS: 3 families max, no unused weights loaded.
- [ ] 8. Walk the state matrix for links, buttons, inputs, pagination against style-guide section 8.
- [ ] 9. Test 360px and 200% zoom: measure holds, no horizontal scroll, pull quotes fold cleanly into the flow.
- [ ] 10. Ask the authority question: does the page read like a publication or a template? If a stock-theme pattern (centered hero card, pill buttons) survives, remove it.
