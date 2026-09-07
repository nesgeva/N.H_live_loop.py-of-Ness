# N.H Controller — Automatic Supervisor and Continuation-Batch Mechanical Change Specification

**Filename:** `NH_AUTOMATIC_SUPERVISOR_MECHANICAL_CHANGE_SPEC_v1_0_CANDIDATE.md`  
**Date:** 2026-08-18  
**Status:** MECHANICAL CHANGE SPECIFICATION CANDIDATE — NOT INSTALLED, NOT ACCEPTED, NOT GOVERNANCE  
**Applies to:** a future versioned successor of the installed Repair31 controller and the local `interview_ui`  
**Controlling Ness input:** `../NESS_DESIGN_INPUTS/NH_LIVE_LOOP_AUTOMATIC_SUPERVISOR_DECISION_v1_0.md`  

---

# 0. Purpose and strict boundary

This specification changes one settled controller behaviour because Ness has
explicitly changed the desired outcome:

- **old behaviour:** five automatic correction rounds are the lifetime limit of
  one authenticated candidate chain;
- **new behaviour:** five automatic correction rounds are one bounded batch;
  exhausting a batch enters fresh independent diagnosis, and a proved new safe
  correction strategy may open another bounded batch without erasing or
  resetting lifetime history.

This is not permission for unlimited single-process execution, uncontrolled
provider retry, hidden counter reset, weaker candidate custody, or fake PASS.

Every existing protection remains unless this specification names its exact
replacement:

- Controller v1 remains DESIGN-ONLY and read-only toward all existing N.H
  governance files.
- Claude still writes only one seeded next-version candidate in a disposable
  workspace.
- Earlier candidates remain immutable and version-contiguous.
- Every candidate receives one fresh independent Codex audit.
- A genuine Ness choice still reaches only the authenticated Piece-3 interview.
- No model can accept, adopt, integrate, implement, commit, push, or weaken
  authority.

The active `controller/nh_loop.py`, `NH-GOVERNANCE`, and current
`nh_interview_state` are not installation targets during candidate development.

---

# 1. Proved current blocker this change addresses

The installed controller contains all of these mechanics:

1. `MAX_AUTOMATIC_CORRECTION_ROUNDS = 5`.
2. `run_audit_and_correction_loop()` initializes a resumed chain's spent
   count from `len(chain) - 1`.
3. When that lifetime count is at least five, it returns
   `CORRECTION_ROUND_LIMIT` and invokes no further correction.
4. Candidate custody replay, correction binding validation, write-ahead
   recording, stranded-candidate declaration, and corrected-candidate
   verification all refuse a `correction_round` above five.
5. The authenticated current chain already has correction rounds 1 through 5;
   the tail is the exact v1.5 candidate recorded in event 15.
6. The last actual v1.5 audit returned `BLOCKED`, with the remaining blocking
   finding routed `claude_mechanical`.

Therefore a superficial change to only the loop condition is invalid. It would
still be rejected by custody replay and write-ahead validation, would misreport
round 6 as “6 of at most 5,” and would provide no durable diagnosis authority or
supervisor recovery record.

---

# 2. Required public workflow states

The candidate controller must expose exactly these supervisor states:

- `IDLE`
- `WORKING`
- `DIAGNOSING`
- `WAITING_RECOVERING`
- `NEEDS_NESS_DECISION`
- `NEEDS_USER_ACTION`
- `SAFETY_HOLD`
- `READY_FOR_ACCEPTANCE`

`READY_FOR_ACCEPTANCE` is not acceptance. No `ACCEPTED` state or acceptance
write command is added by this change.

The controller must expose a read-only `supervisor-status` command returning:

- `supervisor_capability_version`;
- the exact current state;
- package scope and source binding;
- current candidate identity;
- current correction batch number;
- rounds used in the current batch;
- cumulative lifetime correction rounds;
- current audit/checkpoint/diagnosis identities;
- next safe controller command, if one exists;
- whether a genuine Ness decision, user action, or acceptance is required;
- `journal_authentication_proved`, `authenticated_state_current`, and
  `source_state_current`, all true before any non-IDLE claim is emitted;
- the controller-confirmed live-change event list, re-derived from authenticated
  audit/custody/checkpoint/diagnosis/change-explanation/pass events on every
  call;
- the exact current run lease projection described in §13;
- the authenticated journal tail and standing-chain digest.

It must write nothing and invoke no model.

`controller_confirmed_change_events` is a JSON array in authenticated event
sequence order. Each item has exactly:

```text
controller_authenticated = true
recorded_at
id
kind = problem_found | candidate_changed | audit_passed
title
what
why
status
technical
```

`technical` always includes `controller_event_seq`, `controller_event_sha256`,
`candidate_path`, and `candidate_sha256`; other values are bounded projections
of that same authenticated event. `problem_found` comes only from
`mechanical_audit_recorded` with verdict BLOCKED; `candidate_changed` comes only
from matching candidate custody plus either
`mechanical_change_explanation_recorded` or the fixed controller fallback in
§12;
`audit_passed` comes only from current `mechanical_pass_recorded` plus its exact
PASS audit. Model prose or the operational journal cannot create an item.

---

# 3. Counter semantics

Replace the old single-purpose constant with:

```text
CORRECTION_BATCH_SIZE = 5
```

The following values are distinct and must never be inferred from one another:

- `correction_round_lifetime`: position of the corrected candidate in the
  complete authenticated chain; round 6 remains round 6 forever;
- `correction_batch_number`: one-based batch containing that lifetime round;
- `correction_round_in_batch`: one through five within that batch;
- `correction_batch_size`: exactly five for this controller version.

The deterministic relationship is:

```text
correction_batch_number = ((correction_round_lifetime - 1) // 5) + 1
correction_round_in_batch = ((correction_round_lifetime - 1) % 5) + 1
```

Those formulas apply when `correction_round_lifetime > 0`. The selected initial
candidate is the unique round-zero tail and is represented in audit/diagnosis
records as the exact triple `(0, 0, 0)`; it is not a correction and consumes no
batch position. If its first attempted correction is byte-identical, the
`mechanical_no_progress_recorded` event is bound to the round-zero candidate
but authorizes diagnosis for exactly `(1, 1, 1)`. No other zero appears in a
round triple.

There is no package-abandonment condition derived from cumulative lifetime
round count. Serialized input remains byte-bounded and integers must still be
real non-negative JSON integers, so removing the policy cap does not make input
unbounded in bytes.

Every old field or message named `correction_round_limit` must be replaced or
versioned. It must never retain the value 5 while describing a lifetime round
above 5. The new report keys are:

