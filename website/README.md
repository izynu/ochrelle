# Ochrelle website

The Next.js source of the Ochrelle project website: the page you are reading
on GitHub Pages, plus the privacy and terms pages. It is a fully static site:
no database, no API routes, no server runtime.

GitHub Actions builds this folder and publishes it (see
`.github/workflows/deploy-pages.yml` at the repository root, and `DEPLOY.md`
for the walkthrough). You can also run it locally:

```bash
bun install
bun run dev        # development server

# Static export, the same thing CI builds for GitHub Pages:
NEXT_PUBLIC_STATIC_EXPORT=1 NEXT_PUBLIC_BASE_PATH=/ochrelle bun run build
# output lands in out/
```

Environment variables understood at build time:

- `NEXT_PUBLIC_STATIC_EXPORT=1` switches from the standalone server build to a
  static `out/` folder.
- `NEXT_PUBLIC_BASE_PATH=/ochrelle` prefixes all URLs for GitHub Pages
  project sites. Leave it empty when serving from a domain root.
- `NEXT_PUBLIC_SITE_URL` sets the origin used for canonical and Open Graph
  metadata. Defaults to `https://izynu.github.io/ochrelle`.
