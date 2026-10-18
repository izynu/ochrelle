# Publishing Ochrelle on GitHub

Step-by-step, from this folder to a public repository. Commands assume the
repository folder is called `ochrelle`.

## 1. Prepare the repository locally

```bash
cd ochrelle

# Initialize git (skip if the folder already has a .git directory)
git init -b main

# Sanity checks before the first commit
python3 scripts/validate_skills.py      # expect 28/28
python3 scripts/validate_repository.py  # expect 9/9
python3 -m pytest tests/ -q             # expect all pass
```

## 2. Owner fields (already filled)

The owner fields are filled in and point at the current maintainer:

- Copyright holders: **Zynu and Shraddha** (`LICENSE` line 3)
- Repository URLs and contacts: **github.com/izynu/ochrelle**
  (`CHANGELOG.md`, `CITATION.cff`, `README.md`, `SECURITY.md`,
  `SUPPORT.md`, `CODE_OF_CONDUCT.md`)

If the GitHub username ever changes, run this from the repository root and
commit the result:

```bash
grep -rl "izynu" . --include="*.md" --include="*.cff" | \
  xargs sed -i 's/izynu/NEW-USERNAME/g'
```

## 3. Commit

```bash
git add -A
git commit -m "Ochrelle 2.0.0: 28 Agent Skills for interface art direction"
git tag v2.0.0
```

## 4. Create the GitHub repository and push

With the GitHub CLI (recommended):

```bash
gh auth login
gh repo create ochrelle --public --source=. --push
git push origin v2.0.0
```

Without the GitHub CLI:

1. Create an empty repository named `ochrelle` on github.com
   (no README, no .gitignore, no license: the repo already ships all three).
2. Add the remote and push:

```bash
git remote add origin https://github.com/izynu/ochrelle.git
git push -u origin main
git push origin v2.0.0
```

## 5. Make it citable and discoverable

- About panel: description "28 Agent Skills for interface art direction.
  One router, 27 style specialists. MIT." + topics: `agent-skills`,
  `design-system`, `ui-ux`, `ai-agents`, `design-tokens`.
- Releases: create a release from tag `v2.0.0` and attach
  `ochrelle-2.0.0.zip` (the same archive linked from the website).
- CITATION.cff makes GitHub show a "Cite this repository" button.

## 6. Publish the website on GitHub Pages (free, included)

The repository hosts its own website in `website/` (the full Next.js site:
hero, skill catalog, verification commands, privacy, terms). The included
workflow `.github/workflows/deploy-pages.yml` builds it as a static export
and publishes it to GitHub Pages on every push to `main`.

Short version:

1. Push the repository (step 4).
2. On GitHub, open **Settings > Pages** and set **Source** to
   **GitHub Actions**.
3. Re-run the deploy workflow if it ran before Pages was enabled.
4. The site goes live at `https://izynu.github.io/ochrelle/`.

## 7. Optional: a custom domain, and where the full walkthrough lives

The complete, current deployment guide is **`DEPLOY.md`** at the repository
root. It covers the GitHub Pages activation, verification, serving the site
from a domain you already own (a `CNAME` file plus four DNS records; the
workflow handles the rebuild automatically), and troubleshooting.

Earlier versions of this document pointed the full website at a separate
hosting platform (Vercel) and a registered domain. That is no longer
necessary: the repository is self-hosting on GitHub Pages.

The separate `.github/workflows/validate.yml` runs the validators and tests
on every push, so broken content cannot land quietly.
