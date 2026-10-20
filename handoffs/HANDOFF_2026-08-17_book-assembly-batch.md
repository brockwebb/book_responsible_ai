# HANDOFF — 2026-08-17 book-assembly batch

**Runbook:** `cc_tasks/2026-08-17_RUNBOOK2.md`
**Outcome: all 4 tasks complete, nothing blocked. CI green after every push. Zero open Seldon tasks.**

Repo HEAD `4c05b45` · Site https://brockwebb.github.io/book_responsible_ai/ (200, serving
SVG lineart and © 2025) · PDF `book/exports/overresponsible-ai-handbook.pdf`

---

## Needs Brock's eyes at the read-through gate — lead items

1. **The colophon** (full text below) — you asked to review this prose specifically.
2. **The PDF itself** — `book/exports/overresponsible-ai-handbook.pdf`, 67 pp, 12 MB.
   Open in Preview; the grid, TOC, and ⌂ links are click-verified only programmatically
   (headless session — every internal destination audited via pypdf and rendering checked
   under both Poppler and Quartz, but no human has clicked them).
3. **One deliberate spec deviation:** the cover page uses `contain` on a background filled
   with the art's own edge color (`#E8C690`), not a full-bleed crop — the crop cut off
   "THE" and "CERTIFIED 0% INNOVATION" (art is 2:3, Letter is 0.773). It reads as
   full-bleed; see `renders_2026-08-17/pdf_cover.png`.
4. **Web reading-order change:** on each alphabet page the definition now appears as the
   figure caption (directly under the image), with the koan after — previously koan came
   first. Consequence of the caption conversion you asked for; flag if you want koan-first
   restored some other way.

## The colophon, in full (in `book/back-matter.md` + manuscript mirror)

> ## Colophon
>
> This book was written and illustrated in April 2025 and published in 2026. The gap is deliberate: the work is presented as it was made, a snapshot of that moment, unrevised.
>
> The illustrations were generated with OpenAI's ChatGPT image tooling of that era, with the text rendered directly in the images. They have deliberately not been regenerated with newer models; their quirks, including the occasional mangled word, are part of the record.
>
> The text is a human–AI collaboration, as the AI Disclaimer at the front of this book already admits.
>
> The web edition is built with MyST; the PDF edition with Typst. Source and history: [github.com/brockwebb/book_responsible_ai](https://github.com/brockwebb/book_responsible_ai).

## Per task

| # | Task | Status | RESULT | CI |
|---|---|---|---|---|
| 1 | Front/back matter period-piece | ✅ | `2026-08-17_frontback_matter_period_piece_RESULT.md` | `32038052238` ✓ |
| 2 | Lineart optimize (bake-off) | ✅ | `2026-08-17_lineart_optimize_RESULT.md` | `32038323883` ✓ |
| 3 | Document map + validation gate | ✅ | `2026-08-17_book_map_RESULT.md` | `32038416964` ✓ |
| 4 | Typst PDF v2 | ✅ | `2026-08-17_typst_pdf_v2_RESULT.md` | `32039070241` ✓ |

## Lineart: method chosen + sizes

**Winner: A — threshold → mkbitmap → potrace → SVG** (first in the task's A→B→C order to
show zero visible degradation at 100%/300% zoom and in a 300-DPI print render; also the
print-correct answer — resolution-independent coloring pages). The batch-1 potrace risk
didn't materialize: mkbitmap's highpass filter separates the tonal paper noise before
tracing. B (PNG-8) also looked fine but lost on order; C proved the files aren't flat art
(only ~10–22% lossless gain).

| | Before | After |
|---|---|---|
| `book/images/lineart/` | 49 MB (26 PNG, avg 1,936 KB) | **2.0 MB (26 SVG, avg ~77 KB, max 223 KB)** |
| Committed art total | 60 MB | **~13 MB** |
| Live site, one page | 1.7 MB PNG | **44.7 KB SVG** |

Applied with a per-file ink-coverage gate (max delta 0.028, no dropout outliers). Masters
untouched in `assets/`.

## Final PDF

**67 pages, 12 MB** (target ≤ ~25 MB). Portrait cover/front/grid/back/coloring; landscape
for the 26 letter spreads only — facer poster full-bleed left, koan alone in white space
right (17 pt Baskerville italic, ragged-centered), small folio + ⌂. Letter-grid index:
46 pt Baskerville in the cover-sampled rust `#9B5531`. Outline: 64 bookmarks, full tree.
Links: TOC (6), grid (26), home (26) — all destinations verified, zero dangling.

Built by `scripts/build_pdf.sh`: `build_map.py` (validation gate: 26 letters A–Z, files on
disk, no empty fields, no dup paths, toc drift → named nonzero failures) → pandoc md→typst
prose fragments with injected anchors → `typst compile`. `book_map.yaml` and
`book/pdf/_generated/` are gitignored, regenerated every build. **The MyST typst export is
removed from `myst.yml`** — one PDF path, reason documented in-file and in README.

## Spot renders (all in `handoffs/renders_2026-08-17/`)

- `pdf_cover.png` · `pdf_letter_grid.png` · `pdf_letter_A_spread.png` ·
  `pdf_letter_M_spread.png` · `pdf_coloring_A.png`
- `lineart_bakeoff_n_orig-A-B.png` / `lineart_bakeoff_g_orig-A-B.png` (300% zoom,
  original | SVG | PNG-8) · `lineart_winner_g_print300dpi.png`

## Seldon graph — batch reconciliation

| ID | Task | State |
|---|---|---|
| `6472df92` | period-piece matter corrections | completed |
| `012b6690` | lineart optimization | completed |
| `aba6f53f` | document map | completed |
| `5ba79aed` | typst PDF v2 | completed |

`seldon verify` all 7 green. Zero open tasks (all 9 in the graph completed).

## Notes for the next session

- **Cross-task rule check (runbook):** lineart winner was SVG; the map derives extensions
  from disk (resolved `.svg`) and typst consumes the map's paths — agreement by
  construction, verified in the generated map and the compiled PDF.
- Batch-1's cosmetic complaint about the MyST-export PDF ("2.4 D is for Doubt" numbering,
  definition run-over) is moot — that pipeline no longer exists.
- PDF prose sections each start on their own page (`pagebreak(weak)` between pandoc
  fragments); first build ran them together.
- Tools installed this batch: `potrace`/`mkbitmap`, `oxipng` (brew), `pypdf` (pip).
  `pandoc` 3.8.3 and `typst` 0.14.2 were already present.

## Out of scope — not started, per the runbook

Zenodo record / `.zenodo.json` / DOI backfill (waits on your read-through) ·
web-edition letter-grid nav · `manuscript/` freeze · CI packaging of the PDF.
