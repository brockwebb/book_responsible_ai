# Task: Read-through revisions, round 1 (Brock's edits, 2026-08-17)

All decisions below are settled — apply, don't re-ask. Brock reviews the rebuilt PDF
afterward. Mirror every content change into the manuscript/ counterpart.

## A. Content edits — book/front-matter.md
1. Foreword, signature block — Dr. Prudence's titles become (stacked, both lines):
   "Chief Executive Officer, The Responsible AI Decommissioning (RAID) Society"
   "Founding Chair, International Bureau of Oversight, Hesitation, and Second-Guessing"
   (keep the "Author of ..." line)
2. Foreword: "to Zero Trust (in anything remotely innovative)" →
   "to Zero AI (the perfect model that generates nothing)"
3. Foreword: "alphabetized absurdity" → "alphabetized rigor" (she believes it — she
   would never call it absurd)
4. Foreword, "May this book serve..." sentence → "May this book serve as both
   inspiration and reassurance for ethics committees, oversight boards, and concerned
   citizens everywhere — and for those brave souls who have achieved perfect AI safety
   by never using it at all."
5. Author's Note: "technology that works for everyone. This requires..." → "technology
   that works for the benefit of humanity. It will never work equally for everyone, and
   honesty about that beats pretending otherwise. Progress has never waited for
   unanimous consent, and it shouldn't start now. This requires..."
6. Praise section: NO change (Will B. Done stays — decided).
7. TOC section in markdown: reformat as a one-item-per-line list (no page numbers in
   markdown; real page numbers come from the PDF template, see C1).

## B. Content edits — book/alphabet.md + book/back-matter.md + book/coloring-pages.md
1. E koan: "The eye blinked." → "The eye just blinked and stared." (Brock's edit)
2. Afterword: replace ENTIRE section with the four-paragraph draft in
   handoffs-adjacent source below — verbatim:

   If you've made it this far, you already know the truth behind the satire:
   responsible AI matters. It works best as an enabler — focused on outcomes, not
   performances of concern.

   Everything in moderation, including moderation. There will be risk. There will be
   accidents and unintended consequences. These are reasons to pay attention — not
   excuses to do nothing.

   The honest problem is that we don't know what we don't know, and no exhaustive
   list of what-ifs will fix that. The only way out is through: build, test, learn,
   improve. Discovery teaches what speculation never will.

   So laugh at our alphabet of overresponsibility. Then go make meaningful progress —
   and don't let too much responsibility get in the way.

3. Colophon, first paragraph → "This book was written and illustrated in April 2025 —
   a line in the sand, drawn on purpose. Whether it ages like wine, rots on schedule,
   or persists like a Twinkie through the AI apocalypse is left as an exercise for the
   future. The work is presented as it was made, a snapshot of that moment, unrevised."
   (Delete "and published in 2026". Keep remaining colophon paragraphs unchanged.)
4. Coloring pages: add intro line + note that PDF gets its own linked grid (C4).

## C. PDF template edits — book/pdf/*.typ
1. Real TOC page: sections with leader dots, actual page numbers, internal links.
2. Letter-grid index intro line above the grid:
   "Select any letter below to be transported directly to its designated instructional
   unit. All navigation pathways have been risk-assessed and approved for your safety."
3. Koan typography: set par linebreaks to "optimized" for the koan block AND bind the
   final two words of each koan with a non-breaking space at render time (template-side,
   not in the markdown). Acceptance: zero single-word lines across all 26 koans —
   verify by rasterizing all letter pages and checking, not by sampling.
4. Coloring section: add a linked letter grid as its opening page (same component as
   the alphabet grid, links target coloring pages).
5. New final page of the book, exactly:

   THIS PAGE INTENTIONALLY LEFT BLANK

   [small italic] Upon review, the Committee finds the above statement renders this
   page non-blank. A remediation plan is under development. Estimated completion:
   eventually.

   THE END (pending final approval)

## D. Rebuild + verify
- build_map.py must still validate (the E koan and afterword changes pass through it).
- scripts/build_pdf.sh → fresh PDF; spot-render: foreword page, TOC, letter C and E
  pages (orphan check + koan edit), afterword, colophon, coloring grid, final page →
  handoffs/renders_round1/.
- myst build --html green; push; CI green; seldon verify --fix; register + close
  ResearchTask.
- RESULT: before/after page count and size, plus paths to renders.
