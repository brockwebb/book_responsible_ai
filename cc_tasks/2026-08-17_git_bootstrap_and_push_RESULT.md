# RESULT — bootstrap git repo, create GitHub repo, push, enable Pages

**Task:** `cc_tasks/2026-08-17_git_bootstrap_and_push.md`
**Date:** 2026-08-17 · **Status:** complete
**Executed by:** Claude Code, locally against `/Users/brock/GitHub/book_responsible_ai`

---

## Summary

| Item | Value |
|---|---|
| Commit hash | `d4172d9` |
| Commit message | Organize manuscript, art assets, and MyST publishing structure |
| Files committed | 121 |
| Repo URL | https://github.com/brockwebb/book_responsible_ai |
| Visibility | public |
| Default branch | `main` |
| Pages source | GitHub Actions (`build_type: workflow`) — **enabled** |
| Pages URL | https://brockwebb.github.io/book_responsible_ai/ |
| First Actions run | `32025472032` — **success** |
| Live site | https://brockwebb.github.io/book_responsible_ai/ — all 5 pages HTTP 200 |

---

## 1. Stale git state — what was actually there

The handoff warned about a possibly-broken `.git/` from the Cowork session. It was worse
than a stuck lockfile, and this is worth recording because it would have shipped the wrong
repo if `rm -rf .git` had been skipped as unnecessary.

Inspected before deleting:

- **Zero commits** (`git rev-list --all --count` → 0), zero stashes. Nothing was at risk.
- The index held **the pre-rename directory layout**: `assets/art/main/` (26 files) and
  `assets/art/coloring/` (26 files) — the names used *before* the reorganization to
  `facer/` and `lineart/`.
- The real `assets/art/facer/` and `assets/art/lineart/` were **untracked** (`??`).
- The index also held **51 files under `assets/art/archive/`** — the rejected art variants
  and `.xcf` sources — staged as added, then deleted from the working tree (`AD`).

Committing that index would have published 51 rejected variants and two GIMP sources
while omitting the entire final art set. `rm -rf .git` was correct and necessary.

This also **contradicts the handoff's §5 claim** that `assets/art/archive/` was "not
tracked by git." It was staged in that index at the time the claim was written. The
directory is empty on disk and — now that the index is gone and git does not track empty
directories — the claim is finally true. Corrected in `CLAUDE.md`.

## 2. Verification 1 — `git status --short` before commit

Required check: none of `arc/`, `cc_tasks/`, `handoffs/`, `audits/`, `.DS_Store` present.

```
$ git status --short | grep -Ei 'arc/|cc_tasks|handoffs|audits|DS_Store|_build'
CLEAN: none of arc/, cc_tasks/, handoffs/, audits/, .DS_Store, _build/ staged

$ git diff --cached --name-only | wc -l
121
```

**PASS.** The 121 staged files break down as 15 non-image files + 53 `book/images/` +
53 `assets/art/`:

```
.github/workflows/deploy.yml   book/alphabet.md          manuscript/01_front_matter.md
.gitignore                     book/back-matter.md       manuscript/02_alphabet.md
CLAUDE.md                      book/coloring-pages.md    manuscript/03_back_matter.md
README.md                      book/cover.md             manuscript/04_coloring_pages.md
                               book/front-matter.md      manuscript/art_selections.md
                               book/myst.yml
```

## 3. Verification 2 — commit and remote

```
$ git log --oneline -1
d4172d9 Organize manuscript, art assets, and MyST publishing structure

$ git remote -v
origin  https://github.com/brockwebb/book_responsible_ai.git (fetch)
origin  https://github.com/brockwebb/book_responsible_ai.git (push)
```

**PASS.** One commit, `origin` points at the right repo.

## 4. Verification 3 & 4 — repo and Pages

```
$ gh repo view brockwebb/book_responsible_ai --json name,owner,visibility,defaultBranchRef,url
{"defaultBranchRef":{"name":"main"},"name":"book_responsible_ai",
 "owner":{"login":"brockwebb"},
 "url":"https://github.com/brockwebb/book_responsible_ai","visibility":"PUBLIC"}
```

**PASS.** Public, owned by `brockwebb`, default branch `main`.

**Pages — task's premise was wrong, in our favor.** The task said Pages "cannot be done
from the CLI" and flagged it as a possible manual browser step for the user. It can:

```
$ gh api -X POST repos/brockwebb/book_responsible_ai/pages -f build_type=workflow
{"html_url":"https://brockwebb.github.io/book_responsible_ai/",
 "build_type":"workflow","source":{"branch":"main","path":"/"},
 "public":true,"https_enforced":true}
```

Read back to confirm it stuck. **No user action required.** Recorded the command in
`CLAUDE.md`'s Build System section so it is not rediscovered next time.

## 5. Verification 5 — first Actions build