- `correction_batch_size`;
- `correction_batch_number`;
- `correction_rounds_started_this_batch`;
- `correction_rounds_completed_this_batch`;
- `correction_rounds_lifetime_before`;
- `correction_rounds_lifetime_after`.

---

# 4. Candidate custody changes

The existing HMAC-authenticated interview journal remains the authority for
candidate write-ahead and custody. Do not create a second candidate-custody
system.

For `candidate_write_ahead_recorded`, `candidate_write_ahead_aborted`, and
`candidate_custody_recorded`:

- rename the semantic use of `correction_round` to
  `correction_round_lifetime` in a new journal schema version;
- add `correction_batch_number` and `correction_round_in_batch`;
- replay derives all three from chain position and rejects any mismatch;
- replay no longer rejects a valid contiguous chain merely because its lifetime
  position exceeds five;
- pending and committed records still share the exact same candidate and parent
  identities;
- one pending write-ahead per package remains mandatory;
- aborted intents still add no custody and consume no lifetime round;
- filename succession remains exact: same controlled stem and major, minor
  exactly one higher;
- all existing branch, HEAD, source-binding, no-follow, exclusive-create,
  read-back, and terminal-chain proofs remain.

Backward replay must support the current journal schema carrying rounds 1–5 and
upgrade its meaning in memory without rewriting those events. New events use the
new schema version only. The authenticity key and old event bytes remain
unchanged.

## 4.1 Exact journal-version transition

The numeric transition is **journal version 4 → journal version 5**.

Replace the one-version constant with:

```text
INTERVIEW_JOURNAL_CURRENT_VERSION = 5
INTERVIEW_JOURNAL_SUPPORTED_VERSIONS = {4, 5}
```

The six envelope keys remain exactly:

```text
journal_version, event_seq, prev_event_sha256, event_sha256,
event_auth_sha256, type
```

Version 4 event types and body-key sets remain byte-for-byte the currently
installed `INTERVIEW_EVENT_TYPES` and `INTERVIEW_EVENT_BODY_KEYS`. Version 5
accepts every version-4 type. For the six non-candidate version-4 types
(`validation_recorded`, `routed_issue_recorded`, `review_signal_recorded`,
`question_coverage_review_recorded`, `group_presented`, `answer_recorded`), the
version-5 body-key set is exactly the existing version-4 body-key set. New
appends always use version 5; no new version-4 event is ever written.

For the three candidate events, version 5 uses the existing version-4 body-key
set with `correction_round` removed and these three keys added:

```text
correction_round_lifetime, correction_batch_number, correction_round_in_batch
```

No version-5 candidate event may carry legacy `correction_round`. Replay maps a
version-4 candidate event in memory as:

```text
correction_round_lifetime = event.correction_round
correction_batch_number = ((event.correction_round - 1) // 5) + 1
correction_round_in_batch = ((event.correction_round - 1) % 5) + 1
```

It then applies the same chain-position derivation to version 4 and version 5
events. Stored version-4 bytes are never rewritten.

Authentication becomes version-dependent without changing the authentication
of any existing record:

```text
bound = event without event_sha256 and event_auth_sha256
auth_material = canonical_json([
  INTERVIEW_AUTH_LABEL,
  event.journal_version,
  bound
]).encode("utf-8")
event_auth_sha256 = HMAC-SHA256(existing_auth_key, auth_material).hexdigest()
event_sha256 = SHA256(canonical_json(event without event_sha256)).hexdigest()
```

`canonical_json` remains the installed encoding: sorted keys, separators
`(',', ':')`, `ensure_ascii=True`. Because every existing event records version
4 and the installed controller also authenticated it with numeric 4, its HMAC
input remains exactly unchanged. Validation chooses the body-key set by the
pair `(event.journal_version, event.type)`, verifies that event's own version in
the HMAC material, and keeps one uninterrupted event sequence and ordinary hash
chain across the 4→5 boundary. An unsupported version, a version/type pair with
no exact schema, or a version-5 event before a valid version-4 prefix ends fails
closed. Once the first version-5 event exists, a later version-4 event is
refused as version rollback.

## 4.2 Exact new version-5 event body schemas

The following shorthand is only set notation; implementation expands it into
literal `frozenset` values.

```text
PACKAGE_SOURCE = {
  package_key, package_scope_id, package_id,
  branch, head_sha, source_binding_sha256, standing_before_sha256
}
CANDIDATE = {
  candidate_path, candidate_sha256, candidate_bytes,
  correction_round_lifetime, correction_batch_number,
  correction_round_in_batch
}
OPERATION_BINDING = {
  controller_executable_identity,
  package_scope_id, source_binding_sha256,
  candidate_path, candidate_sha256, candidate_bytes,
  controller_report_sha256
}
```

Version 5 adds exactly these types and body keys:

```text
mechanical_audit_recorded = PACKAGE_SOURCE | CANDIDATE | {
  settled_decision_binding_sha256, audit_identity, verdict,
  highest_severity, findings, mechanical_blocker_refs,
  review_required_blocker_refs, codex_invoked, codex_exit_code,
  audit_schema_valid, audit_source_stable, terminal_chain_sha256
}

correction_batch_checkpoint_recorded = PACKAGE_SOURCE | CANDIDATE | {
  checkpoint_identity, audit_identity, blocking_finding_refs,
  checkpoint_outcome
}

mechanical_no_progress_recorded = PACKAGE_SOURCE | CANDIDATE | {
  no_progress_identity, blocking_finding_refs,
  correction_specification_sha256, diagnosis_strategy_sha256,
  claude_result_facts_sha256, diagnosis_required
}

correction_diagnosis_recorded = PACKAGE_SOURCE | CANDIDATE | {
  diagnosis_trigger_type, diagnosis_trigger_event_seq,
  diagnosis_trigger_identity, diagnosis_input_sha256,
  diagnosis_result_sha256, diagnosis_outcome, source_paths_checked,
  blocking_finding_refs, root_cause_plain,
  why_previous_approach_survived, strategy_identity_material,
  diagnosis_strategy_sha256, mechanical_correction_specification,
  review_signal, dependency, plain_language_problem,
  plain_language_impact, authorized_next_lifetime_round,
  authorized_batch_number, authorized_round_in_batch,
  next_workflow_state
}

diagnosis_strategy_consumption_started = PACKAGE_SOURCE | CANDIDATE | {
  consumption_identity, diagnosis_event_seq, diagnosis_event_sha256,
  diagnosis_strategy_sha256, blocking_finding_refs,
  correction_specification_sha256, target_candidate_path,
  authorized_next_lifetime_round, authorized_batch_number,
  authorized_round_in_batch
}

diagnosis_strategy_consumption_completed = PACKAGE_SOURCE | CANDIDATE | {
  consumption_identity, consumption_started_event_seq,
  diagnosis_event_seq, diagnosis_event_sha256,
  diagnosis_strategy_sha256, blocking_finding_refs,
  correction_specification_sha256, produced_candidate_path,
  produced_candidate_sha256, produced_candidate_bytes,
  produced_lifetime_round, produced_batch_number,
  produced_round_in_batch
}

mechanical_change_explanation_recorded = PACKAGE_SOURCE | CANDIDATE | {
  parent_candidate_path, parent_candidate_sha256, parent_candidate_bytes,
  change_explanation_identity, blocking_finding_refs,
  correction_specification_sha256, diff_sha256,
  reviewer_result_sha256, source_paths_checked, plain_language_change,
  plain_language_real_use_effect, meaning_or_policy_changed,
  changed_sections, technical_summary
}

mechanical_pass_recorded = PACKAGE_SOURCE | CANDIDATE | {
  pass_identity, audit_identity, terminal_chain_sha256,
  settled_decision_binding_sha256, validation_set_id,
  coverage_review_event_seq, no_pending_write_ahead,
  frozen_envelope_clean, pass_outcome
}

supervisor_operation_started = PACKAGE_SOURCE | CANDIDATE | {
  controller_executable_identity,
  supervisor_operation_id, supervisor_command, pre_state_sha256,
  input_envelope_sha256, controller_report_sha256
}

supervisor_operation_completed = PACKAGE_SOURCE | CANDIDATE | {
  controller_executable_identity,
  supervisor_operation_id, supervisor_started_event_seq,
  supervisor_command, controller_returncode, controller_report_sha256,
  operation_outcome, post_state_sha256
}
```

