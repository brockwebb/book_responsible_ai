# HANDOFF — 2026-08-17 launch-prep batch

**Runbook:** `cc_tasks/2026-08-17_RUNBOOK.md`
**Outcome: all 5 steps complete. Nothing blocked, nothing skipped.**

Repo: https://github.com/brockwebb/book_responsible_ai · Site:
https://brockwebb.github.io/book_responsible_ai/ · HEAD `8517519` · CI green

---

## Blockers

**None.** Every task in the batch finished. Read on for the four findings that changed a
task's premise — those are the parts worth your attention.

## Per task

| # | Task | Status | RESULT |
|---|---|---|---|
| 1 | License → CC BY 4.0 | ✅ done | `cc_tasks/2026-08-17_license_cc_by_4_RESULT.md` |
| 2 | Addendum steps 1–4 (bundle, untrack `assets/`, docs, purge) | ✅ done | `cc_tasks/2026-08-17_addendum_assets_untracked_masters_RESULT.md` |
| 3 | Re-encode art + Typst PDF (as amended) | ✅ done | `cc_tasks/2026-08-17_reencode_art_then_typst_pdf_RESULT.md` |
| 4 | Addendum step 5 (history rewrite + force-push) | ✅ done | same RESULT as #2 |
| 5 | Seldon upstream ontology/rebuild fix | ✅ done | `cc_tasks/2026-08-17_seldon_upstream_ontology_rebuild_fix_RESULT.md` |

## The numbers

| | Before | After |
|---|---|---|
| `.git` pack | 134.18 MiB | **54.14 MiB** (−60%) |
| Tracked working files | 259.7 MB | **~60 MB** (−77%) |
| Fresh clone (`.git` / total) | — | **54 MB / 114 MB** |
| Committed art `book/images/` | 130 MB | **60 MB** |
| facer, per file | 3,057 KB PNG | **393 KB JPEG** (−87%) |
| One illustration, over the wire | 3,076,622 B | **380,476 B** (−88%) |
| HTML build output | 183 MB | **108 MB** |
| **PDF** | did not exist | **47 MB, 74 pages** |
| Pages Action | green | **green** (`32032991014` on `8517519`) |

Before/after pack sizes were both measured after `git gc --aggressive`, so they are
comparable.

## Seldon graph — reconciled, zero open

| ID | Task | State |
|---|---|---|
| `eada9ba4` | git bootstrap and push | completed |
| `f85cc674` | art re-encode | completed — **description amended** per addendum, outcome note added |
| `aa47145d` | typst export | completed — outcome note added |
| `7c893186` | **license flip** (registered this batch) | completed |
| `300f70fe` | **Seldon upstream fix** (registered this batch) | completed |

`seldon verify`: **all 7 checks green.** `seldon status`: **no open tasks, no stale
artifacts.**

**The runbook's "one more task from init" does not exist.** It asked me to identify a third
open task beyond `f85cc674` and `aa47145d`. There wasn't one: the `blank` template seeded
**0** bootstrap tasks (stated in the init output), and the only other ResearchTask was
`eada9ba4`, the git-bootstrap task registered in the prior session — already `completed`,
and already recorded in its own RESULT file. No unrecorded task was ever created.

**Superseded-claim scan of the graph:** two artifacts matched. `f85cc674` asserted the
byte-identical convention → amended. `99d19e41` matched "commercial" but is the inherited
read-only ontology term *"cloud parity gap"*, whose definition refers to commercial cloud
regions — a false positive, correctly left alone.

## Four findings that changed a task's premise

**1. The stale-intent grep nearly returned a false clean.** In this shell `grep` is a
function wrapping **ugrep with `--ignore-files`**, which honors `.gitignore` — and
`arc/`, `cc_tasks/`, `handoffs/`, `assets/` are all gitignored. My first sweep reported no
hits in exactly the directories the task asked me to search, silently. Re-run with
`/usr/bin/grep`: **15 hits across 11 files.** Anyone repeating this check must bypass the
wrapper.

Of those 15, two were live stale signals and are now purged. The origin was
`handoffs/HANDOFF_2026-08-17_cowork-to-claude-code.md:45` — "No LICENSE file — deliberate,
defaults to all-rights-reserved (headed toward commercial distribution, unlike the CC-BY
`ai-workflow-design`)". **That is the sentence that propagated the wrong license into
CLAUDE.md and README.md.** Both hits were replaced with dated SUPERSEDED markers rather
than deleted, so the assertion is dead but the audit trail survives.

**2. Typst *does* support WebP — and JPEG is still right, for a different reason.** The
task's premise ("Typst does not support WebP") is outdated; typst 0.14.2 renders it fine.
But PDF has no WebP object type, so typst decodes and reflates it. Same image, to PDF:

