# Design Routing Framework

Maps product type, audience, brand vibe, and platform context to one of the 27 Ochrelle
specialist skills. Route to exactly one primary specialist; consult others only for
secondary techniques under the combination rules below.

## Critical category distinctions

Before routing, classify correctly - these six categories are often confused:

| Skill | Category | The question it answers |
|---|---|---|
| skeuomorphism, neumorphism, glassmorphism, claymorphism, brutalism, minimalism, maximalism | **Visual style** | "What does it look and feel like?" |
| flat-design, material-design, hand-drawn, pixel-art, corporate-memphis | **Visual style** (material-styles family) | "What does it look and feel like?" |
| neo-brutalism, editorial-design, terminal-console, japandi | **Visual style** (typographic-expressive family) | "What does it look and feel like?" |
| retro-design, memphis-design, frutiger-aero, art-deco | **Period aesthetic** | "Which documented era's visual language is being revived?" |
| cyberpunk, y2k, vaporwave, futuristic-hud | **Thematic genre** | "Which story or world does the interface stage?" |
| bento-grid | **Layout / information architecture pattern** | "How is content organized into modules?" |
| spatial-ui | **Presentation / interaction paradigm** | "How does the UI use depth and space?" |
| liquid-glass | **Platform material system** | "Which named Apple material does this target?" |

Consequences:

- Bento Grid is **not a visual style**. A "minimalist bento dashboard" is one bento layout
  wearing minimalist styling - a fully legitimate combination.
- Spatial UI changes how interface elements are presented and interacted with (depth,
  anchoring, environment), independent of visual style.
- Liquid Glass is Apple's platform material with defined adaptive behaviors. It is
  **distinct from generic glassmorphism**: glassmorphism is a web-era visual style with
  frosted blur; Liquid Glass is a system material whose appearance adapts to content and
  context per Apple's platform documentation. Any web/CSS implementation of Liquid Glass
  is an approximation and must be reported as an approximation.
- Neumorphism, glassmorphism, and claymorphism all live or die on contrast; treat their
  contrast risks as routing constraints, not implementation afterthoughts.
- Period aesthetics borrow a documented era's materials, type, and palette. Executing
  one without period fidelity is vague "vintage", not the named style.
- Thematic genres stage a fictional or nostalgic world. They carry an atmosphere
  budget, and most of them demand an irony check before touching trust-critical
  surfaces (several name banking, healthcare, and government in their avoid lists).

## Per-style routing tables

### ochrelle-skeuomorphism

| Choose when | Avoid when |
|---|---|
| Physical familiarity aids comprehension (mixing decks, analog dials, musical instruments, simulators) | The metaphor is decoration only; users know the digital-native interaction |
| Training or onboarding users who come from the physical equivalent | High information density (textures fight data) |
| The brand is explicitly nostalgic, artisanal, or toy-like | Accessibility requires high contrast on many small controls |
| The surface area of skeuomorphic treatment is small (a few hero controls) | Fast, cheap scaling across a large product is needed (heavy assets) |

### ochrelle-neumorphism

| Choose when | Avoid when |
|---|---|
| Monochromatic, calm, low-stimulation surfaces (wellness, ambient status, smart-home panels) | Text sits on neumorphic surfaces (near-identical fg/bg tones fail 4.5:1) |
| The UI is mostly large controls, few dense data regions | Data-heavy dashboards, tables, or forms |
| A light or dark base tone with strong accent layering is acceptable as a system | Users include low-vision audiences without a parallel high-contrast mode |
| Pressed/raised states genuinely communicate interaction | The style would need heavy remediation to pass AA - then it is the wrong style |

### ochrelle-glassmorphism

| Choose when | Avoid when |
|---|---|
| Layered depth is meaningful: media-rich backgrounds, overlays, headers, players | Frosted surfaces sit on busy backgrounds behind body text (readability collapses) |
| The design needs hierarchy between background content and floating UI | Performance budget excludes backdrop-filter (large blur areas are expensive) |
| Brand mood is premium, airy, futuristic | Content-first tools (docs, spreadsheets) where chrome should disappear |
| Used sparingly: overlay layers, not entire app surfaces | The only differentiator would be "blurry rounded rectangles" |

### ochrelle-claymorphism

