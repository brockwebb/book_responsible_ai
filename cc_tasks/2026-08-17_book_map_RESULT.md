# RESULT — Document map: scripts/build_map.py → book/book_map.yaml

**Task:** `cc_tasks/2026-08-17_book_map.md`
**Runbook2 step:** 3 of 4 · **Date:** 2026-08-17 · **Status:** complete
**Seldon ResearchTask:** `aba6f53f-7278-464c-a0e9-9eb51f777e7c` — closed `completed`

---

## Delivered

- `scripts/build_map.py` — stdlib + PyYAML only, committed.
- `book/book_map.yaml` — generated, **gitignored** (same policy as `keyword_index.md`);
  the PDF build regenerates it every run.
- Run on current content: **passes clean** — 26 letters, 7 front sections, 3 back sections.

## Deviation from spec, per the runbook's ordering

The task's parser spec describes the pre-edit entry structure (`image → koan →
definition`). Step 1 of this batch changed it: the definition is now the **figure
caption** and the koan follows the figure. The runbook orders "matter edits before map
(the map parses them)", so the parser targets the post-edit structure. Documented in the
script docstring.

## Cross-task rule check (SVG lineart)

Lineart derivation is extension-agnostic — it globs `book/images/lineart/<letter>_lineart.*`
and takes what is actually on disk, failing named (`lineart-missing` / `lineart-ambiguous`)
otherwise. After the lineart task, it resolves to **`.svg`** for all 26. Verified in the
generated map. The typst task consumes these paths from the map, so map and template agree
by construction.

## Validation gate (all named, all exit nonzero)

| Failure name | Check |
|---|---|
| `letter-count` | exactly 26 records |
| `letter-order` | A–Z, each exactly once, in order |
| `empty-field` | no empty title / koan / definition |
| `file-missing` | every facer and lineart exists on disk |
| `lineart-missing` / `lineart-ambiguous` | derivation found exactly one file |
| `duplicate-paths` | no image path used twice |
| `toc-drift` | the four content files are still in `myst.yml` toc |

## Negative test (required)

```
$ sed 's/## Q is for/## Q is fer/'   # break one heading
$ python3 scripts/build_map.py
MAP VALIDATION FAILED [letter-count]: expected 26 letter records, parsed 25
exit=1
$ revert && python3 scripts/build_map.py
OK ... exit=0, alphabet.md byte-identical to HEAD
```

## Sample record — letter M (multi-clause koan + definition, parser stress)

```yaml
- letter: M
  title: Model Review
  koan: The critic had never cooked a meal, but he could taste bias in any dish. "Too much
    salt," he said of the soup he hadn't tried. The kitchen closed. The critic published.
  definition: Inspect every model for fairness, harm, and bias. Bonus credibility if
    reviewers have never built a model themselves.
  facer: images/facer/m_facer.jpg
  lineart: images/lineart/m_lineart.svg
```

(Note: the alphabet page's M definition is shorter than the Compendium's — the map parses
`alphabet.md`, the per-letter source of truth, as specified.)

## Meta block

```yaml
meta: {title: The Overresponsible AI Handbook,
       subtitle: 'An Alphabetical Guide to Doing Nothing, Responsibly',
       author: Brock Webb, copyright_year: 2025, published_year: 2026, license: CC-BY-4.0}
front: [copyright, ai_disclaimer, dedication, foreword,
        praise_for_the_overresponsible_ai_handbook, table_of_contents, author_s_note]
back:  [afterword, the_abbreviated_compendium_..., colophon]
```

`seldon verify` all green.
