# Task: Lineart optimization — decision-rule task

Batch-1 finding changed the premise: lineart is 49 MB at ~1,936 KB/file, anti-aliased
with tonal noise — NOT flat bitonal art. Potrace is therefore not a safe default (it
needs thresholded bitonal input and may mangle noisy antialiasing). Do not pick a
method a priori; run the bake-off below on TWO representative files (pick one clean-ish
and one noisy-looking), then apply the winner to all 26 + decide cover applicability (no
— cover is color, out of scope).

## Candidates (test each on both sample files)
A. **Threshold → potrace → SVG.** Grayscale, Otsu or fixed threshold, despeckle,
   potrace. Wins if: lines stay smooth, no dropout/blob artifacts at 300% zoom, file
   < 300 KB. If it wins, it's the best answer for print (resolution-independent
   coloring pages) — that's why it's tested first despite the noise risk.
B. **Raster cleanup → PNG-8.** Grayscale, mild levels/threshold to crush tonal noise
   toward white, palette-quantize (pngquant, 8–16 levels) + oxipng. Wins if A fails
   visually; expect ~70–85% size cut.
C. **Do-nothing floor:** oxipng -o4 on originals — the fallback if B visibly degrades
   line quality (unlikely).

## Decision rule (no ratification needed)
Print fidelity beats bytes: judge each candidate at 100% and 300% zoom AND in a test
print-render at 8.5×11 (rasterize the page at 300 DPI and inspect). First candidate in
A→B→C order that shows no visible line degradation wins. Record the losing candidates'
artifacts with one screenshot each in the RESULT.

## Apply
1. Winner applied to all 26 → `book/images/lineart/` (extension may change; update
   references in `book/coloring-pages.md` and anywhere else lineart is referenced).
   Masters in `assets/art/lineart/` untouched, as always.
2. If SVG wins: confirm MyST web build renders SVGs correctly before committing.
3. Report per-file and total before/after sizes; expected total ≲ 10–15 MB (B) or
   ≲ 8 MB (A).
4. `myst build --html` green; push; CI green. `seldon verify --fix`; register + close
   ResearchTask with the method chosen and why.
