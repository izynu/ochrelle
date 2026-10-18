# Hand Drawn - Implementation Examples

A complete, original, runnable component set in semantic HTML + CSS with tokens. Follows [style-guide.md](style-guide.md).

---

## 1. Tokens

```css
:root {
  /* Color */
  --paper: #FFFCF2;     /* 12.8:1 with ink */
  --card: #FFEFD9;      /* 11.7:1 with ink */
  --highlight: #FFE45C; /* 10.3:1 with ink */
  --leaf: #B9E4A8;      /* 9.2:1 with ink */
  --sky: #8FC7F2;       /* 7.3:1 with ink */
  --coral: #FF8A75;     /* 5.7:1 with ink - large text/graphics only */
  --ink: #33302A;
  --ink-soft: #5A544A;  /* 7.3:1 on paper */
  --error: #8A2E1F;     /* 8.2:1 on paper */
  --success: #1F5C3D;   /* 7.7:1 on paper */

  /* Structure */
  --bw: 3px;
  --radius-wobble: 255px 15px 225px 15px / 15px 225px 15px 255px;
  --radius-chip: 125px 10px 120px 10px / 10px 120px 10px 125px;

  /* Type */
  --font-body: "Comic Neue", "Trebuchet MS", "Segoe UI", sans-serif;
  --font-hand: "Caveat", "Patrick Hand", "Segoe Print", cursive;

  /* Space */
  --s1: 8px; --s2: 16px; --s3: 24px; --s4: 40px; --s5: 64px;

  /* Motion */
  --dur: 200ms;
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
}
```

## 2. Component set (HTML)

```html
<header class="site-nav">
  <a class="brand" href="/">Sketchpad</a>
  <nav aria-label="Primary">
    <a href="/lessons">Lessons</a>
    <a href="/practice" aria-current="page">Practice</a>
    <a href="/notes">Notes</a>
  </nav>
</header>

<main>
  <h1 class="display">Let's draw <mark>today's lesson</mark></h1>

  <section class="card" aria-labelledby="tip-h">
    <h2 id="tip-h">Warm-up sketch</h2>
    <p>Draw three boxes and connect them with arrows. <mark>Any order counts.</mark></p>
    <button class="btn" type="button">Start sketching</button>
  </section>

  <form class="signup" novalidate>
    <div class="field">
      <label for="name">Your name</label>
      <input id="name" name="name" type="text" autocomplete="name" required>
      <p class="field-hint" id="name-hint">first name is fine</p>
    </div>
    <p class="field-error" id="name-error" hidden>Please write a name first.</p>
    <button class="btn" type="submit">Save my sketchbook</button>
  </form>
</main>
```

## 3. Component set (CSS)

```css
* { box-sizing: border-box; margin: 0; }
body {
  background:
    repeating-linear-gradient(0deg, transparent 0 31px, rgba(51, 48, 42, 0.06) 31px 32px),
    var(--paper);
  color: var(--ink);
  font: 500 17px/1.6 var(--font-body);
}

/* Nav: folder tabs */
.site-nav { display: flex; align-items: center; gap: var(--s2); padding: var(--s2) var(--s3); }
.brand { font: 800 1.35rem var(--font-body); color: var(--ink); text-decoration: none; transform: rotate(-1deg); }
.site-nav nav { display: flex; gap: var(--s1); margin-left: auto; }
.site-nav nav a {
  color: var(--ink);
  text-decoration: none;
  font-weight: 700;
  padding: 10px 18px;
  border: var(--bw) solid var(--ink);
  border-bottom-width: 0;
  border-radius: 14px 14px 0 0;
  background: var(--card);
  transform: translateY(4px);
}
.site-nav nav a[aria-current="page"] { background: var(--highlight); transform: translateY(2px); }
.site-nav nav a:hover { background: var(--leaf); }
.site-nav a:focus-visible { outline: 3px dashed var(--ink); outline-offset: 4px; }

/* Display heading with marker highlight */
.display { font-size: clamp(2rem, 5vw, 3.25rem); line-height: 1.15; font-weight: 800; margin: var(--s3) var(--s3) 0; }
mark { background: var(--highlight); color: var(--ink); padding: 0 6px; border-radius: 6px 10px 8px 12px; }

/* Card with tape strip */
.card {
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius-wobble);
  background: var(--card);
  padding: var(--s3);
  margin: var(--s3);
  max-width: 34rem;
  position: relative;
  transform: rotate(-0.5deg);
}
.card::before {
  content: "";
  position: absolute;
  top: -12px; left: 32px;
  width: 88px; height: 24px;
  background: rgba(143, 199, 242, 0.55);
  border: 1px solid rgba(51, 48, 42, 0.2);
  transform: rotate(-3deg);
}
.card h2 { font-size: 1.5rem; font-weight: 700; }
.card p { margin: var(--s1) 0 var(--s2); }

/* Button */
.btn {
  font: 700 1rem var(--font-body);
  color: var(--ink);
  background: var(--highlight);
  border: var(--bw) solid var(--ink);
  border-radius: var(--radius-chip);
  padding: 12px 24px;
  min-height: 48px;
  cursor: pointer;
  box-shadow: 0 2px 0 rgba(51, 48, 42, 0.15);
  transition: transform var(--dur) var(--ease-out);
}
.btn:hover { transform: rotate(-1deg) translateY(-2px); }
.btn:active { transform: translateY(1px); box-shadow: none; }
.btn:focus-visible { outline: 3px dashed var(--ink); outline-offset: 4px; }

/* Ruled-line form */
.signup { margin: var(--s4) var(--s3); max-width: 34rem; display: grid; gap: var(--s2); justify-items: start; }
.field { width: 100%; }
.field label { font-weight: 700; display: block; margin-bottom: 4px; }
.field input {
  font: 500 17px var(--font-body);
  color: var(--ink);
  background: transparent;
  border: 0;
  border-bottom: 2px solid var(--ink);
  padding: 8px 4px;
  width: 100%;
}
.field input:focus-visible { outline: 3px dashed var(--ink); outline-offset: 4px; }
.field-hint { font: 400 1.3rem var(--font-hand); color: var(--ink-soft); margin-top: 4px; }
.field-error { color: var(--error); font-weight: 700; }
.signup input[aria-invalid="true"] { border-bottom: 3px solid var(--error); }

@media (max-width: 767px) {
  .site-nav { flex-wrap: wrap; }
  .site-nav nav { margin-left: 0; width: 100%; }
  .card, .signup, .display { margin-inline: var(--s2); }
}
```

