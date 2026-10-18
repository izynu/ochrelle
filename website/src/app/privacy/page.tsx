import type { Metadata } from "next";
import Link from "next/link";
import { PigmentChip } from "@/components/pigment-chip";
import { SiteFooter } from "@/components/site-footer";

export const metadata: Metadata = {
  title: "Privacy Policy",
  description:
    "What the Ochrelle website collects, stores, and shares. Short version: nothing beyond standard hosting logs.",
};

const SECTIONS = [
  {
    title: "Scope",
    body: "This policy covers the Ochrelle website and its showcase pages. It does not cover third-party sites linked from here, such as external documentation or the agentskills.io specification. Those sites have their own policies.",
  },
  {
    title: "What we collect",
    body: "This site is static. Pages are plain HTML, CSS, and JavaScript served from a web server. The site itself does not collect, store, or process personal data. Your hosting provider may record standard server logs, such as IP address, requested URL, user agent, and timestamp, for security and reliability. Log retention is governed by the hosting provider's own policy.",
  },
  {
    title: "Cookies",
    body: "This site sets no cookies and uses no cookie-based sessions. No consent banner is needed because no tracking technologies are present.",
  },
  {
    title: "Analytics and advertising",
    body: "The site embeds no analytics scripts, no advertising networks, and no third-party trackers. If analytics are ever added, this page will be updated before that change ships.",
  },
  {
    title: "Fonts and assets",
    body: "Fonts (IBM Plex Sans and JetBrains Mono) are self-hosted as part of the build output. They are served from the same origin as the site, so no request is sent to a font vendor when you visit.",
  },
  {
    title: "Third parties",
    body: "The only third-party interaction is your connection to the hosting provider that serves the pages. The site makes no background requests to other domains.",
  },
  {
    title: "Children",
    body: "This site is technical documentation for software developers. It is not directed at children, and no personal information is collected from any visitor.",
  },
  {
    title: "Your rights",
    body: "Because the site collects no personal data, there is nothing to export, correct, or delete. Requests about server-side hosting logs should be directed to the hosting provider.",
  },
  {
    title: "Changes",
    body: "Material changes to this policy will be published on this page with an updated effective date. The effective date shown below reflects the current version.",
  },
];

export default function PrivacyPage() {
  return (
    <div className="min-h-screen flex flex-col bg-[#FAFAF9] text-[#1C1917]">
      <header className="border-b border-[#E7E5E4] bg-[#FAFAF9]">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
          <Link href="/" className="flex items-center gap-3 group">
            <span className="w-8 h-8 rounded-md bg-[#1C1917] flex items-center justify-center">
              <PigmentChip size={17} maskId="ochrelle-chip-privacy" />
            </span>
            <span className="font-semibold tracking-tight">Ochrelle</span>
          </Link>
          <Link
            href="/"
            className="text-sm text-[#57534E] hover:text-[#C2410C] transition-colors duration-200"
          >
            Back to home
          </Link>
        </div>
      </header>

      <main className="flex-1">
        <article className="max-w-3xl mx-auto px-4 sm:px-6 py-12 sm:py-16">
          <p className="text-sm font-mono text-[#C2410C] mb-3">Legal</p>
          <h1 className="text-3xl sm:text-4xl font-bold tracking-tight">
            Privacy Policy
          </h1>
          <p className="mt-3 text-[#57534E]">
            Effective date: October 18, 2026. Applies to the Ochrelle website
            and showcase.
          </p>

          <div className="mt-10 space-y-8">
            {SECTIONS.map((s) => (
              <section key={s.title}>
                <h2 className="text-lg font-semibold tracking-tight">{s.title}</h2>
                <p className="mt-2 text-[#57534E] leading-relaxed">{s.body}</p>
              </section>
            ))}
          </div>

          <div className="mt-12 p-5 border border-[#E7E5E4] rounded-md bg-white">
            <h2 className="font-semibold tracking-tight">Contact</h2>
            <p className="mt-2 text-sm text-[#57534E] leading-relaxed">
              Questions about this policy can be opened as an issue in the
              Ochrelle repository, or sent through the contact channel listed
              in the repository README.
            </p>
          </div>
        </article>
      </main>

      <SiteFooter />
    </div>
  );
}
