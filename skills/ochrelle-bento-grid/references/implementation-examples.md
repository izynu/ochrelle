# Bento Grid - Implementation Examples

Reference for the `ochrelle-bento-grid` skill. Both examples are complete and
runnable: save the HTML and CSS into one page and open it in a browser. Sample
values (names, numbers) are illustrative placeholders for real data - replace
them with actual content in production.

---

## 1. Example A - analytics dashboard (9 tiles, 12-column grid)

### 1.1 Content plan and sizing justification

| # | Tile | Content priority | Desktop span | Justification (sizing test) |
| --- | --- | --- | --- | --- |
| 1 | Revenue overview | 1 - the reason users open the page | 6 cols × 2 rows | Hero metric plus trend; largest area earns the primary question. |
| 2 | Active users | 2 | 3 × 1 | Secondary KPI; one number plus delta. |
| 3 | Conversion | 2 | 3 × 1 | Peer of Active users - equal size, paired. |
| 4 | Traffic chart | 3 | 6 × 1 | Supporting trend below hero detail level. |
| 5 | Recent activity | 4 | 4 × 2 | List needs height for scanning, not width. |
| 6 | Top products | 4 | 4 × 2 | Peer of Recent activity - equal size, same row pair. |
| 7 | Storage used | 5 | 2 × 1 | Atomic fact. |
| 8 | Team seats | 5 | 2 × 1 | Atomic fact, paired with Storage. |
| 9 | System status | 6 | 4 × 1 | Composed of several atomic facts; tertiary. |

DOM order equals the desktop reading order (rows, left to right): 1, 2, 3, 4,
5, 6, 7, 8, 9.

### 1.2 HTML

```html
<section class="bento" aria-label="Overview dashboard">
  <article class="tile tile--revenue">
    <header class="tile__header">
      <h2>Revenue</h2>
      <p class="tile__meta">Last 30 days</p>
    </header>
    <div class="tile__content">
      <p class="tile__metric">$248,910</p>
      <p class="tile__delta">▲ 8.2% vs prior 30 days</p>
    </div>
    <footer class="tile__footer">
      <a href="/reports/revenue">View revenue report</a>
    </footer>
  </article>

  <article class="tile tile--users">
    <header class="tile__header"><h2>Active users</h2></header>
    <div class="tile__content">
      <p class="tile__metric">12,408</p>
      <p class="tile__delta">▲ 3.1% WoW</p>
    </div>
  </article>

  <article class="tile tile--conversion">
    <header class="tile__header"><h2>Conversion</h2></header>
    <div class="tile__content">
      <p class="tile__metric">4.6%</p>
      <p class="tile__delta tile__delta--down">▼ 0.3 pts WoW</p>
    </div>
  </article>

  <article class="tile tile--traffic">
    <header class="tile__header">
      <h2>Traffic</h2>
      <p class="tile__meta">Sessions per day</p>
    </header>
    <div class="tile__content">
      <!-- replace with your real chart component; reserve its height -->
      <div class="chart-slot" role="img" aria-label="Line chart of daily sessions, trending up over 30 days"></div>
    </div>
  </article>

  <article class="tile tile--activity">
    <header class="tile__header"><h2>Recent activity</h2></header>
    <div class="tile__content">
      <ul class="feed">
        <li>Invoice #1042 paid - 2m ago</li>
        <li>New customer: Meridian Labs - 18m ago</li>
        <li>Refund issued for order #881 - 1h ago</li>
      </ul>
    </div>
    <footer class="tile__footer"><a href="/activity">All activity</a></footer>
  </article>

  <article class="tile tile--products">
    <header class="tile__header"><h2>Top products</h2></header>
    <div class="tile__content">
      <ol class="ranked">
        <li><span>Atlas plan</span><span>41%</span></li>
        <li><span>Beacon add-on</span><span>27%</span></li>
        <li><span>Compass seats</span><span>19%</span></li>
      </ol>
    </div>
  </article>

  <article class="tile tile--storage">
    <header class="tile__header"><h2>Storage</h2></header>
    <div class="tile__content">
      <p class="tile__metric">612 GB</p>
      <p class="tile__meta">of 1 TB</p>
    </div>
  </article>

  <article class="tile tile--team">
    <header class="tile__header"><h2>Team seats</h2></header>
    <div class="tile__content">
      <p class="tile__metric">14 / 20</p>
      <p class="tile__meta">seats in use</p>
    </div>
  </article>

  <article class="tile tile--status">
    <header class="tile__header"><h2>System status</h2></header>
    <div class="tile__content">
      <ul class="status-list">
        <li><span class="dot" aria-hidden="true"></span>API - operational</li>
        <li><span class="dot" aria-hidden="true"></span>Dashboard - operational</li>
        <li><span class="dot dot--warn" aria-hidden="true"></span>Exports - degraded</li>
      </ul>
    </div>
  </article>
</section>
```

Accessibility details baked in:

- Each tile is an `<article>` with exactly one `<h2>`; the section is labeled.
- Status meaning is **not color-only**: the dot is decorative (`aria-hidden`),
  and the text carries the state ("operational", "degraded").
- The chart slot carries a text alternative; swap in your chart with an
  accessible name and, where feasible, a data table alternative.
- All interactive elements are real `<a>` elements inside the DOM flow.

### 1.3 CSS - desktop (≥ 1025 px): 12 columns, span classes

```css
.bento {
  --bento-gap: 16px;
  --bento-radius: 20px;
  --tile-pad: 24px;

  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-auto-rows: minmax(140px, auto);
  grid-auto-flow: row;          /* never 'dense': it would break reading order */
  gap: var(--bento-gap);
  max-width: 1200px;
  margin-inline: auto;
}

.tile {
  padding: var(--tile-pad);
  border-radius: var(--bento-radius);
  background: #ffffff;
  border: 1px solid #e5e5ea;
  min-width: 0;                 /* lets inner content shrink instead of overflowing */
}

/* Desktop span classes (see sizing table in section 1.1) */
.tile--revenue    { grid-column: span 6; grid-row: span 2; }
.tile--users      { grid-column: span 3; }
.tile--conversion { grid-column: span 3; }
.tile--traffic    { grid-column: span 6; }
.tile--activity   { grid-column: span 4; grid-row: span 2; }
.tile--products   { grid-column: span 4; grid-row: span 2; }
.tile--storage    { grid-column: span 2; }
.tile--team       { grid-column: span 2; }
.tile--status     { grid-column: span 4; }
```

Auto-placement check (12 columns): Revenue fills cols 1–6, rows 1–2; Users and
Conversion complete row 1 (cols 7–9, 10–12); Traffic fills row 2 (cols 7–12);
Activity (cols 1–4) and Top products (cols 5–8) span rows 3–4; Storage (cols
9–10) and Team (cols 11–12) fill row 3; Status fills row 4 (cols 9–12). The
rectangle is complete - no holes, no dense flow needed, and the DOM order
matches the visual scan exactly.

### 1.4 CSS - tablet (769–1024 px): 6 columns via `grid-template-areas`

Named areas give exact placement and keep the reading order under explicit
control at this breakpoint:

```css
@media (max-width: 1024px) {
  .bento {
    grid-template-columns: repeat(6, 1fr);
    grid-auto-rows: minmax(120px, auto);
    grid-template-areas:
      "revenue  revenue  revenue  revenue  revenue  revenue"
      "users    users    users    conversion conversion conversion"
      "traffic  traffic  traffic  traffic  traffic  traffic"
      "activity activity activity products products products"
      "activity activity activity products products products"
      "storage  storage  storage  status   status   status"
      "team     team     team     team     team     team";
  }
  .tile--revenue    { grid-area: revenue;    grid-column: auto; grid-row: auto; }
  .tile--users      { grid-area: users;      grid-column: auto; grid-row: auto; }
  .tile--conversion { grid-area: conversion; grid-column: auto; grid-row: auto; }
  .tile--traffic    { grid-area: traffic;    grid-column: auto; grid-row: auto; }
  .tile--activity   { grid-area: activity;   grid-column: auto; grid-row: auto; }
  .tile--products   { grid-area: products;   grid-column: auto; grid-row: auto; }
  .tile--storage    { grid-area: storage;    grid-column: auto; grid-row: auto; }
  .tile--team       { grid-area: team;       grid-column: auto; grid-row: auto; }
  .tile--status     { grid-area: status;     grid-column: auto; grid-row: auto; }
}
```

Reflow decisions at this breakpoint: the hero keeps a full row; the two KPIs
stay paired; the two list tiles stay paired at two rows high; the two atomic
tiles (Storage, Status) are grouped, and Team becomes a full-width strip
because it no longer has a natural partner.

### 1.5 CSS - mobile (≤ 768 px): 2 columns

```css
@media (max-width: 768px) {
  .bento {
    grid-template-columns: repeat(2, 1fr);
    grid-auto-rows: minmax(96px, auto);
    grid-template-areas:
      "revenue  revenue"
      "users    conversion"
      "traffic  traffic"
      "activity activity"
      "products products"
      "storage  team"
      "status   status";
  }
}

@media (max-width: 480px) {
  .bento {
    --bento-gap: 12px;   /* tightens without changing structure */
  }
  .tile { --tile-pad: 16px; }
}
```

Reflow decisions at this breakpoint: only tiles that are genuinely paired at
equal priority share a row (Users/Conversion, Storage/Team); everything else
goes full width so no tile drops below a comfortable reading measure. The
2-column grid with full-width tiles also satisfies WCAG 1.4.10 reflow at 320 px
width.

### 1.6 Keyboard tab order

Because the DOM order matches the desktop reading order and `grid-auto-flow`
is plain `row` (never `dense`), the Tab order through the three links
(Revenue report → All activity, plus any links you add) follows the same
logical sequence as the visual scan. Verify by tabbing through the page: the
focus outline should move in reading order, top-left to bottom-right on
desktop. Do not "fix" a wrong Tab order with `tabindex` - fix the DOM order.