## 4. Advanced recipe A - flashcard quiz with real answer states

Three-choice flashcard: selecting an answer locks the card, draws the check/cross, and shows an encouraging note. Fully keyboard operable via real radios; feedback is glyph + word + color.

```html
<section class="card quiz" aria-labelledby="q1-h">
  <h2 id="q1-h">Question 3 of 10</h2>
  <p class="quiz-q">Which one is a <strong>wobbly border</strong> token?</p>
  <fieldset class="quiz-choices">
    <legend class="visually-hidden">Choose one answer</legend>
    <label class="choice"><input type="radio" name="q3" value="a"> border-radius: 4px</label>
    <label class="choice"><input type="radio" name="q3" value="b"> 255px 15px 225px 15px / 15px 225px 15px 255px</label>
    <label class="choice"><input type="radio" name="q3" value="c"> border-radius: 50%</label>
  </fieldset>
  <p class="quiz-verdict" id="q3-verdict" role="status"></p>
  <p class="quiz-note" id="q3-note" aria-hidden="true"></p>
</section>
```

```css
.quiz-choices { border: 0; padding: 0; margin: var(--s2) 0; display: grid; gap: var(--s1); }
.choice {
  display: flex; align-items: center; gap: var(--s1);
  border: 2px solid var(--ink);
  border-radius: var(--radius-chip);
  padding: 12px 16px;
  cursor: pointer;
  background: var(--paper);
  font-weight: 500;
}
.choice:hover { background: var(--sky); }
.choice input { accent-color: var(--ink); width: 20px; height: 20px; }
.choice input:focus-visible { outline: 3px dashed var(--ink); outline-offset: 3px; }
.choice.is-correct { background: var(--leaf); font-weight: 700; }
.choice.is-wrong { background: var(--coral); text-decoration: line-through 2px var(--error); }
.quiz-verdict { font-weight: 700; min-height: 1.5em; }
.quiz-verdict.ok { color: var(--success); }
.quiz-verdict.bad { color: var(--error); }
.quiz-note { font: 400 1.4rem var(--font-hand); color: var(--ink-soft); }
.visually-hidden {
  position: absolute; width: 1px; height: 1px;
  clip-path: inset(50%); overflow: hidden; white-space: nowrap;
}
```

```js
(() => {
  const form = document.querySelector(".quiz");
  const choices = Array.from(form.querySelectorAll(".choice"));
  const verdict = document.getElementById("q3-verdict");
  const note = document.getElementById("q3-note");
  const ANSWER = "b";

  choices.forEach((choice) => {
    choice.addEventListener("change", () => {
      const input = choice.querySelector("input");
      if (input.checked) {
        const correct = input.value === ANSWER;
        choice.classList.add(correct ? "is-correct" : "is-wrong");
        verdict.textContent = correct ? "Correct! Nice line work." : "Not quite. Look again at the numbers.";
        verdict.classList.add(correct ? "ok" : "bad");
        note.textContent = correct ? "that one wobbles just right" : "hint: the wobble lives in the huge first value";
        choices.forEach((c) => { if (c !== choice) { c.querySelector("input").disabled = true; } });
      }
    });
  });
})();
```

