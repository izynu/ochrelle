# Maximalism - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Anchor + hue roles */
  --paper: #FAF3E7;            /* anchor neutral - ≥50% of surface */
  --ink: #14100E;
  --hot-pink: #FF3EA5;         /* primary action */
  --sun: #FFD23F;              /* highlights, safe text ground */
  --cobalt: #2E5EAA;           /* links, cool zones */
  --leaf: #0FA36B;             /* success */
  --muted-fill: #B7AB9B; --muted-ink: #3F362C;  /* disabled pair, 5.3:1 */

  /* Voices */
  --font-display: "Playfair Display", "Didot", Georgia, serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;

  /* Patterns (CSS-first) */
  --pat-stripes: repeating-linear-gradient(45deg, var(--hot-pink) 0 12px, var(--sun) 12px 24px, var(--cobalt) 24px 36px);
  --pat-dots: radial-gradient(var(--ink) 1.5px, transparent 1.5px) 0 0 / 16px 16px;

  /* Z-scale contract */
  --z-pattern: 0; --z-photo: 1; --z-sticker: 2; --z-content: 3; --z-interactive: 10;

  /* Motion */
  --ease-out-quint: cubic-bezier(0.22, 1, 0.36, 1);
  --dur-in: 400ms; --dur-hover: 150ms;
}
```

## 2. Component set (HTML)

```html
<header class="nav">
  <a class="nav__brand" href="/">Riot Bloom</a>
  <nav aria-label="Primary">
    <a href="/drop">The Drop</a>
    <a href="/tour" aria-current="page">Tour</a>
    <a href="/archive">Archive</a>
  </nav>
  <a class="btn" href="/tickets">Tickets</a>
</header>

<div class="pattern-band" aria-hidden="true"></div>

<main>
  <section class="hero">
    <h1 class="hero__title">LOUD<br><em>colors</em>,<br>LOUDER IDEAS.</h1>
    <span class="sticker" aria-hidden="true">NEW DROP ✳</span>
    <div class="island">
      <p class="mono-label">SS26 COLLECTION</p>
      <h2>Everything, on purpose.</h2>
      <p>Twelve pieces of pattern-clash tailoring, cut for people who refuse
         to whisper. Ships worldwide from Friday.</p>
      <a class="btn" href="/lookbook">See the lookbook</a>
    </div>
  </section>

  <form class="signup" novalidate>
    <label for="email">Get drop alerts</label>
    <input id="email" name="email" type="email" autocomplete="email" required>
    <p class="field-error" id="email-error" hidden>That address is missing an @ - try name@studio.com.</p>
    <button class="btn" type="submit">Alert me</button>
  </form>
</main>

<footer class="footer-wall">
  <p class="marquee" role="presentation"><span class="marquee__track" aria-hidden="true">RIOT BLOB ✳ RIOT BLOB ✳ RIOT BLOB ✳ </span></p>
  <nav aria-label="Footer"><a href="/about">About</a> <a href="/contact">Contact</a> <a href="/returns">Returns</a></nav>
