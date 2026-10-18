"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { SiteFooter } from "@/components/site-footer";
import { PigmentChip } from "@/components/pigment-chip";
import { withBase, GITHUB_URL, REPO_ZIP_URL, IS_STATIC_EXPORT } from "@/lib/site";
import {
  Check,
  Download,
  ExternalLink,
  FileCode2,
  Files,
  FlaskConical,
  FolderTree,
  Github,
  Package,
  ShieldCheck,
  Terminal,
} from "lucide-react";

type Skill = {
  name: string;
  type: string;
  bestFor: string;
  master?: boolean;
};

const SKILLS: Skill[] = [
  {
    name: "ochrelle-design-master",
    type: "Master skill",
    bestFor:
      "Interviews the product context, weighs 27 candidate directions, records the decision, and routes the work to a specialist",
    master: true,
  },
  { name: "ochrelle-skeuomorphism", type: "Style specialist", bestFor: "Real-object metaphors, tactile controls, physical familiarity" },
  { name: "ochrelle-neumorphism", type: "Style specialist", bestFor: "Soft-UI extruded surfaces on monochrome, low-contrast scenes" },
  { name: "ochrelle-glassmorphism", type: "Style specialist", bestFor: "Frosted translucency layered over vivid media" },
  { name: "ochrelle-claymorphism", type: "Style specialist", bestFor: "Puffy, friendly shapes for playful products and onboarding" },
  { name: "ochrelle-brutalism", type: "Style specialist", bestFor: "Raw structure, hard borders, deliberate and controlled roughness" },
  { name: "ochrelle-minimalism", type: "Style specialist", bestFor: "Reduction, whitespace rhythm, typographic clarity" },
  { name: "ochrelle-maximalism", type: "Style specialist", bestFor: "Expressive density, layered type and pattern, kept under control" },
  { name: "ochrelle-liquid-glass", type: "Platform material", bestFor: "Apple's adaptive Liquid Glass and honest web approximations" },
  { name: "ochrelle-bento-grid", type: "Layout pattern", bestFor: "Modular tile layouts sized by information priority" },
  { name: "ochrelle-spatial-ui", type: "Interaction paradigm", bestFor: "Depth, scale, and environment-aware interfaces" },
  { name: "ochrelle-flat-design", type: "Style specialist", bestFor: "Solid fills, simple geometry, typography-first hierarchy" },
  { name: "ochrelle-material-design", type: "Style specialist", bestFor: "Elevation, FABs, and physical motion per Google's paper-and-ink system" },
  { name: "ochrelle-neo-brutalism", type: "Style specialist", bestFor: "Thick borders, hard offset shadows, saturated flats, loud brands" },
  { name: "ochrelle-y2k", type: "Thematic genre", bestFor: "Translucent plastics, chrome gradients, dot-com optimism" },
  { name: "ochrelle-cyberpunk", type: "Thematic genre", bestFor: "Neon noir on near-black for gaming, nightlife, and streetwear" },
  { name: "ochrelle-retro-design", type: "Period aesthetic", bestFor: "Mid-century warmth: cream, burnt orange, groovy type, halftone" },
  { name: "ochrelle-editorial-design", type: "Style specialist", bestFor: "Magazine craft on the web: dominant type, decks, pull quotes" },
  { name: "ochrelle-memphis-design", type: "Period aesthetic", bestFor: "Squiggles, terrazzo, deliberate 1980s postmodern clash" },
  { name: "ochrelle-japandi", type: "Style specialist", bestFor: "Japanese restraint meets Scandinavian warmth for calm products" },
  { name: "ochrelle-frutiger-aero", type: "Period aesthetic", bestFor: "Glossy aqua optimism: gel buttons, glass shine, nature plus tech" },
  { name: "ochrelle-corporate-memphis", type: "Style specialist", bestFor: "Flat vector illustration systems, trade-offs stated honestly" },
  { name: "ochrelle-vaporwave", type: "Thematic genre", bestFor: "VHS nostalgia, statues, sunset gradients, mall-era memory" },
  { name: "ochrelle-pixel-art", type: "Style specialist", bestFor: "Limited palettes, crisp pixels, integer scaling for games" },
  { name: "ochrelle-terminal-console", type: "Style specialist", bestFor: "Monospace grids, box-drawing frames, phosphor on near-black" },
  { name: "ochrelle-hand-drawn", type: "Style specialist", bestFor: "Sketchbook borders, doodles, paper texture, human warmth" },
  { name: "ochrelle-art-deco", type: "Period aesthetic", bestFor: "1920s geometry and gold: sunbursts, symmetry, marquee luxury" },
  { name: "ochrelle-futuristic-hud", type: "Thematic genre", bestFor: "Film-grade telemetry panels with contrast-safe glow" },
];

