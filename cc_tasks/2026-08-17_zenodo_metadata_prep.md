# Task: Zenodo metadata prep — .zenodo.json + CITATION.cff

No dependencies; safe any time. Produces the canonical metadata record.

## Changes
1. `.zenodo.json` at repo root:
   - upload_type: publication, publication_type: book
   - title: exact book title from front-matter (with subtitle)
   - creators: [{name: "Webb, Brock"}]
   - description: 2–3 sentence abstract, factual register, mentioning April 2025
     creation and satirical genre. Draft it; Brock sees it at upload anyway.
   - license: cc-by-4.0
   - publication_date: leave "2026-08-17" placeholder — corrected at publish
   - dates: [{type: created, date: "2025-04"}]
   - keywords: responsible AI, AI governance, satire, AI ethics, alphabet book
   - related_identifiers: repo URL and the GitHub Pages URL, using the closest
     relations in Zenodo's vocabulary (e.g. isDerivedFrom for the repo,
     isIdenticalTo/isVariantFormOf for the web edition — pick, and note the choice
     in RESULT)
2. `CITATION.cff` at repo root (GitHub "Cite this repository" box): same facts,
   cff-version 1.2.0, doi field left commented with TODO until backfill.
3. Honest scope note for the RESULT: Brock is uploading the PDF manually, so Zenodo
   will NOT auto-read .zenodo.json (that only happens via the GitHub-release
   integration). The file is the crib sheet for the upload form and the durable
   record; state this so nobody expects prefill magic.
4. Commit, CI green, `seldon verify --fix`, register + close ResearchTask.
