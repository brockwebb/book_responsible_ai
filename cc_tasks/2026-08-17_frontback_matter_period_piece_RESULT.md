# RESULT — Front/back matter period-piece corrections

**Task:** `cc_tasks/2026-08-17_frontback_matter_period_piece.md`
**Runbook2 step:** 1 of 4 · **Date:** 2026-08-17 · **Status:** complete
**Seldon ResearchTask:** `6472df92-3686-4eb1-a9df-8436dae4d8dd` — closed `completed`

---

## Changes

| # | Change | Files |
|---|---|---|
| 1 | © 2026 → **© 2025** (license text untouched) | `book/front-matter.md`, `manuscript/01_front_matter.md` |
| 2 | Fictional page-numbered TOC (39 lines incl. "print edition" note) → one section-only line | both front matters |
| 3 | **Colophon** added after the Compendium | `book/back-matter.md`, `manuscript/03_back_matter.md` (verified identical by diff) |
| 4 | 26 × `{image}` → `{figure}` with the bold definition line as the caption | `book/alphabet.md` |
| 5 | 26 × generic `— illustration` alt → definition-derived alt text | `book/alphabet.md` |
| 6 | Mirroring | © + TOC + colophon mirrored; `manuscript/02_alphabet.md` untouched — no *content* changed in the alphabet (the caption/alt conversion is book-side MyST markup; every word is identical) |

## New TOC line (replaces the fiction)

> Foreword · Author's Note · The Alphabet · Afterword · The Abbreviated Compendium · Coloring Pages

## Colophon — full text, for Brock's read-through gate

> ## Colophon
>
> This book was written and illustrated in April 2025 and published in 2026. The gap is deliberate: the work is presented as it was made, a snapshot of that moment, unrevised.
>
> The illustrations were generated with OpenAI's ChatGPT image tooling of that era, with the text rendered directly in the images. They have deliberately not been regenerated with newer models; their quirks, including the occasional mangled word, are part of the record.
>
> The text is a human–AI collaboration, as the AI Disclaimer at the front of this book already admits.
>
> The web edition is built with MyST; the PDF edition with Typst. Source and history: [github.com/brockwebb/book_responsible_ai](https://github.com/brockwebb/book_responsible_ai).

The AI Disclaimer up front was **not** removed or softened.

## Figure conversion detail

Transform was programmatic (regex over the perfectly regular 26-entry structure) with
hard assertions: exactly 26 matches, zero `{image}` directives left, zero `— illustration`
alts left. Entry order after conversion: heading → figure (image + definition caption) →
koan. The definition now sits with the image it captions; the koan follows the figure.
Sample:

```
```{figure} images/facer/a_facer.jpg
:alt: A is for Alignment — No one knows what it means, but saying it frequently makes everyone nod in solemn agreement.
:width: 100%

**A is for Alignment** — No one knows what it means, but saying it frequently makes everyone nod in solemn agreement.
```
```

Alt text = the definition line as plain text (bold stripped). The poster's baked-in text
is invisible to screen readers; the definition is its accessible copy.

## Verification

- `myst build --html` green, 5 pages.
- **26 `<figcaption>` elements** in the built alphabet page (counted by occurrence — the
  built HTML is minified to few lines, so `grep -c` line-counting undercounts; `grep -o | wc -l`
  is the correct check).
- Real alt text confirmed in built HTML.
- Zero "print edition"/page-number TOC content in built front matter.
- `seldon verify` all green after `seldon paper sync` (3 sections updated).

## Note for the map task (step 3)

The alphabet entry structure changed: the parser spec in `2026-08-17_book_map.md` describes
the pre-edit order (image → koan → definition). Post-edit reality is **figure(caption=definition) → koan**.
Per the runbook ("matter edits before map — the map parses them"), `build_map.py` is written
against the post-edit structure.