const PROBLEMS = [
  {
    title: "Nobody asks which style",
    body: 'Most briefs say "make it look good". The model answers with the same interface every time: a centered card, a soft shadow, Inter, and one safe gradient. The master skill forces an explicit style decision and records why it was made.',
  },
  {
    title: "Craft details get averaged away",
    body: "Every style has rules that generic training data blurs out. Neumorphism needs monochrome surfaces and dies on busy backgrounds. Brutalism is rough in structured ways. Claymorphism needs three stacked shadows to read as soft 3D. Each specialist carries its own rules.",
  },
  {
    title: "Bold styles hide contrast traps",
    body: "Glassmorphism and maximalism can fail WCAG quietly while looking finished. Every skill ships accessibility guidance written for its own style, targeting WCAG 2.2 Level AA.",
  },
];

const VALIDATION = [
  {
    icon: ShieldCheck,
    label: "Skill validator",
    body: "Checks frontmatter, reference links, and content invariants for all 28 skills. Stdlib only, no dependencies.",
    cmd: "python3 scripts/validate_skills.py",
  },
  {
    icon: FolderTree,
    label: "Repository validator",
    body: "Asserts the repo layout: skill directories, docs, examples, license, citation file, and CI workflow.",
    cmd: "python3 scripts/validate_repository.py",
  },
  {
    icon: FlaskConical,
    label: "Unit tests",
    body: "29 pytest cases over skill metadata and repository structure, including negative fixtures that must fail cleanly.",
    cmd: "python3 -m pytest tests/ -q",
  },
  {
    icon: Files,
    label: "File count",
    body: "229 files in the repository, counted without git internals. The download zip ships exactly these files and nothing else.",
    cmd: "find ochrelle -type f -not -path '*/.git/*' | wc -l",
  },
];

const INSTALL_STEPS = [
  {
    n: "1",
    title: "Install the skills",
    body: "Run the installer to copy skill folders into your agent's skills directory, or into any project folder.",
    code: "./scripts/install.sh --claude\n# or: ./scripts/install.sh ./skills",
  },
  {
    n: "2",
    title: "Ask for art direction, not just UI",
    body: "The master skill interviews the product context, compares candidate styles, and commits to one with reasons.",
    code: '"Design a dashboard for our analytics\n  product. Pick the style and justify it."',
  },
  {
    n: "3",
    title: "Validate before you ship",
    body: "Run the validators and the test suite. Both are stdlib-only Python and run in seconds.",
    code: "python3 scripts/validate_skills.py && \\\n  python3 -m pytest tests/ -q",
  },
];

const REPO_TREE = `ochrelle/
├── skills/       28 self-contained skills
│   ├── ochrelle-design-master/
│   │   └── references/   7 documents
│   └── 27 specialists, 6 families:
│       visual styles, layout patterns,
│       period aesthetics, thematic genres,
│       platform materials, interaction paradigms
├── docs/           7 guides + compatibility matrix
├── examples/
│   └── web-showcase/  live 10-style demo + catalog
├── website/        the Next.js site you are reading
├── scripts/        2 validators + install.sh
├── tests/          29 test cases
└── README, LICENSE, CITATION.cff, CI`;

