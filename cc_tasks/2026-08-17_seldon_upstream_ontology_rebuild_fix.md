# Task: Fix Seldon rebuild/ontology round-trip upstream

Repo: `~/Documents/GitHub/seldon` (the clone the installed CLI runs from — NOT
`~/GitHub/seldon`, a duplicate at the same commit).

## Defect (verified on book-responsible-ai, 2026-08-17)
`seldon init` emits an `ontology_synced` event; `seldon rebuild`'s replay does
not handle that event type ("Unknown event_type 'ontology_synced' — skipped"),
so any rebuild silently drops the ontology to epoch 0 and `seldon verify` fails
the Ontology check. Artifacts/tasks survive. Affects every Seldon project.

## Fix — decision: fix it, don't just file it
This is Brock's own tool, the failure mode is silent state loss on the
advertised recovery path, and the workaround is currently documented per-project
(a smell). Fix in the seldon repo:

1. Locate the rebuild/replay dispatcher and add a handler for
   `ontology_synced` that restores ontology state equivalently to
   `seldon ontology sync` (reuse that code path — do not duplicate sync logic).
2. Audit the replay dispatcher for any OTHER emitted-but-unhandled event types
   (grep event emitters vs. handled types). The class of bug matters more than
   the instance; list what you find in RESULT even if you only fix this one.
3. Test: on a scratch project (or this book's DB, it round-trips safely now),
   `seldon rebuild` alone → `seldon verify` all green, ontology at correct
   epoch, no paired `ontology sync` needed.
4. Commit upstream with a message referencing the failure mode. If seldon has
   its own test suite, add a replay round-trip test.
5. Then update `book_responsible_ai/CLAUDE.md`: shrink the "Known Seldon
   defect" block to one line ("fixed upstream <commit>; rebuild round-trips").

## Verification
- RESULT file in book_responsible_ai/cc_tasks/ with: commit hash, list of any
  other unhandled event types found, test evidence.