Nullable fields are still present: `package_id`,
`diagnosis_strategy_sha256`, `mechanical_correction_specification`,
`review_signal`, and `dependency` carry JSON `null` where their outcome does
not use them. `codex_exit_code` may be null only when `codex_invoked` is false.
The `supervisor_operation_started.controller_report_sha256` field is present
and JSON `null`, because the invoked operation has not returned a report yet;
its pre-state report is instead bound by `pre_state_sha256`. No other new event
field is implicitly nullable.
All other fields are non-null and type/bound validated. Every collection has an
existing controller byte/count bound; finding-ref lists are sorted, unique, and
non-empty where a BLOCKED trigger requires them.

All new mechanical/supervisor events are Piece-3-standing neutral. Their
`standing_before_sha256` must equal the replayed standing digest at their exact
event position and their standing delta is the empty canonical delta. They can
never admit, settle, present, answer, retire, park, or clear a question and can
never reduce a routed signal. Only the existing Piece-3 event types retain those
effects.

## 4.3 Exact derived identities

Every identity below is the lowercase SHA-256 hex digest of installed
`canonical_json([DOMAIN, OBJECT])`, where `OBJECT` has exactly the named keys:

```text
audit_identity / "NH_MECHANICAL_AUDIT_ID_V1":
  package_scope_id, source_binding_sha256,
  settled_decision_binding_sha256, candidate_path, candidate_sha256,
  candidate_bytes, correction_round_lifetime, correction_batch_number,
  correction_round_in_batch, audit_prompt_sha256, required_files_sha256

checkpoint_identity / "NH_CORRECTION_BATCH_CHECKPOINT_ID_V1":
  package_scope_id, source_binding_sha256, candidate_path, candidate_sha256,
  candidate_bytes, correction_round_lifetime, correction_batch_number,
  audit_identity, blocking_finding_refs, checkpoint_outcome

no_progress_identity / "NH_MECHANICAL_NO_PROGRESS_ID_V1":
  package_scope_id, source_binding_sha256, candidate_path, candidate_sha256,
  blocking_finding_refs, correction_specification_sha256,
  diagnosis_strategy_sha256, claude_result_facts_sha256

diagnosis_trigger_identity / "NH_DIAGNOSIS_TRIGGER_ID_V1":
  diagnosis_trigger_type, diagnosis_trigger_event_seq,
  trigger_event_sha256, package_scope_id, source_binding_sha256,
  candidate_path, candidate_sha256, blocking_finding_refs

diagnosis_input_sha256 / "NH_CORRECTION_DIAGNOSIS_INPUT_V1":
  diagnosis_trigger_identity, package_scope_id, source_binding_sha256,
  candidate_path, candidate_sha256, candidate_bytes,
  blocking_finding_refs, prior_strategy_digests, source_manifest_sha256

diagnosis_result_sha256 / "NH_CORRECTION_DIAGNOSIS_RESULT_V1":
  every validated diagnosis response field listed in §7, with no omissions

diagnosis_strategy_sha256 / "NH_CORRECTION_STRATEGY_ID_V1":
  diagnosis_trigger_identity, root_cause_plain,
  strategy_identity_material, mechanical_correction_specification,
  candidate_path, candidate_sha256, blocking_finding_refs,
  source_binding_sha256

consumption_identity / "NH_DIAGNOSIS_CONSUMPTION_ID_V1":
  diagnosis_event_seq, diagnosis_event_sha256,
  diagnosis_strategy_sha256, package_scope_id, source_binding_sha256,
  candidate_path, candidate_sha256, target_candidate_path,
  authorized_next_lifetime_round, authorized_batch_number,
  authorized_round_in_batch

change_explanation_identity / "NH_CHANGE_EXPLANATION_ID_V1":
  package_scope_id, source_binding_sha256, parent_candidate_path,
  parent_candidate_sha256, candidate_path, candidate_sha256,
  blocking_finding_refs, correction_specification_sha256, diff_sha256,
  reviewer_result_sha256

pass_identity / "NH_MECHANICAL_PASS_ID_V1":
  package_scope_id, source_binding_sha256, candidate_path, candidate_sha256,
  candidate_bytes, audit_identity, terminal_chain_sha256,
  settled_decision_binding_sha256, validation_set_id,
  coverage_review_event_seq

supervisor_operation_id / "NH_SUPERVISOR_OPERATION_ID_V1":
  supervisor_command, controller_executable_identity,
  package_scope_id, source_binding_sha256,
  candidate_path, candidate_sha256, candidate_bytes,
  pre_state_sha256, input_envelope_sha256

controller_executable_identity / "NH_CONTROLLER_EXECUTABLE_ID_V1":
  controller_repo_relative_path, controller_sha256, controller_bytes,
  journal_current_version, supervisor_protocol_version
```

All named identity fields store that 64-character digest directly except
`supervisor_operation_id`, which stores `op_` followed by the complete
64-character digest.