| Source | Source | PDF | Filter |
|---|---|---|---|
| JPEG q85 | 400 KB | **404 KB** | `DCTDecode` — native passthrough |
| WebP q85 | 318 KB | **2,428 KB** | `FlateDecode` — decoded, 6× bloat |

Smallest file, worst PDF. If someone later revisits this because "typst supports WebP now"
— it does, and it still shouldn't be used on the PDF path.

**3. Dropping `assets/` from history would alone have freed almost nothing.** `assets/` and
`book/images/` were byte-identical, so git stored **one blob** per image. The rewrite's
actual payload was the 27 superseded facer/cover PNG blobs, not the directory. The old
duplication convention cost double in the working tree but nothing in object storage — the
storage cost was the old PNGs.

**4. The Seldon defect was 3 bugs, not 1.** Auditing the whole event surface as the task
asked: `ontology_synced` (reported), plus **`ontology_ingested`** (same state loss, hits
seldon's own repo) and **`paper_fix`** (audit-only, but firing the same
`Unknown event_type` warning — training readers to ignore the warning that was hiding the
real bug). Fixed at seldon `86b039b`, 7 regression tests.

The subtlest part: `_do_sync` emits an event, so a naive replay handler would append one
**on every rebuild**, triggering another restore next time — an ever-growing log. Guarded
by `emit_event=False` and a dedicated test.

## Recommended next — the largest remaining lever

**Lineart is now 81% of the committed art (49 MB of 60 MB), at 1,936 KB per file.** The
re-encode task scoped it out on the assumption that "flat line art compresses well." It
does not, here — genuinely flat 1024×1536 line art should be tens of KB. At ~1.9 MB these
are almost certainly anti-aliased with tonal noise across the white field, which is
worst-case for PNG. A quantized palette or a lossless re-compress would likely take another
30–40 MB off the repo and the PDF. **Bigger than the win just banked.** Not started — out of
scope, flagged only.

Also open, minor:
- **Cosmetic PDF typography.** The typst template numbers book body sections ("2.4 D is for
  Doubt", "4.12 L") and the previous letter's definition runs into the top of the next
  page. Fine for a proof; wants a pass before publication.
- **Pre-existing seldon test failure**, unrelated to this batch:
  `tests/test_paper_build.py::test_build_paper_unknown_xref_passthrough`. Confirmed
  pre-existing by stashing my changes and re-running.
- **Seldon `conftest.py` reads `NEO4J_USERNAME`/`NEO4J_PASSWORD`**, but this machine sets
  `NEO4J_USER`/`NEO4J_PASS`. The mismatch makes all 15 Neo4j tests **silently skip** — a
  green run that tested nothing. `init.py` already accepts both spellings; conftest should
  too. Run meanwhile with:
  `NEO4J_USERNAME="$NEO4J_USER" NEO4J_PASSWORD="$NEO4J_PASS" python3 -m pytest tests/ -q`

## Deviations from the tasks as written

1. **LICENSE holds the full legal code, not the sibling's 12-line summary.** The task asked
   for both ("full legal text" *and* "match `ai-workflow-design`"), which conflict. CC states
   the deed summary "is not a substitute for the license", so the real grant ships here with
   the sibling's header framing preserved. `ai-workflow-design` is now the weaker of the
   two — flagged, not changed.
2. **A second safety bundle** was taken at the pre-rewrite HEAD. The task's bundle predates
   the license and untracking commits, so it was not a valid rollback point for the
   force-push. Both bundles verify as complete histories:
   `../book_responsible_ai_pre_restructure.bundle` (124M) and
   `../book_responsible_ai_pre_filterrepo.bundle` (134M).
3. **Stale-intent hits were annotated, not deleted.** The addendum says "purge"; the
   CLAUDE.md convention says task/handoff files are records. The assertion is removed (so it
   cannot re-seed) and a dated marker records that it existed and was corrected.
4. **The Seldon fix was committed only to its three files.** `seldon_events.jsonl` and an
   untracked design doc were already dirty in that repo when I arrived; both left alone.

## Out of scope — not started, per the runbook

- Zenodo record / `.zenodo.json` / DOI backfill — waits on Brock.
- `manuscript/` freeze.

## Useful facts for the next session

- Seldon ResearchTask lifecycle does not allow jumping to `completed`; walk
  `proposed → accepted → in_progress → completed`. And `seldon task update` needs the
  **full UUID** — an 8-char prefix returns "Task not found" (though `seldon artifact update`
  accepts the prefix).
- `seldon verify --fix` registers *new* files but does **not** re-hash *modified* tracked
  ones. After editing `book/*.md`, run `seldon paper sync`.
- `assets/` is now the untracked local master corpus — 130 MB, on this machine and in the
  bundles only. Art changes touch `book/images/` and regenerate from those masters.
