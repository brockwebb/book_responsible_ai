# RESULT — Typst PDF v2: the real book layout

**Task:** `cc_tasks/2026-08-17_typst_pdf_v2.md`
**Runbook2 step:** 4 of 4 · **Date:** 2026-08-17 · **Status:** complete
**Seldon ResearchTask:** `5ba79aed-9a05-442a-8516-69cae44b933f` — closed `completed`

---

## The book

| | |
|---|---|
| Output | `book/exports/overresponsible-ai-handbook.pdf` |
| Size | **12 MB** (acceptance ≤ ~25 MB) |
| Pages | **67** — cover · 7 front sections · grid · 26 landscape letter spreads · 3 back sections · coloring intro · 26 coloring pages |
| Outline | **64 bookmarks**, full tree: front sections → The Alphabet → 26 × "A — Alignment" → back sections → Coloring Pages → 26 × "Coloring: A — Alignment" |
| Engine | Typst 0.14.2, standalone — supersedes the batch-1 MyST typst export (47 MB / 74 pp pipeline test) |

## Files

- `book/pdf/main.typ` — the whole book, driven by `book_map.yaml` (`yaml()` native read; no codegen).
- `scripts/build_pdf.sh` — regenerate map (validation gate) → pandoc md→typst prose fragments → `typst compile --root book`. Requires typst, pandoc, PyYAML.
- `book/pdf/_generated/` — pandoc fragments, gitignored (regenerated per build).
- `book/myst.yml` — `exports:` block **removed**, with an in-file comment: the MyST typst export flattened the book into a numbered-article template; two PDF paths would mean two divergent books. One path only.
- `README.md` — build instructions updated: `myst build --html` = web, `scripts/build_pdf.sh` = PDF.

## Design decisions (mine to make, recorded)

- **Prose pipeline: pandoc (3.8.3) md→typst per section**, not hand-transcribed content (drift) and not a hand-rolled converter (re-derivation; pandoc is the prior art). The build script splits front/back matter into H2 sections, converts each, injects a `#metadata("sec-<id>")` anchor before each so native typst links can target them. Pandoc's template-provided `#horizontalrule` is defined in a small prelude.
- **Navigation anchors** use the `metadata`-element + `query()` pattern (labels can't be attached dynamically in loops); invisible outline entries use `place(hide(heading(...)))` — verified they still register bookmarks.
- **Accent color** `#9B5531` — the cover laurel's rust (sampled `#C26A3D`) darkened for text on white. Fonts: Baskerville (Georgia/Libertinus fallback); grid letters 46 pt bold accent; koans 17 pt italic, ragged-centered (justify produced ugly gaps at this measure).
- **Cover: `contain` on a page filled with the art's own edge color (sampled `#E8C690`), not `cover`.** The art is 2:3, US Letter is 0.773 — the spec's full-bleed crop cut off "THE" and "CERTIFIED 0% INNOVATION". Contain-on-matched-fill reads as full-bleed and loses zero pixels. This is the one deliberate deviation from the letter of the spec, in favor of its intent.
- **Letter spread** per spec: left half facer `fit: cover` (2:3 art on 5.5×8.5 half — the sliver crops, no letterbox, no distortion); right half koan only, generous white space, small ⌂→grid + page number bottom-right, nothing else added.
- Front/back sections get `pagebreak(weak: true)` between them — first build ran them together, which is not book form.

## Verification

**Spot renders at 300 DPI** (scratchpad `pdfv2/`): cover (`cover2.png` — full art, seamless fill), grid (`r9.png` — 5×6, even, restrained), letter A (`p10-10.png`) and M (`r22.png`) — poster left, italic koan right, ⌂ + folio; coloring page (`r42.png`) — full-page SVG, zero chrome, crisp.

**Links & bookmarks — verified programmatically on every annotation** (60 total: 58 internal GoTo + 2 URI):

| Check | Result |
|---|---|
| TOC page 7 → | 5 (Foreword) · 8 (Author's Note) · 9 (Alphabet) · 36 (Afterword) · 37 (Compendium) · 41 (Coloring) ✓ |
| Grid page 9 → | letter pages 10–35, all 26 ✓ |
| 26 × ⌂ home links → | page 9, all ✓ |
| Dangling destinations | none |

**Two-viewer requirement, honestly stated:** headless session — no interactive clicking. Substituted: dest-level audit via pypdf (the ground truth a viewer consults) + rendering/opening under **two independent engines**, Poppler (`pdftoppm`/`pdfinfo`) and Apple Quartz (Preview's engine, 67 pages). Brock's read-through in Preview will exercise the links by hand; nothing in the annotation table can behave differently per conforming viewer.

**Web edition unaffected:** `myst build --html` green after the `myst.yml` exports removal. `seldon verify` all green.

## Not done

- Zenodo: untouched, per the task's explicit DO NOT and the runbook's out-of-scope list.
