# RESULT — DOI backfill + final PDF rebuild

**Task:** `cc_tasks/2026-08-17_doi_backfill_rebuild.md`
**Date:** 2026-08-17 · **Status:** complete · **Commit:** `5c1df6a`, CI green
**Seldon ResearchTask:** `2fe21edb-45dc-4da5-921a-7ff5d21ff308` — closed `completed`
**DOI:** `10.5281/zenodo.21983981` (parameter confirmed in the task file; not a placeholder)

## Pages URL verification (required before writing it anywhere)

Fetched first, per the task:

```
https://brockwebb.github.io/book_responsible_ai/ -> HTTP 200, 29,288 bytes
content check: page contains "The Overresponsible AI Handbook"
gh api .../pages -> html_url matches
```

## Backfill locations

| Target | What |
|---|---|
| `book/front-matter.md` copyright page (+ manuscript mirror) | "This edition: DOI 10.5281/zenodo.21983981 (https://doi.org/10.5281/zenodo.21983981)." — styled like the license line |
| Colophon (+ mirror) | "This edition is archived as DOI …" **plus the 1b link fix**: closing line is now read-online-first — "Read online: brockwebb.github.io/book_responsible_ai · Source and history: github.com/brockwebb/book_responsible_ai" |
| `README.md` | Zenodo DOI badge (shields style) above the license badge + `## Citation` with the plain-text citation |
| `CITATION.cff` | `doi:` uncommented with the real value |
| `.zenodo.json` | `publication_date` is today's actual date (2026-08-17 — the placeholder happened to already be correct) |

1b sweep: `grep github.com/brockwebb` across book content found exactly one repo-only
link — the colophon line, now fixed. No other book content links only the repo.

In passing: README still said "© 2026 Brock Webb"; aligned to the settled © 2025 decision
(r1: copyright vests at creation). One word, same commit.

## Rebuild

- 68 pages (unchanged — within the ±1 acceptance), **11.8 MB** (in the 12 MB range).
- DOI verified in the extracted PDF text on **both** pages (copyright p2 logical-1,
  colophon p40 logical-39); 3 total occurrences (copyright line carries it twice: DOI +
  resolver URL).
- Renders: `handoffs/renders/doi_copyright-02.png`, `handoffs/renders/doi_colophon-40.png`.
- `myst build --html` green; **DOI live on the deployed site** (fetched
  `/back-matter`, contains `zenodo.21983981`).
- `seldon verify` all green after `paper sync`.

## CI note

The metadata-prep commit's run (`32055880708`) failed at the **Deploy to Pages** step with
a GitHub-side 503 ("No server is currently available… is githubstatus.com reporting a
Pages outage?") — the HTML build itself was green, and the rerun API returned the same 503.
Not caused by the commit. This task's push (`5c1df6a`) deployed green and the live site is
current, which supersedes the failed deploy.

## Next manual step for Brock (the only thing left)

1. Open the Zenodo draft and upload **`book/exports/overresponsible-ai-handbook.pdf`**
   (68 pp, 11.8 MB — this exact rebuilt file; it contains its own DOI).
2. Verify the form fields against **`.zenodo.json`** (title, creator, description,
   license cc-by-4.0, publication date, keywords, the two related identifiers:
   repo = isDerivedFrom, web edition = isVariantFormOf). Zenodo does **not** auto-read
   the file on a manual upload — it is your crib sheet.
3. Publish.
