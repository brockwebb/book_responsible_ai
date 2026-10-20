# RESULT — Fix Seldon rebuild/ontology round-trip upstream

**Task:** `cc_tasks/2026-08-17_seldon_upstream_ontology_rebuild_fix.md`
**Runbook step:** 5 of 5 · **Date:** 2026-08-17 · **Status:** complete
**Upstream commit:** `86b039b` in `~/Documents/GitHub/seldon` (the clone the installed CLI runs from)

---

## Files changed

| File | Change |
|---|---|
| `seldon/core/sync.py` | replay branches for ontology + audit-only events; `_restore_ontology()`; wired into both `full_replay` and `incremental_sync` |
| `seldon/commands/ontology.py` | `_do_sync(..., emit_event: bool = True)`; emission guarded |
| `tests/test_sync.py` | 7 new regression tests |

## The class of bug — 3 unhandled types, not 1

The task asked me to audit for *other* emitted-but-unhandled event types. There were two
more beyond the reported one. Every `event_type` literal emitted anywhere in the codebase,
against the replay dispatcher's branches:

| Event type | Emitted at | Was handled? | Now |
|---|---|---|---|
| `artifact_created` | core | ✅ | unchanged |
| `artifact_updated` | core | ✅ | unchanged |
| `artifact_state_changed` | core | ✅ | unchanged |
| `link_created` | core | ✅ | unchanged |
| `link_removed` | core | ✅ | unchanged |
| `ontology_synced` | `commands/ontology.py:370` | ❌ **the reported bug** | restores ontology state |
| `ontology_ingested` | `commands/ontology.py:526` | ❌ **newly found** | same handling |
| `paper_fix` | `commands/paper.py:739` | ❌ **newly found** | recognised as audit-only |

`ontology_ingested` is the same failure with a different blast radius — it writes to
Seldon's *own* repo event store, so it degrades a rebuild of the seldon project itself.

`paper_fix` is different in kind: its payload is an edit audit record (file, find, replace,
diff_chars) that legitimately projects no graph state. It was never a state-loss bug, but
it was firing the same `Unknown event_type` warning, which trains readers to ignore that
warning — the exact thing that let the real bug hide. It is now classified explicitly.

**The unknown-type warning is deliberately preserved** for anything genuinely unrecognised.
That warning is the mechanism by which a future emitter added without a replay decision
gets noticed, so it is now a real signal rather than routine noise. There is a test
asserting it still fires.

## Design decisions worth recording

**Ontology state cannot be replayed from the log.** `ontology_synced`'s payload carries
`master_epoch` and counts — never the terms. So the handler cannot project; it must
re-derive from the ontology's actual source of truth, the master database. Per the task's
instruction to reuse rather than duplicate, `_restore_ontology()` calls the existing
`_do_sync()`.

**Restore runs once per replay, after the loop** — not per event. The sync is idempotent
and converges on the current master epoch, so replaying it per event would repeat identical
work. It runs after the session block because `_do_sync` opens its own session.

**`emit_event=False` during replay — this one is load-bearing.** `_do_sync` ends by
appending an `ontology_synced` event. A naive handler calling it would mean *every rebuild
appends an event*, which would trigger another restore on the next rebuild, growing the
event log without bound. Restoring existing state is not a new fact about the project and
must not be recorded as one. `test_replay_does_not_append_to_the_event_log` guards this
specifically; it is the subtlest part of the change.

**Restore failure logs, does not raise.** A rebuild that recovered every artifact but could
not reach the master ontology is degraded, not lost — and `seldon verify` already reports
the epoch mismatch. Raising would discard a successful artifact replay over a recoverable
condition.

**Lazy import.** `seldon.commands.ontology` imports from `seldon.core`, so importing
`_do_sync` at module level in `core/sync.py` would be circular. Imported inside the
function.

## Test evidence

7 new tests in `tests/test_sync.py`, all passing:

```
test_apply_event_signals_restore_for_ontology_events        PASSED
test_apply_event_does_not_signal_restore_for_artifact_events PASSED
test_audit_only_event_is_recognised_not_warned              PASSED
test_genuinely_unknown_event_still_warns                    PASSED
test_full_replay_restores_ontology_once                     PASSED
test_full_replay_skips_restore_when_no_ontology_events      PASSED
test_replay_does_not_append_to_the_event_log                PASSED
test_incremental_sync_also_restores_ontology                PASSED
```

**Full suite: 669 passed, 1 failed.**

The one failure is `tests/test_paper_build.py::test_build_paper_unknown_xref_passthrough`.
**It is pre-existing, not caused by this change** — verified by stashing all three modified
files and re-running it, where it fails identically. Untouched: out of scope for this task,
and worth its own investigation.

### Running the suite requires credential aliasing

`tests/conftest.py` reads `NEO4J_USERNAME` / `NEO4J_PASSWORD`. This machine's environment
sets `NEO4J_USER` / `NEO4J_PASS`. The mismatch makes `_neo4j_reachable()` fall back to the
literal password `"password"`, auth fails, and **all 15 Neo4j tests silently skip** — a
green-looking run that tested nothing. Run them as:

```bash
NEO4J_USERNAME="$NEO4J_USER" NEO4J_PASSWORD="$NEO4J_PASS" python3 -m pytest tests/ -q
```

Note `seldon/commands/init.py` already accepts both spellings
(`os.getenv("NEO4J_USERNAME") or os.getenv("NEO4J_USER")`). `conftest.py` does not. Worth
aligning, but that is a change to the test harness and was not in scope here.

## End-to-end verification (task step 3)

On this book's live database — `seldon rebuild` **alone**, with no paired `ontology sync`:

```
$ wc -l < seldon_events.jsonl
96
$ seldon rebuild
Rebuild complete: 96 events replayed in 2.06s          # no "Unknown event_type" warning
$ seldon verify
  ✓ File hashes ✓ Ontology (epoch 3) ✓ Glossary ✓ References
  ✓ Stale artifacts ✓ Blocking tasks ✓ Unregistered files
  All checks passed.
$ wc -l < seldon_events.jsonl
96                                                      # log did not grow
```

Before the fix this same sequence produced `Local epoch 0, master epoch 3 — run
seldon ontology sync` and a failed Ontology check. All 4 ResearchTasks and all 38
PaperSection artifacts survived the rebuild intact.

## Step 5 — book CLAUDE.md updated

The "Known Seldon defect" block (14 lines, including the paired-command workaround) is
replaced by one line recording that rebuild round-trips as of `86b039b`, pointing here.

## Not done

- The pre-existing `test_build_paper_unknown_xref_passthrough` failure — out of scope,
  reported above.
- `conftest.py` credential-alias fix — identified, out of scope.
