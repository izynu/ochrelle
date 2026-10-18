import type { Metadata } from "next";
import { IBM_Plex_Sans, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";
import { SITE_URL } from "@/lib/site";

const plexSans = IBM_Plex_Sans({
  variable: "--font-plex-sans",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-jetbrains-mono",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

/**
 * Production origin used for canonical URLs and Open Graph metadata.
 * Lives in src/lib/site.ts. The default is the GitHub Pages project site;
 * override at build time with NEXT_PUBLIC_SITE_URL=https://your-domain.com
 * (the GitHub Actions deploy workflow sets this automatically, including
 * for custom domains detected via a CNAME file).
 */
export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: "Ochrelle: design intelligence skills for AI coding agents",
    template: "%s | Ochrelle",
  },
  description:
    "28 open-source Agent Skills that give coding agents real art direction. One master skill picks the visual style; 27 specialists execute it with WCAG 2.2 AA guidance. MIT licensed.",
  keywords: [
    "Ochrelle",
    "Agent Skills",
    "AI coding agents",
    "design system",
    "open source",
  ],
  authors: [{ name: "Zynu" }, { name: "Shraddha" }],
  openGraph: {
    title: "Ochrelle: design intelligence skills for AI coding agents",
    description:
      "28 open-source Agent Skills for art direction. One router, 27 style specialists, WCAG 2.2 AA guidance throughout.",
    url: SITE_URL,
    siteName: "Ochrelle",
    type: "website",
  },
  twitter: {
    card: "summary",
    title: "Ochrelle: design intelligence skills for AI coding agents",
    description:
      "28 open-source Agent Skills for art direction. One router, 27 style specialists, WCAG 2.2 AA guidance throughout.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      suppressHydrationWarning
      className={`${plexSans.variable} ${jetbrainsMono.variable}`}
    >
      <body className="antialiased bg-background text-foreground">
        {children}
        <Toaster />
      </body>
    </html>
  );
}
