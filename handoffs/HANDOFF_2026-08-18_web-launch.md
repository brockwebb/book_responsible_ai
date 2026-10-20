# HANDOFF — 2026-08-18 web launch

**Batch:** `cc_tasks/2026-08-18_web_launch_batch.md` — **all six items complete.**
Commit `b5231dc`, CI green, live site verified. Zenodo record untouched (read-only GETs
only). RESULT: `cc_tasks/2026-08-18_web_launch_batch_RESULT.md`.

## The cover, attributed

`handoffs/renders_web/cover_attributed-01.png` — "BROCK WEBB" letterspaced in the
title's own ink (`#2D2419`, sampled) in a reserved bottom band of the fill. The image
file is untouched; the band is pure layout. It reads like it was always there.

## LinkedIn first-comment crib

> Read it free online: https://brockwebb.github.io/book_responsible_ai/
> Archived, citable PDF (DOI): https://doi.org/10.5281/zenodo.21983981

One line each, web first, per the read-online-first pattern used everywhere else.

## What changed

| Item | State |
|---|---|
| Cover attribution (PDF band + web landing text) | ✅ rendered, live |
| Web letter-grid nav (alphabet + coloring, 26 links each) | ✅ live-verified, wraps on mobile, no h-scroll |
| Manuscript freeze (5 files + CLAUDE.md rule change) | ✅ `book/` is sole source of truth |
| Link hygiene (README read-online-first, badge 200, front-matter DOI) | ✅ |
| `.zenodo.json` publication_date vs live record | ✅ API says 2026-08-17 — already correct, untouched |
| Optional v2 PDF | ✅ **built, waiting on your call** |

## The v2 decision (yours, no urgency)

`book/exports/overresponsible-ai-handbook.pdf` is the attributed-cover build. Verified
against v1: 68 = 68 pages, +710 bytes, the only text difference is "BROCK WEBB", and an
interior spot page is byte-identical. If you want it on Zenodo:

1. Record 21983981 → **New version**
2. Upload the PDF from `book/exports/`
3. Changelog: "Added author attribution to cover."
4. Publish. (Concept DOI keeps resolving; if you skip this, v1 stands and nothing breaks.)

## Seldon

`c42ef2df` (cover + v2) and `a3ea30da` (nav + freeze + hygiene) — both completed.
`seldon verify` all 7 green. No open tasks.

## Notes for the next session

- The coloring page's web grid must stay **below** the first `---`: `build_pdf.sh`
  extracts everything above it as the PDF intro, and web-only `#a` anchors must not
  leak into the PDF.
- MyST heading slugs are GitHub-style; the irregulars are `x-is-for-x-risk`,
  `z-is-for-zero-ai`, `i-is-for-impact-assessments` — the grid links were generated
  from the actual built ids, not guessed.
- `manuscript/` is frozen. Do not edit it; the mirror rule is dead.
- CLAUDE.md's "Open Items (as of 2026-08-17)" block is stale (art re-encode and typst
  items are long done) — the Seldon graph is authoritative; the block could use a
  cleanup pass some session.