`audit_prompt_sha256`, `required_files_sha256`, `source_manifest_sha256`,
`prior_strategy_digests`, `diff_sha256`, `reviewer_result_sha256`,
`pre_state_sha256`, `post_state_sha256`, `input_envelope_sha256`, and
`controller_report_sha256` are themselves SHA-256 of the installed canonical
JSON encoding of the exact validated object or byte inventory their names
identify. Raw file bytes use SHA-256 directly and are represented in the object
by path, byte length, and digest. Nothing model-authored can supply or override
one of these derived values.

`controller_executable_identity` is recomputed from the installed candidate
controller's exact bytes before every supervisor command and on replay. A
started operation may be recovered by a later controller version only by the
read-only recovery command: the new executable replays the old event under its
recorded identity, refuses to act as though it authored that event, and either
returns an already proved `COMPLETED`/`SAFE_TO_RESUME` result or `SAFETY_HOLD`.
It may never repeat a provider operation merely because the executable identity
changed.

---

# 5. Durable audit record

The final audit result must no longer exist only in process output.

After a usable fresh Codex audit and after the candidate/source fences at that
boundary pass, append `mechanical_audit_recorded` with exactly:

- package key, scope, and controlled ID state;
- source branch, HEAD, source binding, and settled-decision binding;
- candidate path, SHA-256, byte length, lifetime round, batch number, and
  round-in-batch;
- one controller-derived `audit_identity` over all bound audit inputs;
- verdict, highest severity, and the complete validated finding objects;
- mechanical blocker refs and review-required blocker refs;
- Codex invocation/return/schema/source-stability facts;
- terminal candidate-chain proof digest;
- `standing_before_sha256`.

The event is evidence, not acceptance and not question routing.

Replay requires at most one usable audit event for one exact audit identity. A
different result for the same identity is a contradiction and fails closed.

---

# 6. Batch checkpoint

Whenever authenticated replay proves that the current batch already contains
five completed lifetime rounds and the current fresh audit of that exact batch
tail remains fully mechanical `BLOCKED`, the controller must perform the
checkpoint transition below. This condition is independent of how many of
those five candidates the current process created. It therefore applies both
to a newly completed batch and to the actual resumed round-5/v1.5 chain, where
the resumed process created zero of the five candidates. The checkpoint identity
makes the transition idempotent: if the exact checkpoint is already recorded,
the controller returns it; if it is absent, it appends it once; a conflicting
checkpoint for the same identity fails closed.

The controller must:

1. preserve the usable audit as above;
2. re-prove the complete candidate chain and source state;
3. append or re-use the one exact `correction_batch_checkpoint_recorded` containing:
   - package and source binding;
   - batch number;
   - lifetime round at the batch tail;
   - batch-tail candidate identity;
   - audit identity and blocking finding refs;
   - `checkpoint_outcome = "diagnosis_required"`;
   - `standing_before_sha256`;
4. return a proved, non-PASS workflow transition:
   - `ok = true` for preservation of the workflow transition itself;
   - `final_design_audit_verdict = "BLOCKED"`;
   - `stop_reason = "CORRECTION_BATCH_LIMIT"`;
   - `next_workflow_state = "DIAGNOSING"`;
   - `next_command = "diagnose-next-correction-batch"`.

`ok = true` here must never be described as package success. It means only that
the bounded command completed its checkpoint correctly.

The existing `CORRECTION_ROUND_LIMIT` remains readable only as a legacy result
from an older controller. The new controller never emits it.

---

# 7. Fresh independent diagnosis command

Add:

```text
python3 nh_loop.py diagnose-next-correction-batch
```

It takes no model prose or findings on stdin.

Before invoking a model it must:

1. replay and authenticate the complete journal;
2. prove exactly one package has one current replayable diagnosis trigger. The
   trigger is the union of:
   - an exhausted-batch `correction_batch_checkpoint_recorded` whose outcome is
     `diagnosis_required`; or
   - a `mechanical_no_progress_recorded` event with
     `diagnosis_required = true` and no later diagnosis consuming that exact
     no-progress identity;
3. re-prove its complete candidate chain against the real checkout;
4. re-prove current Piece-3 interview clearance for that package;
5. re-prove source branch, HEAD, source binding, settled decisions, required
   files, and candidate bytes;
6. refuse if a newer audit, diagnosis, candidate, routed issue, Ness answer, or
   source change superseded the diagnosis trigger;
7. refuse if the checkpoint carries any blocking finding not routed
   `claude_mechanical`.

Then invoke exactly one fresh, ephemeral, read-only Codex diagnosis with no
Claude context and no earlier model conversation. It reads:

- the actual current candidate completely;
- every earlier candidate in the authenticated chain as needed;
- the actual governing and accepted source files;
- the current validated blocking findings as data;
- the current batch checkpoint;
- prior authenticated diagnosis strategies for the same candidate lineage.

The diagnosis response has exactly:

```text
whole_check_complete: boolean
source_paths_checked: [repository-relative paths]
diagnosis_outcome: one of
  safe_new_mechanical_strategy
  possible_ness_choice
  temporary_technical_dependency
  external_user_action_required
  authority_or_safety_conflict
  no_currently_safe_strategy
root_cause_plain: bounded plain-language string
why_previous_approach_survived: bounded string
strategy_identity_material: bounded structured object or null
mechanical_correction_specification: existing exact correction-spec schema or null
review_signal: existing exact review-signal schema or null
dependency: bounded structured object or null
plain_language_problem: bounded everyday-language string
plain_language_impact: bounded everyday-language string
diagnosis_trigger_type: exhausted_batch or no_progress
authorized_next_lifetime_round: positive integer or null
authorized_batch_number: positive integer or null
authorized_round_in_batch: integer 1..5 or null
```

Validation rules:

- every source path must be one of the controller-required real sources or an
  authenticated candidate in this chain;
- every current blocker ref appears exactly once in a safe mechanical strategy;
- a safe strategy has a correction specification and no review signal or
  dependency;
- a possible Ness choice has a valid review signal and no correction
  specification;
- a dependency outcome has one exact dependency record and no correction;
- an authority/safety conflict cannot authorize correction;
- plain-language fields are explanatory only and cannot add a requirement;
- the controller derives `diagnosis_strategy_sha256` from the validated root
  cause, strategy material, correction specification, candidate identity,
  finding refs, and source binding;
- the same strategy digest may not be authorized twice for the same unchanged
  candidate and blocker set after it already produced no progress;
- for an exhausted-batch trigger, a safe strategy authorizes lifetime round
  `tail + 1`, which is round 1 of batch `old_batch + 1`;