export default function Home() {
  const [copied, setCopied] = useState<string | null>(null);

  const copy = (text: string, key: string) => {
    navigator.clipboard?.writeText(text).then(() => {
      setCopied(key);
      setTimeout(() => setCopied(null), 1600);
    });
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#FAFAF9] text-[#1C1917]">
      {/* Header */}
      <header className="border-b border-[#E7E5E4] bg-[#FAFAF9]/95 backdrop-blur-sm sticky top-0 z-40">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between gap-4">
          <a href="/" className="flex items-center gap-3 shrink-0 group">
            <span className="w-8 h-8 rounded-md bg-[#1C1917] flex items-center justify-center">
              <PigmentChip size={17} />
            </span>
            <span className="leading-tight">
              <span className="block font-semibold tracking-tight">Ochrelle</span>
              <span className="block text-xs text-[#78716C] hidden sm:block">
                Design skills for AI coding agents
              </span>
            </span>
          </a>
          <nav aria-label="Main" className="flex items-center gap-1 sm:gap-2">
            <Button
              variant="ghost"
              size="sm"
              className="hidden sm:inline-flex"
              onClick={() => document.getElementById("skills")?.scrollIntoView({ behavior: "smooth" })}
            >
              Skills
            </Button>
            <Button
              variant="ghost"
              size="sm"
              className="hidden sm:inline-flex"
              onClick={() => document.getElementById("proof")?.scrollIntoView({ behavior: "smooth" })}
            >
              Verification
            </Button>
            <Button
              variant="ghost"
              size="sm"
              className="hidden sm:inline-flex"
              onClick={() => document.getElementById("install")?.scrollIntoView({ behavior: "smooth" })}
            >
              Install
            </Button>
            <Button asChild size="sm" className="bg-[#C2410C] hover:bg-[#9A3412] text-white shrink-0">
              <a href={withBase("/showcase/index.html")} target="_blank" rel="noopener">
                Showcase
                <ExternalLink size={14} className="ml-1.5" aria-hidden="true" />
              </a>
            </Button>
          </nav>
        </div>
      </header>

      <main className="flex-1">
        {/* Hero */}
        <section className="max-w-6xl mx-auto px-4 sm:px-6 pt-14 pb-12 sm:pt-20 sm:pb-16">
          <Badge variant="outline" className="mb-6 border-[#C2410C]/40 text-[#C2410C] bg-transparent rounded-md font-medium">
            Open source, MIT licensed, Agent Skills format, v2.0.0
          </Badge>
          <h1 className="text-4xl sm:text-6xl font-bold tracking-tight max-w-3xl leading-[1.06]">
            28 Agent Skills for interface art direction.
          </h1>
          <p className="mt-6 text-lg sm:text-xl text-[#57534E] max-w-2xl leading-relaxed">
            Ochrelle is a repository of design skills for AI coding agents.
            The master skill interviews your product, weighs 27 candidate
            directions, and routes the work to a specialist that ships
            production UI under WCAG 2.2 Level AA rules. Plain markdown, CSS,
            and Python. Works with any agent that reads markdown.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Button asChild size="lg" className="bg-[#C2410C] hover:bg-[#9A3412] text-white h-12 px-6 rounded-md">
              <a href={withBase("/showcase/index.html")} target="_blank" rel="noopener">
                Browse the style catalog
                <ExternalLink size={16} className="ml-2" aria-hidden="true" />
              </a>
            </Button>
            <Button
              variant="outline"
              size="lg"
              className="h-12 px-6 border-[#D6D3D1] rounded-md"
              onClick={() =>
                copy(
                  "./scripts/install.sh --claude",
                  "install"
                )
              }
            >
              <Terminal size={16} className="mr-2" aria-hidden="true" />
              {copied === "install" ? "Copied to clipboard" : "Copy install command"}
            </Button>
            {IS_STATIC_EXPORT ? (
              <Button asChild variant="outline" size="lg" className="h-12 px-6 border-[#D6D3D1] rounded-md">
                <a href={REPO_ZIP_URL} target="_blank" rel="noopener">
                  <Download size={16} className="mr-2" aria-hidden="true" />
                  Download the repo (.zip)
                </a>
              </Button>
            ) : (
              <Button asChild variant="outline" size="lg" className="h-12 px-6 border-[#D6D3D1] rounded-md">
                <a href="/download/ochrelle-2.0.0.zip" download>
                  <Download size={16} className="mr-2" aria-hidden="true" />
                  Download the repo (.zip)
                </a>
              </Button>
            )}
            {IS_STATIC_EXPORT ? (
              <Button asChild variant="outline" size="lg" className="h-12 px-6 border-[#D6D3D1] rounded-md">
                <a href={GITHUB_URL} target="_blank" rel="noopener">
                  <Github size={16} className="mr-2" aria-hidden="true" />
                  View source on GitHub
                </a>
              </Button>
            ) : (
              <Button asChild variant="outline" size="lg" className="h-12 px-6 border-[#D6D3D1] rounded-md">
                <a href="/download/ochrelle-deployment-kit.zip" download>
                  <Package size={16} className="mr-2" aria-hidden="true" />
                  Deployment kit (.zip)
                </a>
              </Button>
            )}
          </div>

          {/* Verifiable facts. Numbers are counted from the repository, not projections. */}
          <dl className="mt-12 grid grid-cols-2 sm:grid-cols-4 gap-6 max-w-2xl">
            {[
              ["28", "skills in the repository"],
              ["27", "specialist directions"],
              ["229", "files in the repo"],
              ["29", "unit tests"],
            ].map(([v, l]) => (
              <div key={l}>
                <dt className="sr-only">{l}</dt>
                <dd className="text-3xl font-bold tracking-tight font-mono">{v}</dd>
                <dd className="text-sm text-[#78716C] mt-1">{l}</dd>
              </div>
            ))}
          </dl>
          <p className="mt-4 text-sm text-[#78716C] max-w-2xl">
            Counts are taken from the repository at v2.0.0. The Verification
            section below shows the commands that reproduce them.
          </p>
        </section>

        {/* Problem */}
        <section className="max-w-6xl mx-auto px-4 sm:px-6 py-12 sm:py-16 border-t border-[#E7E5E4]">
          <h2 className="text-2xl sm:text-3xl font-bold tracking-tight">
            Why generated interfaces all look the same
          </h2>
          <p className="mt-3 text-[#57534E] max-w-2xl leading-relaxed">
            The problem is not model capability. It is that three specific
            inputs are missing from the prompt.
          </p>
          <div className="mt-8 grid gap-4 md:grid-cols-3 [&>*]:min-w-0">
            {PROBLEMS.map((p, i) => (
              <Card key={p.title} className="border-[#E7E5E4] bg-white rounded-md">
                <CardHeader className="pb-2">
                  <CardTitle className="text-base flex items-baseline gap-2">
                    <span className="font-mono text-sm text-[#C2410C]">
                      0{i + 1}
                    </span>
                    {p.title}
                  </CardTitle>
                </CardHeader>
                <CardContent className="pt-0">
                  <p className="text-sm leading-relaxed text-[#57534E]">{p.body}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </section>

        {/* Skills grid */}
        <section id="skills" className="max-w-6xl mx-auto px-4 sm:px-6 py-12 sm:py-16 border-t border-[#E7E5E4]">
          <h2 className="text-2xl sm:text-3xl font-bold tracking-tight">
            28 skills, one quality bar
          </h2>
          <p className="mt-3 text-[#57534E] max-w-2xl leading-relaxed">
            One master skill routes and supervises. 27 specialists cover
            visual styles, layout patterns, period aesthetics, thematic
            genres, platform materials, and interaction paradigms. Every
            skill carries a style guide, runnable code recipes, documented
            failure modes, and a quality checklist.
          </p>
          <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3 [&>*]:min-w-0">
            {SKILLS.map((s) => (
              <Card
                key={s.name}
                className={`border-[#E7E5E4] transition-colors duration-200 hover:border-[#C2410C]/50 ${
                  s.master ? "bg-[#1C1917] text-[#FAFAF9] border-[#1C1917]" : "bg-white"
                }`}
              >
                <CardHeader className="pb-3">
                  <div className="flex items-start justify-between gap-2">
                    <CardTitle className={`text-[15px] font-semibold tracking-tight font-mono ${s.master ? "text-[#FAFAF9]" : ""}`}>
                      {s.name}
                    </CardTitle>
                    {s.master && (
                      <Badge className="bg-[#C2410C] hover:bg-[#C2410C] text-white shrink-0 rounded-md">
                        master
                      </Badge>
                    )}
                  </div>
                  <CardDescription className={s.master ? "text-[#A8A29E]" : "text-[#78716C]"}>
                    {s.type}
                  </CardDescription>
                </CardHeader>
                <CardContent className="pt-0">
                  <p className={`text-sm leading-relaxed ${s.master ? "text-[#D6D3D1]" : "text-[#57534E]"}`}>
                    {s.bestFor}
                  </p>
                </CardContent>
              </Card>
            ))}
          </div>
        </section>

        {/* Verification */}
        <section id="proof" className="max-w-6xl mx-auto px-4 sm:px-6 py-12 sm:py-16 border-t border-[#E7E5E4]">
          <h2 className="text-2xl sm:text-3xl font-bold tracking-tight">
            Check every claim yourself
          </h2>
          <p className="mt-3 text-[#57534E] max-w-2xl leading-relaxed">
            No testimonials, no star ratings, no usage counters. The evidence
            is a repository you can audit in an afternoon, plus four commands
            that verify it.
          </p>
          <div className="mt-8 grid lg:grid-cols-2 gap-8 [&>*]:min-w-0">
            <ul className="space-y-4 min-w-0">
              {VALIDATION.map((v) => (
                <li key={v.label}>
                  <Card className="border-[#E7E5E4] bg-white rounded-md">
                    <CardHeader className="pb-2">
                      <CardTitle className="text-base flex items-center gap-2.5">
                        <v.icon size={19} className="text-[#C2410C]" aria-hidden="true" />
                        {v.label}
                      </CardTitle>
                    </CardHeader>
                    <CardContent className="pt-0 space-y-3 min-w-0">
                      <p className="text-sm leading-relaxed text-[#57534E]">{v.body}</p>
                      <div className="relative min-w-0">
                        <pre className="text-xs bg-[#1C1917] text-[#FAFAF9] rounded-md p-3 pr-10 overflow-x-auto font-mono">
                          {v.cmd}
                        </pre>
                        <button
                          onClick={() => copy(v.cmd, v.label)}
                          aria-label={`Copy command for ${v.label}`}
                          className="absolute top-2.5 right-2.5 text-[#A8A29E] hover:text-white transition-colors duration-200"
                        >
                          {copied === v.label ? <Check size={14} /> : <Terminal size={14} />}
                        </button>
                      </div>
                    </CardContent>
                  </Card>
                </li>
              ))}
            </ul>
            <Card className="border-[#1C1917] bg-[#1C1917] text-[#FAFAF9] rounded-md overflow-hidden h-fit">
              <CardHeader className="pb-2">
                <CardTitle className="text-sm font-medium text-[#A8A29E] flex items-center gap-2">
                  <FileCode2 size={16} aria-hidden="true" />
                  Repository layout
                </CardTitle>
              </CardHeader>
              <CardContent className="pt-0">
                <pre className="text-xs sm:text-sm leading-relaxed overflow-x-auto text-[#D6D3D1] font-mono">
                  {REPO_TREE}
                </pre>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Install */}
        <section id="install" className="max-w-6xl mx-auto px-4 sm:px-6 py-12 sm:py-16 border-t border-[#E7E5E4]">
          <h2 className="text-2xl sm:text-3xl font-bold tracking-tight">
            Install on any agent
          </h2>
          <div className="mt-8 grid gap-6 md:grid-cols-3 [&>*]:min-w-0">
            {INSTALL_STEPS.map((s) => (
              <Card key={s.n} className="border-[#E7E5E4] bg-white rounded-md">
                <CardHeader className="pb-3">
                  <div className="w-8 h-8 rounded-md bg-[#C2410C]/10 text-[#C2410C] font-mono font-semibold text-sm flex items-center justify-center mb-3">
                    {s.n}
                  </div>
                  <CardTitle className="text-base">{s.title}</CardTitle>
                  <CardDescription className="leading-relaxed">{s.body}</CardDescription>
                </CardHeader>
                <CardContent className="pt-0 min-w-0">
                  <div className="relative min-w-0">
                    <pre className="text-xs bg-[#1C1917] text-[#FAFAF9] rounded-md p-3 pr-10 overflow-x-auto font-mono">
                      {s.code}
                    </pre>
                    <button
                      onClick={() => copy(s.code, s.n)}
                      aria-label={`Copy step ${s.n} command`}
                      className="absolute top-2.5 right-2.5 text-[#A8A29E] hover:text-white transition-colors duration-200"
                    >
                      {copied === s.n ? <Check size={14} /> : <Terminal size={14} />}
                    </button>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>

          <div className="mt-10 border border-[#E7E5E4] rounded-md bg-white p-5 sm:p-6">
            <h3 className="font-semibold tracking-tight">What Ochrelle is not</h3>
            <p className="mt-2 text-sm text-[#57534E] leading-relaxed max-w-3xl">
              Ochrelle is not a plugin market, a framework, or a hosted
              service. There is no runtime and nothing to execute inside
              your app. Each skill is a folder of markdown with frontmatter:
              copy it where your agent can read it, and the agent follows it.
              The Agent Skills format works with Claude Code natively, and
              with any other tool that can read project files.
            </p>
          </div>

          <div className="mt-10 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <p className="text-[#57534E] max-w-xl leading-relaxed">
              The interactive showcase demonstrates ten core styles as working
              components with keyboard navigation and reduced-motion support,
              plus the full 27-style catalog.
            </p>
            <Button asChild size="lg" className="bg-[#C2410C] hover:bg-[#9A3412] text-white h-12 px-6 rounded-md shrink-0">
              <a href={withBase("/showcase/index.html")} target="_blank" rel="noopener">
                Open the showcase
                <ExternalLink size={16} className="ml-2" aria-hidden="true" />
              </a>
            </Button>
          </div>
        </section>
      </main>

      <SiteFooter />
    </div>
  );
}
