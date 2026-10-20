# RESULT — Re-encode facer art, then run the Typst PDF export

**Task:** `cc_tasks/2026-08-17_reencode_art_then_typst_pdf.md`
**As amended by:** `cc_tasks/2026-08-17_addendum_assets_untracked_masters.md`
**Runbook step:** 3 of 5 · **Date:** 2026-08-17 · **Status:** complete
**Seldon ResearchTasks:** `f85cc674` and `aa47145d` — both closed `completed` with outcome notes

---

## Headline numbers

| Metric | Before | After | Δ |
|---|---|---|---|
| `book/images/` (committed art) | 130 MB | **60 MB** | −54% |
| facer, per file (avg) | 3,057 KB PNG | **393 KB JPEG** | −87% |
| facer set total | 78 MB | **10 MB** | −87% |
| cover | 3.0 MB PNG | **376 KB JPEG** | −87% |
| lineart (unchanged, per task) | 49 MB PNG | 49 MB PNG | — |
| HTML build output | 183 MB | **108 MB** | −41% |
| Live site, one illustration | 3,076,622 B | **380,476 B** | −88% |
| **PDF (first ever built)** | — | **47 MB, 74 pages** | under the <100 MB target |

Pixel dimensions unchanged at **1024×1536** for all 27 converted images — verified post-
conversion (`27  1024 x 1536`, single bucket). Encoding was the lever, exactly as the
CLAUDE.md open item predicted; resolution was never the problem.

## The WebP premise was wrong — and JPEG is still right

The task states: *"Typst does **not** support WebP (pixmap formats: PNG/JPEG/GIF)"* and asks
for a one-image test build before converting all 26. I ran that test. **The premise is
outdated — typst 0.14.2 renders WebP fine.**

But the conclusion survives, for a better reason. Same source image, three formats, each
compiled to PDF and the PDF's image filters inspected:

| Source | Source bytes | PDF bytes | PDF filter |
|---|---|---|---|
| JPEG q85 | 400,109 | **403,547** | `DCTDecode` — embedded natively, no transcode |
| WebP q85 | 317,980 | **2,427,712** | `FlateDecode` only — decoded and reflated |
| PNG (master) | 3,076,622 | 3,527,372 | `FlateDecode` |

WebP is the smallest *file* and the worst *PDF*: **6× larger output** than JPEG. PDF has no
WebP object type, so typst must decode it and re-deflate raw pixels. JPEG is the only
format PDF carries through untouched.

So: **JPEG confirmed, on mechanism rather than on a format-support claim.** If anyone
later revisits this because "typst supports WebP now" — it does, and it still shouldn't be
used for the PDF path. Verified in the shipped PDF: **27 `DCTDecode` objects** = 26 facer
JPEGs + cover, all passed through without re-encoding.

## Amendment compliance

Per the addendum, the original steps 1–3 were changed. What was actually done:

- ✅ Masters in `assets/art/facer/` **untouched** — still 26 lossless PNG, 78 MB, verified
  after conversion. `assets/art/cover/0-OAIH-BookCover.png` likewise untouched.
- ✅ JPEG outputs written **only** to `book/images/facer/` and `book/images/cover.jpg`.
- ✅ **No mirror-copy step** performed. The "byte-identical, change both" convention is dead.
- ✅ Replaced PNGs deleted from `book/images/` only.
- ✅ `lineart/` untouched — 26 PNG.

## Build and reference updates

- `book/alphabet.md` — 26 refs `.png` → `.jpg`, zero `.png` facer refs remaining.
- `book/cover.md` and `book/myst.yml` (`cover:` key) → `images/cover.jpg`.
- `myst build --html` — 5 pages, 53 image files resolved (26 JPEG + 26 lineart PNG + cover).
- `myst build --typst` — **succeeded on the first run.** Both items flagged as unverified
  in CLAUDE.md work as written: the `plain_typst_book` template (fetched from the MyST
  template repo at build time) and the `cover:` key.
- `seldon verify` — all 7 green, after `seldon paper sync` (see the license RESULT: `--fix`
  does not re-hash *modified* tracked files, only registers new ones).
- Pushed; Actions run `32031654922` **success** on HEAD `5362736`. Live site: all 5 pages
  HTTP 200, facer serving as `image/jpeg`.

## Visual spot-check (required by step 6)

Rendered from the built PDF at 60 dpi and inspected:

| Page | Content | Result |
|---|---|---|
| 1 | Cover | Title, subtitle, cover art, author all render. No JPEG artifacts visible. |
| 12 | Facer — *D is for Doubt* | Headline, koan, full-color illustration correct. |
| 60 | Lineart — *L is for LLMs* | Clean black-and-white line art, crisp edges. |

Page count **74** — sane for cover + front matter + 26 alphabet + back matter + 26 coloring
pages.

## New finding — lineart is now the dominant cost, and the assumption behind it is wrong

The task says keep `lineart/` as PNG because *"flat line art compresses well."* It does not,
here:

- lineart averages **1,936 KB per file** — 49 MB of the remaining 60 MB, **81% of the
  committed art**.
- Genuinely flat 1024×1536 line art should be tens of KB. ~1.9 MB means these are not flat:
  almost certainly anti-aliased with subtle tonal noise across the white field, which is
  worst-case input for PNG's filter+deflate.

Left alone — the task explicitly scopes lineart out, and I did not expand scope. But it is
now the single largest lever left, larger than the one just pulled. Recorded in
`f85cc674`'s outcome note and carried into the handoff as recommended follow-up.

## Cosmetic observation (not blocking, not in scope)

The PDF carries the typst template's section numbering into the book body — alphabet pages
render as "2.4 D is for Doubt" and coloring pages as "4.12 L" — and the previous letter's
one-line definition runs into the top of the next page. Fine for a proof; a real typography
pass on `plain_typst_book` would want numbering suppressed. Not part of this task.

## Not done

Nothing in scope. Steps 1–8 all complete.