- for a no-progress trigger on the initial round-zero tail, a safe strategy
  authorizes exactly lifetime round 1, batch 1, round-in-batch 1;
- for a no-progress trigger before round 5 of its derived batch, a safe strategy
  authorizes lifetime round `tail + 1` in that **same** derived batch and at its
  next derived round-in-batch; it does not open or renumber a batch;
- a no-progress trigger at round 5 is normalized to the exhausted-batch
  checkpoint for that same tail and cannot create a second trigger;
- every authorized lifetime/batch/in-batch triple must equal the §3 formulas;
- before any corrected successor exists, the authenticated selected candidate
  is the round-zero tail defined in §3; its only first-correction triple is
  lifetime round 1, batch 1, round-in-batch 1;
- any ambiguity, missing blocker, contradictory source, or technical result is
  rejected in full.

---

# 8. Diagnosis outcomes and journal events

Append one `correction_diagnosis_recorded` event only after all diagnosis input
and output checks pass. It contains:

- checkpoint identity;
- diagnosis input digest and result digest;
- package/source/candidate identities;
- diagnosis outcome;
- source paths checked;
- current blocker refs;
- root-cause and previous-approach explanation;
- strategy digest and exact correction specification where applicable;
- review signal or dependency where applicable;
- plain-language problem and impact;
- next state;
- `standing_before_sha256`.

Outcome routing is exact:

- `safe_new_mechanical_strategy` → `WORKING`; for an exhausted-batch trigger it
  opens exactly one new batch and authorizes exactly its first correction; for
  a mid-batch no-progress trigger it authorizes exactly the next lifetime round
  in the existing batch;
- `possible_ness_choice` → record through the existing routed-signal mechanism;
  then Piece-3 validation decides whether `NEEDS_NESS_DECISION` is real;
- `temporary_technical_dependency` → `WAITING_RECOVERING` with controller-owned
  retry classification and bounded backoff metadata;
- `external_user_action_required` → `NEEDS_USER_ACTION`; it is never represented
  as a Ness design question;
- `authority_or_safety_conflict` → `SAFETY_HOLD`;
- `no_currently_safe_strategy` → `WAITING_RECOVERING` with no retry time unless
  the dependency/source/capability changes.

The diagnosis command returns no PASS and creates no candidate.

---

# 9. Consuming a diagnosis strategy

On the next `execute-next-claude-task`:

- the newest current unconsumed `safe_new_mechanical_strategy` diagnosis is
  mandatory whether its trigger was `exhausted_batch` or `no_progress`;
- that diagnosis is the **sole** authority for its recorded authorized
  lifetime/batch/in-batch triple, and the correction consumes the exact stored
  correction specification instead of asking GPT for another specification;
- before Claude is invoked, append a one-time strategy-consumption intent bound
  to diagnosis event, candidate, blocker refs, target path, and the exact
  authorized triple;
- after the corrected candidate is promoted and custodied, append the matching
  consumption completion;
- interrupted consumption follows the existing write-ahead recovery model;
- the same diagnosis cannot authorize two candidates or be consumed twice;
- the ordinary fresh-GPT correction-specification path is permitted only where
  replay proves that no safe diagnosis remains unconsumed for the current
  candidate/blocker set. A mid-batch no-progress diagnosis therefore cannot be
  discarded merely because its authorized target remains in the same batch.

Claude begins a fresh session at a cross-process diagnosis boundary unless an
existing session can be independently re-proved. No correctness or authority
claim depends on session continuity. A fresh session reads the real blocked
candidate and required sources under the existing disposable-workspace rules.

---

# 10. No-progress handling

The current byte-identical-candidate rule remains: no cosmetic successor is
promoted.

Replace its terminal abandonment meaning with:

1. append `mechanical_no_progress_recorded` bound to candidate, blocker refs,
   correction specification, strategy digest if any, Claude result facts, and
   source binding;
2. make that exact no-progress event the replayable diagnosis trigger when the
   current round is the initial round 0 or rounds 1–4 in their derived batch;
   round 0 can authorize only `(1, 1, 1)`. When it is round 5, append/re-use the
   exhausted-batch checkpoint instead;
3. set `next_workflow_state = "DIAGNOSING"` and require a fresh diagnosis
   against that exact trigger before another Claude correction;
4. forbid reauthorization of the same strategy digest against unchanged inputs;
5. if diagnosis cannot find a materially different safe route, enter the
   appropriate waiting, user-action, or safety state without hot-looping.

---

# 11. Technical recovery and backoff

The persistent supervisor, not the design-audit command, owns retry scheduling.
Individual model calls remain single-attempt and bounded.

## 11.1 Exact operation envelope and controller events

Before a supervisor-launched command, the worker constructs this exact bounded
JSON envelope:

```text
supervisor_command
controller_executable_identity
package_scope_id
source_binding_sha256
candidate_path
candidate_sha256
candidate_bytes
pre_state_sha256
input_envelope_sha256
supervisor_operation_id
```

`pre_state_sha256` is the digest of
`canonical_json(["NH_SUPERVISOR_STATE_BINDING_V1", projection])`, where
`projection` has exactly these keys and excludes volatile heartbeat/expiry:

```text
controller_executable_identity, package_scope_id, source_binding_sha256,
candidate_path, candidate_sha256, candidate_bytes, workflow_state,
next_command, dependency_identity, authenticated_event_seq,
authenticated_tail_sha256
```

`input_envelope_sha256` is the canonical digest of every preceding envelope
field. All canonical encodings here are the installed `ensure_ascii=True`
encoding from §4.1. A version-1 private scheduling journal created by the UI
prototype's former `ensure_ascii=False` encoding is refused, not migrated or
silently reinterpreted; the local scheduling-journal version for this protocol
is 2.
`supervisor_operation_id` is derived exactly as §4.3 specifies. The controller
recomputes both and refuses disagreement. The envelope contains no model prose,
finding text, Ness answer, credential, or file content.

Before the first provider call, promotion, or journal transition for that
operation, the controller appends `supervisor_operation_started`, including the
exact executable and current candidate identities and a present JSON-null
`controller_report_sha256`. On a normal
return it appends `supervisor_operation_completed`. Re-use of one completed
operation ID returns the already authenticated outcome without another provider
call. One ID bound to different inputs is a journal contradiction.

## 11.2 Exact read-only recovery command

Add:

```text
python3 nh_loop.py supervisor-operation-status
```

It reads the exact operation envelope above from stdin, invokes no model, writes
nothing, and returns exactly these operation fields in the normal controller
report:

