---
name: ochrelle-vaporwave
description: Applies the vaporwave aesthetic, the 2010s internet-born music-movement look built from 1980s and 1990s consumer technology nostalgia, to web and product surfaces. Vaporwave combines Roman busts and Greek statuary, VHS tracking glitches, Windows 95 era chrome, mall culture, katakana accents, chrome lettering, checkerboards and sunset gradients in pink, cyan, magenta and violet over deep violet night palettes. Use this skill when the user mentions vaporwave, retrowave nostalgia, VHS glitch, mallsoft, seapunk-adjacent visuals, 90s computer nostalgia, or asks for music release pages, event and party sites, streetwear drops, DJ/producer profiles or creative portfolios targeting the aesthetic. It is not for enterprise tools, accessibility-first services or brands without an irony budget.
license: MIT
metadata:
  author: ochrelle
  version: "2.0.0"
  family: thematic-genres
---

# Vaporwave

Full guidance: [references/style-guide.md](references/style-guide.md) · runnable components: [references/implementation-examples.md](references/implementation-examples.md) · ship gate: [references/quality-checklist.md](references/quality-checklist.md).

## Definition

Vaporwave is the visual language of a 2010s internet music microgenre: a dreamlike collage of consumer-technology nostalgia. Its surfaces mix classical statuary (Roman busts, Greek columns), degraded analog video (VHS tracking lines, chroma bleed), early-PC chrome (Windows 95-style windows and dialogs), shopping-mall and airliner nostalgia, Japanese katakana signage, chrome and holographic lettering, checkerboard floors, and saturated sunset gradients in pink, cyan, magenta and violet. The palette is historically correct content: magenta and violet are the genre's signature hues, used with explicit contrast rules rather than avoided.

It is NOT outrun/synthwave. Outrun is chrome sports cars, neon grid horizons and midnight-drive heroics; vaporwave is quieter and weirder: malls, muzak, dead software, corporate sculpture. It is also NOT generic "retro 80s": vaporwave's irony lives in the collision of the ancient (marble) and the obsolete (floppy disks), not in neon nostalgia alone.

| Signal | Real vaporwave | Lazy imitation |
|---|---|---|
| Palette | Deep violet night base + pink/cyan/magenta accents, sunset gradients with a defined hierarchy | Every surface neon, all hues equally loud |
| Type | Chrome/holo display lettering + clean monospace or system-UI body | All-caps neon script everywhere, unreadable body |
| Statuary | Classical bust/column as composed focal element | Random emoji or clip-art statue dropped in a corner |
| Glitch | VHS artifacts as accents (tracking bar, scanlines, chroma offset) | Constant strobing distortion over everything |
| Icons of era | Win95 dialog, floppy, cassette, mall signage, katakana | Generic "retro wave sun" only |
| Irony | The dead-mall melancholy is legible in copy and composition | Pure celebration, no point of view |

## Philosophy

1. **Nostalgia for futures that never shipped.** The style is about dead media and abandoned optimism: malls after closing, unattended kiosks, software nobody installs anymore. Curate artifacts; do not just decorate.
2. **Marble meets plastic.** The genre's core image is the classical bust next to a consumer gadget. Every strong composition pairs one "ancient" element with one "obsolete tech" element.
3. **Degradation as texture.** Scanlines, chroma bleed and tracking bars are the grain of the style, like film grain for noir. They are accents on top of clean structure, never a replacement for it.
4. **Night palette, loud accents.** The base is always a deep violet-navy dark mode; pink, cyan, magenta and mint are currency spent deliberately on focus points, actions and key type.
5. **Type is a specimen.** Chrome, holographic and outline display type are the genre's couture. They headline; they never carry paragraphs. Body copy stays plain, monospaced or system-UI, high contrast.
6. **Japanese text is signage, not confetti.** Katakana appears the way it appears in 80s Tokyo and 90s tech marketing: as product labels, pricing tags and system messages. Mark it with `lang="ja"` and treat it as real content or explicit decoration.

## Brief historical context (verifiable)

- **Daniel Lopatin** released *"Chuck Person's Eccojams Vol. 1"* in **2010**, slowing and looping 1980s pop into hazy fragments; it is widely cited as proto-vaporwave alongside his broader output as Oneohtrix Point Never.
- **Vektroid** (Ramona Langley) released *"Floral Shoppe"* in **December 2011** under the alias **Macintosh Plus**; its cover, a classical bust against pink-cyan gradients with glitch text, became the genre's definitive visual.
- **James Ferraro's** *"Far Side Virtual"* (**2011**) celebrated the eerie cheer of consumer operating systems and ringtone-era muzak, defining the style's conceptual side.
- The microgenre crystallized on **Bandcamp and Tumblr through 2011-2013**, spawning derivatives such as **future funk** and **mallsoft**, each with its own visual dialects of the same nostalgic palette.
- The visual scene absorbed **1980s-90s Japan** aesthetics (bubble-economy signage, city pop artwork, katakana tech manuals) and **Windows 95/98** UI culture, both of which remain core reference points.
- From the mid-2010s the aesthetic crossed into streetwear, festival branding and editorial design; the adjacent **outrun/synthwave** scene (grid horizons, neon chrome) shares palette DNA but is a distinct genre.

