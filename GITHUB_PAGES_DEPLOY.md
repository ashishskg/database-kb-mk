# GitHub Pages Deployment (Public)

This repository is configured to publish the MkDocs site to GitHub Pages using GitHub Actions.

## Prerequisites

- A GitHub.com repository
- This project pushed to the repository
- Default branch named `main` (the workflow deploys on pushes to `main`)

## Files already included in this repo

- `requirements.txt`
  - Pins MkDocs so GitHub Actions builds with a consistent version.
- `.github/workflows/deploy-mkdocs.yml`
  - Builds the site with MkDocs and deploys the generated `site/` directory to GitHub Pages.

## Steps

## 1) Create a repository on GitHub.com

- Create a new repository (any name).
- Choose Public if you want the published documentation to be accessible to anyone.

## 2) Push this project to GitHub

From your local project directory:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<org-or-user>/<repo>.git
git push -u origin main
```

If your repo already exists locally, just ensure you are pushing to `main`.

## 3) Enable GitHub Pages for the repository

In GitHub:

- Open the repo
- Go to `Settings` -> `Pages`
- Under **Build and deployment**
  - Set **Source** to `GitHub Actions`

## 4) Trigger a deployment

The workflow runs automatically on:

- Every push to `main`

You can also run it manually:

- Repo -> `Actions` -> `Deploy MkDocs to GitHub Pages` -> `Run workflow`

## 5) Get the public URL

After the workflow completes, GitHub will show the published URL in:

- `Settings` -> `Pages`

Typical format:

- `https://<org-or-user>.github.io/<repo>/`

## Troubleshooting

- If the workflow fails, check:
  - Repo -> `Actions` -> latest run logs
- If Pages shows 404, confirm:
  - `Settings` -> `Pages` -> **Source** is `GitHub Actions`
  - The workflow completed successfully
- If your default branch is not `main`, update `.github/workflows/deploy-mkdocs.yml` to match.