## 5. Advanced recipe B - annotated hero with doodle arrows and draw-in underline

A hero where the eyebrow is handwriting, the key phrase gets a marker highlight, and an SVG arrow draws in once (then sits still). The arrow is decorative and points at the CTA.

```html
<header class="hero">
  <p class="hero-eyebrow" aria-hidden="true">step one: this way</p>
  <h1 class="hero-title">Big ideas,<br><span class="hero-mark">small sketches</span></h1>
  <p class="hero-sub">A notebook that plans, teaches, and nudges - drawn by hand, built with care.</p>
  <a class="btn hero-cta" href="/start">Start your sketchbook</a>
  <svg class="hero-arrow" viewBox="0 0 120 60" width="120" height="60" aria-hidden="true" focusable="false">
    <path d="M8 10 C 40 8, 78 22, 100 42 M 100 42 l -14 -3 M 100 42 l 2 -13"
          fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
  </svg>
</header>
```

```css
.hero { padding: var(--s4) var(--s3); max-width: 46rem; position: relative; }
.hero-eyebrow { font: 400 1.6rem var(--font-hand); color: var(--ink-soft); transform: rotate(-1deg); }
.hero-title { font-size: clamp(2.25rem, 6vw, 3.75rem); line-height: 1.08; font-weight: 800; margin: var(--s1) 0; }
.hero-mark {
  background: linear-gradient(104deg, transparent 2%, var(--highlight) 6%, var(--highlight) 94%, transparent 98%);
  padding: 0 8px;
  border-radius: 8px 14px 10px 16px;
}
.hero-sub { color: var(--ink-soft); max-width: 42ch; margin-bottom: var(--s2); }
.hero-cta { display: inline-block; text-decoration: none; }
.hero-arrow { position: absolute; right: 12%; top: 58%; color: var(--ink); }
.hero-arrow path { stroke-dasharray: 260; stroke-dashoffset: 260; animation: draw 600ms ease-out 300ms forwards; }
@keyframes draw { to { stroke-dashoffset: 0; } }
@media (max-width: 767px) { .hero-arrow { display: none; } }
@media (prefers-reduced-motion: reduce) {
  .hero-arrow path { animation: none; stroke-dashoffset: 0; }
  .btn, .hero-cta { transition: none; }
  .btn:hover { transform: none; }
}
```

## 6. Failure modes & fixes

**Broken: handwriting as body copy.**
```css
.card p { font: 400 1rem var(--font-hand); } /* script at 16px: unreadable and untranslatable */
```
```css
.card p { font: 500 1.0625rem var(--font-body); }
.card .note { font: 400 1.35rem var(--font-hand); } /* accents only, larger */
```

**Broken: random radii everywhere.**
```css
.card { border-radius: 30px 60px 10px 200px; }
.btn { border-radius: 12px; } /* two unrelated curves, reads as bugs */
```
```css
.card, .btn { border-radius: var(--radius-wobble); }
.chip { border-radius: var(--radius-chip); } /* one token per scale */
```

**Broken: light text on marker fills.**
```css
.btn { background: var(--coral); color: #fff; } /* white on coral ~2.5:1 */
```
```css
.btn { background: var(--highlight); color: var(--ink); } /* ink on marker 10.3:1 */
```

**Broken: color-only quiz feedback.**
```css
.choice.is-correct { background: var(--leaf); } /* meaning carried by hue alone */
```
```css
.choice.is-correct { background: var(--leaf); font-weight: 700; }
.quiz-verdict::before { content: "\2713 "; } /* glyph + text word + color */
```

**Broken: doodles that never stop moving.**
```css
.hero-arrow { animation: bob 2s infinite; } /* loops forever, fights reading */
```
```css
.hero-arrow path { animation: draw 600ms ease-out 300ms forwards; } /* once, then still */
@media (prefers-reduced-motion: reduce) { .hero-arrow path { animation: none; stroke-dashoffset: 0; } }
```

**Broken: sketchy focus rings removed to look tidy.**
```css
.btn:focus { outline: none; } /* keyboard users lost */
```
```css
.btn:focus-visible { outline: 3px dashed var(--ink); outline-offset: 4px; } /* sketchy AND 12.8:1 */
```
