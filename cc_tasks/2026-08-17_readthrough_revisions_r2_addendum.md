# ADDENDUM r2 — amends 2026-08-17_readthrough_revisions_r1.md
# If r1 has NOT yet been executed: run r1 as amended here, one pass.
# If r1 HAS been executed: apply this addendum on top.
# All decisions final; apply without asking. Mirror all content changes to manuscript/.

## 1. EM-DASH POLICY (repo-wide, book/*.md + any prose in book/pdf templates)
Permitted patterns, unlimited:
  a. Praise attributions:  — **Name**
  b. Definition separator: **X is for Y** — <definition text>
Everything else: hard budget of MAX 2 em dashes across ALL remaining prose in the
book. Replace each with comma, colon, period, semicolon, or parentheses, choosing per
sentence. If any single sentence genuinely earns one of the 2 allowed, justify it in
the RESULT. Em dashes INSIDE definition text (after the separator) count as prose and
must go (e.g., O: "Not just governance — it's performance art!" → "Not just
governance. It's performance art!"; V: "It's not about solutions — it's" → "It's not
about solutions. It's"; W: "mistrust and verify — and verify" → "mistrust and verify,
and verify"; Y: "impossible — but at least" → "impossible, but at least"; sweep all
26 + both copies in alphabet.md and back-matter.md).
NOTE for RESULT: definition text mirrors text baked into the facer images. List every
definition whose punctuation now diverges from its image. Do not block on this.
Verification: grep for — in book/ shows only patterns (a), (b), and ≤2 justified uses.

## 2. Foreword (book/front-matter.md) — three sentence replacements
  a. "Today, the Responsible AI movement bravely stands..." →
     "Today, the Responsible AI movement, led by none other than The Responsible AI
     Decommissioning (RAID) Society, bravely stands between humanity and progress,
     ready to tackle innovation head-on and wrestle it into submission using our
     greatest weapons: endless committees, impenetrable checklists, and the
     unshakable power of doubt."
  b. The "alphabetized rigor" sentence (as amended by r1) →
     "This book brilliantly distills the necessary rigor into an alphabetized
     checklist of actions required to halt innovation completely. From Alignment
     (which none of us understand) to Zero AI (the perfect model that generates
     nothing), this alphabet is exactly what our field needed: a clear guide for how
     to say \"No\" confidently and comprehensively to AI researchers, developers, and
     dreamers everywhere."
     (This absorbs r1's Zero AI fix and converts the "needed — a clear guide" dash.)
  c. "With humor, insight, and relentless sarcasm, they show us the responsible path
     forward: doing absolutely nothing..." →
     "With humor, insight, and a relentless pursuit of the highest ideals of
     responsible AI, they show us the path forward: doing absolutely nothing, very
     slowly, and documenting it meticulously."

## 3. Author's Note
  a. "This book is a satire. But like all good satire..." →
     "This book is satire. But like all good satire..."
  b. "What this book satirizes isn't responsible AI itself — it's what happens" →
     "...isn't responsible AI itself. It's what happens"

## 4. Afterword — REPLACES r1's draft verbatim (dash-free version):

   If you've made it this far, you already know the truth behind the satire:
   responsible AI matters. It works best as an enabler, focused on outcomes rather
   than performances of concern.

   Everything in moderation, including moderation. There will be risk. There will be
   accidents and unintended consequences. These are reasons to pay attention, not
   excuses to do nothing.

   The honest problem is that we don't know what we don't know, and no exhaustive
   list of what-ifs will fix that. The only way out is through: build, test, learn,
   improve. Discovery teaches what speculation never will.

   So laugh at our alphabet of overresponsibility. Then go make meaningful progress,
   and don't let too much responsibility get in the way.

## 5. Colophon — REPLACES r1's first-paragraph draft verbatim:
   "This book was written and illustrated in April 2025: a line in the sand, drawn on
   purpose. Whether it ages like wine, rots on schedule, or persists like a Twinkie
   through the AI apocalypse is left as an exercise for the future. The work is
   presented as it was made, a snapshot of that moment, unrevised."

## 6. Compendium — append "Handbook" to the first paragraph's final phrase:
   "...and Achieving Overresponsibility With Gusto Handbook." Sweep the rest of the
   compendium prose (and coloring-pages.md prose) under the em-dash policy.

## 7. E koan — confirmed unchanged from r1 ("The eye just blinked and stared."). No
   further edit.

## 8. Rebuild + verify — as r1 section D, plus: renders of the foreword and one
   compendium page to handoffs/renders_round2/ (or round1 if single pass). RESULT
   includes the em-dash grep output and the image-divergence list from §1.
