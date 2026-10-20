# Task: Re-encode facer art, then run the Typst PDF export

Covers Seldon ResearchTasks f85cc674 (art re-encoding) and aa47145d (untested
typst export). Ordering is deliberate: **re-encode first, then build the PDF**,
so the PDF is built once from final-weight assets instead of a ~130 MB PNG set.

## Constraint that changes the plan
Typst does **not** support WebP (pixmap formats: PNG/JPEG/GIF). The CLAUDE.md
open item says "JPEG/WebP for facer" — for a repo whose PDF path is
`myst build --typst`, that resolves to **JPEG for facer**. Verify against the
installed typst/mystmd versions with a one-image test build before converting
all 26; if WebP unexpectedly works end-to-end, say so in the RESULT file, but
JPEG is the default call.

## Changes
1. `assets/art/facer/*.png` → JPEG, quality ~85, keep 1024×1536 px exactly
   (dimensions are correct per CLAUDE.md — encoding is the only lever).
   `cover.png` likewise if it's photographic-style; keep `lineart/` as PNG.
2. Copy the converted set to `book/images/facer/` (the two dirs must stay
   byte-identical per repo convention). Update image references in
   `book/*.md` and `book/myst.yml` (`cover:` key) from `.png` to `.jpg`.
3. Delete the now-replaced PNGs from both locations. Note in RESULT the before/
   after repo size (`du -sh assets book`).
4. `cd book && myst build --html` — confirm all 60 images resolve.
5. `cd book && myst build --typst` — first-ever run. Expect template friction
   (`plain_typst_book`, `cover:` key both unverified). Output:
   `book/exports/overresponsible-ai-handbook.pdf`.
6. Visual spot-check the PDF: cover renders, one facer page, one lineart page,
   page count sane. Report PDF file size (Zenodo cap is 50 GB/record — not a
   constraint, but a <100 MB PDF is the target for a downloadable book).
7. `seldon verify --fix` (book/*.md hashes changed), then close f85cc674 and
   aa47145d in the graph with outcome notes.
8. Push to main and confirm the Pages Action goes green (CI runs latest mystmd,
   local is 1.8.2 — local pass is not proof).

## Verification
- RESULT file with: sizes before/after, typst build log outcome, Pages Action
  run URL/status, both graph tasks closed.
