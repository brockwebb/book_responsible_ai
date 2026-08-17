# The Overresponsible AI Handbook

*An Alphabetical Guide to Doing Nothing, Responsibly*

**Status:** Manuscript complete, art in review, production in progress.

## What This Is

A satirical alphabet book — twenty-six letters, twenty-six koans, twenty-six illustrations — skewering what happens when "responsible AI" curdles into pure process: committees, checklists, and the confident art of doing nothing at all. Each letter pairs a short koan with a full-page illustration and a one-line definition. A bonus coloring-page section runs in the back.

It is a satire with a straight face underneath it: see the Author's Note in the front matter.

## Format

This is an ebook-first project — a PDF edition and a web/GitHub "book" edition (built with [MyST](https://mystmd.org)) — no print run planned at this time. Image sizing and resolution are being evaluated for on-screen (not print) delivery.

## Repository Structure

```
book_responsible_ai/
├── manuscript/        # Source prose — the editorial working copy
├── book/               # MyST publishing project (the buildable book)
│   ├── myst.yml         # Book config / table of contents
│   ├── cover.md, front-matter.md, alphabet.md, back-matter.md, coloring-pages.md
│   ├── images/           # Final selected art used in the book (facer + lineart)
│   └── exports/           # Build output (PDF), not tracked in git
├── assets/art/          # Selected art corpus (source copies of what the book uses)
│   ├── facer/              # Color "facer" illustrations (one per letter, final)
│   ├── lineart/             # Lineart coloring-page illustrations (one per letter, final)
│   └── cover/                # Cover art master
└── .github/workflows/    # CI: builds and deploys the MyST web edition
```

`arc/` at the repo root holds old/rejected art variants. It's gitignored — not tracked, not published. Every file that made the cut already lives at the top level of `assets/art/` and `book/images/`; `arc/` is just a local scratch pile, kept around in case an old variant is ever needed again.

## Building

```bash
npm install -g mystmd
cd book
myst build --html     # web edition
myst build --typst    # PDF edition (exports/overresponsible-ai-handbook.pdf)
```

## Author

Brock Webb.

## License

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

CC BY 4.0. See [LICENSE](LICENSE).

© 2026 Brock Webb. You may share and adapt this work, including commercially, provided you give appropriate credit, link to the license, and indicate if changes were made.
