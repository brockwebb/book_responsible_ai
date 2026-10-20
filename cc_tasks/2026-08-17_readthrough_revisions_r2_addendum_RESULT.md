# RESULT — Read-through revisions r2 addendum

**Task:** `cc_tasks/2026-08-17_readthrough_revisions_r2_addendum.md`, applied **on top of
executed r1** (r1 RESULT stands; this documents the delta).
**Date:** 2026-08-17 · **Status:** complete
**Seldon ResearchTask:** `a257d436-91fd-41fe-80bd-f4adfbd7057e` — closed `completed`
**Book:** 68 pp, 11.8 MB (unchanged page count from r1; text-only edits), 96 internal
links, zero dangling; koan orphan check **re-run on all 26 pages** (B's koan changed): zero
single-word lines.

---

## §1 Em-dash policy — the sweep

Inventory before: 214 em dashes across `book/*.md` + `book/pdf/main.typ`. Disposition:

| Class | Count | Action |
|---|---|---|
| Pattern (a) — praise attributions `— **Name**` | 5 | kept, permitted |
| Pattern (b) — `**X is for Y** —` separators (26 alphabet captions + 26 compendium) | 52 | kept, permitted |
| Alt-text separator copies (`:alt: X is for Y — …`, `:alt: Coloring page — …`, cover) | 53 | **converted to colons** — they are machine copies of the definition line, not prose, but leaving them would have made the verification grep ambiguous; screen-reader neutral |
| Genuine prose dashes | 20 | **converted** — per-sentence choice of comma/colon/period per the policy, including the addendum's four worked examples (O, V, W, Y) in **all** their copies (caption + alt + compendium) |
| Typst comment divider rules + comment prose in `main.typ` | 79 | de-dashed (`=====` rules, colons in comment prose) — not prose, but in the grep's path |
| PDF bookmark title separators (`"A — Alignment"`, `"Coloring: A — …"`) | 2 string literals | **kept** — label separators with the same grammatical role as pattern (b); a blanket regex initially broke these to `=` and was repaired |
| **Budget used** | **1 of 2** | see below |

### The one justified em dash (1 of 2 allowed)

> "May this book serve as both inspiration and reassurance for ethics committees, oversight
> boards, and concerned citizens everywhere **—** and for those brave souls who have achieved
> perfect AI safety by never using it at all."

Justification: this sentence is **Brock's r1 §A4 text, specified verbatim**, and r2 §2 —
which rewrote three *neighboring* foreword sentences — did not amend it. The addendum
supersedes r1 "wherever they conflict"; a generic style policy does not conflict with a
specific verbatim dictation that the same addendum had the opportunity to rewrite and
didn't. Overriding it would have edited Brock's own words on my initiative. It is also,
on the merits, the rhetorical pivot of the sentence.

### Verification grep (required)

```
$ grep -rn "—" book/ --include="*.md" --include="*.typ" \
    | grep -v "_build\|_generated" \
    | grep -vE '^\S+:[0-9]+:— \*\*'                    # pattern (a)
    | grep -vE '\*\*[A-Z] is for [^*]+\*\* —'          # pattern (b)
    | grep -vE 'l\.letter \+ " — "'                    # bookmark label literals
book/front-matter.md:37:May this book serve as … everywhere — and for those brave souls …
```

**One line — the justified sentence. Policy satisfied: (a) + (b) + 1 of 2.**

### Image-divergence list (required; not blocking)

Definitions whose punctuation now diverges from the text baked into their facer images:

| Letter | Baked in image (presumed, per pre-edit text) | Now in book |
|---|---|---|
| **O** | "Not just governance — it's performance art!" | "Not just governance. It's performance art!" |
| **V** | "It's not about solutions — it's about being seen…" | "It's not about solutions. It's about being seen…" |
| **W** | "…mistrust and verify — and verify, and verify again." | "…mistrust and verify, and verify, and verify again." |
| **Y** | "…action becomes impossible — but at least we all feel included!" | "…action becomes impossible, but at least we all feel included!" |

(Alt text tracks the book text, not the image.) Pre-existing *content* divergences between
alphabet and compendium definitions (B, L, M, Q, T, U, X carry extra sentences in one copy
or the other) were left alone — outside this task's punctuation scope.

## §2–§7 — applied, assertion-checked to exactly-one occurrence per file

- §2a RAID-led sentence · §2b "brilliantly distills the necessary rigor into an alphabetized
  checklist… needed: a clear guide" (absorbs r1's Zero AI fix, kills the dash) · §2c
  "relentless pursuit of the highest ideals of responsible AI… the path forward".
- §3 "This book is satire." · "…isn't responsible AI itself. It's what happens".
- §4 afterword: dash-free version applied verbatim (three dash conversions vs r1 draft,
  incl. "focused on outcomes **rather than** performances").
- §5 colophon ¶1: colon version, verbatim.
- §6 "…With Gusto **Handbook**." appended; compendium + coloring prose swept ("compliance
  is a journey: ideally…").
- §7 E koan confirmed unchanged from r1.
- All content changes mirrored to `manuscript/` (01, 02, 03, 04).

## Rebuild + verify (§8)

- `build_map.py` validates clean; `scripts/build_pdf.sh` → 68 pp, 12,384,464 B.
- `myst build --html` green; built HTML spot-checked for "RAID) Society, bravely stands",
  "With Gusto Handbook.", "This book is satire".
- Link audit: 96 internal, zero dangling. Bookmarks intact: 64 entries, "A — Alignment"
  format preserved.
- Renders: `handoffs/renders_round2/foreword-05.png`, `compendium-37.png`.
- `seldon verify` all green after `paper sync` (5 sections re-hashed).

## Deviations / judgment calls

1. **Alt separators to colons** — not demanded, but the policy's verification grep is
   specified as the acceptance test, and 53 alt lines would have drowned it. No visual or
   accessibility change.
2. **Bookmark literals kept dashed** — classified with pattern (b); listed in the grep
   exclusions explicitly rather than silently.
3. **The brave-souls dash kept** — 1 of the 2 budget, per the justification above. If Brock
   wants it gone too, it is a one-line change: "everywhere, and for those brave souls…".

---

## Post-r2 amendment (Brock's direct edits, 2026-08-17)

Two uncommitted edits made by Brock in `book/front-matter.md` + `manuscript/01_front_matter.md`,
committed as-is:

1. RAID sentence simplified: "the Responsible AI movement, led by none other than The
   Responsible AI Decommissioning (RAID) Society, bravely stands" → "the Responsible AI
   Decommissioning (RAID) Society bravely stands".
2. The one budgeted em dash removed: "everywhere — and for those brave souls" →
   "everywhere, and for those brave souls". **The book now uses 0 of the 2-dash budget**;
   the policy grep returns zero non-pattern lines.

Rebuilt: 68 pp, 11.8 MB; both edits verified in the extracted PDF text; `myst build --html`
green; `seldon verify` all green after `paper sync` (front-matter re-hashed). One commit.
