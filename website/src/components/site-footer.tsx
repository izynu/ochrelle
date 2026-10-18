import Link from "next/link";
import { PigmentChip } from "@/components/pigment-chip";
import { withBase } from "@/lib/site";

const links = [
  { href: "/", label: "Home" },
  { href: withBase("/showcase/index.html"), label: "Showcase", external: true },
  { href: "/privacy", label: "Privacy" },
  { href: "/terms", label: "Terms" },
];

export function SiteFooter() {
  return (
    <footer className="mt-auto border-t border-[#E7E5E4] bg-[#FAFAF9]">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 py-8 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 pb-[max(2rem,env(safe-area-inset-bottom))]">
        <div className="flex items-center gap-2.5">
          <span className="w-7 h-7 rounded-md bg-[#1C1917] flex items-center justify-center">
            <PigmentChip size={15} maskId="ochrelle-chip-footer" />
          </span>
          <div className="text-sm text-[#57534E]">
            <p className="font-semibold text-[#1C1917]">Ochrelle</p>
            <p>&copy; 2026 Zynu and Shraddha. Open source under the MIT license. v2.0.0.</p>
          </div>
        </div>
        <nav aria-label="Footer">
          <ul className="flex flex-wrap items-center gap-x-5 gap-y-2 text-sm">
            {links.map((l) => (
              <li key={l.href}>
                {l.external ? (
                  <a
                    href={l.href}
                    className="text-[#57534E] hover:text-[#C2410C] transition-colors duration-200"
                  >
                    {l.label}
                  </a>
                ) : (
                  <Link
                    href={l.href}
                    className="text-[#57534E] hover:text-[#C2410C] transition-colors duration-200"
                  >
                    {l.label}
                  </Link>
                )}
              </li>
            ))}
          </ul>
        </nav>
      </div>
    </footer>
  );
}
