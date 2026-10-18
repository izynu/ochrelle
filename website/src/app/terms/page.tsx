import type { Metadata } from "next";
import Link from "next/link";
import { PigmentChip } from "@/components/pigment-chip";
import { SiteFooter } from "@/components/site-footer";

export const metadata: Metadata = {
  title: "Terms and Conditions",
  description:
    "Terms for using the Ochrelle website and the MIT-licensed Ochrelle repository.",
};

const SECTIONS = [
  {
    title: "The service",
    body: "Ochrelle is an open-source repository of design skills for AI coding agents, published as technical documentation and a web showcase. These terms govern your use of the website. Use of the software and content in the repository is governed by its license, described below.",
  },
  {
    title: "License",
    body: "The repository is released under the MIT License. You may use, copy, modify, merge, publish, distribute, sublicense, and sell copies of it, subject to the license text included in the LICENSE file. The license grant applies to the repository content, not to services or content provided by third parties.",
  },
  {
    title: "No warranty",
    body: "The website and the repository are provided AS IS, WITHOUT WARRANTY OF ANY KIND, express or implied, including the implied warranties of merchantability, fitness for a particular purpose, and non-infringement. Design guidance produced by these skills is advisory. You remain responsible for reviewing, testing, and approving anything you ship with it.",
  },
  {
    title: "Limitation of liability",
    body: "To the maximum extent permitted by law, the Ochrelle contributors are not liable for any claim, damages, or other liability arising from, out of, or in connection with the website, the repository, or your use of them.",
  },
  {
    title: "Acceptable use",
    body: "Do not interfere with the operation of the site, attempt to gain unauthorized access to hosting infrastructure, or use the site to distribute unlawful content. Automated crawling that degrades service for others is not permitted.",
  },
  {
    title: "Contributions",
    body: "Contributions to the repository are welcome under the process described in CONTRIBUTING.md. By submitting a contribution, you agree that it is licensed under the same MIT License as the repository, and you confirm you have the right to submit it.",
  },
  {
    title: "Intellectual property",
    body: "The repository content is licensed as stated above. Product names, styles referenced in the documentation, and trademarks of third parties belong to their respective owners and are referenced for identification only.",
  },
  {
    title: "Availability",
    body: "The site is served on a best-effort basis. Features, pages, or the showcase may change or be removed without notice.",
  },
  {
    title: "Changes to these terms",
    body: "We may update these terms as the project evolves. The current version is always published on this page with an effective date. Continued use of the site after a change constitutes acceptance.",
  },
];

export default function TermsPage() {
  return (
    <div className="min-h-screen flex flex-col bg-[#FAFAF9] text-[#1C1917]">
      <header className="border-b border-[#E7E5E4] bg-[#FAFAF9]">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
          <Link href="/" className="flex items-center gap-3 group">
            <span className="w-8 h-8 rounded-md bg-[#1C1917] flex items-center justify-center">
              <PigmentChip size={17} maskId="ochrelle-chip-terms" />
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
            Terms and Conditions
          </h1>
          <p className="mt-3 text-[#57534E]">
            Effective date: October 18, 2026. Governs use of the Ochrelle
            website. Repository code is governed by its MIT License.
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
              Questions about these terms can be opened as an issue in the
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
