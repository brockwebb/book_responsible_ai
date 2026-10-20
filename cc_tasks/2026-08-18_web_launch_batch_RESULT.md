# RESULT — Web launch batch

**Task:** `cc_tasks/2026-08-18_web_launch_batch.md`
**Date:** 2026-08-18 · **Status:** complete · **Commit:** `b5231dc`, CI green
**Seldon ResearchTasks:** `c42ef2df` (cover + v2 artifact), `a3ea30da` (nav + freeze + hygiene) — both closed
**Live Zenodo record:** untouched, as required. Read-only GETs only.

## 1. Cover attribution

"BROCK WEBB" typeset into a **reserved bottom band** (0.72 in) of the cover fill —
the contain-fit art previously had side bands only, so the bottom band was created by
the layout, not by editing the image. Letterspaced (4.5 pt tracking) Baskerville bold in
the title's own ink, sampled `#2D2419` from the actual title area. Render:
`handoffs/renders_web/cover_attributed-01.png`. Web landing page already carried
"*Brock Webb*" as text (pre-existing in `cover.md`); confirmed rendering live.

## 2. Web letter-grid nav

Linked 26-letter grids at the top of both web pages, with the PDF's bureaucratic intro
line on the alphabet page:

- `alphabet.md` → anchors `#a-is-for-alignment` … `#z-is-for-zero-ai` (slugs verified
  against the built HTML ids, including the irregulars: `x-is-for-x-risk`,
  `z-is-for-zero-ai`, `i-is-for-impact-assessments`)
- `coloring-pages.md` → anchors `#a`…`#z`

Markup is inline paragraph flow (`<p>`, no table): wraps at any width, no horizontal
scroll. All 26/26 targets exist in both built pages; **live site verified: 26 unique
hrefs on each page.**

Pipeline guard: the coloring grid sits *below* the intro divider, because
`build_pdf.sh` extracts everything above the first `---` as the PDF's coloring intro —
web-only `#a` anchors must never reach the PDF. Verified: map validates, PDF intro
unchanged.

## 3. Manuscript freeze

Freeze header in **all five** `manuscript/*.md` (including `art_selections.md`):
"FROZEN 2026-08-18 — editorial working copy, superseded by book/…". CLAUDE.md: structure
line marks the directory frozen; conventions drop the mirror-every-edit rule and name
`book/` the sole source of truth.

## 4. Link + record hygiene

- README: DOI badge **fetch-verified HTTP 200**; new status line is read-online-first
  (web URL · DOI · repo); stale pre-launch "Status: production in progress" corrected.
- Web front matter/back matter: DOI + read-online/source links confirmed in built HTML.
- `.zenodo.json` `publication_date`: **checked against the live record via the Zenodo
  API** (`zenodo.org/api/records/21983981` → `publication_date: 2026-08-17`). The file
  already said 2026-08-17 — correct, no change made.

## 5. Optional v2 artifact — built, not uploaded

`book/exports/overresponsible-ai-handbook.pdf` is the v2 candidate. Verified against the
preserved v1 baseline:

| Check | Result |
|---|---|
| Page count | 68 = 68 |
| Size delta | +710 bytes (0.001 MB; limit 0.1) |
| Text diff | exactly one addition: "BROCK WEBB" (cover) |
| Interior spot-check | page 22 rasterized **byte-identical** |

**Manual path if Brock wants v2** (his call; v1 stands fine otherwise):
Zenodo record 21983981 → **New version** → upload the PDF at `book/exports/` →
changelog "Added author attribution to cover." → Publish. The concept DOI keeps
resolving; nothing breaks if skipped.

## 6. Close-out

Push `b5231dc`, CI green, live site checked (both grids work, cover name shows on the
landing page), `seldon verify` all 7 green, both ResearchTasks closed. Handoff:
`handoffs/HANDOFF_2026-08-18_web-launch.md`.
