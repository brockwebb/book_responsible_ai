# ADDENDUM — supersedes parts of 2026-08-17_reencode_art_then_typst_pdf.md
# and the "byte-identical duplicate" convention in CLAUDE.md

## Decision (Brock, 2026-08-17, chat)
`assets/` is NOT published content and must not be committed. It is the local,
untracked **master corpus** (clean lossless originals, kept in case resolution/
re-encoding work is ever redone). `book/images/` is the ONLY committed art —
derived, web/PDF-weight copies. The old convention "assets and book/images must
stay byte-identical, change both" is dead.

This supersedes step 2 of the re-encode task: do **not** convert `assets/` to
JPEG and do **not** mirror-copy. Masters stay PNG in `assets/`; JPEG conversion
outputs go only to `book/images/facer/`.

## Changes (run BEFORE the re-encode task)
1. Safety first: `git bundle create ../book_responsible_ai_pre_restructure.bundle --all`
2. Add `assets/` to `.gitignore`; `git git rm -r --cached assets/`; commit.
3. Update `CLAUDE.md` and `README.md`: repo-structure sections and the
   duplication convention → assets = untracked local masters, book/images =
   committed derived copies, art changes touch book/images only (regenerate
   from masters when needed).
4. Grep the whole repo (including `arc/`, `handoffs/`, `cc_tasks/` history,
   any stray notes) for the stale commercial-intent signal: `Amazon`,
   `commercial`, `all rights reserved`, `no open license` (case-insensitive).
   Report every hit in RESULT and purge any that could re-seed the wrong
   license decision in a future session. This is how the CC BY intent got
   flipped once; kill the source.

## Changes (run AFTER the re-encode task completes and builds are green)
5. History rewrite: `git filter-repo` to drop `assets/` and the deleted
   `book/images/facer/*.png` blobs from history. Force-push main. Confirm the
   Pages Action re-runs green and the site serves. Report clone size before/
   after (`git count-objects -vH`).
   Assumption on record: single-developer repo, no other clones that matter,
   bundle backup exists. If filter-repo is not installed and can't be installed
   cleanly, skip step 5, say so in RESULT — gitignore alone fixes the
   doubling going forward; history bloat is then a known cost, not a blocker.

## Verification
- `git ls-files | grep ^assets/` returns nothing.
- CLAUDE.md/README no longer state the byte-identical convention.
- RESULT file: `cc_tasks/2026-08-17_addendum_assets_untracked_masters_RESULT.md`
  with grep hits, purge actions, and size numbers.