```text
command = "supervisor-operation-status"
ok
supervisor_operation_id
supervisor_command
package_scope_id
source_binding_sha256
pre_state_sha256
started_event_seq
completed_event_seq
recovery_outcome
recovered_workflow_state
next_command
provider_retry_safe
candidate_reconciliation
authenticated_event_seq
authenticated_tail_sha256
journal_authentication_proved
source_state_current
errors
```

`recovery_outcome` is exactly one of:

```text
COMPLETED
SAFE_TO_RESUME
SAFE_TO_RETRY
WAIT
NEEDS_USER_ACTION
SAFETY_HOLD
```

The derivation is exact:

- `COMPLETED`: matching authenticated completion exists; return its recorded
  state and never repeat the command.
- `SAFE_TO_RESUME`: no completion exists, but authenticated custody/audit/
  checkpoint/diagnosis events prove a later durable phase; `next_command` is the
  one non-provider continuation for that phase.
- `SAFE_TO_RETRY`: no matching durable side effect exists, no pending candidate
  is present, source and clearance remain current, and repeating the one
  provider operation cannot duplicate candidate custody or question delivery.
- `WAIT`: reconciliation is temporarily incomplete; `provider_retry_safe` is
  false and `next_command` is null.
- `NEEDS_USER_ACTION`: one named external dependency cannot be restored by the
  controller; it is not a Ness design question.
- `SAFETY_HOLD`: any source, authority, journal, pending-child, identity, or
  envelope contradiction exists.

`candidate_reconciliation` is exactly one of `none`, `pending_child_absent`,
`pending_child_exact`, `custody_committed`, or `contradiction`. A report may set
`provider_retry_safe = true` only for `SAFE_TO_RETRY`. Every other outcome sets
it false.

The worker calls this read-only command for every local
started-without-completion operation before it calls any provider command. It
marks its local operation reconciled only after `COMPLETED` or `SAFE_TO_RESUME`,
or abandoned-and-retryable only after `SAFE_TO_RETRY`. `WAIT`, user action, and
safety hold never invoke the provider.

The worker branches on the six exact `recovery_outcome` strings above. It never
looks for substitute booleans such as `needs_user_action` or `safety_hold`.
`NEEDS_USER_ACTION` and `SAFETY_HOLD` persist as non-retrying states; neither
schedules backoff or becomes a Ness design question.

## 11.3 Exact durable backoff

The private local scheduling journal records only:

```text
dependency_identity, attempt, first_failure_epoch, scheduled_at_epoch,
next_eligible_epoch, delay_seconds, maximum_delay_seconds,
controller_state_sha256
```

It stores no complete controller report, finding text, Ness answer, candidate
bytes, source contents, token, or credential. The directory is a real,
non-symlink, current-owner `0700` directory opened by anchored descriptor. The
journal is a real, current-owner, regular, single-link `0600` file opened
relative to that descriptor with no-follow, locked for every append, fsynced,
and read back. An insecure pre-existing directory or file is refused. Its
unkeyed hash chain detects damage but is explicitly **not** authority for
workflow state, audit, PASS, custody, questions, or acceptance readiness.

The clock is UTC Unix seconds from `time.time()` and is used only for waiting,
never for authority. `controller_state_sha256` is the §11.1 state-binding digest
from a **fresh authenticated post-operation `supervisor-status`** read after
the controller's started/completed events have been durably appended; it is
never the pre-call digest. For a stable `dependency_identity` and unchanged
post-operation `controller_state_sha256`:

```text
attempt starts at 1 and is preserved across process restart
delay_seconds = min(15 * (2 ** (attempt - 1)), 900)
next_eligible_epoch = scheduled_at_epoch + delay_seconds
```

A restart reads this record, obtains a fresh authenticated status, compares the
same non-volatile projection, and does no provider work before
`next_eligible_epoch`. If the wall clock is earlier than
`scheduled_at_epoch`, the worker schedules one maximum 900-second wait rather
than treating the retry as eligible. A changed freshly authenticated controller
state or dependency identity clears the old series. A successful operation also
clears it. Merely restarting the process never resets `attempt` or the first
failure time.

Every private operational-journal payload—state change, run start, observed
report, completion/reconciliation/abandonment, and backoff schedule/clear—also
carries one exact bounded `binding` object:

```text
controller_executable_identity, source_binding_sha256, package_scope_id,
candidate_path, candidate_sha256, candidate_bytes, controller_report_sha256
```

For run start, `controller_report_sha256` is the exact pre-operation
authenticated `supervisor-status` report digest. For result records it is the
exact returned controller-report digest. For state/backoff records it is the
fresh authenticated `supervisor-status` digest. Candidate fields are present
and may be null only when authenticated state proves no current candidate. A
binding mismatch, controller upgrade without successful read-only
reconciliation, or unsupported local-journal version fails closed.

Source change, unsafe state, invalid output, contradictory journal, and
authority conflict are not retryable provider errors.

---

# 12. Plain-language live-change evidence

The controller report and authenticated event history must support the UI feed
without trusting Claude's self-report.

## Problem explanation

Extend the independent design-audit response schema with:

- `plain_language_problem`;
- `plain_language_impact`.

They are bounded everyday-language translations of the finding's already
validated substance. They cannot add a source, requirement, route, severity, or
correction. If their content is missing or invalid, the audit result may still
stand technically but the UI uses a conservative controller-owned fallback.

## Actual-change explanation

After a corrected candidate is verified, promoted, read back, and custodied—but
before any claim about what changed is shown—invoke one fresh read-only
change-explanation review over:

- exact parent and candidate identities;
- mechanically computed bounded diff/changed-section inventory;
- exact correction specification and finding refs;
- actual current sources required for those refs.

It returns exactly:

- `whole_check_complete`;
- `source_paths_checked`;
- `finding_refs_covered`;
- `plain_language_change`;
- `plain_language_real_use_effect`;
- `meaning_or_policy_changed`: `true`, `false`, or `unproved`;
- `changed_sections`;
- `technical_summary`.

The controller validates identities, coverage, bounds, paths, and section
existence. If the review fails, candidate custody remains valid and no invented
plain explanation is recorded. The candidate must nevertheless remain visible
through a controller-owned fallback feed projection derived only from the
authenticated custody event and the mechanically computed parent/candidate
identity and diff inventory. Its fixed text is:

```text
title: "A mechanical correction candidate was preserved"
what: "N.H preserved a new correction candidate. A safe plain-language explanation is not currently available."
why: "The exact parent, candidate, and technical difference are available below. No claim is made that the correction succeeded or that meaning or policy stayed unchanged."
status: "Waiting for or reporting the independent audit result"
```