</footer>
```

## 3. Component set (CSS)

### Nav - calm spine inside a loud world

```css
* { box-sizing: border-box; margin: 0; }
body {
  background: var(--paper);
  background-image: var(--pat-dots);        /* ambient pattern, z 0 */
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.6;
}
.nav {
  display: flex; align-items: center; gap: 24px;
  padding: 16px 24px;
  background: var(--paper);                 /* solid - nav never sits on pattern */
  border-bottom: 3px solid var(--ink);
  position: relative; z-index: var(--z-interactive);
}
.nav__brand { font: 800 1.25rem var(--font-display); text-decoration: none; color: var(--ink); }
.nav nav { display: flex; gap: 16px; }
.nav nav a {
  font: 600 1rem var(--font-body);
  color: var(--ink); text-decoration: underline 2px;
  text-decoration-color: var(--cobalt); text-underline-offset: 0.2em;
  padding: 10px 0;
}
.nav nav a[aria-current="page"] { text-decoration-color: var(--hot-pink); }
.nav .btn { margin-left: auto; }
```

### Pattern band + sticker

```css
.pattern-band {
  height: 24px;
  background: var(--pat-stripes);
  border-block: 3px solid var(--ink);
}
.sticker {
  position: relative; z-index: var(--z-sticker);
  display: inline-block;
  padding: 8px 16px;
  background: var(--sun);
  border: 3px solid var(--ink);
  box-shadow: 6px 6px 0 0 var(--ink);
  font: 700 0.875rem var(--font-mono);
  letter-spacing: 0.05em;
  transform: rotate(-4deg);
}
```

### Button - loud fill, verified contrast, mechanical press

```css
.btn {
  display: inline-block;
  font: 700 1rem var(--font-body);
  color: var(--ink);
  background: var(--hot-pink);
  border: 3px solid var(--ink);
  border-radius: 0;
  padding: 12px 24px;
  min-height: 48px;
  box-shadow: 6px 6px 0 0 var(--ink);
  text-decoration: none;
  cursor: pointer;
  transition: transform var(--dur-hover) var(--ease-out-quint),
              box-shadow var(--dur-hover) var(--ease-out-quint),
              background-color var(--dur-hover) var(--ease-out-quint);
}
.btn:hover { background: var(--cobalt); color: #fff; transform: translate(-2px, -2px) rotate(-1deg); }
/* Hover re-verifies contrast: white on cobalt is ~6.4:1; ink on cobalt is ~3.0:1 -
   that is why the label swaps to white whenever the fill goes cobalt. */
.btn:active { transform: translate(2px, 2px); box-shadow: 4px 4px 0 0 var(--ink); }
.btn:focus-visible { outline: 3px solid var(--ink); outline-offset: 3px; box-shadow: 0 0 0 5px var(--sun); }
.btn:disabled { background: var(--muted-fill); color: var(--muted-ink); box-shadow: none; cursor: not-allowed; }
```

### Hero - one focal point, layered z, readability island

```css
.hero {
  position: relative;
  padding: 48px 24px 64px;
  max-width: 1100px; margin-inline: auto;
}
.hero__title {
  position: relative; z-index: var(--z-content);
  font: 900 clamp(3rem, 9vw, 7rem)/0.95 var(--font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}
.hero__title em { font-style: italic; color: var(--hot-pink); }
.hero .sticker { position: absolute; top: 24px; right: 8%; }
.hero .sticker:hover { transform: rotate(2deg); transition: transform var(--dur-hover) var(--ease-out-quint); }

.island {
  position: relative; z-index: var(--z-content);
  margin-top: 32px; margin-left: clamp(0px, 8vw, 96px);
  max-width: 65ch;
  background: var(--paper);                /* solid backing over ambient dots */
  border: 3px solid var(--ink);
  box-shadow: 8px 8px 0 0 var(--ink);
  padding: 24px;
}
.island h2 { font: 800 1.75rem var(--font-display); margin: 4px 0 12px; }
.island p { font-size: 1.0625rem; }
.island .btn { margin-top: 16px; }
.mono-label { font: 500 0.8125rem var(--font-mono); letter-spacing: 0.05em; text-transform: uppercase; }
```

### Form - quiet inside the noise

```css
.signup {
  max-width: 34rem; margin: 0 auto 64px;
  padding: 24px;
  background: var(--paper);
  border: 3px solid var(--ink);
  box-shadow: 8px 8px 0 0 var(--ink);
}
.signup label { font: 700 1rem var(--font-body); }
.signup input {
  display: block; width: 100%;
  margin-top: 8px; padding: 12px;
  font: 400 1rem var(--font-body);
  background: #fff; color: var(--ink);
  border: 3px solid var(--ink);
}
.signup input:focus-visible { outline: 3px solid var(--cobalt); outline-offset: 3px; }
.signup input[aria-invalid="true"] { border-color: #C0392B; }
.field-error { margin-top: 8px; padding: 8px 12px; background: #fff;
               border: 2px solid #C0392B; color: #8E2418; font-weight: 600; }
.signup .btn { margin-top: 16px; }
```

### Footer wall - loud frame, calm links

```css
.footer-wall {
  background: var(--ink); color: var(--paper);
  border-top: 6px double var(--paper);
  padding-bottom: 24px;
}
.marquee { overflow: hidden; border-bottom: 3px solid var(--paper); }
.marquee__track {
  display: inline-block; white-space: nowrap;
  font: 700 1.5rem var(--font-display);
  padding: 8px 0;
  animation: drift 30s linear infinite;
}
@keyframes drift { to { transform: translateX(-50%); } }
.footer-wall nav {
  display: flex; gap: 24px; justify-content: center;
  padding-top: 24px; position: relative; z-index: var(--z-interactive);
}
.footer-wall a { color: var(--paper); font-weight: 600;
                 text-decoration: underline 2px; text-underline-offset: 0.2em;
                 text-decoration-color: var(--hot-pink); }
.footer-wall a:focus-visible { outline: 3px solid var(--sun); outline-offset: 3px; }
```

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  .marquee__track { animation: none; }
  .btn, .sticker, .island { transition: none; transform: none; }
  *, *::before, *::after { transition-duration: 0ms !important; }
}
```

---

## 4. Advanced recipe A - anchored collage hero (grid-breaking with a spine)

```html
<section class="collage">
  <h1 class="collage__title">SUMMER<br>NOISE</h1>
  <img class="collage__cutout cutout-a" src="look-01.avif" alt="Model in striped suit, yellow backdrop" width="420" height="560">
  <img class="collage__cutout cutout-b" src="look-02.avif" alt="Model in checked coat, pink backdrop" width="380" height="500">
  <span class="sticker collage__sticker" aria-hidden="true">24 LOOKS ✳</span>
  <div class="island collage__island">
    <p>The campaign, shot in Lisbon. Twelve looks, zero restraint.</p>
  </div>
</section>
```

```css
.collage { position: relative; max-width: 1100px; margin-inline: auto; padding: 64px 24px; }
.collage__title {                              /* the anchor: stays on the grid */
  position: relative; z-index: var(--z-content);
  font: 900 clamp(3.5rem, 10vw, 8rem)/0.9 var(--font-display);
  mix-blend-mode: multiply;                    /* type "prints" over photos */
}
.collage__cutout {
  position: relative; z-index: var(--z-photo);
  border: 3px solid var(--ink);
  box-shadow: 8px 8px 0 0 var(--ink);
  object-fit: cover;
}
.cutout-a { position: absolute; top: 120px; right: 6%; width: clamp(180px, 30vw, 380px); transform: rotate(3deg); }
.cutout-b { position: absolute; top: 320px; right: 24%; width: clamp(160px, 26vw, 330px); transform: rotate(-2deg); }
.collage__sticker { position: absolute; top: 90px; right: 30%; z-index: var(--z-sticker); }
.collage__island { position: relative; z-index: var(--z-content); margin-top: 480px; max-width: 60ch;
                   background: var(--paper); border: 3px solid var(--ink); padding: 24px; }

@media (max-width: 767px) {                    /* reduce layers, not quality */
  .collage { padding: 32px 16px; }
  .cutout-a, .cutout-b { position: static; width: 100%; max-width: 420px; margin-top: 16px; transform: rotate(0deg); }
  .collage__sticker { position: static; display: inline-block; margin-top: 16px; }
  .collage__island { margin-top: 24px; }
}
```

Why it works: the headline is the single mega element and never leaves the column flow (anchor); photos and sticker rotate and overlap above it; the body copy ends in an island at z-content - nothing decorative ever crosses it, and mobile flattens the overlaps entirely.

## 5. Advanced recipe B - hue-swap filter chips (state via sticker flip)

```html
<fieldset class="chips">
  <legend>Filter the archive</legend>
  <button class="chip" type="button" aria-pressed="true">All</button>
  <button class="chip" type="button" aria-pressed="false">Prints</button>
  <button class="chip" type="button" aria-pressed="false">Tailoring</button>
</fieldset>
```

```css
.chips { border: 0; padding: 0; }
.chips legend { font: 500 0.8125rem var(--font-mono); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px; }
.chip {
  font: 700 0.9375rem var(--font-body);
  color: var(--ink);
  background: var(--paper);
  border: 3px solid var(--ink);
  padding: 10px 18px; min-height: 44px;
  margin: 0 8px 8px 0;
  cursor: pointer;
  transform: rotate(-1deg);
  transition: transform var(--dur-hover) var(--ease-out-quint),
              background-color var(--dur-hover) var(--ease-out-quint);
}
.chip:nth-child(odd) { transform: rotate(1deg); }
.chip:hover { transform: rotate(-3deg) scale(1.03); }
.chip[aria-pressed="true"] { background: var(--hot-pink); transform: rotate(-3deg);
                             box-shadow: 4px 4px 0 0 var(--ink); }
.chip:focus-visible { outline: 3px solid var(--cobalt); outline-offset: 3px; }
@media (prefers-reduced-motion: reduce) { .chip { transform: none; transition: none; } }
```

Selected state is communicated three ways - fill color, rotation, and shadow - plus `aria-pressed` for assistive tech, so no single channel (including motion) is load-bearing.

---

## 6. Failure modes & fixes

### 6.1 - Body text on pattern

```css
/* BROKEN: prose directly on stripes - contrast is a coin flip per pixel */
.section { background: var(--pat-stripes); }
.section p { color: var(--ink); }

/* FIXED: the island carries the reading, the band carries the energy */
.section { background: var(--pat-stripes); padding: 48px 24px; }
.section .island { background: var(--paper); border: 3px solid var(--ink); padding: 24px; max-width: 65ch; }
```

### 6.2 - Six fonts, no jobs (voice-swap)

```css
/* BROKEN: hierarchy dissolves into font soup */
h1 { font-family: "FontA"; } h2 { font-family: "FontB"; }
h3 { font-family: "FontC"; } p { font-family: "FontD"; } span { font-family: "FontE"; }

/* FIXED: three voices with permanent jobs */
h1, h2 { font-family: var(--font-display); }   /* display speaks   */
p, .btn, nav a { font-family: var(--font-body); } /* workhorse acts */
.mono-label, time { font-family: var(--font-mono); } /* annotator labels */
```

### 6.3 - Vibrating palette (no anchor)

```css
/* BROKEN: every block saturated, nothing to rest on - the page hums */
.b1 { background: var(--hot-pink); } .b2 { background: var(--sun); }
.b3 { background: var(--cobalt); } .b4 { background: var(--leaf); }

/* FIXED: anchor covers ≥50%; hues occupy their roles against it */
body { background: var(--paper); }             /* the anchor           */
.b-cta { background: var(--hot-pink); }        /* one primary action   */
.b-highlight { background: var(--sun); }       /* highlights only      */
.b-cool { background: var(--cobalt); }         /* one cool zone        */
```

### 6.4 - Decoration over controls

```css
/* BROKEN: marquee and stickers render above buttons; focus rings buried */
.marquee { position: fixed; z-index: 99; }
.sticker-cloud { z-index: 50; }

/* FIXED: z-scale contract - decoration can never cross content/interactive */
.marquee { position: relative; z-index: var(--z-pattern); }
.sticker-cloud { z-index: var(--z-sticker); }
.btn, input, a { position: relative; z-index: var(--z-interactive); }
```

### 6.5 - Faded rich colors for disabled

```css
/* BROKEN: opacity fades a saturated fill to mush; text unreadable */
.btn:disabled { opacity: 0.3; }

/* FIXED: dedicated muted pair that still reads */
.btn:disabled { background: var(--muted-fill); color: var(--muted-ink); box-shadow: none; cursor: not-allowed; }
```

### 6.6 - Un-zoned density (uniform noise)

```html
<!-- BROKEN: every section is a collage; no reading zone anywhere -->
<section class="collage">…</section>
<section class="collage">…</section>
<section class="collage">…</section>

<!-- FIXED: alternate density zones; body copy gets islands and calm spacing -->
<section class="collage">…</section>        <!-- loud -->
<section class="prose-band"><div class="island">…</div></section>  <!-- calm -->
<section class="collage">…</section>        <!-- loud -->
```

### 6.7 - Rotated body text

```css
/* BROKEN: reading text rotated for "energy" - reading speed tanks, a11y worse */
.island p { transform: rotate(-4deg); }

/* FIXED: rotation is a display-voice privilege only */
.hero__title { transform: rotate(-2deg); }   /* display text: fine  */
.island p { transform: none; }               /* body text: never    */
```
