# RESULT — Flip license to CC BY 4.0 International

**Task:** `cc_tasks/2026-08-17_license_cc_by_4.md`
**Runbook step:** 1 of 5 · **Date:** 2026-08-17 · **Status:** complete
**Seldon ResearchTask:** `7c893186-9c9a-43df-9b52-f4fd6deb59db` — closed `completed`

---

## Changes made

| # | Target | Change |
|---|---|---|
| 1 | `LICENSE` (new) | CC BY 4.0 header + copyright + **full legal code** (415 lines, 19,357 bytes) |
| 2 | `README.md` | License section → CC BY 4.0, badge, attribution line |
| 3 | `CLAUDE.md` | `**License:**` line → CC BY 4.0; "commercial work / no LICENSE deliberate" rationale removed |
| 4 | `book/myst.yml` | added `license: CC-BY-4.0` and `copyright: '2026 Brock Webb'` under `project:` |
| 5 | `book/front-matter.md` | new `## Copyright` section with CC BY 4.0 notice |
| 5 | `manuscript/01_front_matter.md` | same section, added so the two copies do not drift |
| 6 | Seldon graph | ResearchTask registered and closed |

## Deviation from the task as written — LICENSE content

The task gave two instructions that conflict in one sentence: *"full CC BY 4.0 legal text
(legalcode.txt)"* **and** *"Match how `ai-workflow-design` does it; that repo is the prior
art."*

They disagree. The sibling's `LICENSE` is a **12-line human-readable summary** ending in a
link — it is the CC *deed*, not the license grant. Creative Commons states explicitly that
the deed "is not a substitute for the license."

**Call: full legal code, with the sibling's header framing on top.** Reasoning:

- "Full legal text" is the task's own primary and more specific instruction; "match the
  sibling" reads as direction on *style and license choice*, which is preserved — same
  license, same `Copyright (c) 2026 Brock Webb` line, same "You are free to / Under the
  following terms" structure.
- A deed summary is legally weak as the operative license file in a repo. Shipping the
  real grant costs nothing and is what GitHub's license detector reads.
- The book title line was added so the grant names the work it covers.

The sibling repo is now the *weaker* of the two. Flagged, not changed — out of scope.

## Verification

**1. Zero "All rights reserved" in tracked files**

```
$ git ls-files -z | xargs -0 grep -ril "all rights reserved"
NONE (tracked)
$ grep -ic "all rights reserved" LICENSE
0
```

The CC BY 4.0 legal code does not itself contain the phrase, so the check is unambiguous.

**2. CC BY 4.0 present in every required file**

```
LICENSE                          CC BY 4.0 ✓
README.md                        CC BY 4.0 ✓
CLAUDE.md                        CC BY 4.0 ✓
book/front-matter.md             CC BY 4.0 ✓
manuscript/01_front_matter.md    CC BY 4.0 ✓
book/myst.yml                    CC BY 4.0 ✓
```

**3. `myst build --html` green** — 5 pages built, no errors.

**4. `seldon verify` all 7 checks green.**

Note: `seldon verify --fix` did **not** resolve the changed `front-matter.md` hash on its
own — it reported `run seldon paper sync`. `--fix` registers *new* files but does not
re-hash *modified* tracked ones. `seldon paper sync` fixed it (`1 updated, 4 unchanged`).
Worth knowing: `--fix` is not a superset of `paper sync`.

## Seldon lifecycle finding

`seldon task update --state completed` cannot jump straight from `proposed`. The
ResearchTask state machine requires walking:

```
proposed → accepted → in_progress → completed
```

`proposed` also allows `rejected` / `superseded`; `accepted` allows `in_progress` /
`superseded`. Also: `seldon artifact update` accepts an 8-char ID prefix, but
`seldon task update` requires the **full UUID** — an 8-char prefix returns
`Error: Task '7c893186' not found`, which reads like a missing task rather than a
too-short identifier.

## Not done

Nothing. All 6 changes and all 4 verification items complete.
