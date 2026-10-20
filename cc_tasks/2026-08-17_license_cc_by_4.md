# Task: Flip license to CC BY 4.0 International

## Decision (from Brock, 2026-08-17, chat)
This book is **CC BY 4.0**, same as his other books (`ai-workflow-design`). The
"All rights reserved — deliberate, commercial work" language in CLAUDE.md and
README.md contradicts his stated intent and is superseded. Do not re-ask.

## Changes
1. Add `LICENSE` at repo root — full CC BY 4.0 legal text
   (https://creativecommons.org/licenses/by/4.0/legalcode.txt). Match how
   `ai-workflow-design` does it; that repo is the prior art for license
   handling here.
2. `README.md` — replace the License section: CC BY 4.0, attribution line,
   badge if the sibling repo uses one.
3. `CLAUDE.md` — fix the `**License:**` line in Project Overview and remove the
   "commercial work / no LICENSE file deliberate" rationale.
4. `book/myst.yml` — add `license: CC-BY-4.0` under `project:` (MyST renders
   this on the site and embeds it in exports).
5. `book/front-matter.md` — check the copyright page. Add/replace with a CC BY
   4.0 notice: "© 2026 Brock Webb. Licensed under CC BY 4.0
   (https://creativecommons.org/licenses/by/4.0/)." Mirror the phrasing used in
   ai-workflow-design's front matter. Also propagate to
   `manuscript/01_front_matter.md` so the two copies don't drift.
6. Register this as a ResearchTask in the Seldon graph and close it on
   completion; run `seldon verify --fix` after editing `book/*.md`.

## Verification
- `LICENSE` present, README/CLAUDE.md/front-matter all say CC BY 4.0, zero
  remaining occurrences of "All rights reserved" in the repo (`grep -ri`).
- `cd book && myst build --html` still green.
- `seldon verify` all checks green.
- Write `cc_tasks/2026-08-17_license_cc_by_4_RESULT.md`.
