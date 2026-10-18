/**
 * Central place for URLs that depend on where the site is deployed.
 *
 * Ochrelle is deployed GitHub-only: the repository's GitHub Actions workflow
 * (deploy-pages.yml) builds this site as a static export and publishes it to
 * GitHub Pages for free.
 *
 * - Project site: https://izynu.github.io/ochrelle/
 * - Custom domain: a CNAME file at the repository root makes the workflow
 *   rebuild for the domain root (no base path) with matching metadata.
 *
 * NEXT_PUBLIC_STATIC_EXPORT=1 switches the build to static export mode. In that
 * mode the large local zip files are not shipped; the download buttons point
 * at GitHub instead. In dev (this sandbox) the local zip files are served
 * from /download/.
 */

export const GITHUB_URL = "https://github.com/izynu/ochrelle";

/** GitHub builds this archive on demand from the repository. */
export const REPO_ZIP_URL = `${GITHUB_URL}/archive/refs/heads/main.zip`;

export const SITE_URL =
  process.env.NEXT_PUBLIC_SITE_URL || "https://izynu.github.io/ochrelle";

const BASE_PATH = process.env.NEXT_PUBLIC_BASE_PATH || "";

/**
 * Prefix a site-absolute path with the GitHub Pages base path.
 * next/link handles this automatically; plain <a> tags need this helper.
 */
export function withBase(path: string): string {
  return `${BASE_PATH}${path}`;
}

/** True while building the static export that GitHub Pages serves. */
export const IS_STATIC_EXPORT = process.env.NEXT_PUBLIC_STATIC_EXPORT === "1";