Run `32025472032` (`deploy-book`), triggered by the push to `main`. **Conclusion:
success.** Every step passed:

```
Set up job                  success     Install MyST Markdown     success
Run actions/checkout@v4     success     Build HTML Assets         success
Setup Pages                 success     Upload artifact           success
Run actions/setup-node@v4   success     Deploy to GitHub Pages    success
```

Note a race worth knowing about, since it nearly bit: the push fired the workflow *before*
Pages was enabled, and `actions/configure-pages@v3` fails outright if Pages is not yet
configured. The run was still queued when the `gh api` call landed, so `Setup Pages`
cleared. If a first run on a fresh repo ever fails at that step, this is the cause, and
`gh run rerun` after enabling Pages fixes it. Enabling Pages *before* the first push
avoids it entirely.

**Live site verified** — not just "the workflow was green":

```
https://brockwebb.github.io/book_responsible_ai/                 HTTP 200
  /alphabet  /coloring-pages  /front-matter  /back-matter        HTTP 200 (each)
  /build/a_facer-9155ac18....png     HTTP 200, 3,076,622 bytes, image/png
```

The whole book is published and the art loads. That last line is also the image-weight
problem in §6 made concrete: **3.07 MB over the wire for a single illustration**, and a
reader paging through the alphabet pulls 26 of them.

**Independent local build, run before pushing** — so CI failure and content failure can be
told apart:

```
$ cd book && myst build --html
```

Succeeded. 5 pages built (`index`, `front-matter`, `alphabet`, `back-matter`,
`coloring-pages`), all served 200, 60 image files copied into `_build/html`, no errors.
Output is 183 MB. **`book/myst.yml` and all image paths are confirmed good** — the open
item from the handoff predicting possible path/config problems is resolved for the HTML
path.

One caveat: local `myst` is **v1.8.2**; CI does `npm install -g mystmd`, i.e. latest
(**v1.10.1** today). A clean local build is not proof of a clean CI build. Noted in
`CLAUDE.md`.

`myst build --typst` (the PDF export) was **not** run — out of scope for this task, and
still untested. Left as an open item.

## 6. Handoff open items — disposition

Task asked whether the handoff's two open items were left untouched. Both were, but the
audit produced findings on them that are recorded rather than acted on:

| Item | Status | Note |
|---|---|---|
| `b_colorpage.png` reference | **Closed, no work needed** | `manuscript/art_selections.md` already documents the resolution on its face: no file by that name ever existed anywhere in the project; only `b_lineart.png` did, and it is what the book uses. Stale reference, not a lost asset. No follow-up task needed. |
| Image sizing / resolution | **Open, but re-diagnosed** | Untouched, as required. However the item's premise was never measured and is wrong — see below. Follow-up task warranted. |

**Image sizing — the premise was wrong.** The handoff and `CLAUDE.md` both inferred "very
likely oversized, downsize toward 8×10" from *file size alone*. Measured:

- Every PNG — cover, all 26 facer, all 26 lineart — is **1024×1536 px**.
- That is modest, not oversized: roughly 128 DPI at an 8×10 page. Downsizing pixels is the
  wrong lever and would visibly degrade the art.
- The real cost is **encoding**. 2.5–3.4 MB for 1024×1536 is ~2 bytes/pixel — PNG doing
  badly on photographic-style art. A format change (JPEG or WebP for `facer/`, keep PNG
  for `lineart/` where flat line art compresses well) cuts ~90% of the weight at
  *identical* pixel dimensions.

**Also found:** `assets/art/` and `book/images/` hold the same bytes twice — verified
byte-identical via `diff -rq` on both directories and `cmp` on the cover. ~130 MB each,
~260 MB committed. Fine for GitHub, but pushes are slow and every art change costs double.
The encoding fix above addresses most of it.

Both findings are recorded in `CLAUDE.md` Open Items. Neither was acted on — out of scope.

## 7. Deviations from the task as written

1. **Pages was automated** rather than flagged as a manual browser step (§4). Task
   permitted flagging it back; doing it was strictly better.
2. **`CLAUDE.md` was corrected before the commit, not merely placed.** Task step 5 asked
   only that it be present and tracked at commit time. It was already at the repo root, but
   an audit against the actual tree found four factual errors, so it was fixed first and
   committed accurate rather than committed stale and amended. Changes: `assets/art/archive/`
   added to the structure block; `.gitignore`'s full exclusion set documented; the art
   duplication documented; the B-lineart and archive items moved to a Closed section; the
   image-sizing item re-diagnosed per §6; the HTML build marked verified; the Pages command
   and the local-vs-CI myst version drift recorded.
3. **A local `myst build --html` was run** (§5), which the task did not ask for. Cheap, and
   it separates "CI is misconfigured" from "the book itself does not build" — worth having
   before the first CI run reports.

Nothing in the task was skipped.
