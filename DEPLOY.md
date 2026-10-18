# Deploying Ochrelle on GitHub

The whole project lives in this one repository, and GitHub Pages hosts the
website for free. No Vercel, no paid hosting, no extra services. The only
requirement is a free GitHub account.

What you end up with:

- Repository: `https://github.com/izynu/ochrelle`
- Website: `https://izynu.github.io/ochrelle/` (served by GitHub Pages)
- The download buttons on the website point at GitHub, so code, site, and
  downloads all live in one place

The repository ships a ready workflow (`.github/workflows/deploy-pages.yml`)
that builds `website/` into a static export and publishes it on every push
to `main`.

## 1. Create the repository on GitHub

1. Sign in at github.com (account `izynu`, or your own account).
2. Click **New repository**.
3. Name: `ochrelle`.
4. Visibility: **Public**. GitHub Pages is free for public repositories;
   private repositories need a paid plan for Pages.
5. Do **not** initialize with a README, .gitignore, or license. This folder
   already ships all three.

## 2. Push the repository

From the folder containing this file (it has a ready `.git` history):

```bash
cd ochrelle
git remote add origin https://github.com/izynu/ochrelle.git
git branch -M main
git push -u origin main
git push origin v2.0.0
```

Git will open a browser window to authenticate (or accept a personal access
token). With the GitHub CLI instead:

```bash
gh auth login
gh repo create ochrelle --public --source=. --push
git push origin v2.0.0
```

If the folder ever loses its `.git` directory, recreate the history first:

```bash
git init -b main
git add -A
git commit -m "Ochrelle 2.0.0: 28 Agent Skills for interface art direction"
git tag v2.0.0
```

## 3. Turn on GitHub Pages

The website is deployed by the included workflow, but Pages must be pointed
at it once:

1. Open the repository on GitHub, then **Settings > Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. The first push already triggered the deploy workflow. If it ran before
   you completed step 2, open the **Actions** tab, select the latest
   **Deploy website to GitHub Pages** run, and click **Re-run jobs**.

Within a minute or two the site is live at
`https://izynu.github.io/ochrelle/`.

## 4. Verify the deployment

- The home page renders with styles, fonts, and the ochre pigment-chip mark.
- **Privacy** and **Terms** open from the footer.
- **Showcase** opens the interactive style demo.
- **Download the repo (.zip)** lands on a GitHub archive download.
- No mixed-content or console errors in the browser dev tools.

## 5. Optional: serve the site from your own domain

The site is complete without this step. To use a domain you already own:

1. At the repository root, add a file named `CNAME` (no extension) whose
   single line is your domain, for example:

   ```text
   ochrelle.example.com
   ```

   Commit and push it. The deploy workflow detects the file, rebuilds the
   site for the domain root (no `/ochrelle/` prefix, matching metadata), and
   publishes the `CNAME` marker with the site.

2. Point the DNS records at GitHub, wherever the domain's DNS is managed
   (registrar or current host's DNS panel):

   | Record | Name | Value |
   | --- | --- | --- |
   | A | `@` | `185.199.108.153` |
   | A | `@` | `185.199.109.153` |
   | A | `@` | `185.199.110.153` |
   | A | `@` | `185.199.111.153` |
   | CNAME | `www` | `izynu.github.io` |

3. Back on GitHub: **Settings > Pages > Custom domain**, enter the domain,
   save, and wait for the DNS check to pass. Then tick **Enforce HTTPS**
   (it becomes available once the certificate is issued).

Your existing hosting account is not needed to serve the site; only its DNS
panel (or your registrar's) is used to point records at GitHub.

## 6. Updating the site later

Edit files, commit, push to `main`. The workflow rebuilds and republishes
automatically. Site source lives in `website/` (see `website/README.md` for
local development commands). Before pushing repository content changes
(skills, docs), run the validators:

```bash
python3 scripts/validate_skills.py      # expect 28/28
python3 scripts/validate_repository.py  # expect 9/9
python3 -m pytest tests/ -q             # expect all pass
```

## Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| Deploy job fails or the page 404s right after the first push | Pages source was not set yet. Finish step 3, then re-run the workflow. |
| Site loads but styles and scripts are missing | The workflow writes `.nojekyll` (GitHub otherwise ignores folders starting with an underscore, like `_next/`). Make sure the **Finalize the output folder** step ran in the workflow. |
| Pages shows the old one-page showcase | An older workflow run is still published. Re-run the latest **Deploy website to GitHub Pages** run. |
| "Verify the build output" step fails | The step prints exactly which file is missing. Re-run after fixing; the build must produce `index.html`, `privacy/`, and `terms/`. |
| Repository is private and Pages refuses to deploy | Pages for private repositories needs a paid plan. Make the repository public. |
| Custom domain shows the `github.io` address or wrong links | The `CNAME` file must sit at the repository root and the DNS records above must exist. Once both are in place, push (or re-run the workflow) and the site rebuilds for the domain. |
| Push asks for credentials in a headless terminal | Use `gh auth login`, or create a personal access token and paste it as the password. |

## Why GitHub only

Earlier versions of this kit assumed a second platform (Vercel) for the
Next.js site and a separately registered domain. None of that is needed:
one repository, one workflow, free hosting, and a custom domain is strictly
optional.
