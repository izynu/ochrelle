import type { NextConfig } from "next";

/**
 * NEXT_PUBLIC_STATIC_EXPORT=1 switches the build to a fully static export: a
 * plain out/ folder of HTML, CSS, and JS that runs on any web host (GitHub
 * Pages, shared hosting, cPanel, Apache, Nginx, S3). Default remains the
 * standalone server build used by the dev sandbox.
 */
const isStaticExport = process.env.NEXT_PUBLIC_STATIC_EXPORT === "1";

const nextConfig: NextConfig = {
  // Pin the workspace root to this folder so Next.js never walks up the
  // directory tree and picks up a parent project's config (nested git
  // checkouts, the deployment kit layout, CI workspaces).
  turbopack: {
    root: __dirname,
  },
  typescript: {
    ignoreBuildErrors: true,
  },
  reactStrictMode: false,
  ...(isStaticExport
    ? {
        output: "export",
        trailingSlash: true,
        images: { unoptimized: true },
        // GitHub Pages project sites are served from /<repository-name>.
        // The deploy workflow passes NEXT_PUBLIC_BASE_PATH=/ochrelle (or an
        // empty value when a CNAME custom domain is present).
        basePath: process.env.NEXT_PUBLIC_BASE_PATH || undefined,
      }
    : {
        output: "standalone",
      }),
};

export default nextConfig;