Its technical object contains only the custody event sequence/hash, parent and
candidate path/hash/byte length, lifetime/batch/in-batch triple, and computed
`diff_sha256` plus changed-section identifiers. It cannot contain a PASS,
success, acceptance, or meaning/policy claim. A later valid explanation event
replaces this fallback for the same custody identity; it never creates a second
candidate-change item.

Append `mechanical_change_explanation_recorded` bound to parent, candidate,
finding refs, correction specification digest, diff digest, reviewer result
digest, and source binding.

The UI wording is exact:

- before the new candidate's audit: “Claude made a correction candidate intended
  to address …”;
- after a fresh PASS: “Codex confirmed the exact candidate passes”;
- after a fresh BLOCKED: “Codex checked the new candidate and found …”;
- never “Claude fixed it” on Claude's own authority.

The UI may display “Nothing changed N.H meaning or policy” only when the
change-explanation event says `false` and the later fresh audit remains usable.

---

# 13. Persistent local supervisor process

The supervisor is a process separate from the browser tab. Closing or reloading
the page must not terminate mechanical work.

It performs only this state machine:

```text
read supervisor-status
  NEEDS_NESS_DECISION  -> wait for authenticated answer/revalidation
  NEEDS_USER_ACTION    -> wait for the named external action
  READY_FOR_ACCEPTANCE -> wait for separate explicit acceptance
  SAFETY_HOLD          -> wait for a proved safe unlock
  WAITING_RECOVERING   -> wait until eligible, then call recovery/status
  DIAGNOSING           -> call diagnose-next-correction-batch once
  WORKING              -> call execute-next-claude-task once
```

It never composes questions, findings, correction specs, filenames, candidate
bytes, routes, PASS, or acceptance. It follows exact controller states and
commands only.

Only one live package lease is allowed. Before any state-changing or provider
step, a worker may perform one read-only `supervisor-status` to obtain the exact
package/source/executable binding, then must acquire the lease. A second worker
that cannot acquire may read/display status but performs no workflow command.

The anchored state directory is the absolute `NH_SUPERVISOR_STATE_DIR` when set;
otherwise it is exactly `interview_ui/.nh_supervisor_state` below the controller
project root resolved without symlinks. It must be current-owner mode `0700`.
The paths below it are exactly:

```text
supervisor_events.jsonl
supervisor_lease.json
supervisor_lease.json.lock
```

The lock and lease are each current-owner, regular, single-link mode `0600`
files opened relative to the anchored directory with `O_NOFOLLOW` where
available. Every acquire, heartbeat, takeover, and release holds an exclusive
`flock` on `supervisor_lease.json.lock` from read through directory fsync.

The lease lives in the same anchored owner-only state directory as the private
scheduling journal, but it is a separate `0600`, regular, single-link file. It
contains exactly:

```text
lease_version = 1
run_id
pid
process_start_ticks
boot_id_sha256
controller_executable_identity
package_scope_id
source_binding_sha256
acquired_at_epoch
heartbeat_at_epoch
expires_at_epoch
```

`run_id` is
`SHA256(canonical_json(["NH_SUPERVISOR_LEASE_ID_V1", identity]))`, where
`identity` has every lease field except `run_id`, `heartbeat_at_epoch`, and
`expires_at_epoch`. `process_start_ticks` is read from `/proc/<pid>/stat` field 22;
`boot_id_sha256` is the SHA-256 of the exact bytes read from
`/proc/sys/kernel/random/boot_id`. Heartbeat interval is 10 seconds and expiry
is 35 seconds after the last successful heartbeat. The controller reports
`run_lease = {live_proved, run_id, expires_at}` with `live_proved = true` only
when owner/mode/link/no-follow checks pass, boot ID matches, `/proc/<pid>` exists,
process start ticks match, package/source match current authenticated state, and
current UTC time is not later than expiry. Failure of any one condition means
`live_proved = false`; stale durable workflow state may be shown only as history.

Acquisition is an exact compare-and-swap under the lock:

1. validate any existing lease's schema, run-id derivation, owner/mode/link, and
   process/boot/time facts;
2. if it is live and has a different run ID, return `BUSY` without writing;
3. if it is live and has the caller's run ID and the exact same
   package/source/executable binding, renew it;
4. if it is absent or stale, write a new complete lease to an exclusive-create
   owner-only temporary file in the anchored directory, fsync it, atomically
   replace `supervisor_lease.json`, and fsync the directory;
5. any malformed, redirected, wrong-owner, wrong-mode, multi-link, or
   contradictory live lease is `SAFETY_HOLD`, not stale takeover.

While a controller command or backoff wait is active, the owning process writes
an atomic heartbeat every 10 seconds. A heartbeat may extend expiry only if the
locked current file still has the exact caller run ID and binding. Loss of that
proof stops further workflow calls and enters `SAFETY_HOLD`. A normal worker
stop or transition to `NEEDS_NESS_DECISION`, `NEEDS_USER_ACTION`,
`READY_FOR_ACCEPTANCE`, or `SAFETY_HOLD` releases by atomically writing the same
lease with `expires_at_epoch = 0`; a crash writes nothing and becomes takeover-
eligible only after expiry. PID reuse cannot prove ownership because boot ID
and `/proc` start ticks must also match. Reboot invalidates the old boot ID.

`WORKING`, `DIAGNOSING`, and `WAITING_RECOVERING` use active present-tense UI
wording only when `run_lease.live_proved` is true. Without it the page says that
automatic work is not running and labels the durable state as the last saved
state. Ness-decision and acceptance-ready records remain readable without a live
worker, but only from authenticated controller events.

The UI server reads state and events; it does not have to own the worker thread.
Development may run both in one process only in a disposable rehearsal.

---

# 14. Acceptance-ready transition

Append `mechanical_pass_recorded` only when all are true:

- exact final candidate audit verdict is `PASS`;
- audit result is schema-valid and source-stable;
- complete candidate chain is terminally re-proved;
- no tracked/staged or unexpected untracked change exists outside the frozen
  envelope;
- candidate custody is current and no write-ahead is pending;
- Piece-3 clearance and settled-decision binding remain current;
- no newer candidate, audit, question route, or source change supersedes it.

`supervisor-status` then returns `READY_FOR_ACCEPTANCE`.

No acceptance endpoint is implemented by this change. The browser may present
the exact candidate and explain what acceptance would mean, but its acceptance
button remains unavailable until a separate accepted acceptance-record design
exists.

---

# 15. UI integration contract

The local browser displays:

- persistent package context;
- framework and addition position proved by source;
- bundle placement only when settled, otherwise “Not decided yet”;
- current supervisor state;
- `Your decisions`, `What's changing`, `Current status`, and `Technical details`
  tabs;
