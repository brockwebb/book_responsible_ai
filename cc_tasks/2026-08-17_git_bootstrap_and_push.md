# CC TASK — bootstrap git repo, create GitHub repo, push, enable Pages

**Date:** 2026-08-17 · **Status:** dispatched
**Context:** `handoffs/HANDOFF_2026-08-17_cowork-to-claude-code.md` — full background on why
this is a Claude Code task and not a Cowork one (Cowork's cloud sandbox has no network
access on the device-bash path and no usable GitHub token scope for this repo). Read that
file first if anything below is ambiguous.

## Change

1. **Clear stale git state before anything else** — a prior Cowork session attempted
   `git init && git add -A` locally and left a stuck `.git/index.lock` it couldn't clear
   (its sandbox can't delete files). There may be a broken `.git/` directory in the repo
   root. Do not assume it's usable:
   ```bash
   cd ~/GitHub/book_responsible_ai
   rm -rf .git
   ```
2. **Init and commit:**
   ```bash
   git init -b main
   git add -A
   git status --short   # sanity check below
   git commit -m "Organize manuscript, art assets, and MyST publishing structure"
   ```
   Sanity check on `git status --short` before committing: `arc/`, `cc_tasks/`,
   `handoffs/`, `audits/`, and `.DS_Store` must NOT appear (all gitignored per
   `.gitignore`). If any of them show up, stop and fix `.gitignore` matching before
   committing — do not commit session scaffolding or rejected art variants into the
   public repo.
3. **Create the GitHub repo and push** (public, per standing decision — see README's
   license section):
   <!-- SUPERSEDED 2026-08-17: this step originally added "this is headed toward
   commercial distribution but the repo itself is public". That commercial-intent
   claim was wrong and has been purged per
   cc_tasks/2026-08-17_addendum_assets_untracked_masters.md step 4. The book is
   CC BY 4.0. The repo being public is unchanged and was always correct. -->

   ```bash
   gh repo create brockwebb/book_responsible_ai --public --source=. --remote=origin --push
   ```
   If `gh` isn't authenticated or available, create the repo manually at
   github.com/new — public, **no** README/gitignore/license (all three already exist
   locally, adding them on GitHub's side will conflict) — then:
   ```bash
   git remote add origin git@github.com:brockwebb/book_responsible_ai.git
   git push -u origin main
   ```
4. **Enable GitHub Pages:** repo Settings → Pages → set source to "GitHub Actions".
   This lets `.github/workflows/deploy.yml` publish the MyST web edition on push to
   `main`. (Cannot be done from the CLI; flag back if it needs to stay a manual
   browser step for the user.)
5. **Copy `CLAUDE.md` into place** — a draft was prepared during the Cowork session
   and delivered to the user as a file; if it's not already at the repo root, ask the
   user for it or regenerate from this task's sibling context rather than guessing.
   Confirm it's the version tracked at commit time in step 2, not added after (add it
   in step 2's `git add -A` if present before committing; otherwise a follow-up commit
   is fine, just don't leave it untracked).

## Verification (required, RESULT sidecar)

1. `git status --short` immediately before the commit in step 2 — attach output,
   confirm none of `arc/`, `cc_tasks/`, `handoffs/`, `audits/`, `.DS_Store` are listed.
2. `git log --oneline -1` and `git remote -v` at close — confirm one commit, `origin`
   points at `github.com/brockwebb/book_responsible_ai`.
3. `gh repo view brockwebb/book_responsible_ai` (or manual confirmation) — repo exists,
   is public, default branch is `main`.
4. Pages: confirm source is set to "GitHub Actions" in Settings, or explicitly flag
   that this step was skipped/blocked and needs the user.
5. Note whether `.github/workflows/deploy.yml` ran (Actions tab) and whether it
   succeeded — first real build may surface path/config issues per the handoff's open
   items; a failed first build is expected-possible, not a task failure, but report it.

## Result

Write `cc_tasks/2026-08-17_git_bootstrap_and_push_RESULT.md` in the repo. Note there:
final commit hash, repo URL, Pages status, and whether the two open items from the
handoff (`b_colorpage.png` reference, image sizing) were left untouched (they should
be — out of scope for this task) or need a follow-up task filed.
