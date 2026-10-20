# Task: DOI backfill + final PDF rebuild
# PARAMETER REQUIRED — do not run until Brock replaces the placeholder below.

DOI: 10.5281/zenodo.21983981   <-- confirmed by Brock, 2026-08-17 (chat)

If this line still contains XXXXXXX, STOP and report. It does not.

## Changes
1. Backfill the DOI into:
   - `book/front-matter.md` copyright page (citation line with DOI, styled like the
     license line) — mirror to `manuscript/01_front_matter.md`
   - Colophon in `book/back-matter.md` (mirror to manuscript counterpart)
   - `README.md` (DOI badge, shields.io zenodo style, + plain-text citation)
   - `CITATION.cff` (uncomment doi field)
   - `.zenodo.json` publication_date → today's actual date
1b. Colophon link fix (Brock's read-through catch): the colophon's closing link
   points only at the source repo (github.com/...), i.e. "the plain git site", not
   the readable book. Replace that line with TWO links:
   "Read online: https://brockwebb.github.io/book_responsible_ai/ · Source and
   history: https://github.com/brockwebb/book_responsible_ai"
   FIRST verify the live Pages URL by fetching it (check the deployed workflow /
   repo Settings→Pages if the default URL 404s) — do not assume. Mirror to the
   manuscript counterpart. Apply the same read-online-first pattern anywhere else
   in book content that links only the repo (grep for github.com/brockwebb).
2. Rebuild: `scripts/build_pdf.sh` → fresh `book/exports/overresponsible-ai-handbook.pdf`
   containing its own canonical citation. Confirm page count unchanged (±1) and size
   in the 12 MB range; spot-render the copyright page and colophon, save to
   handoffs/renders/.
3. Push; CI green (web edition now shows the DOI too).
4. `seldon verify --fix`; register + close ResearchTask.
5. RESULT ends with the exact next manual step for Brock: upload the rebuilt PDF at
   book/exports/overresponsible-ai-handbook.pdf to the Zenodo draft, verify the form
   fields against .zenodo.json, publish.
