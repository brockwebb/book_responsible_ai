# RESULT — Zenodo metadata prep

**Task:** `cc_tasks/2026-08-17_zenodo_metadata_prep.md`
**Date:** 2026-08-17 · **Status:** complete · **Commit:** `04f519e`
**Seldon ResearchTask:** `14da1c20-026c-49bc-b818-9cd185e136ca` — closed `completed`

## Delivered

- **`.zenodo.json`** (valid JSON): `publication` / `book`, exact title + subtitle,
  `Webb, Brock`, `cc-by-4.0`, `publication_date: 2026-08-17` (placeholder, corrected at
  publish), `dates: [{created, 2025-04}]`, the five specified keywords.
- **`CITATION.cff`** (valid YAML, cff 1.2.0): same facts; `doi` field commented with a
  `TODO(doi-backfill)` marker. Powers GitHub's "Cite this repository" box on push.

## Relation choices (task asked for the reasoning)

| Target | Relation | Why |
|---|---|---|
| `github.com/brockwebb/book_responsible_ai` | **`isDerivedFrom`** | The deposited PDF is *built from* the repo (map → pandoc → typst). The repo is the source, not a supplement to the book. |
| `brockwebb.github.io/book_responsible_ai/` | **`isVariantFormOf`** | DataCite defines it as a different form of the same resource — exactly what the web edition is. `isIdenticalTo` was rejected: the web edition is the same *work* but not the same *object* (different pagination, no PDF-only pages like the letter grid or final page). |

## Description drafted (Brock sees it at upload)

> A satirical A-to-Z alphabet book on AI governance theater: twenty-six letters, each
> pairing a koan, a full-page illustration, and a one-line definition, with a bonus
> section of twenty-six coloring pages. Written and illustrated in April 2025 and
> presented as it was made, the book skewers what happens when responsible-AI practice
> curdles into pure process, while its front and back matter make the sincere case
> underneath the satire.

## Honest scope note (required)

**Zenodo will not auto-read `.zenodo.json` for this upload.** That prefill only happens
through the GitHub-release integration; Brock is uploading the PDF manually, so the form
starts blank. `.zenodo.json` is the **crib sheet** to copy from and the durable record in
the repo — do not expect prefill magic.

## Verify

CI green on `04f519e`; `seldon verify` all 7 checks green.