---

## 2. Example B - marketing feature grid (7 tiles, 4-column grid)

For a product overview page. Same principles, smaller grid, one skin
(minimalist) applied.

### 2.1 Content plan

| # | Tile | Priority | Area | Justification |
| --- | --- | --- | --- | --- |
| 1 | Hero feature | 1 | `hero` (2×2) | The capability that sells the product; earns image + copy. |
| 2–3 | Supporting features | 2 | `f1`, `f2` (1×1) | Peer capabilities, equal weight. |
| 4 | Customer quote | 3 | `quote` (2×1) | Proof; wide but short. |
| 5 | Supporting feature | 2 | `f3` (1×1) | Peer of f1/f2. |
| 6 | CTA | action | `cta` (2×1) | Single conversion action; visually distinct. |
| 7 | Supporting feature | 2 | `f4` (1×1) | Peer of f1/f2. |

### 2.2 HTML (abridged tiles, complete structure)

```html
<section class="bento-marketing" aria-label="What the product does">
  <article class="mtile mtile--hero">
    <h2>Scheduled reporting that writes itself</h2>
    <p>Describe the report once; it refreshes on your cadence and lands in the
       inboxes you choose.</p>
    <img src="/img/hero-feature.png" alt="Report builder showing a weekly revenue report being scheduled" width="800" height="500">
  </article>

  <article class="mtile mtile--f1"><h3>Live dashboards</h3><p>Metrics update as data lands.</p></article>
  <article class="mtile mtile--f2"><h3>Alerting</h3><p>Thresholds that page a human.</p></article>

  <figure class="mtile mtile--quote">
    <blockquote><p>We replaced three spreadsheets with one schedule.</p></blockquote>
    <figcaption>Example attribution line</figcaption>
  </figure>

  <article class="mtile mtile--f3"><h3>Exports</h3><p>CSV, Sheets, warehouse sync.</p></article>

  <div class="mtile mtile--cta">
    <a class="cta" href="/signup">Start free</a>
    <p class="mtile__meta">No credit card required</p>
  </div>

  <article class="mtile mtile--f4"><h3>Access control</h3><p>Reports scoped per team.</p></article>
</section>
```

Note on the quote: it is sample copy demonstrating tile structure, not a claim
about a real customer. Never ship invented testimonials - use a real one or
remove the tile (and re-run the sizing test).

### 2.3 CSS - all breakpoints via named areas

```css
.bento-marketing {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(160px, auto);
  gap: 20px;
  grid-template-areas:
    "hero hero f1    f2"
    "hero hero quote quote"
    "f3   cta  cta   f4";
}

.mtile        { padding: 24px; border-radius: 20px; background: #fff; border: 1px solid #e5e5ea; min-width: 0; }
.mtile--hero  { grid-area: hero; }
.mtile--f1    { grid-area: f1; }
.mtile--f2    { grid-area: f2; }
.mtile--quote { grid-area: quote; }
.mtile--f3    { grid-area: f3; }
.mtile--cta   { grid-area: cta; display: grid; place-content: center; justify-items: center; }
.mtile--f4    { grid-area: f4; }

@media (max-width: 768px) {
  .bento-marketing {
    grid-template-columns: 1fr;
    grid-template-areas:
      "hero" "f1" "f2" "quote" "f3" "cta" "f4";
  }
}
```

Reading order note: the DOM order (hero → f1 → f2 → quote → f3 → cta → f4)
matches the desktop visual scan row by row, and the single-column mobile stack
preserves it. The CTA is intentionally the penultimate stop on mobile: the page
earns the click before asking for it.

---

## 3. Reading-order rules (both examples)

1. **Write the HTML in reading order.** Grid placement changes what users see
   first per breakpoint; the DOM order is the one canonical order that screen
   readers, search engines, and (mostly) Tab follow.
2. **Never use `grid-auto-flow: dense`, the `order` property, or negative grid
   lines to "fix" placement at the cost of order.** If placement and order
   conflict, the content plan is wrong - fix the plan.
3. **Acceptable exception:** a footer cluster whose tiles swap positions
   between breakpoints is tolerable when all swapped tiles belong to the same
   informational group and no interactive flow depends on their sequence.
   Audit it with the tab-through test; when in doubt, keep strict parity.
4. **Interactive tiles:** if the whole tile is one action, make the tile's
   link the real element and keep its label meaningful ("View revenue report",
   not "Read more" five times). Keep `:focus-visible` styles:
   `outline: 2px solid currentColor; outline-offset: 2px;`

## 4. Layout-shift and loading notes

- Reserve space for charts and images inside tiles (`aspect-ratio`,
  `width`/`height` attributes, or a fixed-height slot) so late-loading media
  does not push tiles and shift rows (CLS).
- Let `grid-auto-rows: minmax(N, auto)` absorb the last word: if content grows
  one row taller, the whole row grows - that is graceful; content clipped by a
  fixed height is not.
