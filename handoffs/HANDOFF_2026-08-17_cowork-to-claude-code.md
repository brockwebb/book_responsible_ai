# Handoff: book_responsible_ai — Cowork session → Claude Code

**Date:** 2026-08-17
**From:** Claude (Cowork, cloud sandbox session)
**To:** Claude Code, run locally against `/Users/brock/GitHub/book_responsible_ai`
**Why this handoff exists:** Cowork's cloud sandbox has no working path to create the GitHub repo or push to it (details below). Everything else — file reorganization, manuscript/book content — is done and correct on disk. Claude Code should pick up from "make this a real git repo on GitHub" onward.

---

## 1. What this project is

*The Overresponsible AI Handbook: An Alphabetical Guide to Doing Nothing, Responsibly* — a satirical A–Z alphabet book on AI governance theater. Each letter: a koan, a full-page color illustration, a one-line definition. Bonus section in the back: 26 coloring pages (lineart versions of the same illustrations). Ebook-first (PDF + a MyST-built web/GitHub "book" edition) — no print run planned.

Structural model was copied from a sibling repo, `/Users/brock/GitHub/ai-workflow-design` (a MyST-based book with the same book/, assets/, .github/workflows/deploy.yml pattern) — reference it if anything below is ambiguous.

## 2. Current state of `/Users/brock/GitHub/book_responsible_ai` (all done, verified on disk)

```
book_responsible_ai/
├── README.md                  # project overview, structure, build commands
├── .gitignore                 # see §4 — includes arc/, book/_build/, etc.
├── .github/workflows/deploy.yml   # MyST build → GitHub Pages, on push to main
├── manuscript/                 # source prose (editorial working copy)
│   ├── 01_front_matter.md
│   ├── 02_alphabet.md
│   ├── 03_back_matter.md
│   ├── 04_coloring_pages.md    # new stub for the bonus section
│   └── art_selections.md       # which art file is used per letter (now finalized, see §5)
├── book/                        # MyST publishing project — this is what gets built
│   ├── myst.yml                  # title, TOC, exports config
│   ├── cover.md, front-matter.md, alphabet.md, back-matter.md, coloring-pages.md
│   ├── images/facer/               # 26 files, final color illustrations, copied from assets/art/facer/
│   ├── images/lineart/              # 26 files, final coloring-page lineart, copied from assets/art/lineart/
│   ├── images/cover.png              # cover art
│   └── exports/                        # empty, PDF build output goes here (gitignored)
├── assets/art/                   # source copies of the FINAL selected art (one set, not variants)
│   ├── facer/                      # 26 files
│   ├── lineart/                     # 26 files
│   └── cover/                         # 1 file (0-OAIH-BookCover.png)
├── arc/                            # 51 old/rejected art variants + 2 .xcf source files — GITIGNORED, not part of the book
├── cc_tasks/, handoffs/              # empty / working dirs, gitignored
└── (no .git yet — see §3)
```

Title used throughout: **The Overresponsible AI Handbook: An Alphabetical Guide to Doing Nothing, Responsibly**.

> **[SUPERSEDED 2026-08-17 — DO NOT ACT ON THE ORIGINAL TEXT HERE]**
> This paragraph originally asserted that the book had no LICENSE file "deliberately",
> defaulted to all-rights-reserved, and was headed toward commercial distribution "unlike
> the CC-BY `ai-workflow-design`". **That was wrong and is the sentence that re-seeded an
> incorrect license decision into CLAUDE.md and README.md.** The stale assertion has been
> purged per `cc_tasks/2026-08-17_addendum_assets_untracked_masters.md` step 4.
> **The book is CC BY 4.0**, the same license as `ai-workflow-design`. See
> `cc_tasks/2026-08-17_license_cc_by_4.md` and its RESULT.

## 3. What's blocked — the actual reason for this handoff

Three independent dead ends hit in the Cowork session, in case any of this is useful debugging context later:

1. **Cowork's local-device shell (`device_bash`) has no network access at all.** Confirmed via `curl` — flat failure. `git push`/`git clone`/`gh` anything was never going to work from there.
2. **That same shell also cannot delete files** (its sandbox policy). Mid-session, a `git init && git add -A` was attempted there to at least get local history started — it left a stuck `.git/index.lock` that couldn't be cleared, because clearing it requires deleting a file. **There may still be a broken `.git/` directory in the repo root from this attempt.** Claude Code should run `rm -rf .git` before doing anything else, to be safe — do not assume any existing `.git/` folder is usable.
3. **Cowork's cloud sandbox has its own GitHub token, but it's scoped only to a repo the session was launched against** — this session wasn't launched from any repo, so it had zero usable scope. Confirmed via direct API calls: both `GET /repos/brockwebb/book_responsible_ai` and `POST /user/repos` returned 403 "sessions are bound to their configured repositories."
4. **Bonus finding, not blocking but worth flagging:** the user's locally-connected GitHub MCP connector (visible to Cowork via the device bridge, normally used for `mcp__remote-devices__github__*` tools) returned "Bad credentials" when asked to create a repo. That connector may need re-authentication in Claude Desktop's connector settings if it's meant to keep working for future Cowork sessions.

None of this should be a problem for Claude Code running locally with the user's normal terminal/git/gh setup (the same one that already pushed `ai-workflow-design` to GitHub).

## 4. Next steps for Claude Code

```bash
cd ~/GitHub/book_responsible_ai

# Clear any stale/broken git state from the Cowork attempt — do this even if .git looks fine
rm -rf .git

git init -b main
git add -A
git status --short   # sanity check: arc/, cc_tasks/, handoffs/, audits/, .DS_Store should NOT appear (gitignored)
git commit -m "Organize manuscript, art assets, and MyST publishing structure"

# Create the GitHub repo and push (public, per user's earlier decision)
gh repo create brockwebb/book_responsible_ai --public --source=. --remote=origin --push
```

If `gh` isn't authenticated or available, create the repo manually at github.com/new (public, **no** README/gitignore/license — all three already exist locally) and instead run:

```bash
git remote add origin git@github.com:brockwebb/book_responsible_ai.git
git push -u origin main
```

After that, GitHub Pages needs to be enabled once in the repo's Settings → Pages → "GitHub Actions" as the source, so `.github/workflows/deploy.yml` can publish the MyST web edition on push to `main`.

## 5. Open items / things the user still owns

- **Sanity check on B's lineart:** `manuscript/art_selections.md` used to reference `b_colorpage.png`, but no such file exists anywhere in the project (checked root and `arc/`). Only `b_lineart.png` exists, and that's what's wired into the book now. Confirm nothing was lost, or this is a non-issue.
- **Image sizing/resolution for ebook delivery:** explicitly flagged by the user as a later task, not started. Both `book/images/` and `assets/art/` currently hold the original full-resolution PNGs (roughly 1.3–6.3MB each). Since this is ebook-only (PDF + web, no print), these are very likely oversized for on-screen delivery — worth a pass to check actual pixel dimensions against reasonable ebook/web targets and downsize if needed. The user mentioned "8×10 paper as a general size guide" as a rough reference point even though this isn't going to print.
- **Build has not been tested.** No one has run `myst build --html` or the typst PDF export against this content yet — first real build may surface path or config issues in `book/myst.yml`.
- **`assets/art/archive/`** is an empty leftover directory from an earlier (corrected) reorganization attempt — harmless, not tracked by git, safe to ignore or remove.

## 6. Reference

Sibling repo used as the structural template: `/Users/brock/GitHub/ai-workflow-design` — same book/, assets/, MyST + typst + GitHub Pages pattern, further along in its build pipeline (has `scripts/build_pdf.py`, `table_map.yaml`, etc. worth borrowing from once this book needs its own PDF build script).