- automatically refreshed controller-confirmed events;
- prominent interruption only for a genuine decision, a practical user action,
  or readiness for acceptance;
- expandable candidate, hash, finding, specification, diff, audit, custody, and
  journal evidence.

The browser never reads the private operational journal as authority and never
derives a feed card from a report merely because an unkeyed digest matches. It
obtains workflow state and feed cards only from a fresh successful
`supervisor-status` whose authentication/source-current booleans are true. Each
returned feed item carries the authenticated controller event sequence/digest
it was derived from. If `supervisor-status` is absent, refused, stale, or
unproved, the page shows no supervisor PASS/change claim and says no
authenticated supervised run is active.

Before `supervisor-status` exists, package context may be projected from the
interview journal only by first obtaining a successful authenticated
`interview-status` and then rechecking the exact bytes read for contiguous event
sequence, ordinary event digests, hash links, returned event count, and returned
tail digest. A mismatch displays generic current-package context. Bundle
placement is never inferred by filename: for this package the source-bound value
remains “Not decided yet.”

Question presentation and answer recording continue to use only:

- `next-question-group`;
- `record-ness-answer`;
- the existing authenticated Piece-3 journal and revalidation path.

A `possible_ness_choice` diagnosis records a routed signal and keeps the
supervisor non-interrupting while it automatically runs the existing
question-validation and independent coverage-review commands named by
`supervisor-status.next_command`. It may enter `NEEDS_NESS_DECISION` only after
fresh authenticated `interview-status` proves either
`deliverable_question_count > 0` or `open_group_index != null`. A routed signal
or `piece3_question_validation_required` flag alone never interrupts Ness.

The supervisor journal used by the browser is an observation/recovery log. It
never becomes candidate custody, question authority, or acceptance evidence.

---

# 16. Required test seams

Provider invocations, clock/backoff, filesystem promotion, journal append,
process interruption, and UI event consumption must all be dependency-injected
or otherwise replaceable by deterministic rehearsal doubles.

The candidate must pass tests for:

1. legacy journal rounds 1–5 replay without byte rewrite;
2. lifetime rounds 6, 7, 10, and 11 map to correct batch/round-in-batch;
3. a noncontiguous, reset, repeated, or mismatched lifetime/batch count fails;
4. five corrections in one command create no sixth correction;
5. the fifth BLOCKED audit records a diagnosis checkpoint;
6. checkpoint state survives restart;
7. diagnosis sees actual current files and every current blocker;
8. identical previously unsuccessful strategy is refused;
9. new safe strategy opens exactly one next batch;
10. diagnosis can route a possible Ness choice only through Piece 3;
11. temporary dependency waits with backoff and no hot retry;
12. external action is not represented as a Ness design question;
13. safety conflict creates no candidate and remains fail-closed;
14. byte-identical Claude result promotes nothing and requires diagnosis;
15. an interrupted diagnosis or strategy consumption is not duplicated;
16. every new candidate is contiguous, exclusive, read back, custodied, and
    terminally re-proved;
17. feed fallback never says “fixed” before a fresh PASS;
18. policy-unchanged summary appears only with explicit independent proof;
19. final PASS creates `READY_FOR_ACCEPTANCE` but no acceptance;
20. closing/reloading the browser does not stop the separate supervisor;
21. a genuine question stops mechanical work until exact answer preservation and
    fresh revalidation;
22. real controller, governance, and interview-state trees remain hash-identical
    throughout disposable rehearsal.
23. existing version-4 event bytes and HMACs validate unchanged under mixed
    replay, version 5 appends validate with their own version, and 5→4 rollback
    fails;
24. the already-existing round-5/v1.5 tail creates or reuses its diagnosis
    checkpoint even though the resumed process created zero corrections;
25. mid-batch no-progress diagnosis authorizes the next derived position in the
    same batch, while round-5 no progress normalizes to one exhausted checkpoint;
26. restart preserves retry attempt/eligibility, backward wall-clock movement
    waits the maximum, and no provider runs before eligibility;
27. every incomplete operation calls `supervisor-operation-status` first and
    exercises all six recovery outcomes without duplicate provider work;
28. an insecure directory, insecure file, symlink, hard link, wrong owner, or
    full-report payload in the private operational log is refused;
29. rewriting the unkeyed operational log cannot create a UI finding, active
    run, PASS, or acceptance-ready card;
30. a stale/expired lease uses inactive wording, including after process exit;
31. a routed possible choice stays non-interrupting until authenticated Piece-3
    status proves a deliverable question or open presented group;
32. round-zero byte-identical first correction diagnoses and authorizes exactly
    lifetime/batch/in-batch `(1, 1, 1)`;
33. every unconsumed safe diagnosis—mid-batch or exhausted-batch—is consumed
    exactly once and its correction specification cannot be replaced by the
    ordinary GPT path;
34. authenticated event sequence/tail changes on every operation, backoff binds
    the fresh post-operation projection, and restart preserves that series;
35. every private operational event has exact executable/source/package/
    candidate/report bindings, and executable-version change requires read-only
    reconciliation before any provider retry;
36. ASCII canonical encoding matches the controller, old local-journal encoding
    is refused, and non-ASCII status text cannot change cross-component digests;
37. two-worker exclusion, heartbeat, clean release, crash expiry, stale takeover,
    PID reuse, reboot, wrong-link/mode, and lost-lease behavior are deterministic;
38. failed explanation review still emits exactly one authenticated fixed
    fallback card with technical custody/diff facts and no success or policy
    claim.

---

# 17. Implementation and review order

1. Independently red-team this specification against the actual installed
   controller and current decision sources.
2. Correct the specification itself until that review passes.
3. Copy the installed controller into a newly created disposable shadow.
4. Have Claude apply only the reviewed specification to the shadow candidate.
5. Run deterministic unit and fault-injection tests with no provider calls.
6. Run a full fake-provider rehearsal through multiple batches.
7. Run a bounded live-provider rehearsal only after all earlier gates pass.
8. Fresh Codex audit reads the actual candidate and real sources.
9. Compare protected real-tree hashes before and after.
10. Stop and report. Do not install without separate Ness approval.

---

# 18. Completion rule

This change is complete only when the browser can truthfully show this sequence
from durable controller evidence:

```text
Mechanical work is continuing automatically
→ a bounded batch ended
→ a fresh diagnosis found a different safe route
→ another bounded batch began without erasing lifetime history
→ corrections and fresh audits continued
→ the exact candidate reached PASS
→ ready for Ness acceptance
```

At no point may the loop ask Ness to solve mechanics, run forever inside one
unbounded command, weaken an N.H protection, or manufacture acceptance.
