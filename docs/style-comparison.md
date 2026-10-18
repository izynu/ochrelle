# Ochrelle Style Comparison

All 27 Ochrelle specialist skills side by side. The point of this table is to
force the right question before implementation: **is this a look, an
organization, a behavior, a period revival, a staged world, or a platform
material?** Combining across rows is
normal (a minimalist bento dashboard); collapsing rows into one aesthetic is
how designs become incoherent.

- **Accessibility risk** describes the style's inherent hazard level *when
  implemented carelessly* - every Ochrelle skill targets WCAG 2.2 AA regardless.
- **Performance cost** describes typical web implementations; platform-native
  rendering can shift it.

## Comparison table

| Skill | Type | Core materials | Best for (products) | Avoid for | Accessibility risk (why) | Performance cost | Key CSS/JS techniques | Combos that work |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ochrelle-skeuomorphism** | Visual style | Rendered textures, gradients, bevels, highlights, realistic lighting | Music players, instrument panels, retro games, learning apps for physical controls | Dense data tools, minimal brands, anything needing fast scanning | **Medium** - ornament can obscure affordances; heavy imagery vs. contrast | **High** - many layered gradients/shadows, textures | Multi-stop gradients, inset/outset `box-shadow`, texture layers, pseudo-element highlights | + bento grid (control panels); + claymorphism-lite |
| **ochrelle-neumorphism** | Visual style | Monochrome surfaces, dual soft shadows (light + dark), extruded/inset forms | Smart-home controls, fitness rings, settings screens with few controls | Text-heavy pages, high-stakes forms, colorful brands | **High** - low-contrast tonal boundaries hide state and edges | **Medium** - two shadows on many elements, but cheap paint | Dual `box-shadow`, single-hue palette, `border-radius` scale, pressed/inset states | + minimalism (same restraint); avoid + glass (mud) |
| **ochrelle-glassmorphism** | Visual style | Translucent fills, `backdrop-filter` blur, 1 px light borders, layered depth | Media overlays, floating toolbars, hero panels over rich imagery | Forms, long reading, busy low-end devices | **High** - contrast depends on what is behind the blur | **High** - backdrop-filter is a per-frame GPU cost on area | `backdrop-filter: blur() saturate()`, rgba fills, `@supports` fallbacks, stacking contexts | + spatial UI (floating panels); + bento grid (tiles) |
| **ochrelle-claymorphism** | Visual style | Soft volumetric fills, large radii, inner highlights, diffused shadows | Kids' products, habit trackers, playful onboarding | Enterprise tools, dense dashboards, serious trust contexts | **Medium** - pastel palettes drift below contrast minimums | **Medium** - layered shadows, occasional blur | Layered soft `box-shadow`, inner highlight shadows, 24–40 px radii | + bento grid (playful hubs); + maximalism-lite |
| **ochrelle-brutalism** | Visual style | Flat fills, hard borders, offset shadows, raw type (often mono) | Zines, event pages, dev-tool brands, portfolios with attitude | Banking, healthcare, accessibility-first defaults without care | **Medium** - deliberate harshness breaks conventions; focus states must be re-earned | **Low** - flat color, no blur | 2–3 px solid borders, hard offset `box-shadow`, `border-radius: 0`, loud `:focus-visible` | + maximalism (carefully); + bento grid (editorial) |
| **ochrelle-minimalism** | Visual style | Whitespace, 1 px rules, restrained palette, strong type scale | Reading products, SaaS defaults, premium brands, docs | Brands needing maximal expressiveness (it will look "empty" to them) | **Low** - the discipline *is* accessibility; residual risk is gray-on-gray text and missing affordances | **Low** - almost nothing to render | Type scale + measure, spacing tokens, 1 px borders, progressive disclosure | + bento grid (dashboards); + spatial UI (restraint) |
| **ochrelle-maximalism** | Visual style | Layered pattern, rich color, mixed type, collage, texture | Fashion, music/festival, culture brands, editorial features | Tools users live in for hours; UI chrome | **High** - competing colors/textures threaten legibility | **High** - large imagery, many layers | Layered backgrounds, `mix-blend-mode`, rotated/repeating elements, disciplined type system underneath | + brutalism (zine energy); keep chrome minimal |
| **ochrelle-liquid-glass** | Platform material | The platform's own translucent material system (Apple-documented), specular/adaptive behavior on device | Native apps on platforms shipping it; UI that must match system chrome | Pretending CSS blur reproduces it; thin-content screens that gain nothing | **High** - translucency over changing content; platform rules evolve | **High** (web approximations) - same class of cost as glassmorphism | On-device: system materials. Web: honest approximations (`backdrop-filter`) labeled as approximations | + spatial UI; + minimalism (let the material star) |
| **ochrelle-bento-grid** | Layout pattern | CSS Grid tiles, gaps, radii - visual skin is a free variable | Dashboards, feature overviews, portfolio/about pages, settings hubs | Linear narrative, long-form reading, one-CTA marketing pages | **Low** - structure aids scanning; risks are order breaks and tile overflow | **Low** - pure CSS Grid | `grid-template-columns: repeat(12, 1fr)`, span classes, `grid-auto-rows: minmax()`, `grid-template-areas` reflow | + minimalism, + glass, + brutalism, + claymorphism (any skin) |
| **ochrelle-spatial-ui** | Interaction paradigm | Depth systems, perspective, layered transforms, platform windows/materials on headset | Product showcases, 3D data viz, immersive brand moments, visionOS-style apps | Reading, forms, checkout, accessibility-critical paths | **High** - gaze ≠ pointer, motion discomfort, text-on-3D contrast | **High** - 3D scenes; medium for 2D parallax variant | `perspective`, `translateZ`, rAF-throttled pointer parallax, transform/opacity-only animation, reduced-motion gates | + glassmorphism/liquid-glass (panels); + minimalism; + bento grid (flat shell) |
| **ochrelle-flat-design** | Visual style | Solid color fills, simple geometry, type-driven hierarchy; no shadows, no gradients | SaaS dashboards, admin panels, settings, docs, unopinionated marketing skins | Luxury or hospitality brands, atmosphere-led youth products, weak single-accent palettes | **Low-medium** - few effects to hide behind, but bright Flat-UI fills tempt white-on-color failures | **Low** - paint-cheap fills, no blur | Tokenized role fills, 2px form borders, one hairline-shadow token for floating layers, instant state swaps | + bento grid (dashboards); + corporate-memphis (illustration systems) |
| **ochrelle-material-design** | Visual style | Elevation model with z-level shadows, state layers, ripple feedback, Material You dynamic color | Android apps, Google-ecosystem products, card/chip-heavy structured SaaS | Anti-corporate or expressive brands, atmosphere-first landing pages, tiny brochure sites | **Low** - battle-tested AA component pairs; dynamic-color seeds need pair-by-pair checks | **Low-medium** - elevation shadows and state layers are cheap paint | Elevation shadow scale, state-layer opacities, ripple animation, tonal palettes generated from a seed color | + bento grid (any skin); + corporate-memphis (big-tech illustration lineage) |
| **ochrelle-neo-brutalism** | Visual style | 2-4px solid black borders, hard offset shadows (4px 4px 0 #000), candy fills, sticker badges, chunky type | Indie products, creator/merch shops, event tickets, Gen Z-facing startups | Banking, healthcare, government; luxury; long-form reading | **Medium** - high contrast by default, but loud motion and pressed states must be re-earned | **Low** - flat fills and solid shadows, no blur | Hard offset `box-shadow`, thick solid borders, press-in active states, visible sticker/grid vocabulary | + maximalism (campaign energy); + bento grid (merch hubs) |
| **ochrelle-y2k** | Thematic genre | Translucent candy plastics, chrome and metallic gradients, gel buttons, lens flares, hi-tech silver whites | Rave and festival pages, fashion drops, Gen Z revival campaigns, playful games | Trust-critical services, dense B2B tools, dark-mode-first products, austere guidelines | **High** - silver-on-white gloss and glow-heavy text; every pair needs measuring | **Medium** - layered gradients and highlight overlays | Multi-stop chrome `linear-gradient`s, inset gel shadows, bubble-button highlights, sparkle/lens-flare layers | + vaporwave (nostalgia neighbors, different decades); keep working surfaces calm |
| **ochrelle-cyberpunk** | Thematic genre | Near-black blue-cast surfaces, sparing neon cyan/magenta/yellow, glitch slices, CRT scanlines, rain-slick mood | Games, club nights, security and developer brands, night-mode portfolios | Healthcare, finance, government, kids' products; calm corporate SaaS | **High** - dark grounds and neon glow tempt contrast failures; measure with glow off | **Medium** - scanline overlays and glitch animation, gated by reduced-motion | Neon accent tokens, `text-shadow` glow, clip-path glitch slices, scanline overlays | + futuristic-hud (shared diegetic chrome); keep body text solid |
| **ochrelle-retro-design** | Period aesthetic | Cream, burnt orange, mustard, avocado, brown; Googie starbursts, halftone dots, badge seals, groovy display type | Cafes, diners, breweries, vinyl stores, food packaging, event posters | Fintech/health/government, data-dense dashboards, luxury, dark-mode dev tools | **Low-medium** - warm mid-tones need ink labels; badge text must hold 4.5:1 | **Low** - flat color and simple shapes; starbursts are clip-path | `clip-path` starbursts, halftone `radial-gradient` dots, badge stamps, 2px rules, tracked display type | + hand-drawn (warm indie craft brands) |
| **ochrelle-editorial-design** | Visual style | Dominant headline type, decks, kickers, pull quotes, drop caps, baseline-grid rhythm, asymmetric grids | Blogs, digital magazines, essays, press pages, story-driven marketing | Dashboards, checkout flows, youth-culture drops, motion-heavy campaign pages | **Low** - disciplined 60-75ch measure and strong hierarchy are access-positive | **Low** - typography and whitespace, almost no paint cost | `::first-letter` drop caps, baseline-grid line-height math, ch-based measure, asymmetric column grids | + minimalism (quiet chrome under loud headlines) |
| **ochrelle-memphis-design** | Period aesthetic | Squiggles, zigzags, terrazzo speckle, clashing pastels on primaries, B&W stripes, chunky black outlines | Creative tools, music and club culture, party brands, youth products, merch | Banking/insurance/healthcare, enterprise B2B dashboards, luxury, continuous reading | **Medium** - clashing fills threaten text contrast; confine patterns to non-text zones | **Medium** - repeating SVG patterns and layered shapes | Repeating `radial-gradient` terrazzo, SVG squiggle/zigzag patterns, 4-6px black borders, hard offset shadows | + maximalism (carefully); keep working surfaces calm |
| **ochrelle-japandi** | Visual style | Muted naturals (beige, clay, moss, charcoal), matte linen/wood textures, negative space, asymmetric balance | Wellness and mindfulness apps, boutique hospitality, skincare and tea brands, calm productivity | Trading/analytics dashboards, hype drops, safety-critical alerts, neon brands | **Medium** - low-contrast layering must stay AA-safe; check pairs pair-by-pair | **Low** - flat matte surfaces and hairline rules | Warm tonal tokens (clay at 5.1:1), hairline rules, asymmetric spacing, restrained 200ms motion | + minimalism (shared restraint; japandi supplies the warmth) |
| **ochrelle-frutiger-aero** | Period aesthetic | Aqua gel buttons, glass gloss, water droplets, bubbles, sky-and-grass nature imagery, humanist sans | Music players, throwback microsites, sustainability and wellness-tech branding, kiosks | Dense data tools, high-field-count forms, austere/editorial brands, long reading | **High** - gloss over variable backgrounds; translucency hard to guarantee everywhere | **High** - `backdrop-filter` plus layered highlights on glossy surfaces | `backdrop-filter` gloss, inset gel `box-shadow`s, specular `linear-gradient` shine, nature-image layers | + skeuomorphism-lite (shared shine era); text stays on solid backplates |
| **ochrelle-corporate-memphis** | Visual style | Flat vector illustration: bendy figures with tiny heads, muted-saturated fills, geometric plant props | Onboarding, HR and internal tools, empty states, community pages, friendly SaaS heroes | Premium/luxury brands, serious domains, editorial storytelling, craft-competitive products | **Low-medium** - decorative art, but figure scenes must never carry instructions alone | **Low** - inline SVG, tiny payloads, trivially themeable | Inline SVG figures, flat fills with no gradients, shared prop library, one stroke/fill system | + flat-design (illustration over a flat product shell) |
| **ochrelle-vaporwave** | Thematic genre | Roman busts, VHS glitch, Win95 chrome, katakana accents, checkerboards, pink/cyan/violet sunset gradients | Music releases, club events, streetwear drops, VJ and 3D portfolios | Enterprise/banking/health, children's products, long reading, heritage brands | **High** - dark violet grounds with saturated accents; check every pair and cap strobe effects | **Medium** - gradient skies, repeating scanlines, glitch filters | Sunset `linear-gradient`s, `repeating-linear-gradient` scanlines, chrome text, checkerboards, glitch `filter` frames | + y2k (nostalgia neighbors); + cyberpunk (night palettes) |
| **ochrelle-pixel-art** | Visual style | Limited 8-64 color palettes, crisp 1px edges, dithered shading, bitmap fonts, hard offset shadows | Games, launchers, emulation frontends, retro-gaming brands, achievement systems | Data-dense/finance/medical software, long reading, luxury, photographic content | **Medium** - bitmap fonts need size discipline; dithered areas can shimmer | **Low** - flat sprites at integer scales; CRT filters optional | `image-rendering: pixelated`, integer-multiple sizing, `steps()` motion, dither ramps instead of gradients | Scoped to one personality surface (achievement popups, empty states) inside a neutral product |
| **ochrelle-terminal-console** | Visual style | Monospace cell grid, box-drawing frames, phosphor green/amber on near-black, status bars, prompt symbols | Developer tools, log viewers, CI dashboards, API explorers, status pages | Long-form reading, consumer/luxury marketing, non-technical audiences | **Medium** - phosphor pairs must be measured; brightness-as-hierarchy needs a non-color fallback | **Low** - text and borders; blinking cursors gated by reduced-motion | Monospace grid with ch units, box-drawing characters or borders, inverse-video states, `aria-live` log regions | + minimalism (developer dashboards: terminal panel, quiet chrome) |
| **ochrelle-hand-drawn** | Visual style | Wobbly hand-inked borders, doodle arrows, paper textures, marker highlights, handwriting accents | Education platforms, kids' tools, creative apps, onboarding and how-to guides | Banking/medical/legal, dense dashboards, luxury, strict certification contexts | **Medium** - wobbly borders must still hit 3:1; focus states need explicit design | **Low** - CSS radius tricks and small SVG doodles | Asymmetric wobble `border-radius`, scribble SVG underlines, repeating paper-grid `linear-gradient`, marker highlights | + retro-design (warm indie craft brands) |
| **ochrelle-art-deco** | Period aesthetic | Stepped forms, sunburst fans, ziggurat corners, double hairlines, ivory/ink/gold with emerald, midnight, oxblood | Boutique hotels, cocktail bars, theaters, jewelry and spirits brands, gala invitations | Developer tools, fintech dashboards, kids' products, dark-mode reading | **Low** - ivory on near-black measures about 14:1; gold is reserved for large text on dark grounds | **Low** - flat geometric fills and gradients, no blur | `conic-gradient` sunbursts, stepped `linear-gradient` frames, double hairline borders, letterspaced display caps | + conventional UI (deco scoped to hero and invitation moments) |
| **ochrelle-futuristic-hud** | Thematic genre | Translucent data panels on near-black, cyan/amber instrument text, chamfered brackets, radar sweeps | Robotics/drone/IoT telemetry, sci-fi games, launch events, mission-control pages | Long reading, healthcare and safety-critical controls, checkout, kids' products | **Medium** - glow is decoration only; every text pair passes 4.5:1 with glow off | **Medium** - scanline/sweep animation with a static reduced-motion fallback | `clip-path` chamfers and corner brackets, monospace telemetry readouts, `repeating-linear-gradient` scanlines, status-color tokens | + cyberpunk (shared night chrome); body text on solid panels |

## Per-style summaries

**Skeuomorphism** renders digital controls with the visual language of their
physical ancestors - textures, bevels, highlights, and lighting that make a
knob look graspable. Done with purpose it shortens learning curves for
familiar controls; done lazily it is shadows on everything. The skill teaches
physical affordance and material consistency, and insists skeuomorphism is a
metaphor decision, not a default coat of paint.

**Neumorphism** extrudes and insets monochrome surfaces with paired light and
dark shadows, producing soft, embossed panels. Its charm is tonal calm; its
documented weakness is contrast - boundaries and states nearly disappear. The
skill teaches the correct dual-shadow technique, consistent light direction,
and the accessible fallbacks (visible borders/states) that make it usable at
all.

**Glassmorphism** builds translucent, blurred panels that let a rich
background read through them, creating depth through material rather than
through shadows alone. Its risks are exactly its mechanics: contrast becomes
background-dependent and `backdrop-filter` is expensive. The skill covers
correct blur/saturate recipes, `@supports` fallbacks, and readability testing
against the busiest background region.

**Claymorphism** rounds and volumizes: soft 3D shapes with inner highlights
and diffused shadows, friendly and toy-like without demanding photorealism.
It suits playful, low-density products and collapses under dense data or
serious contexts. The skill keeps the geometry consistent (radii, shadow
layers) while forcing the pastel palette through contrast checks.

**Brutalism** (and its neo- variant) commits to raw structure: hard borders,
flat fills, offset shadows, unapologetic type. Its power is directness and
distinctiveness; its trap is confusing "hostile to users" with "hostile to
taste". The skill separates architectural/digital/neo strains and requires
loud focus states and readable defaults underneath the attitude.

**Minimalism** is disciplined reduction: fewer elements, stronger hierarchy,
generous space, purposeful typography. It is the lowest-risk style only when
its reductions stop before removing affordances and contrast. The skill
frames minimalism as information design - what remains must carry everything
the removed elements used to.

**Maximalism** is controlled richness - layered color, pattern, imagery, and
type in compositions that feel abundant rather than noisy. It lives or dies
on the strength of the hierarchy underneath the spectacle. The skill teaches
restraint exactly where maximalists usually lose users: chrome, forms, and
reading paths stay calm while the art direction goes loud.

**Liquid Glass** is Apple's platform material language for translucent,
adaptive interface surfaces - a system capability documented by Apple, not a
CSS trick. The skill keeps the distinction honest: use platform materials on
platform; on the web, build clearly-labeled approximations and expect them to
fall short of the adaptive, specular behavior the real material exhibits.

**Bento Grid** organizes content into mixed-size, gap-separated tiles sized
by content priority - information architecture first, decoration second. It
excels wherever unequal emphasis meets scannable content and fails wherever
reading is linear. The skill teaches the grid mechanics (12/6/2-column
reflow), the sizing justification discipline, and the rule that DOM order is
reading order.

**Spatial UI** places interfaces in depth: floating system windows on headset
platforms, real 3D scenes on the web, or layered z-depth and parallax on
conventional pages. Its obligations follow its power - motion comfort,
honest platform claims, hover-alternatives, backplated text, and
transform/opacity-only performance practice. The skill's three-environment
model keeps headset, spatial-web, and flat-page techniques from being
confused with one another.

## Choosing quickly

- Need a **look**? Pick one visual style - skeuomorphism through maximalism, plus the newer flat/material and typographic families (flat, material, hand-drawn, pixel, corporate-memphis, neo-brutalist, editorial, terminal, japandi) - never two competing ones.
- Need **organization** for scannable, unequal content? Add bento grid.
- Need **depth or immersion** with a real reason? Add spatial UI, naming the environment.
- Need a **documented era** or a **staged world**? Pick one period aesthetic (retro, memphis, frutiger-aero, art deco) or one thematic genre (cyberpunk, y2k, vaporwave, futuristic HUD) and commit to its register.
- Building **on an Apple platform** and want the system's own material? Liquid glass - read the platform docs first.
- Everything ships at WCAG 2.2 AA, whatever you picked.
