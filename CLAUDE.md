# CLAUDE.md — The Overresponsible AI Handbook

## Project Overview

*The Overresponsible AI Handbook: An Alphabetical Guide to Doing Nothing, Responsibly* — a satirical A–Z alphabet book on AI governance theater. Twenty-six letters, each pairing a koan, a full-page color illustration, and a one-line definition. Bonus back-matter section: 26 coloring pages (lineart versions of the same illustrations).

It's satire with a straight face underneath — see the Author's Note in the front matter.

**Repo:** `brockwebb/book_responsible_ai`
**Author:** Brock Webb
**Format:** Ebook-first — PDF edition + a web/GitHub "book" edition (MyST). No print run planned.
**License:** All rights reserved — no LICENSE file, deliberate (commercial work, unlike the CC-BY `ai-workflow-design`).

Structural model copied from the sibling repo `/Users/brock/GitHub/ai-workflow-design` (MyST-based book, same `book/`, `assets/`, `.github/workflows/deploy.yml` pattern). Reference it if anything here is ambiguous — it's further along in its build pipeline (has `scripts/build_pdf.py`, `table_map.yaml`, etc.) and its `cc_tasks/`/`handoffs/` history is the model for the conventions below.

## Project Structure

```
book_responsible_ai/
├── CLAUDE.md              # This file — project context for AI assistants
├── README.md              # Public-facing project description
├── manuscript/            # Source prose — editorial working copy
│   ├── 01_front_matter.md
│   ├── 02_alphabet.md
│   ├── 03_back_matter.md
│   ├── 04_coloring_pages.md
│   └── art_selections.md  # which art file is used per letter (finalized)
├── book/                  # MyST publishing project — this is what gets built
│   ├── myst.yml              # title, TOC, exports config
│   ├── cover.md, front-matter.md, alphabet.md, back-matter.md, coloring-pages.md
│   ├── images/facer/          # 26 files, final color illustrations
│   ├── images/lineart/         # 26 files, final coloring-page lineart
│   ├── images/cover.png         # cover art
│   └── exports/                  # PDF build output (gitignored)
├── assets/art/            # Source copies of the FINAL selected art (one set, not variants)
│   ├── facer/                 # 26 files
│   ├── lineart/                # 26 files
│   ├── cover/                   # 1 file (0-OAIH-BookCover.png)
│   └── archive/                  # empty leftover dir — see Open Items
├── arc/                    # 51 old/rejected art variants + .xcf sources — GITIGNORED
├── cc_tasks/                # Task specifications — gitignored, local working dir
├── handoffs/                 # Session handoff documents — gitignored, local working dir
└── .github/workflows/deploy.yml   # MyST build → GitHub Pages, on push to main
```

`.gitignore` also excludes `audits/`, `/docs/`, `.claude/`, `book/_build/`, and
`book/exports/*.pdf` — none of those are published. The art in `assets/art/facer|lineart/`
and `book/images/facer|lineart/` is a byte-identical duplicated set: `assets/` is the
source-of-truth corpus, `book/images/` is the copy MyST actually builds from. Changing art
means changing both.

## Workflow Conventions

- **`cc_tasks/`** holds one file per unit of work, named `YYYY-MM-DD_short_description.md`. Each task states the change, and (for anything non-trivial) a verification section. Once dispatched, a task file is treated as a record, not edited in place — corrections go in a new addendum task, not a rewrite of the original.
- Tasks that need a verification record get a sidecar: `cc_tasks/YYYY-MM-DD_short_description_RESULT.md`.
- **`handoffs/`** holds one file per session boundary, named `HANDOFF_YYYY-MM-DD_short-description.md` (or `HANDOFF_YYYY-MM-DD-sessionN.md` for same-day multi-session work). Written when a session ends mid-task and the next session (human or Claude) needs the state of play.
- Both directories are gitignored — they're working scaffolding for whoever (human or Claude) is driving the repo, not published content.
- **File operations:** read the full file → modify in memory → write the full file back. Don't rely on partial in-place string replacement for anything content-bearing.

## Open Items (as of 2026-08-17)

- **Image weight, not image dimensions.** Measured: every PNG is **1024×1536 px** — cover, facer, and lineart alike. That is *modest*, not oversized (about 128 DPI at an 8×10 page), so downsizing pixels is the wrong lever and would visibly hurt. The actual problem is **encoding**: PNG for photographic-style art costs 2.5–3.4 MB per file, ~2 bytes/pixel. The fix is a format change (JPEG/WebP for `facer/`, keep PNG for `lineart/` where flat line art compresses well), which cuts weight ~90% at identical pixel dimensions. Not started. Supersedes the earlier "likely oversized, downsize to 8×10" framing, which was based on file size alone with no dimensions ever measured.
- **Repo weight.** `assets/` and `book/` are ~130 MB each = ~260 MB committed, and they hold the *same* bytes twice (verified identical). Fine for GitHub, but pushes are slow and the duplication doubles the cost of every art change. Resolving the encoding item above fixes most of this.
- **Typst PDF export untested.** `myst build --typst` has never been run against this content — the `plain_typst_book` template and the `cover:` key in `book/myst.yml` are unverified.

**Closed:**
- ~~B's lineart / `b_colorpage.png`~~ — resolved. `manuscript/art_selections.md` now records the finding on its face: no file by that name ever existed anywhere in the project, only `b_lineart.png`, which is what's wired into the book. Stale reference, not a lost asset. Nothing to do.
- ~~`assets/art/archive/`~~ — empty leftover directory. Genuinely untracked now (git does not track empty directories); the old note that it was untracked was wrong at the time — the pre-existing broken `.git/` had 51 `arc/` variants staged in its index. That index is gone. Safe to delete the directory whenever.

## Build System

**MyST** (`mystmd`), matching `ai-workflow-design`.

- HTML site: `cd book && myst build --html` → `book/_build/html/`.
  **Verified working 2026-08-17** — 5 pages (`index`, `front-matter`, `alphabet`, `back-matter`,
  `coloring-pages`), all 60 images resolved, no errors. Output is ~183 MB, dominated by the art.
- PDF export: `myst build --typst` → `book/exports/` (target filename: `overresponsible-ai-handbook.pdf`, per README). **Not yet run** — see Open Items.
- GitHub Pages: `.github/workflows/deploy.yml` deploys on push to `main`. Pages source must be
  "GitHub Actions" (not "Deploy from a branch"); set via
  `gh api -X POST repos/brockwebb/book_responsible_ai/pages -f build_type=workflow`.
- Config: `book/myst.yml`
- **Version drift:** local `myst` is v1.8.2; CI runs `npm install -g mystmd`, i.e. latest (v1.10.1
  as of 2026-08-17). A build that passes locally is not proof CI passes. Check the Actions tab.

## Related Projects

- **`ai-workflow-design`** (`/Users/brock/GitHub/ai-workflow-design`) — sibling repo, structural template. Further along in its build pipeline; borrow from `scripts/build_pdf.py` and `table_map.yaml` once this book needs its own PDF build script.
