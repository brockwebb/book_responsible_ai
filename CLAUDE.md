# CLAUDE.md — The Overresponsible AI Handbook

## Project Overview

*The Overresponsible AI Handbook: An Alphabetical Guide to Doing Nothing, Responsibly* — a satirical A–Z alphabet book on AI governance theater. Twenty-six letters, each pairing a koan, a full-page color illustration, and a one-line definition. Bonus back-matter section: 26 coloring pages (lineart versions of the same illustrations).

It's satire with a straight face underneath — see the Author's Note in the front matter.

**Repo:** `brockwebb/book_responsible_ai`
**Author:** Brock Webb
**Format:** Ebook-first — PDF edition + a web/GitHub "book" edition (MyST). No print run planned.
**License:** CC BY 4.0 International — `LICENSE` at repo root holds the full legal code. Same license as the sibling `ai-workflow-design`.

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
├── assets/art/            # LOCAL MASTER CORPUS — GITIGNORED, never committed
│   ├── facer/                 # 26 lossless PNG masters
│   ├── lineart/                # 26 lossless PNG masters
│   ├── cover/                   # 1 file (0-OAIH-BookCover.png)
│   └── archive/                  # empty leftover dir — see Open Items
├── arc/                    # 51 old/rejected art variants + .xcf sources — GITIGNORED
├── cc_tasks/                # Task specifications — gitignored, local working dir
├── handoffs/                 # Session handoff documents — gitignored, local working dir
└── .github/workflows/deploy.yml   # MyST build → GitHub Pages, on push to main
```

`.gitignore` also excludes `audits/`, `/docs/`, `.claude/`, `book/_build/`, and
`book/exports/*.pdf` — none of those are published.

### Art: masters vs. published copies

**`assets/` is not published content and is never committed.** It is the local master
corpus — clean lossless originals, kept only so resolution or re-encoding work can be
redone from source. It lives on this machine and in the backup bundle, not in git.

**`book/images/` is the only committed art** — derived, web/PDF-weight copies.

So: **art changes touch `book/images/` only.** Regenerate from the masters in `assets/`
when a new derivation is needed. The old convention — "`assets/` and `book/images/` must
stay byte-identical, change both" — is **dead**, superseded 2026-08-17. Do not restore it;
it is what doubled the repo.

## Workflow Conventions

- **`cc_tasks/`** holds one file per unit of work, named `YYYY-MM-DD_short_description.md`. Each task states the change, and (for anything non-trivial) a verification section. Once dispatched, a task file is treated as a record, not edited in place — corrections go in a new addendum task, not a rewrite of the original.
- Tasks that need a verification record get a sidecar: `cc_tasks/YYYY-MM-DD_short_description_RESULT.md`.
- **`handoffs/`** holds one file per session boundary, named `HANDOFF_YYYY-MM-DD_short-description.md` (or `HANDOFF_YYYY-MM-DD-sessionN.md` for same-day multi-session work). Written when a session ends mid-task and the next session (human or Claude) needs the state of play.
- Both directories are gitignored — they're working scaffolding for whoever (human or Claude) is driving the repo, not published content.
- **File operations:** read the full file → modify in memory → write the full file back. Don't rely on partial in-place string replacement for anything content-bearing.

## Open Items (as of 2026-08-17)

- **Image weight, not image dimensions.** Measured: every PNG is **1024×1536 px** — cover, facer, and lineart alike. That is *modest*, not oversized (about 128 DPI at an 8×10 page), so downsizing pixels is the wrong lever and would visibly hurt. The actual problem is **encoding**: PNG for photographic-style art costs 2.5–3.4 MB per file, ~2 bytes/pixel. The fix is a format change (JPEG/WebP for `facer/`, keep PNG for `lineart/` where flat line art compresses well), which cuts weight ~90% at identical pixel dimensions. Not started. Supersedes the earlier "likely oversized, downsize to 8×10" framing, which was based on file size alone with no dimensions ever measured.
- **Repo weight.** Addressed 2026-08-17: `assets/` (~130 MB) is now gitignored, so the committed art is `book/images/` only. See the masters-vs-published-copies section above.
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
- GitHub Pages: **live at https://brockwebb.github.io/book_responsible_ai/** —
  `.github/workflows/deploy.yml` deploys on push to `main`, confirmed working 2026-08-17
  (first run green, all 5 pages HTTP 200, images serving). Pages source must be
  "GitHub Actions", not "Deploy from a branch"; already set, and settable from the CLI via
  `gh api -X POST repos/brockwebb/book_responsible_ai/pages -f build_type=workflow`.
- Config: `book/myst.yml`
- **Version drift:** local `myst` is v1.8.2; CI runs `npm install -g mystmd`, i.e. latest (v1.10.1
  as of 2026-08-17). A build that passes locally is not proof CI passes. Check the Actions tab.

## Seldon (config control)

This project is Seldon-managed as of 2026-08-17. Run `seldon go` at the start of any
session for the full behavioral contract; `seldon briefing` for open tasks.

| | |
|---|---|
| Config | `seldon.yaml` (tracked) |
| Event log | `seldon_events.jsonl` (tracked — **source of truth**, `seldon rebuild` replays it into Neo4j) |
| Neo4j database | `seldon-book-responsible-ai` at `bolt://localhost:7687` |
| Session state | `.seldon/` (gitignored) |
| Template | `blank` — not `paper`; this book registers no research results |
| Shared ontology | read-only from `/Users/brock/Documents/GitHub/seldon/ontology` (epoch 3, 105 terms) |

**Neo4j must be running** (Neo4j Desktop, Enterprise — per-project databases need it).
The database name comes from `project.slug` in `seldon.yaml`, *not* from `$NEO4J_DB` —
so a `NEO4J_DB=wintermute-intake` in the shell environment does not leak into this project.

Registered artifacts: the 5 `book/*.md` content files, as `PaperSection`. `paths.book:
book/` is what makes `book/` the content root — it is the one path key Seldon code
actually reads (via `get_content_dir()`); the others in `seldon.yaml` are documentation.

**After editing any `book/*.md`, run `seldon verify`** — it checks file hashes against the
graph and will report drift. `seldon verify --fix` registers new files and re-syncs hashes.
Verify also regenerates `keyword_index.md` at the repo root; it is gitignored, expected,
and safe to delete.

Open work lives in the graph, not in this file — `seldon status` or `seldon briefing`.
The Open Items section above is narrative context; the graph is authoritative.

**Known Seldon defect — `rebuild` does not round-trip the ontology.** `seldon init` writes
an `ontology_synced` event, but `seldon rebuild` does not handle that event type and skips
it (`Unknown event_type 'ontology_synced' — skipped during sync`). A rebuild therefore
drops the ontology to epoch 0 and `seldon verify` fails the Ontology check. Artifacts and
tasks survive intact; only the ontology is lost. Recovery is one command:

```bash
seldon rebuild && seldon ontology sync   # always pair these
```

Verified on this project 2026-08-17 — rebuild, resync, re-verify, all 7 checks green,
all 3 ResearchTasks preserved. This is a bug in Seldon itself (`~/Documents/GitHub/seldon`),
not in this book; it will affect every Seldon project until fixed upstream.

Also portability: `shared_ontology.source` in `seldon.yaml` is a machine-specific absolute
path (`/Users/brock/Documents/GitHub/seldon/ontology`). Fine here — Seldon runs only on
this machine and never in CI — but it will not resolve on another machine. Override with
`SELDON_ONTOLOGY_PATH` if that ever matters.

## Related Projects

- **`ai-workflow-design`** (`/Users/brock/GitHub/ai-workflow-design`) — sibling repo, structural template. Further along in its build pipeline; borrow from `scripts/build_pdf.py` and `table_map.yaml` once this book needs its own PDF build script.