| Choose when | Avoid when |
|---|---|
| Friendly, playful, approachable products (kids' education, casual games, consumer fintech onboarding) | Enterprise tools, legal, medical dashboards demanding sober authority |
| Illustration-led marketing pages and onboarding flows | Long reading surfaces (heavy shadows inflate visual noise) |
| Bright palette + inflated shapes match the brand | Users expect high information density per screen |
| Tactile joy is a brand differentiator | Accessibility-critical flows where double shadows muddy contrast |

### ochrelle-brutalism

| Choose when | Avoid when |
|---|---|
| Anti-corporate, subcultural, art-adjacent brands; studios, zines, fashion drops | Products where trust and polish drive conversion (banking, healthcare) |
| Content is the hero and chrome should be aggressively plain | Dense forms (raw defaults become hostile fast) |
| The audience reads "raw" as honesty, speed, or edge | The brand needs subtle emotional tonality |
| Speed and simplicity of implementation are real constraints | A11y-sensitive audiences; brutalism must still keep contrast and focus states |

### ochrelle-minimalism

| Choose when | Avoid when |
|---|---|
| Productivity, SaaS, documentation, enterprise tools; daily-use products | Brands whose identity demands expressiveness (youth culture, entertainment) |
| Content and data must dominate | The "minimal" version would hide necessary affordances (then it is spartan, not minimal) |
| Trust, clarity, and speed matter more than delight | Crowded markets where only visual distinction separates brands - pair with strong typography instead |
| Long-term maintainability matters (fewest tokens to keep consistent) | - |

### ochrelle-maximalism

| Choose when | Avoid when |
|---|---|
| Culture, music, fashion, events, editorial, creative portfolios | Core working surfaces of productivity apps (fatigue is real) |
| The brand differentiates through energy and abundance | Users must scan dense data quickly under time pressure |
| Campaign/landing contexts with short dwell time | The expressiveness would outrun the hierarchy (if everything is loud, nothing is heard) |
| A strict underlying grid and type system keeps the chaos legible | Accessibility overhead would be unbounded - constrain the palette |

### ochrelle-liquid-glass

| Choose when | Avoid when |
|---|---|
| Target platform genuinely provides the material (Apple platforms, per current HIG) | Web targets where only an approximation is possible - allowed, but label it |
| Content-forward apps where chrome adapts to what is behind it | Conventional enterprise dashboards (no benefit from adaptive material) |
| The design system already follows Apple platform conventions | Teams that cannot maintain the platform-specific code path |
| Controls float over variable, media-rich backgrounds | Static, flat layouts where material adaptiveness has nothing to adapt to |

### ochrelle-bento-grid (layout pattern)

| Choose when | Avoid when |
|---|---|
| Content decomposes into genuinely modular, scannable units (settings, stats, feature summaries) | Content is sequential/long-form (articles, documentation) |
| Landing pages needing dense feature coverage at a glance | Strictly linear narratives or step-by-step flows |
| Portfolio/product overview pages mixing media types | Every cell would be same-size filler (the pattern collapses into card soup) |
| Responsive collapse is plan-first: 2–3 col → 1 col, deliberate order | No plan exists for what happens below desktop (always design the mobile collapse) |

### ochrelle-spatial-ui

| Choose when | Avoid when |
|---|---|
| Target device uses spatial presentation (headset, per its HIG) or a 3D-native product (maps, CAD, AR previews) | Flat web/mobile tasks with no spatial payoff |
| Depth communicates real relationships (layers, scenes, physical space) | Depth is applied as pure decoration (disorientation, motion sickness risk) |
| Comfort guidance from the platform can be followed (stability, reduced motion) | The audience includes vestibular-sensitive users without reduced-motion alternatives |
| Orientation is always obvious: fixed anchors, readable persistent UI | The team cannot implement comfortable camera/movement controls |

### ochrelle-flat-design

| Choose when | Avoid when |
|---|---|
| SaaS dashboards, admin panels, and analytics tools: flat color blocks scan fast and render cheap | Luxury, fashion, or hospitality brands: flat reads as utilitarian, not premium |
| Settings screens, forms, documentation, and internal tools: clarity over atmosphere | Users who need strong affordance cues (hardware-adjacent apps, kiosks) without careful state design |
| Content-first brands (news, tools, utilities) that want zero style tax | Games, events, or youth brands that need atmosphere and mood |
| Design systems handed to multiple teams: flat tokens are the easiest to enforce | Brands where one accent color cannot carry the identity: flat amplifies palette weakness |

### ochrelle-material-design

| Choose when | Avoid when |
|---|---|
| Android apps and anything expected to feel at home in the Google ecosystem | Anti-corporate or expressive brands: Material reads as Google |
| Cross-platform productivity tools: email, files, notes, settings, admin consoles | Atmosphere-first landing pages (games, events, music): the system optimizes for utility |
| Structured SaaS with lots of cards, lists, filters, and forms | Brand guidelines that forbid Google's type or shape language |
| Teams that need a complete, accessible design system on day one and role tokens to constrain drift | Tiny brochure sites where a full design system is ballast, not value |

### ochrelle-neo-brutalism

| Choose when | Avoid when |
|---|---|
| Indie products, creator tools, newsletters, community apps: the style signals independence and charm | Banking, healthcare, insurance, government: roughness reads as untrustworthy where stakes are high |
| Merch drops, event tickets, festival and gig sites: the ticket/sticker vocabulary is native | Luxury or premium brands: sticker energy undercuts price |
| Portfolios and studio sites that want loud without luxury cliches | Long-form reading products: heavy borders and saturated blocks tax sustained scanning |
| Gen Z-facing startups and prototypes where "honest state" (beta, draft, shipping) is part of the pitch | Accessibility-certified enterprise UIs without budget for the extra contrast and motion care |

### ochrelle-y2k

| Choose when | Avoid when |
|---|---|
| Music events, raves, and festival pages: the chrome-and-candy energy is native | Banking, healthcare, government: trust must read as calm competence |
| Fashion drops, merch, stickers, and Gen Z brand moments built on revival culture | Dense B2B SaaS and data tools: gel materials and glows tax sustained scanning |
| Games and playful apps themed on early-2000s tech | Long-form reading products: decorative surfaces fight text |
| One-off campaign sites where nostalgia is the message | Products needing dark-mode-first ergonomics: Y2K is a light-material system at heart |

### ochrelle-cyberpunk

| Choose when | Avoid when |
|---|---|
| Games and interactive fiction set in neon-noir worlds: the UI is diegetic set dressing | Healthcare, finance, government, or kids' products: the mood reads as untrustworthy or menacing |
| Music and rave events, club nights, festivals: darkness plus neon is the venue's own language | Long-form reading defaults: dark, glowing, dense surfaces tax sustained reading |
| Developer tools, security products, and terminals that want a night-shift identity | Elderly- or accessibility-first audiences without heavy extra contrast work |
| Night-mode-first products, dark portfolios, and sci-fi dashboards where atmosphere is the point | Corporate SaaS that needs to feel calm and neutral |

### ochrelle-retro-design

| Choose when | Avoid when |
|---|---|
| Cafes, diners, bakeries, ice cream shops: menu-board layouts and badge CTAs are native | Fintech, healthcare, insurance, government: period type undermines trust in critical information |
| Breweries, taprooms, pizzerias, BBQ joints: label and packaging DNA translates directly to web | Data-dense dashboards and admin tools: menu-board layouts cannot carry 40 columns of table |
| Record and vinyl stores, barbershops, bowling alleys, retro arcades | Luxury and high fashion: retro warmth reads as friendly, not exclusive |
| Event posters, food festivals, merch: the poster grammar (burst, badge, big type) carries | Dark-mode developer tools: the cream ground is the style's spine; without it the system breaks |

### ochrelle-editorial-design

| Choose when | Avoid when |
|---|---|
| Blogs, digital magazines, essays, and newsletters: the native habitat | Data-dense dashboards, admin consoles, checkout flows: scanning beats reading there |
| Press pages, newsrooms, and annual reports: authority is the product | Youth-culture drops, party brands, gaming: editorial restraint will read as dull |
| Story-driven product marketing: case studies, founder letters, changelogs with a voice | Immersive campaign pages built around motion and full-bleed video |
| Writer and photographer portfolios where the work is text and image | Apps whose primary screen is a table, map, or chat stream |

### ochrelle-memphis-design

| Choose when | Avoid when |
|---|---|
| Creative tools, design-community products, portfolio experiments: audiences that get the joke | Banking, insurance, healthcare, government: trust requires calm |
| Music culture: label sites, festival and club promoters, vinyl merch, band stores | Enterprise B2B dashboards and long data tables: patterns and asymmetry tax scanning |
| Party and event brands, invitations, ticketing for playful formats | Luxury brands: Memphis is laminate, not lacquer; it undercuts premium cues |
| Youth products, sticker packs, merch, indie games; campaigns that must signal "not a bank" in one second | Continuous-reading products (news readers, documentation portals): the style fights sustained reading |

### ochrelle-japandi

| Choose when | Avoid when |
|---|---|
| Wellness, meditation, and mindfulness apps where calm is the product | Trading, analytics, or security dashboards: density and instant scanning beat calm |
| Hospitality: boutique hotels, spa booking, tea and coffee houses, craft-kitchen restaurants | Youth hype drops, gaming, sports: the energy is wrong |
| Skincare, ceramics, stationery, and furniture brands selling material honesty | Emergency, alert-heavy, or safety-critical interfaces: calm must never mute urgency |
| Calm productivity tools (journaling, focus timers, notes) and slow editorial sites | Brands whose identity is loud, maximal, or neon: this style will read as off-brand silence |

### ochrelle-frutiger-aero

| Choose when | Avoid when |
|---|---|
| Music players and audio apps where the "living water" mood fits playback UI | Dense data tools, trading dashboards, IDEs, admin tables: glass and gloss tax scanning speed |
| Throwback marketing pages, anniversary microsites, era-nostalgia campaigns | Accessibility-critical government, health, or emergency interfaces: translucency is hard to guarantee under every background |
| Retro-future branding with clean-eco optimism: sustainability pages, wellness tech, smart-home kiosks | Enterprise forms with high field counts: input affordance gets noisy under shine |
| Product configurators, kiosk screens, portfolios that want bright, touchable period craft | Austere, brutalist, or editorial brands and long-form reading: light-sky palettes and shine tire the eye |

### ochrelle-corporate-memphis

| Choose when | Avoid when |
|---|---|
| Onboarding illustrations: step-by-step flows where a friendly figure reduces first-run anxiety | Premium, luxury, or craft brands: the elastic figures undercut price positioning instantly |
| HR tools, internal portals, and benefits explainers where warmth matters more than brand edge | Serious domains (health crises, legal, finance risk, security incidents): uniform cheer reads as tone-deaf |
| Community pages, event pages, and empty states that need human presence without photography | Editorial storytelling or journalism: the style's abstraction hides the specific human detail stories need |
| SaaS marketing heroes and illustration at scale on a budget: one system, many scenes | Products competing on visual craft: the style signals template, not authorship |

### ochrelle-vaporwave

| Choose when | Avoid when |
|---|---|
| Music releases: album pages, label sites, mixtape covers, cassette and vinyl drops | Enterprise software, banking, health, or government: irony and dark palette undermine trust |
| Events: club nights, listening parties, festival stages and line-ups | Children's products: VHS distortion and strobe-adjacent effects are unsuitable |
| Streetwear and merch: drop pages, lookbooks, size charts with typographic swagger | Long-form reading: the palette and display type fatigue eyes fast |
| Creative portfolios (designers, VJs, 3D artists) and nostalgia marketing where the brand can carry irony | Austere or heritage brands: vaporwave reads as costume; it also clashes with documentary photography |

### ochrelle-pixel-art

| Choose when | Avoid when |
|---|---|
| Games and game-adjacent tools: launchers, emulation frontends, level editors, achievement popups | Data-dense dashboards, finance or medical software: bitmap type and chunky chrome waste scanning speed |
| Playful developer products: hack-club sites, game-jam pages, sprite-artist portfolios | Long-form reading surfaces: pixel fonts fatigue eyes within paragraphs |
| Retro gaming brands: merch stores, stream overlays, podcast identities, arcade bar sites | Luxury or editorial brands: the style reads playful/indie, never premium |
| Kids' and educational tools where game grammar (progress bars, XP, badges) motivates | Internationalized text-heavy UI: pixel fonts often lack full character sets, which breaks trust fast |

### ochrelle-terminal-console

| Choose when | Avoid when |
|---|---|
| Developer tools, log viewers, CI/build dashboards, API explorers, observability products | Long-form reading products: monospace body text fatigues fast at length |
| CLI companion sites, package manager docs, and engineering-first SaaS | Consumer marketing, luxury, or photography-led brands: the metaphor reads technical, not premium |
| Status pages and ops dashboards where density and scanability beat decoration | Non-technical audiences who will read the dark screen with green text as "hacker cosplay" rather than competence |
| Brands that want to signal "built by engineers, for engineers" | - |

### ochrelle-hand-drawn

| Choose when | Avoid when |
|---|---|
| Education platforms, courseware, and kids' tools teaching a skill step by step | Banking, medical, legal, or government products: audiences read sketchiness as unfinished, not friendly |
| Creative apps and workshop or community brands | Dense data tools and dashboards: wobble fights alignment and scanability |
| Indie products selling warmth and approachability | Luxury or premium-positioned brands: the notebook idiom undercuts price justification |
| Onboarding, how-to guides, and documentation walkthroughs where encouragement matters | Strict accessibility certification needs that cannot afford the extra state-design care |

### ochrelle-art-deco

| Choose when | Avoid when |
|---|---|
| Boutique hotels, cocktail bars, speakeasies, tasting rooms: the facade metaphor is native | Developer tools, fintech dashboards, admin consoles: marquee type kills dense data |
| Theaters, cinemas, concert halls, museum and exhibition pages | Kids' products, sports, casual fast food: the register is wrong |
| Jewelry, perfume, spirits, watches, patisserie: crafted luxury with a story | Healthcare and government: ornament here reads as unserious |
| Wedding and event invitations, launch parties, gala microsites: engineered glamour as the promise | Dark-mode reading products: the ivory ground is structural to this system |

### ochrelle-futuristic-hud

| Choose when | Avoid when |
|---|---|
| Robotics, drone, and IoT dashboards where telemetry is the content | Long-form reading products, docs, legal: scanline density taxes reading |
| Sci-fi games, fan tools, and ARG/event sites that want diegetic chrome | Healthcare and safety-critical control surfaces: style must not dress urgency down |
| Launch events, product reveals, mission-control-style live pages | E-commerce checkout and everyday productivity apps: the chrome outweighs the task |
| Cyberpunk club and event branding, night-mode kiosks, concept UI explorations | Kids' products: the palette and density are not child-legible |

## Routing decision tree

Answer in order; stop at the first match.

1. Is the target a **spatial device** or 3D-native product? → `spatial-ui` (+ any visual
   style as dressing, per platform HIG).
2. Does the target platform provide **Liquid Glass** as its system material, and does the
   product follow that platform's conventions? → `liquid-glass`.
3. Is the primary problem **organizing many modular pieces of content**? → `bento-grid`
   as the layout pattern, then continue 4–6 to pick the visual style.
4. Is there a **physical metaphor** that materially aids comprehension? → `skeuomorphism`.
5. What is the dominant **brand vibe**?
   - calm / trustworthy / content-first → `minimalism`
   - friendly / playful / approachable → `claymorphism`
   - premium / immersive / media-rich → `glassmorphism`
   - soft / ambient / low-stimulation (and mostly control-based UI) → `neumorphism`
   - raw / rebellious / anti-corporate → `brutalism`
   - expressive / cultural / loud → `maximalism`
6. Default and fallback: **`minimalism`** - or plain conventional platform UI when even
   minimalism would add friction. Never choose an expressive style by default.

Then validate the choice against: audience accessibility needs, content inventory, and
performance budget. Any hard conflict (e.g. neumorphism + low-vision audience without a
high-contrast mode) re-routes the decision.

## Combination rules

- **One primary direction** owns the visual language. Secondary techniques must be
  load-bearing (they organize, clarify, or scaffold the primary direction).
- **Material budget**: at most 2 expressive materials per surface (e.g. glass +
  neumorphic inset is already at the limit; adding clay on top is incoherent).
- Legitimate, common combinations:
  - Minimalism × Bento Grid - the classic product dashboard.
  - Glassmorphism (or Liquid Glass on Apple platforms) over a conventional readable UI -
    translucency on floating chrome, solid readability on content.
  - Skeuomorphic hero controls inside a conventional layout - physical familiarity where
    it teaches; convention everywhere else.
  - Maximalist art direction over a strict grid and type system - loud palette, quiet
    structure.
  - Spatial UI with any restrained visual style - depth as presentation, calm as skin.
  - Editorial-design × Minimalism for reading surfaces - editorial owns the typographic
    voice (decks, pull quotes, baseline rhythm), minimalism keeps the chrome quiet.
  - Terminal-console × Minimalism for developer dashboards - the terminal panel carries
    density and monospace grids; minimalism keeps everything around it out of the way.
  - Retro-design × Hand-drawn for warm indie brands - both trade in human warmth and
    craft; hand-drawn accents loosen retro's badge and poster formality.
  - Flat-design × Corporate-memphis for illustration-led products - corporate-memphis
    art is itself flat vector, so one token system can carry both the product shell and
    the onboarding/empty-state scenes.
- Never combine: neumorphism + glassmorphism (two different soft-light models fighting),
  brutalism + claymorphism (opposed value systems), skeuomorphism + brutalism (opposed
  philosophies of finish), maximalism + minimalism as co-equal directions (pick one),
  cyberpunk + japandi (neon-noir menace and quiet natural calm are opposing total
  atmospheres - each cancels the other), futuristic-hud + hand-drawn (diegetic machine
  chrome and sketchbook wobble are opposing registers of authority), retro-design +
  cyberpunk (the cream daylight ground and the near-black neon night ground are
  structurally incompatible spines).
- Full combination mechanics, token sketches, and worked examples:
  `references/hybrid-style-guide.md`.