## When to use / when NOT

**Use for:**

- Music releases: album pages, Bandcamp/label sites, mixtape covers, tracklist UIs, cassette and vinyl drops.
- Events: club nights, listening parties, festival stages and line-ups aimed at the aesthetic.
- Streetwear and merch: drop pages, lookbooks, size charts with the genre's typographic swagger.
- Creative portfolios for designers, VJs and 3D artists working in retro-digital imagery.
- Nostalgia marketing where the brand can carry irony (gaming peripherals, emulation frontends, revival gadgets).

**Do NOT use for:**

- Enterprise software, banking, health or government services: the irony and dark palette undermine trust and accessibility.
- Children's products: VHS distortion and strobe-adjacent effects are unsuitable.
- Long-form reading: the palette and display type fatigue eyes fast.
- Brands with austere or heritage positioning; vaporwave will read as costume.
- Anything requiring photos of real people: the style's artificiality clashes with documentary imagery.

## Quick art-direction token sketch

```css
:root {
  --bg: #1B1035;        /* deep violet night base */
  --bg-deep: #120B24;   /* footer/depth */
  --panel: #241440;     /* raised panels, ink on it 15.17:1 */
  --ink: #F6F1FF;       /* primary text, 16.16:1 on --bg */
  --ink-soft: #C9BCE4;  /* secondary text, 10.06:1 on --bg */
  --accent: #FF71CE;    /* pink, 7.26:1 on --bg; ink on it #26061F 7.54:1 */
  --cyan: #01CDFE;      /* 9.53:1 on --bg; ink on it #06232B 8.70:1 */
  --violet: #B967FF;    /* 5.50:1 on --bg: large text/UI only */
  --mint: #3DFFB0;      /* 13.76:1 on --bg: confirmations */
  --grid: #5A3A8C;      /* decorative horizon lines */
}
```

- Spacing: 4 / 8 / 12 / 16 / 24 / 40 / 64px; panels breathe at 24px; heroes at 64px vertical.
- Type: display via chrome/holo gradient fills (background-clip: text) at 32-72px; body: `"Segoe UI", system-ui, sans-serif` 16px; mono accents: `"Consolas", "Courier New", monospace` for prices, timestamps, system text.
- Radius: 8-12px panels; 999px chips; sharp 0px corners allowed on Win95-style dialog pastiches (bevel borders instead).
- Shadows: none in the classic sense; depth via 1px accent borders, glow `0 0 24px rgba(255, 113, 206, 0.35)` and layered panel tints.
- Motion: 200ms hovers, 250ms panels; glitch bursts 300-900ms, triggered not ambient; grid/scanline loops 8-20s, all gated by reduced motion.

## Component guidance summary

- **Buttons**: solid pink or cyan fills with dark ink labels (both pairs exceed 7:1), 1px lighter top edge, hover adds glow, press nudges 1px; ghost buttons are 1px cyan outlines.
- **Cards**: `--panel` tiles with 1px `rgba(255,255,255,0.14)` borders, optional scanline overlay, price/mono metadata rows in `--ink-soft`.
- **Forms**: dark inputs with 1px violet borders and 2px cyan focus rings; labels in `--ink`, mono helper text in `--ink-soft`.
- **Nav**: top bar with mono links, active link in pink; a thin animated sunset gradient strip (2-4px) is the signature flourish.
- **Dialog pastiche**: Win95-style window with beveled borders and a title bar in `--accent` gradient; use sparingly as a spotlight component.
- **Imagery slots**: busts, columns, checkerboards and palm silhouettes as CSS/SVG shapes; tracklists and price tags are the style's native "photo" content.

## Canonical CSS recipe

