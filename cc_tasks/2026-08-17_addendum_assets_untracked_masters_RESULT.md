# RESULT — Addendum: assets/ as untracked masters

**Task:** `cc_tasks/2026-08-17_addendum_assets_untracked_masters.md`
**Runbook steps:** 2 (addendum steps 1–4) and 4 (addendum step 5) · **Date:** 2026-08-17
**Status:** complete — all 5 steps, including the history rewrite

---

## Size outcome

| Measure | Before | After | Δ |
|---|---|---|---|
| `.git` pack (`size-pack`) | 134.18 MiB | **54.14 MiB** | **−60%** |
| `.git` on disk | 144 MB | **54 MB** | −62% |
| Tracked working files | 259.7 MB | **~60 MB** | −77% |
| **Fresh clone, `.git`** | — | **54 MB** | |
| **Fresh clone, total** | ~400 MB equivalent | **114 MB** | |

Both "before" and "after" pack figures were taken **after `git gc --aggressive --prune=now`**,
so they are directly comparable — filter-repo repacks, and comparing a loose-object repo to
a packed one would have overstated the win.

## Step 1 — Safety bundles

```
../book_responsible_ai_pre_restructure.bundle   124M   @ 3412f4f   "The bundle records a complete history"
../book_responsible_ai_pre_filterrepo.bundle    134M   @ 5362736   "The bundle records a complete history"
```

The task asked for one bundle, taken before the restructure. I took a **second** at the
pre-rewrite HEAD: the first bundle predates the license and untracking commits, so it was
not a usable rollback point for the force-push. Both `git bundle verify` clean.

## Step 2 — assets/ untracked

`.gitignore` gained `assets/` (with a comment explaining masters vs. published copies);
`git rm -r --cached assets/` removed **53 files** from the index. Working tree untouched —
all 130 MB of masters still on disk.

**Verification (required):**
```
$ git ls-files | grep '^assets/'
NONE — assets/ fully untracked ✓
$ git check-ignore -q assets/ && echo IGNORED
assets/ IGNORED ✓
```

## Step 3 — Documentation

`CLAUDE.md` — the structure block now marks `assets/art/` as `LOCAL MASTER CORPUS —
GITIGNORED, never committed`, and the old paragraph asserting the byte-identical
convention was replaced with a new **"Art: masters vs. published copies"** section stating
the rule (art changes touch `book/images/` only) and explicitly recording that the old
convention is dead and must not be restored. The "Repo weight" open item was updated from
open to addressed.

`README.md` — `assets/art/` removed from the published structure block; a new paragraph
describes `assets/` and `arc/` together as the two gitignored, author-machine-only
directories.

**Verification (required):** neither file states the byte-identical convention.

## Step 4 — Stale-intent sweep

### The sweep nearly produced a false clean — worth recording

My first repo-wide `grep` returned **no hits in `arc/`, `cc_tasks/`, or `handoffs/`** and
looked clean. It was wrong. In this shell, `grep` is a **function wrapping `ugrep` with
`--ignore-files`**, which honors `.gitignore` — and every directory the task specifically
asked me to search is gitignored. A gitignore-aware grep is precisely the wrong tool for
"search the ignored working dirs for a stale signal," and it fails **silently**.

Re-run with `/usr/bin/grep`. That is the authoritative sweep below. Anyone repeating this
check must bypass the wrapper.

### All 15 hits, classified

**A. CC BY's own permissive language — keep, this is the new license working as intended**

| File:line | Text |
|---|---|
| `LICENSE:10` | "even commercially" — the CC BY grant |
| `README.md:54` | "including commercially" — attribution notice |
| `book/front-matter.md:9` | same |
| `manuscript/01_front_matter.md:9` | same |

**B. Audit trail describing the flip — keep, these record the correction**

`cc_tasks/2026-08-17_license_cc_by_4.md:5,16` · `..._license_cc_by_4_RESULT.md:15,48,50` ·
`..._addendum_assets_untracked_masters.md:23,24` (the grep spec itself) ·
`2026-08-17_RUNBOOK.md:25` · `seldon_events.jsonl:16`

