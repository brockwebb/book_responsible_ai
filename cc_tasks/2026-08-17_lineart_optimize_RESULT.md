# RESULT — Lineart optimization (bake-off)

**Task:** `cc_tasks/2026-08-17_lineart_optimize.md`
**Runbook2 step:** 2 of 4 · **Date:** 2026-08-17 · **Status:** complete
**Seldon ResearchTask:** `012b6690-d640-4b84-8214-d9d921e34b5c` — closed `completed`
**Winner: Candidate A — threshold → mkbitmap → potrace → SVG**

---

## Headline numbers

| | Before | After | Δ |
|---|---|---|---|
| `book/images/lineart/` | 49 MB (26 PNG) | **2.0 MB (26 SVG)** | **−96%** |
| Per file | avg 1,936 KB | avg ~77 KB, max 223 KB (`x`) | all < 300 KB criterion |
| Committed art total | 60 MB | **~13 MB** | |

Masters in `assets/art/lineart/` untouched (26 lossless PNG). Cover: not applicable —
color art, explicitly out of scope per the task.

## Sample selection (measured, not guessed)

Unique-gray count per file was measured as the noise proxy. Chosen:
- **n** — cleanest (12,784 unique grays)
- **g** — noisiest (61,415 unique grays)

## Bake-off

Tooling installed for the test: `potrace`/`mkbitmap` and `oxipng` via Homebrew
(`pngquant`, ImageMagick already present).

| Candidate | Pipeline | n | g |
|---|---|---|---|
| **A** | gray → `mkbitmap -f 4 -s 1 -t 0.48` → `potrace -s --flat` | **40 KB** | **91 KB** |
| B | gray → `-level 12%,88%` → `pngquant 8` → `oxipng -o4` | 37 KB | 71 KB |
| C | `oxipng -o4` on original | 1,541 KB | 2,680 KB |

Note on B: `pngquant --quality 40-90` **refused the noisy file** (quality floor unmet, no
output); B's g number required dropping the floor. C confirms the batch-1 diagnosis — these
are not flat line art, so lossless recompression recovers only ~10–22%.

## Decision (per the task's rule — no ratification sought)

Judged at 100% and 300% zoom and in a 300-DPI 8.5×11 print render. **A shows no visible
line degradation on either sample**, including the noisy g: lines smooth, no dropout, no
blob artifacts, faces/hatching/in-image text intact. First candidate in A→B→C order to
pass → **A wins**, and it is the best answer for print (resolution-independent coloring
pages), exactly why the task ordered it first despite the noise risk.

The potrace noise risk did not materialize because `mkbitmap`'s highpass filter (`-f 4`)
was designed for exactly this input class — scanned/noisy line art — and cleanly separated
the tonal paper noise from the lines before tracing.

Comparison renders (original | A | B at 300% zoom) and the 300-DPI print renders are in the
session scratchpad: `scratchpad/bakeoff/{n,g}_compare300.png`, `g_print_A.png`,
`g_print_B.png`, plus `x_check.png` (extra spot-check on the most complex file — stippled
textures and "APOCALYPSE PROBABILITY" text preserved). Losing candidates: B showed no
gross artifacts either (it lost only on order); C lost on size, shown by the numbers above.

## Whole-set application gate

A trace can fail locally on one file, so applying the winner included a per-file sanity
check: rasterized each SVG and compared ink coverage against the thresholded source.
Max delta 0.028 with a small uniform positive bias (slightly heavier lines from the
threshold + trace smoothing) and **no negative outliers — the signature of dropped
lines — anywhere**. `x` (the 6.3 MB source) eyeballed additionally.

## Applied

- 26 SVGs → `book/images/lineart/`; 26 PNGs deleted from there.
- `book/coloring-pages.md`: 26 refs `.png` → `.svg`, zero PNG refs left.
- No other lineart references existed outside generated `_build/` output.
- **MyST web build confirmed rendering SVGs before commit** (task step 2): 26 SVGs copied
  into `_build/html`, referenced in the built coloring page.
- `seldon verify` all green after `seldon paper sync`.

## Handoff note for the typst task

Lineart is now **SVG**. Typst renders SVG natively; the map task derives lineart paths
extension-agnostically. Both cross-task rules from the runbook are satisfied downstream.
