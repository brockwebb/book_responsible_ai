# ADDENDUM — amends 2026-08-18_web_launch_batch.md
# Run as one pass with the parent task. Adds a back cover; v2 artifact now contains
# BOTH the cover attribution and the back cover. Live Zenodo record still untouched.

## Back cover (new final page of the PDF — after the THIS PAGE INTENTIONALLY LEFT
## BLANK / THE END page; the back cover is the outside of the book, so it closes it)
Constraint: NO image generation. Colophon states the art is April 2025, never
regenerated; the back cover must not violate that. Pure Typst on the matched-fill
background (#E8C690), portrait, lettering styled to match the front cover treatment
used for the author name in the parent task.

Composition, top to bottom:
1. One or two praise pull-quotes reused verbatim from the front-matter Praise
   section (with their — **Name** attributions; pick the two strongest, favor
   Will B. Done).
2. The anti-blurb, drafted around Brock's transparency joke; working draft:
   "This book has been assessed for transparency. You are now looking at the back
   of it. Nothing is hidden here, which is the highest known form of compliance."
   Keep it to 2–4 sentences, bureaucratic deadpan, zero em dashes.
3. Bottom band: a fake barcode drawn in Typst (plain black rects, plausible
   proportions), captioned "ISBN: pending committee approval", and
   "Suggested retail: $0.00" with a one-clause compliance gag.
4. Small line: CC BY 4.0 + the concept DOI URL (the all-versions one), so the
   physical-object joke still carries the real citation.

Page count after this: 69. That is the expected number; do not add or remove pages
to change it.

## Verification (adds to parent §6)
- Spot-render the back cover to handoffs/renders_web/.
- v2 PDF = attributed front cover + back cover; page count exactly 69.
- RESULT restates the v2 upload path (New version → upload → publish, changelog:
  "Added author attribution to cover; added back cover.").