`seldon_events.jsonl` is an **append-only event log and the source of truth for
`seldon rebuild`** — editing it would corrupt graph replay. Left alone deliberately; its
single hit is the ResearchTask description that records the flip as superseded.

**C. Live stale signal — PURGED (2 hits)**

| File:line | Original text | Action |
|---|---|---|
| `handoffs/HANDOFF_2026-08-17_cowork-to-claude-code.md:45` | "No LICENSE file — deliberate, defaults to all-rights-reserved (this is headed toward commercial distribution, unlike the CC-BY `ai-workflow-design`)" | Assertion removed; replaced with a blockquoted **[SUPERSEDED 2026-08-17 — DO NOT ACT ON THE ORIGINAL TEXT HERE]** marker naming CC BY 4.0 and citing the license task |
| `cc_tasks/2026-08-17_git_bootstrap_and_push.md:32` | "this is headed toward commercial distribution but the repo itself is public" | Clause removed; HTML-comment SUPERSEDED marker in its place |

**The handoff line is the source.** It is the sentence that propagated into `CLAUDE.md` and
`README.md` and caused the wrong license to be recorded in the first place. It is now dead.

Both were **annotated rather than deleted outright** — the assertion is gone (so it cannot
re-seed), but the record that it existed and was corrected survives. This reconciles the
addendum's "purge" with the CLAUDE.md convention that task/handoff files are records, not
editable-in-place. The addendum supersedes on the substance; nothing is lost on the audit.

Post-purge sweep: every surviving hit sits inside an explicit supersession, spec, or audit
context. Zero assert commercial intent as current fact.

## Step 5 — History rewrite

Gate honored: run only after builds and Pages were green. Both were (Actions
`32031654922` success) before starting.

```
git filter-repo --invert-paths \
  --path assets/ \
  --path-glob 'book/images/facer/*.png' \
  --path book/images/cover.png --force
```

### Why `--path assets/` alone would have freed almost nothing

Pre-rewrite object counts looked wrong at first — only **2** objects matched `assets/`,
against 26 for `book/images/facer/*.png`. That is not an error: `assets/` and
`book/images/` held **byte-identical** files, so git stored **one blob** per image and
`rev-list --objects` reports it under a single representative path. Dropping `assets/`
alone would have removed path entries, not bytes. The 27 facer/cover PNG blobs were the
actual payload — which is why the glob mattered more than the directory.

The old byte-identical convention thus cost double in the *working tree* but not in *object
storage*; the storage cost was the superseded PNGs, and only the rewrite reclaims it.

**Verification after rewrite:**

| Check | Result |
|---|---|
| `assets/` objects in history | **0** |
| `book/images/facer/*.png` in history | **0** |
| `book/images/cover.png` in history | **0** |
| `book/images/facer/*.jpg` in history | 26 ✓ current art intact |
| `book/images/lineart/*.png` in history | 26 ✓ |
| `git ls-files \| grep ^assets/` | **0** |
| Commits preserved | 7 of 7 (SHAs rewritten) |
| Working tree | masters 130 MB intact, 26 JPEG + 26 lineart present |

filter-repo removed the `origin` remote as designed; re-added and force-pushed:
`+ 5362736...cbbf3ca main -> main (forced update)`.

**Post-force-push confirmation:** Actions run `32032009119` **success** on `cbbf3ca`; all 5
live pages HTTP 200; facer serving `image/jpeg` at 380,476 bytes. Fresh clone from GitHub:
`.git` 54 MB, total 114 MB, `assets/` absent, 26 JPEGs present.

Assumption on record, as the task required: single-developer repo, no other clones that
matter, two verified bundles exist. Force-push was authorized by the addendum and the
runbook.

## Not done

Nothing. All 5 steps complete; `git-filter-repo` was installed, so the documented skip
path was not needed.
