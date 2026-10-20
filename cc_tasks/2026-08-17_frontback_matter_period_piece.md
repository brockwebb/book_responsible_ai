# Task: Front/back matter — period-piece corrections

## Changes
1. **© 2026 → © 2025** in `book/front-matter.md` (and `manuscript/01_front_matter.md`).
   Copyright vests at creation; the work is April 2025. Keep "Licensed under CC BY 4.0"
   text unchanged.
2. **Kill the fictional TOC.** The current Table of Contents section lists page numbers
   "for the print edition" — no print edition exists. Replace the entire section with a
   short section-only list, no page numbers: Foreword · Author's Note · The Alphabet ·
   Afterword · The Abbreviated Compendium · Coloring Pages. (Letter-level navigation is
   handled by the PDF letter grid + bookmarks and, later, web nav — not by this list.)
3. **Add a Colophon** to `book/back-matter.md` (after the Compendium), factual register,
   not satire. Content to include, CC drafts the prose:
   - Written and illustrated April 2025; published 2026. The gap is deliberate — the
     work is presented as it was made, a snapshot of that moment.
   - Illustrations generated with OpenAI/ChatGPT image tooling of that era, with text
     rendered in-image; deliberately not regenerated with newer models.
   - Text is a human–AI collaboration (consistent with the AI Disclaimer up front —
     do not remove or soften the disclaimer, it stays).
   - Built with MyST (web) and Typst (PDF); source at github.com/brockwebb/book_responsible_ai.
   Brock reviews this at the read-through gate — flag the colophon in the handoff.
4. **Web caption restyle** in `book/alphabet.md`: keep all text, but convert the bold
   definition line under each image into a MyST figure caption (switch `{image}` →
   `{figure}` with the definition as caption). Rationale: on web it reads as a caption
   and stays searchable; the PDF build does not consume this file.
5. **Alt text**: replace the generic "— illustration" alt on each of the 26 images with
   a one-line alt derived from that letter's definition (the baked-in text is invisible
   to screen readers; the alt is the accessible copy of it).
6. Mirror content changes into `manuscript/` counterparts to prevent drift.
7. `seldon verify --fix`; register + close as ResearchTask.

## Verification
- `myst build --html` green, captions render, no page-number TOC anywhere.
- RESULT file with the drafted colophon text quoted in full (for Brock's read-through).
