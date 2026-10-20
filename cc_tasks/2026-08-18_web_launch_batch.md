# Task: Web launch batch — cover attribution, site nav, freeze, link hygiene

The Zenodo record is LIVE (v1, DOI 10.5281/zenodo.21983981). Do not touch the live
record. Everything here is repo/site work plus an optional v2 artifact Brock may or
may not upload.

## 1. Cover attribution
The cover art has no author name; the PDF cover page is the art contained on a
matched-fill band (#E8C690) rendered by Typst. Typeset "Brock Webb" into the fill
band (bottom band preferred), matching the cover art's lettering style as closely as
system/bundled fonts allow, color sampled from the cover's title ink. Do NOT edit the
image. Also add the name to the web edition's cover/landing page (cover.md) as text.
Spot-render the new cover to handoffs/renders_web/.

## 2. Web letter-grid nav
Port the PDF's letter-grid index to the web edition: a linked grid of 26 typographic
letters at the top of alphabet.md (anchor links to each letter's heading), with the
same bureaucratic intro line used in the PDF. Same pattern, smaller: a linked grid at
the top of coloring-pages.md. Must render correctly in the book-theme; check mobile
width (grid wraps, no horizontal scroll).

## 3. Manuscript freeze
Add a header block to every manuscript/*.md: "FROZEN 2026-08-18 — editorial working
copy, superseded by book/. Do not edit; book/ is the sole source of truth." Update
CLAUDE.md conventions accordingly (drop the mirror-every-edit rule, note the freeze).

## 4. Link + record hygiene
- README: confirm DOI badge resolves, "Read online" link first, repo second.
- Web edition front matter: confirm the DOI and read-online/source links render.
- .zenodo.json: set publication_date to the record's ACTUAL published date (check
  the live record page, do not assume).
- LinkedIn first-comment crib in the handoff: web URL, Zenodo DOI URL, one line each.

## 5. Optional v2 artifact (build it; Brock decides whether to upload)
Rebuild the PDF with the attributed cover: scripts/build_pdf.sh. Verify only the
cover page differs materially (page count identical, size within ~0.1 MB). Leave at
book/exports/. RESULT states the two-step manual path: Zenodo record → New version →
upload → publish, changelog "Added author attribution to cover." If Brock skips it,
v1 stands and nothing breaks.

## 6. Close out
Push, CI green, live site checked (grids work, cover name shows). seldon verify
--fix; register + close ResearchTasks. Handoff:
handoffs/HANDOFF_2026-08-18_web-launch.md — lead with the rendered cover and the
LinkedIn crib block.
