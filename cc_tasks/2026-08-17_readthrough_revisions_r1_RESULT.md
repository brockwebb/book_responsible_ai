# RESULT — Read-through revisions, round 1

**Task:** `cc_tasks/2026-08-17_readthrough_revisions_r1.md`
**Date:** 2026-08-17 · **Status:** complete — every item in A–D applied, none re-asked
**Seldon ResearchTask:** `0f8b994c-f0e5-4f6b-8c7a-f29b8d6d24d5` — closed `completed`

## Before / after

| | Before | After |
|---|---|---|
| Pages | 67 | **68** (+1: the intentionally-blank final page; the coloring grid fit on the section opener) |
| Size | 12,155,791 B (11.6 MB) | **12,380,813 B (11.8 MB)** |
| Internal links | 58 | **96** (real TOC rows + 26-link coloring grid) — zero dangling |

## A — front matter (book + manuscript, every edit assertion-checked to exactly 1 occurrence)

1. ✅ Signature stacked: CEO of **The Responsible AI Decommissioning (RAID) Society** / Founding Chair, International Bureau of Oversight, Hesitation, and Second-Guessing / Author line kept. **Plus one fix the task didn't anticipate:** the three lines were soft-wrapped markdown, so both pandoc and MyST ran them into one paragraph — added hard line breaks (`\`); verified stacked in the PDF render and as `<br>` on the web.
2. ✅ "to Zero AI (the perfect model that generates nothing)"
3. ✅ "alphabetized rigor"
4. ✅ "— and for those brave souls who have achieved perfect AI safety by never using it at all." ("Remember, innovation…" sentence retained — the edit targeted only the "May this book serve" sentence.)
5. ✅ Author's Note: "works for the benefit of humanity. It will never work equally for everyone… Progress has never waited for unanimous consent…"
6. ✅ Praise untouched.
7. ✅ TOC → one-item-per-line list, no page numbers in markdown.

## B — alphabet / back matter / coloring (book + manuscript)

1. ✅ E koan: "The eye just blinked and stared." — confirmed flowing through `book_map.yaml` into the PDF.
2. ✅ Afterword replaced verbatim with the four-paragraph draft.
3. ✅ Colophon ¶1 → line-in-the-sand / wine-rot-Twinkie text; "published in 2026" gone; remaining paragraphs untouched.
4. ✅ Coloring intro gains: "In the PDF edition, this section opens with its own linked letter grid — jump straight to the page you want to print, no committee approval required."

## C — PDF template

1. ✅ **Real TOC** (`renders_round1/toc-07.png`): leader dots, live page numbers from `counter(page).at(location)` (4 · 7 · 8 · 35 · 36 · 40 — logical folios matching the printed page numbers), every row an internal link.
2. ✅ Grid intro line, verbatim, small italic above the alphabet grid.
3. ✅ Koan typography: `linebreaks: "optimized"` + final two words nbsp-bound template-side. **Acceptance verified on all 26 letter pages, not a sample:** text-extracted every page, zero single-word lines; every koan's last line ends with a two-word pair (table in the build log — e.g. A "true north.", V "a promotion.", Z "slept well.").
4. ✅ Coloring section opens with the same grid component (`letter-grid("coloring-")`), 26 links → coloring pages 42–67, verified in the annotation audit.
5. ✅ Final page, exactly as written (`renders_round1/final_page-68.png`).

## D — rebuild + verify

- `build_map.py`: validates clean (E koan + afterword pass through).
- `myst build --html`: green; stacked signature (`<br>`) and new afterword confirmed in built HTML.
- Link audit on the final PDF: 96 internal + 2 URI annotations, **zero dangling**; link-heavy pages exactly where expected (TOC p7, alphabet grid p9, coloring grid p41).
- `seldon verify`: all 7 green after `seldon paper sync` (4 sections re-hashed).

## Renders — `handoffs/renders_round1/`

`foreword-05.png` · `toc-07.png` · `letter_C-12.png` · `letter_E-14.png` (koan edit + orphan check) · `afterword-36.png` · `colophon-40.png` · `coloring_grid-41.png` · `final_page-68.png`
