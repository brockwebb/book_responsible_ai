# The Overresponsible AI Handbook

*An Alphabetical Guide to Doing Nothing, Responsibly*

**Status:** Published. **Read online:** https://brockwebb.github.io/book_responsible_ai/ · **Archived:** [DOI 10.5281/zenodo.21983981](https://doi.org/10.5281/zenodo.21983981) · Source: this repo.

## What This Is

A satirical alphabet book — twenty-six letters, twenty-six koans, twenty-six illustrations — skewering what happens when "responsible AI" curdles into pure process: committees, checklists, and the confident art of doing nothing at all. Each letter pairs a short koan with a full-page illustration and a one-line definition. A bonus coloring-page section runs in the back.

It is a satire with a straight face underneath it: see the Author's Note in the front matter.

## Format

This is an ebook-first project: a PDF edition (archived on Zenodo) and a web edition (built with [MyST](https://mystmd.org)). No print run planned at this time.

## Repository Structure

```
book_responsible_ai/
├── manuscript/        # Source prose — the editorial working copy
├── book/               # MyST publishing project (the buildable book)
│   ├── myst.yml         # Book config / table of contents
│   ├── cover.md, front-matter.md, alphabet.md, back-matter.md, coloring-pages.md
│   ├── images/           # THE published art — facer + lineart, web/PDF weight
│   └── exports/           # Build output (PDF), not tracked in git
└── .github/workflows/    # CI: builds and deploys the MyST web edition
```

Two directories at the repo root are gitignored and exist only on the author's machine:

- **`assets/`** — the master art corpus: clean lossless originals, kept so resolution or re-encoding work can be redone from source. Not published content. `book/images/` holds the derived copies that ship, so art changes touch `book/images/` only.
- **`arc/`** — old/rejected art variants and `.xcf` sources. A scratch pile, kept in case an old variant is ever wanted again.

## Building

```bash
npm install -g mystmd
cd book && myst build --html   # web edition

./scripts/build_pdf.sh         # PDF edition (book/exports/overresponsible-ai-handbook.pdf)
                               # requires: typst, pandoc, python3 + PyYAML
```

The PDF is a standalone Typst book (`book/pdf/main.typ`) driven by a generated
document map (`scripts/build_map.py` → `book/book_map.yaml`), not a MyST export —
the book's layout (landscape letter spreads, full-bleed posters, letter-grid
navigation) needs a real template. One PDF path only.

## Author

Brock Webb.

## License

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21983981.svg)](https://doi.org/10.5281/zenodo.21983981)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

CC BY 4.0. See [LICENSE](LICENSE).

© 2025 Brock Webb. You may share and adapt this work, including commercially, provided you give appropriate credit, link to the license, and indicate if changes were made.

## Citation

> Webb, Brock. *The Overresponsible AI Handbook: An Alphabetical Guide to Doing Nothing, Responsibly*. 2026. DOI: 10.5281/zenodo.21983981.

Or use GitHub's "Cite this repository" (from `CITATION.cff`).