```css
:root {
  --bg: #1B1035;
  --panel: #241440;
  --ink: #F6F1FF;
  --ink-soft: #C9BCE4;
  --accent: #FF71CE;
  --accent-ink: #26061F;
  --cyan: #01CDFE;
  --cyan-ink: #06232B;
  --sunset: linear-gradient(90deg, #FF71CE, #FF9A76 45%, #FFD86B 70%, #01CDFE);
}

.vw-button {
  padding: 12px 24px;
  border: 0;
  border-radius: 999px;
  background: var(--accent);
  color: var(--accent-ink);
  font: 700 15px/1.2 "Segoe UI", system-ui, sans-serif;
  letter-spacing: 0.04em;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.45), 0 0 24px rgba(255, 113, 206, 0.35);
  cursor: pointer;
  transition: box-shadow 200ms ease-out, transform 200ms ease-out;
}
.vw-button:hover  { box-shadow: inset 0 1px 0 rgba(255,255,255,0.45), 0 0 36px rgba(255,113,206,0.55); }
.vw-button:active { transform: translateY(1px); }
.vw-button:focus-visible { outline: 2px solid var(--cyan); outline-offset: 2px; }

.vw-panel {
  padding: 24px;
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 12px;
  background: var(--panel);
  color: var(--ink);
  position: relative;
  overflow: hidden;
}
.vw-panel::after {  /* static scanlines: texture, not animation */
  content: "";
  position: absolute; inset: 0;
  background: repeating-linear-gradient(180deg,
    rgba(255,255,255,0.03) 0 1px, rgba(0,0,0,0) 1px 3px);
  pointer-events: none;
}

.vw-chrome {
  font-size: clamp(32px, 6vw, 72px);
  font-weight: 800;
  letter-spacing: 0.02em;
  background: linear-gradient(180deg,
    #F4FBFF 0%, #C3D8EC 38%, #5E7FA6 50%, #DCEBFF 54%, #8FB2D6 72%, #4A6FA5 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  filter: drop-shadow(0 1px 0 rgba(255,255,255,0.25));
}
```

## Accessibility notes

- **Contrast anchors (measured)**: body `#F6F1FF` on `#1B1035` is 16.16:1; secondary `#C9BCE4` is 10.06:1. Pink `#FF71CE` at 7.26:1 and cyan `#01CDFE` at 9.53:1 pass as text on the base; violet `#B967FF` (5.50:1) is fine for large text and UI strokes but keep small body text in `--ink`/`--ink-soft`. On accent fills, use the dark pairs: `#26061F` on pink (7.54:1), `#06232B` on cyan (8.70:1); never white-on-pink or dark-on-violet for body copy.
- **Gradient text**: the chrome treatment (`color: transparent`) must never be applied to body text or anything below 32px bold; supply a solid-color fallback via `@supports not (background-clip: text)` and keep display text in real DOM nodes (never flattened images).
- **Focus-visible**: `outline: 2px solid #01CDFE; outline-offset: 2px` on every control; cyan holds 3:1+ against the panel and base, satisfying WCAG 2.2 AA 1.4.11 (non-text contrast), and never rely on the glow alone to mark focus.
- **Motion safety**: glitch bursts, tracking bars and scanline shimmer are the seizure-adjacent risk in this style. Nothing flashes more than 3 times per second (WCAG 2.2 AA 2.3.1); glitch runs 300-900ms on user action, never on loop; all loops stop under `prefers-reduced-motion`, replaced by static single-frame texture.
- **Katakana and bilingual text**: wrap Japanese strings in `lang="ja"`, provide an English equivalent in the copy or `title`/`aria-label` where meaning matters, and mark purely decorative katakana `aria-hidden="true"` so screen readers do not read ornament as content.
- **Dark-theme polish**: avoid pure black on pure white inversions; keep `--panel` tints and 1px light borders so depth survives high-contrast and forced-color modes.

## Top-5 failure modes

1. **Neon soup.** Every element glows a different hue and nothing is clickable-first. Fix: budget accents: pink for primary actions, cyan for focus/links, mint for success, violet for structure; the base stays 70% of every view.
2. **Unreadable gradient text.** White text over the sunset gradient, or chrome fill below 32px. Fix: text over gradients sits on a `--panel` scrim plate; chrome fills only on display type with the `@supports` fallback.
3. **Genre confusion.** A chrome sports car, a highway grid and a synth sun: that is outrun. Fix: stock the prop library with consumer-nostalgia artifacts (busts, floppy, cassette, mall signs, Win95 dialog) and keep the mood deadpan, not heroic.
4. **Copyright landmines.** Using real Windows assets, anime stills, brand logos or sampled artwork invites takedowns. Fix: draw original approximations in CSS/SVG (bevel borders, generic dialog chrome) and license statuary imagery from free sources or draw it.
5. **Permanent glitch.** Scanlines flickering and tracking bars looping forever: motion sickness bait. Fix: texture is static; distortion is a 300-900ms burst on interaction; everything halts under `prefers-reduced-motion`.

Run [references/quality-checklist.md](references/quality-checklist.md) before delivery.
