# NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md

## 0. STATUS BLOCK

**Status:** `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT.`

**B-INT-5 only.** **Mechanical wiring only.** **No new policy** — this
file asks Ness nothing and decides no meaning. **No implementation** —
no code, schema, database, migration, test, or Cursor/build
instruction exists or is created. **No Bundle 5 closure. No CY-I
closure. B-INT-6, B-INT-7, and B-INT-8 remain open.**

**Date:** July 13, 2026.

**Register item:** B-INT-5 — §9 access model ↔ §25 SIA/SACL/BAI wiring
after A26 (Bundle 5 — privacy, security, access, and TSC authority).

**Version note (v1_5):** one final mechanical consistency cleanup of
v1_4 only (v1_4 SHA-256
`29fe92c6196df54711929d39960638b757b6d0585f7af8e7462c4e9c97cac230`;
1,674 lines; 105,958 bytes — **preserved unchanged, as are v1_0 through
v1_3**). **No concept, record, state, gate, or policy is added; nothing
is redesigned.** **(1) The opened event now agrees with the actual
commit order:** because the truthful opened event is flushed at **step
8** while the operation and target commit at **step 9**, the transition
event carries **`reserved_target_mode_generation`** — **it truthfully
records that runtime activation occurred under that RESERVED target, and
it neither commits the operation nor the generation, and grants no
authority**; the later commit **references the successfully flushed
opened event**, and only then may the session use the target as
`current_committed_mode_generation` and the delivery fence carry and
release under it. Crash seam **4c** is aligned: the event stands as
truthful history under the reserved target, the operation **fails**, the
**target was never committed**, restart is Dry, and **no retrieval was
released**. **(2) The remaining ambiguous generation fields and the
stale order are gone:** the duplicate generic `mode_generation` is
removed from `personal_mode_session` (keeping the runtime epoch and
`current_committed_mode_generation`) and from
`personal_mode_factor_binding` (keeping the runtime epoch and
`reserved_target_mode_generation`); the ordinary and fingerprint opening
sequences, the concurrency rules, the B-INT-6 handoff, and the logging
rule now each name the **exact** generation appropriate to their stage;
and the drafting check now reads **"factor proof → atomic SACL snapshot
→ factor binding."** **(3) The last background-restart contradiction is
removed** — no sentence any longer promises that background work
survives a real process or machine restart. **No accepted meaning or
policy changed; A26 is carried exactly.**

**Version note (v1_4):** one narrow final correction of v1_3 only
(v1_3 SHA-256
`a9193051e053b51f317beae060c9b0cc30d6bce221d777a8d777fa1c8ecb1fbc`;
1,544 lines; 97,739 bytes — **preserved unchanged, as are v1_0, v1_1,
and v1_2**), closing exactly three verified contradiction groups and
**expanding the design no further**. **(1) ONE possible opening order:**
the snapshot is now created **before** the factor binding (so the binding
never references a record that does not yet exist), it carries the
**RESERVED** target generation, it **grants no authority by itself**, it
is **never changed in place**, and it becomes the session's **current
effective-access snapshot only because the successful target-generation
commit references it** — **every claim that it already carries a
committed generation before the commit is removed**. **(2) Every
generation change has ONE parent operation:** the operation type
**`access_change`** [proposed] is added, with a controlled
`access_change_kind` (ceiling reduction; ceiling restoration; step-up
attachment affecting access; step-up removal affecting access;
owner-state invalidation requiring restriction) — **no generation may
advance without a parent operation** carrying its id, idempotency key,
boundary, epoch, base, reserved target, one winning result, terminal
status, and audit references; the ambiguous generation fields are
standardized per record. **(3) Recovery and fence consistency finished:**
the delivery fence gains its complete ownership, epoch-reset,
idempotency, and precedence rules plus the fields to enforce them; the
recovery record's `crash_boundary` now carries the **exact fourteen**
controlled values; and the **background restart contradiction is
removed** — PMA restart cancels only interactive operations bound to the
dead epoch, and **B-INT-5 does not decide whether independent background
work survives, retries, resumes, or fails.** **No accepted meaning or
policy changed; A26 is carried exactly.**

**Version note (v1_3):** one final consistency correction of v1_2 only
(v1_2 SHA-256
`713d8973327ada03e8d4e4411341a243d009601cada3e4b205d9a7f053aeb2af`;
1,293 lines; 81,059 bytes — **preserved unchanged, as are v1_0 and
v1_1**), closing five internal contradictions. **(1) ONE truthful
opening order everywhere:** v1_2 fixed §5A but left stale wording in
§5, §7's table, §10's crash boundary 4, and §20 still implying an
"opened" event before runtime activation. **All of it is corrected: no
durable event says Personal Mode opened unless runtime activation
actually occurred, and no retrieval or delivery happens merely because
activation occurred — the fence must still be released under the same
committed target generation.** The missing **`personal_mode_activation_ready_event`**
[proposed] and the **`personal_mode_delivery_fence`** [proposed]
contract are now fully defined. **(2) The generation ambiguity is
resolved:** `personal_opening` is a **preparatory stage under the base
generation** (Dry permission, fences closed, target **reserved but not
committed**), and the open operation **commits its one target exactly
once into one winning outcome**; `personal_closing` is **restrictive
cleanup after access is already gone**. **One operation → one base →
one reserved target → ONE winning access result; a target is never
committed twice.** Generation fields are standardized per stage (base /
reserved target / committed target / prior / new). **(3) The
mode-boundary uniqueness rule is now consistent:** §11 no longer says
uniqueness is enforced on the session identity — **at most one live
session per `mode_boundary_ref` within the current epoch**, with
`mode_session_id` identifying the session only **after** admission.
**(4) Invalidation is complete and revalidation seams are explicit:**
**any change to the relied-on SACL state version or the channel
observability version invalidates the snapshot**, and the owner truths
are **re-verified at five seams** — before `activation_ready`, before
runtime activation, before the opened-event flush, before fence
release, and at every later retrieval/output under B-INT-6. **(5) The
background boundary is enforceable and properly limited:**
**`mode_authority_dependency_ref`** is now a defined record, cancellation
reaches **only matching dependents**, and the **process-restart
overclaim is removed** — whether background work survives a real
restart belongs to **its own package**, not to B-INT-5. **No accepted
meaning or policy changed; A26 is carried exactly.**

**Version note (v1_2):** one complete correction pass on v1_1 only
(v1_1 SHA-256
`2fdc13982a8bd5c918352df4a65498a00ce93d8673653a36a0d4b1f9b8798068`;
988 lines; 62,263 bytes — **preserved unchanged, as is v1_0**), closing
six mechanical audit findings. **(1) The epoch/generation fence is now
finished, not just declared:** the PMA is the **sole generation
allocator**; every access-affecting operation carries
**`base_mode_generation` + `target_mode_generation` + the current
`mode_runtime_epoch_id`** (§7B); a transition **commits only if its base
generation is still current**; **close and downgrade advance the
restrictive fence before stale permissive work may deliver**; and the
recovery record now carries the **full four-field pair**
(`prior_*` provenance / `new_*` fresh Dry runtime) — **no old generation
ever transfers into a new epoch**. **(2) Duplicate and trusted-boundary
enforcement became recordable:** a stable **`mode_boundary_ref`**
[proposed] (the accepted local user/app session boundary) is carried in
the session, every operation, factor binding, snapshot, recovery event,
and delivery fence — **the one-live-session rule is enforced against the
BOUNDARY, not against a freshly minted session id** — and every
operation carries a required **`idempotency_key`**, while open
operations and factor bindings carry **`trusted_surface_ref`,
`trusted_app_session_ref`, and `device_or_keystore_boundary_ref`**, so
the checks v1_1 merely asserted can actually be performed. **(3) The
SACL handoff is bound to ONE exact SACL truth:** the snapshot now
references the owner-held **`SACL_session_state`** (its
`last_sia_event_id`, `last_audit_event_id`, stream-authorization-set
identity, `primary_addressed_stream`, `shared_output_level` +
`shared_output_level_since`, per-stream `pbr_version` and
`ness_presence_satisfied`) — **all fields derived from that same
committed moment**, with **any stream join/departure/speaker change,
primary-addressed change, PBR change, Ness-presence change, or downgrade
invalidating the snapshot, advancing the generation, and cancelling
stale delivery**; and **channel observability is an owner-held
reference — the PMA can no longer turn a shared path private by writing
a field**. **(4) Activation records are truthful:** preparation and
activation are **separated** — a durable **`activation_ready`** receipt
(which **never claims the mode is active**) precedes runtime activation
**with the retrieval fence still closed**, and the **`personal_active`
transition event is appended only after activation actually occurred**;
**no durable event may claim a state that never existed**, and a
restrictive transition **never waits in a permissive state because
logging failed**. **(5) The step-up reference model is finished:** the
logging table now uses the **exact observation values**
(`observed_active` etc., with the authoritative change happening **in
BAI/SACL**), and top-security is represented by the **complete owner
pair — `bai_lease_ref` AND `sacl_gate1_decision_ref`** — both of which
must be **current and mutually compatible at use time**. **(6)
Separately authorized background work is no longer cancelled:** per
Master §25.4, **background functions run under their own purpose,
authority, privacy, and function rules and do not become guest-level
merely because no active speaker stream is present** — so B-INT-5's
close/suspend/restart/cancellation signals now apply **only to the
interactive Personal Mode session and to operations carrying a
`mode_authority_dependency_ref` on it**, while **nothing a background
operation produces may be exposed through the closed or downgraded
interactive path**. **No accepted meaning or policy changed; A26 is
carried exactly.**

**Version note (v1_1):** one complete correction pass on v1_0 only
(v1_0 SHA-256
`47acb5dbd7ca00358e293c8c8356a424a84567e52064b3f3816e5ec49ef56d79`;
678 lines; 41,645 bytes — **preserved unchanged as historical candidate
evidence**), closing six mechanical audit findings. **(1) Restart-safe
stale fence:** a bare monotonic counter can repeat after a restart, so
the fence is now the **pair `mode_runtime_epoch_id` +
`mode_generation`** — a fresh, non-reused random epoch identity minted
at **every** application/process startup, with the generation monotonic
**inside** one epoch; **every** operation, record, snapshot, signal,
formed output, and delivery fence carries **both**, and any epoch
mismatch — or any older generation within an epoch — is **stale and
discarded**. `current_effective_access_ref` may be null only while
`personal_opening`, with permission fixed at **no personal access**,
and a **fresh snapshot is mandatory** before `personal_active`.
**(2) Valid crash terminal state:** a non-terminal operation now
becomes **`failed`** with a precise reason (`restart_interrupted` /
`crash_interrupted`) — the undeclared value `interrupted` is **never**
assigned, and the recovery event stays **append-only history, not an
authority**. **(3) Complete SACL multi-speaker handoff:** one cached
level is gone; the snapshot and handoff now carry the **addressed
stream**, the **Ness-stream authorization reference**, the **per-stream
levels**, the **`shared_output_level` (the minimum across active
streams)**, whether the channel is **shared/observable or genuinely
private and unobservable**, **PBR references and category limits**, the
**Ness-presence requirement**, and the **assessment identity and
freshness for every relied-on stream** — and **Personal Mode never
turns a shared output path into a private one**. **(4) A lower ceiling
is not a loss of safety:** an access reduction now **discards only work
above the new ceiling** and commits a lower snapshot, with the mode
**staying `personal_active`** where the ordinary session remains valid
(top-security falling back to `recognized_ness`; a step-up expiring or
revoked; **`imitation_risk` blocking Gate 1 while preserving
recognized-Ness access**) and **suspending only when Ness-private use
is no longer safely permitted**; the voice row and the authority-owner
fail-closed clause were corrected accordingly. **(5) A real
purpose-bound fingerprint path:** using Master §25.6's existing
**`extended:<purpose_id>`** vocabulary, the proposed purpose
**`extended:personal_mode_open:<personal_mode_open_operation_id>`**
gives the fingerprint gate a valid BAI proof — bound before the OS
prompt, verified against purpose, requester, operation, session, epoch,
generation, and validity, consumed once, and **never substitutable by a
top-security, TSC, enrollment, BGMM, or any other-purpose artifact**;
a crash after consumption but before activation leaves the mode **Dry**
and requires a **new action and a new token**. **(6) No second step-up
authority:** the step-up link is now **reference/history only** —
observed state, never authoritative; current access must verify the
**actual BAI lease and current SACL Gate 1 result**. **Safe commit
ordering** is stated explicitly (§5A). **No accepted policy or meaning
changed; A26 is carried exactly.**

## 1. PLAIN PURPOSE

B-INT-5 **connects the already-designed "who is present and what
access is safe" system (§25: SIA, SACL, BAI) to the already-designed
Dry / Personal / step-up mode system (§9).** It designs neither of
them — it designs the wires between them, and the guarantees those
wires must hold:

- **identity recognition never silently opens Personal Mode;**
- **Ness must deliberately request Personal Mode;**
- **the normal §9 gate must succeed before Personal Mode becomes
  effective;**
- **voice alone never opens it;**
- **Personal Mode never bypasses SACL or §7Q;**
- **uncertainty immediately reduces effective access;**
- **top-security remains a separate, higher gate;**
- **restart or crash never silently restores private access;**
- **closing or losing access stops private retrieval and output
  before exposure;**
- **retries and duplicate actions never create two live mode sessions
  and never restore stale authority.**

The everyday meaning, carried from accepted A26: **"N.H knowing it is
Ness and Ness choosing to open his private N.H are two different
things."**

## 2. GOVERNING AUTHORITY, REPOSITORY POINT, AND SOURCES

Authority order: (1)
`01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` — **Master V10 governs
every conflict regardless of stale internal status wording**; (2)
`01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; (3)
`01_AUTHORITATIVE/cursorrules`; (4)
`01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`.

**Repository point:** `nesgeva/NH-GOVERNANCE`, branch `main`, head
**`6a057af4203afb690289462149449dcafb5d4a64`**, verified at task start.
The complete delta from `72c15f9c…` was inspected: **exactly one added
file** (the B-INT-4 closure record v1.1), with **no existing file
modified, deleted, or renamed**. **A repository-wide search confirmed
no B-INT-5 candidate and no B-INT-5 closure record exists** — this is
the first.

**Sources read at this head** (SHA-256 first-8): Master V10
`2d9ed4c6` — **§9** (Dry Mode: no personal data accessed; Personal Mode:
full personal access after identity verification; graduated temporary
step-up; the raw-versus-derived boundary; the exact-quote exception for
Ness's own original words; trusted-app-only; zero-copy; code-level
mode separation), **§25.3 SIA**, **§25.4 SACL** (the four access levels
and **Gates 0–3** read verbatim; PBR categories; stale/failed
assessment handling; access reduction; discard-before-output; the Guest
rule that N.H **never signals hidden material exists**), **§25.5** the
Wellbeing / Identity / Security separation (**no wellbeing output ever
serves as identity or security evidence**), **§25.6 BAI** and the
**Top-Security Biometric Lease**, **§7Q** (private access, restriction,
exclusion, redaction, internal use, output), and **§0B**
full-transparency logging. Also read: Defaults `6cd09329`; `cursorrules`
`5050d088`; Companion `cdcc6134`; Map v1.6 `33af648d` (**C-2** interaction
contract, **C-9**, **C-SIA**, **C-SACL**, **C-BAI**, **B-INT-5**,
**B-INT-6**, **CY-I**); the eight-bundle plan `2d6483d1`.

**Accepted packages verified present and consumed — never reopened:**
**A26 v1.1** `41e1f67d` — **accepted and `PACKAGE_COMPLETE` for its
standalone policy scope** (closure record present and verified);
**A7 v1.1** `3deacafb`; **B7 v1.3** `7fda28e9`; the accepted **B9**
retry package `e8f4c3de` (retry classification consumed **by
reference**; no retry value is invented here); and **B-INT-4 v1.3**
`f722ac95` with its closure receipt — read **only** to confirm Bundle 5
status and to avoid conflicting operation patterns.

## 3. THE SETTLED A26 DECISION — CARRIED EXACTLY, NOT REINTERPRETED

1. **The §25 identity/access system and the §9 mode system are separate
   cooperating layers.**
2. **N.H recognizing Ness does not automatically open Personal Mode.**
3. **Ness separately and explicitly opens Personal Mode.**
4. **Inside a properly authenticated private Personal Mode context,
   §7Q applies unchanged, with every existing exception.**
5. **Personal Mode does not unlock top-security.**
6. **Uncertainty reduces access, and protected output stops before
   private exposure.**

**Settled factor roles (the mechanical boundary, consumed as given):**
**PIN is the ordinary §9 gate.** **Fingerprint is the strongest factor**
and may satisfy or replace a weaker ordinary gate **where the accepted
hierarchy permits**. **Voice and speaking-pattern recognition are
convenience and identity evidence only — never a sole hard gate, never
a hard lockout.** **Ness's explicit opening action is required
separately from factor verification.** **SIA determines identity
evidence. SACL determines the current permitted access level and PBR
limits. BAI owns purpose-bound biometric authority and the existing
top-security lease.** **No component may silently take over another's
authority.**

## 4. TWO LAYERS THAT COOPERATE BUT NEVER FUSE

**Layer 1 — §25 identity and access.**
- **SIA** supplies **current identity assessments and provenance** —
  evidence, never permission.
- **SACL** supplies the **current access level** (`top_security` |
  `recognized_ness` | `known_person` | `guest`, decided by its
  **Gates 0–3**), **PBR category limits**, the **assessment identity
  and freshness**, and **downgrade events**. It is the **continuous
  access ceiling**.
- **BAI** supplies **only** its already-accepted **purpose-bound
  biometric token** and **top-security lease** functions.

**Layer 2 — §9 mode.**
- **Dry Mode** controls whether personal material is **eligible for
  private use at all** (no personal data accessed; the §9 exceptions —
  including the **exact-quote exception for Ness's own original
  words** — are consumed exactly as §9 states them, and **no additional
  Dry-Mode data availability is invented here**).
- **Personal Mode** represents **Ness's deliberate choice** to enter his
  private N.H context.
- **Temporary step-up** represents a **separately authorized higher
  operation**.
- **Top-security** remains governed by its **complete existing §25/BAI
  conditions** (SACL Gate 1 + the BAI lease) — B-INT-5 changes none of
  them.

**The effective-permission rule.** Effective permission for any
operation is the **intersection** of:

1. the **current §9 mode permission**;
2. the **current SACL access level and PBR limits**;
3. **§7Q** purpose, privacy, restriction, exclusion, and compartment
   rules;
4. **any separate top-security lease** where the requested material or
   action requires it.

**The most restrictive applicable result wins.** **No layer may use
another layer's state to widen access** — mode never widens SACL or
§7Q; SACL never widens §7Q; §7Q never widens the mode; and none of them
grants top-security.

**Also carried:** the **§25.5 separation** — **no wellbeing output
ever serves as identity or security evidence**, and nothing in this
wiring routes wellbeing state into a gate.

## 5. NORMAL PERSONAL MODE OPENING — THE EXACT SEQUENCE

**The explicit opening action and the authentication proof are two
separate requirements. Neither alone opens Personal Mode.**

1. **Ness performs a deliberate Personal Mode opening action** — an
   unambiguous request to enter his private context.
2. The operation receives a stable **`personal_mode_open_operation_id`**
   [proposed], and the PMA records the **current `mode_runtime_epoch_id`,
   the `base_mode_generation`, and the operation's reserved
   `target_mode_generation`** (§7B) — **each named exactly for its stage,
   and each travelling with everything that follows**.
3. **The request must originate from an accepted trusted local/app
   surface under §9** (trusted-app-only). Any other surface → refused,
   recorded.
4. **The ordinary §9 identity gate is checked:**
   - **PIN is the normal gate.**
   - **Fingerprint is the stronger alternative — and it now has a valid,
     purpose-bound BAI proof (§5B).** It may satisfy the ordinary gate
     **only** through that exact path.
   - **Voice or speaking-pattern recognition alone is never
     sufficient.**
   - **No raw PIN, fingerprint template, or voice biometric is stored in
     any mode record** — only a **reference to the owner-held
     verification result**.
5. **A fresh SACL multi-stream snapshot is obtained** (§13) — **not one
   cached level**: the addressed stream, the **Ness-stream authorization
   reference**, the per-stream levels, the **`shared_output_level`**,
   the PBR references and limits, the Ness-presence requirement where
   applicable, and **the assessment identity and freshness for every
   relied-on stream** — all checked for **freshness and conflicts**.
6. **The explicit opening action and the accepted factor proof are bound
   to the same operation, session, epoch, and generation** —
   `personal_mode_factor_binding` [proposed].
7. **Runtime activation happens FIRST, with the retrieval/delivery fence
   still CLOSED. USABLE Personal Mode access begins only after (a) the
   opened transition event is flushed, (b) the open operation is
   committed, and (c) the fence is released** — all under the same
   committed target generation (§5A). **The mode is never called usable
   or effective before fence release.**
8. **Effective access remains limited by the current SACL result and
   §7Q** (§4) — opening grants **no** access beyond that intersection.
9. **The visible mode indicator changes only after the committed
   transition** (§15).
10. **No private retrieval begins before the delivery fence is RELEASED**
    (§12A), and **never while the effective-access snapshot is absent or
    stale** (§12, record 1). **Runtime activation alone grants nothing.**

**The three distinct opening outcomes:**

- **explicit action + valid ordinary gate + SACL can safely permit
  Ness-private use → `personal_active`;**
- **explicit action + valid ordinary gate, but the current SACL result
  cannot safely permit Ness-private use → `personal_suspended`, with
  ZERO private retrieval** (the mode session exists and is honest; it
  simply grants nothing until safety returns — §8);
- **invalid or ambiguous action, or an invalid ordinary gate → opening
  blocked, and the mode stays `dry`.**

**Absolutely:** a **PIN entry**, a **fingerprint touch**, a **voice
recognition result**, a **prior session**, or a **`recognized_ness`
assessment performed for another purpose** — **none may silently open
Personal Mode.**

### 5A. TRUTHFUL COMMIT AND ACTIVATION ORDERING

**Preparation and activation are separate.** A durable record must never
claim a state that never existed — so nothing says "the mode opened"
until the mode actually opened.

1. **Durable opening intent and operation record** committed (the
   operation reserves its `target_mode_generation` — §7B).
2. **Valid ordinary-factor proof** obtained (PIN result, or the §5B
   consumed purpose-bound BAI proof).
3. **An append-only access snapshot is CREATED UNDER THE RESERVED TARGET
   GENERATION** (§12, record 5) — one atomic SACL truth, not assembled
   pieces. **It grants no authority by itself.**
4. **The factor binding links the intent, the factor proof, and THAT
   ALREADY-EXISTING SNAPSHOT** (§12, record 4) — **it never references a
   record that does not yet exist.**
5. **A durable `activation_ready` receipt is flushed successfully**
   (§12, record 8). **This means only that ALL PERMISSION CHECKS PASSED.
   It does NOT claim Personal Mode is active.**
6. **Owner states are RECHECKED** — the SACL state version and the
   observability version must still match current owner truth (§12B).
7. **The PMA activates the live runtime state** under the current epoch
   and the reserved target — **while the retrieval/delivery fence remains
   CLOSED.**
8. **The TRUTHFUL opened event is flushed** —
   `personal_mode_transition_event` (`personal_opening` →
   `personal_active`), written **only after activation truly occurred**.
9. **The operation AND its target generation COMMIT** — one target, one
   winning result (§7B). **The snapshot of step 3 becomes the session's
   current effective-access snapshot ONLY because this commit references
   it.**
10. **The delivery fence is RELEASED** (§12A).
11. **The indicator is updated** (§15).
12. **Private retrieval may begin** — and not before.

**Crash behavior at each seam:**
- **Crash before `activation_ready`** → **Dry**; the operation becomes
  **`failed`**.
- **Crash after `activation_ready` but before runtime activation** →
  **Dry**; **no "mode opened" event exists**, because none was written.
- **Crash after runtime activation but before the transition-event
  flush** → restart **Dry**; **no private retrieval occurred, because the
  fence stayed closed.**
- **Failure to flush the actual opened event** → **immediately return to
  Dry / fail closed, BEFORE the retrieval fence is opened.**
- **Crash after the opened event but before the retrieval fence is
  released** → restart **Dry**; the event **truthfully records that
  runtime activation occurred**, and **no private retrieval was
  released**.
- **No durable event may claim a state that never existed.**

**Restrictive transitions never wait in an unsafe permissive state
merely because logging fails:** **the restriction applies FIRST**,
**delivery stays blocked**, and the logging failure is **recorded or
carried forward — without reopening access.**

### 5B. THE PURPOSE-BOUND FINGERPRINT OPENING PATH [PROPOSED]

BAI is **purpose-bound**, and a proof for one purpose can never satisfy
another. Master §25.6's accepted purpose vocabulary already includes the
extensible form **`"extended:<purpose_id>"`**, which this path uses
**mechanically — inventing no new biometric meaning and weakening no
purpose binding**:

**Proposed purpose:**
**`extended:personal_mode_open:<personal_mode_open_operation_id>`**

1. **Ness first performs the explicit Personal Mode opening action.**
2. **PMA creates** the stable open operation and the session reference,
   recording the **runtime epoch**, the **base generation**, and the
   **reserved target generation**.
3. **PMA requests BAI biometric authorization using the exact extended
   purpose above.**
4. **BAI binds the purpose BEFORE the OS prompt.**
5. On successful biometric verification, **BAI produces a one-time,
   purpose-bound proof** under its accepted `one_time_authorization_token`
   behavior (single-use; **consumed before the protected action
   begins**).
6. **Before mode activation, PMA verifies:** the **exact purpose**; the
   **requester**; the **operation identity**; the **session identity**;
   the **runtime epoch**; the **base generation and the reserved target
   generation**; and **validity, expiry, and revocation state**.
7. **The proof is consumed once, for that exact Personal Mode open
   operation.**
8. **Only after successful consumption, a fresh SACL check, and the
   explicit-action binding may the mode transition commit** (§5A).

**Cross-purpose prohibitions, absolute:** **a token or lease created for
`top_security_access`, `tsc_promotion:<session_id>`,
`voice_enrollment_ness`, `bgmm_confirmation:…`, or any other purpose
CANNOT open Personal Mode.** **A Personal-Mode opening token CANNOT
unlock top-security** — top-security keeps its own complete SACL Gate 1
conditions plus the BAI lease (§14).

**Crash rule (deliberately unlike B-INT-4's TSC path):** **a crash after
token consumption but before mode activation does NOT forward-complete
or restore Personal Mode.** The mode remains **`dry`**, and **a new
explicit action plus a new token is required.** The **durable BAI audit
record is history and proof of what occurred — it never restores the
volatile mode after a restart.** **No biometric data enters any B-INT-5
record.**

## 6. FACTOR-ROLE MATRIX

| Factor | What it proves / controls | May begin Personal Mode? | May satisfy the ordinary gate? | May unlock top-security? | Survives restart? | Decision owner | Reusable? | Stale / uncertain / revoked / unavailable |
|---|---|---|---|---|---|---|---|---|
| **Explicit opening action** | Ness's **deliberate intent** to enter his private context | **Required — but never sufficient alone** (a valid gate is also required) | **No** — intent is not proof | **No** | **No** — a new explicit action is required after restart | §9 mode layer (Ness) | **No** — one action, one operation | Ambiguous or absent → **no opening**; the prior action is **never** later treated as current identity proof |
| **PIN** | Knowledge factor — **the ordinary §9 gate** | **No, alone** — only together with the explicit action | **Yes — it is the normal gate** | **No** | **No** | §9 gate (verification result owned by its verifier) | **No** — bound to one operation, session, and generation | Missing/failed/stale/unverifiable → **fail closed**; no opening |
| **Fingerprint (via the §5B purpose-bound path)** | Strongest factor — biometric verification through BAI, under the proposed purpose **`extended:personal_mode_open:<open_operation_id>`** | **No, alone** — the explicit action is still required | **Yes — but ONLY through the §5B path**: purpose bound before the OS prompt; proof verified against purpose, requester, operation, session, **epoch**, **generation**, validity/expiry/revocation; **consumed once** | **Not alone, and never via this purpose** — top-security needs SACL **Gate 1** in full (verified biometric within timeout, Ness's Person-Box at high certainty, score separation, **no spoofing suspicion**, **no `imitation_risk`**, no disqualifiers) **plus the BAI lease** | **No** — BAI state is in-memory only (§25.6); tokens and leases die at restart | **BAI** | **No** — single-use and purpose-bound; **a token for any other purpose can never open Personal Mode, and this token can never unlock top-security** | Absent/expired/revoked/wrong-purpose/unverifiable → **no gate satisfaction, no top-security**; **fingerprint alone never restores top-security while identity is uncertain or suspicious**; **BAI unavailable → this path fails, but a PIN-only opening is unaffected** (§17) |
| **SIA recognition** | **Identity evidence and provenance** — never permission | **Never** — recognition alone **never** opens Personal Mode | **No** | **No** | **No** — recalculated under §25's accepted startup rules | **SIA** | Evidence is referenced, never "spent" | Stale/conflicting/failed → SACL treats it per its accepted rules → **access reduces** (§8) |
| **SACL access result** | The **current permitted access level + PBR limits** — the **continuous ceiling** | **Never** — a ceiling is not an opening act | **No** | **It gates Gate 1**, but top-security also needs the BAI lease | **No** — recomputed at startup | **SACL** | Read continuously; **never cached as authority** | Unavailable/stale/conflicting/suspicious/lowered → **effective access reduces immediately** (§8); Gate 0 spoofing suspicion → **guest** |
| **Voice / speaking-pattern recognition** | **Convenience and identity evidence only** — real evidence to SIA, never a §9 permission | **Never** | **Never — voice is never the sole §9 hard gate** | **No** | **No** | **SIA** (as evidence); **SACL** decides what that evidence means for access | Evidence only — never "spent" | **Missing or uncertain voice does NOT by itself invalidate a valid PIN result** — the ordinary gate stands on its own, and there is **never a hard voice lockout**. **But it is not "no effect":** **SIA may still use voice and speaking-pattern evidence**, and **SACL may independently reduce the output ceiling** under its accepted identity and security rules (e.g. certainty falling below Gate 2's threshold, or Gate 0 spoofing suspicion → `guest`) — which reduces effective access through §8, **not** through the mode gate |
| **BAI token (any other purpose)** | **Purpose-bound** biometric authority for **its exact declared purpose only** (`top_security_access`, `tsc_promotion:<session_id>`, `voice_enrollment_ness`, `bgmm_confirmation:…`) | **NEVER** — **a token issued for any other purpose can never open Personal Mode**; only the §5B `extended:personal_mode_open:<open_operation_id>` proof can | **No** | Only as part of its own accepted purpose | **No** (§25.6: in-memory only) | **BAI** | **No** — one-time, purpose-bound; **cross-purpose reuse is prohibited** | Absent/expired/revoked/wrong-purpose/unverifiable → **fail closed** for the path that needs it |
| **Top-Security Biometric Lease** | The **separate higher authority** for top-security operations | **No** | **No** | **Yes — it is top-security's own gate**, together with SACL Gate 1's complete conditions | **No** | **BAI** (with SACL's Gate 1) | **No** — time-bounded, revocable, purpose-bound | Absent/expired/revoked/unverifiable → **top-security authority is gone**; effective access falls back to the still-valid Personal Mode / SACL / §7Q intersection |

**Boundaries preserved, restated:** an **explicit action without a
valid ordinary gate does not open Personal Mode**; a **valid gate
without an explicit opening action does not open Personal Mode**;
**recognition alone does not open Personal Mode**; **voice alone never
satisfies a hard gate**; **Personal Mode does not grant top-security**;
**fingerprint alone does not restore top-security while identity
remains uncertain or suspicious**; and **`recognized_ness` is never
made a universally mandatory opening factor** — it is a continuous
access and safety input, not an opening act.

## 7. PERSONAL MODE STATE MODEL [PROPOSED]

**Authoritative owner of the live mode state:** the **§9 Personal Mode
Authority (PMA)** [proposed] — a **runtime, code-level-separated**
authority. **The live mode authority is never restored from an audit
log.** **Durable logs preserve history; they do not grant current
access.**

**States** [proposed]: `dry` | `personal_opening` | `personal_active` |
`personal_suspended` | `personal_closing` | `personal_closed`.
**Step-up is not a mode state**: it is a **separately owned authority,
observed by reference only** (§12, record 7; §14), so it **never
rewrites the Personal Mode session**. "`step_up_active`" is therefore
expressed as **`personal_active` + a verified-at-use-time step-up/lease
authority owned by BAI/SACL.**

### 7A. THE STALE-RESULT FENCE — EPOCH + GENERATION

A bare monotonic counter is **not** restart-safe: runtime state dies at
restart, and the number can repeat. **The complete fence is therefore a
pair:**

- **`mode_runtime_epoch_id`** [proposed] — a **fresh, non-reused, random
  epoch identity generated at EVERY application/process startup**. It is
  never derived from a counter and never reused across startups.
- **`mode_generation`** [proposed] — **the generation counter itself:
  monotonically increasing INSIDE one epoch.** **It is a COUNTER FAMILY,
  not a record field:** concrete records never carry a bare
  `mode_generation` — they carry the **stage-qualified** name that says
  exactly which generation is meant: **`base_mode_generation`**,
  **`reserved_target_mode_generation`**, **`committed_target_mode_generation`**,
  **`current_committed_mode_generation`**, or the **prior / new-restart**
  pair (§7B, §12).

**Every** open, close, suspend, resume, step-up request, factor binding,
transition, access snapshot, recovery event, indicator update, retrieval
request, formed output, cancellation signal, and delivery fence **must
carry the runtime epoch AND the exact stage-qualified generation
appropriate to it.**

**Staleness rules:**
- **Any epoch mismatch is stale and MUST be discarded** — no exceptions.
- **Any older generation inside the same epoch is stale and MUST be
  discarded.**
- **Restart creates a new epoch and starts in `dry`.**
- **Durable history may record the old epoch for provenance, but it
  never restores authority.**
- **No old output may be delivered merely because its numeric generation
  matches a number in the new epoch** — the epoch is what makes the
  match meaningless.

### 7B. THE GENERATION-ALLOCATION CONTRACT

**The PMA is the SOLE allocator of mode generations.** No other
component mints, guesses, or advances one.

**Every access-affecting operation carries three values:**
**`mode_runtime_epoch_id`** (the current epoch),
**`base_mode_generation`** (the generation the operation was formed
against), and **`target_mode_generation`** (the generation it intends to
commit).

**A new target generation is RESERVED when the operation is admitted,
and COMMITTED only with its transition.** Generation advances cover, at
minimum: **open; close; suspend; resume; access-ceiling reduction;
access-ceiling restoration; step-up attachment or removal where it
changes effective access; and restart recovery** (which begins a new
epoch entirely).

**Rules, binding:**
- **One target generation can have only ONE winning access result** — a
  second attempt to commit against the same target is refused and
  recorded as absorbed.
- **A transition may commit only if its `base_mode_generation` is still
  current.** A stale base loses, always.
- **Close or downgrade ADVANCES the restrictive fence BEFORE any stale
  permissive work may deliver** — the restriction lands first; delivery
  is blocked immediately.
- **An upgrade or resume cannot commit after a newer restriction** — its
  base is no longer current.
- **Outputs, snapshots, and cancellation signals use the COMMITTED
  target generation.**
- **An operation from another epoch ALWAYS loses, regardless of its
  number** — the epoch decides before the number is even compared.

**EVERY GENERATION-CHANGING ACTION HAS EXACTLY ONE PARENT OPERATION.**
**No generation may advance without one.** That parent — an `open`,
`close`, `suspend`, `resume`, `step_up_request`, or **`access_change`**
(with its `access_change_kind`: ceiling reduction, ceiling restoration,
step-up attachment affecting access, step-up removal affecting access, or
owner-state invalidation requiring restriction) — **must carry: a stable
operation id; an idempotency key; the `mode_boundary_ref`; the
`mode_runtime_epoch_id`; the `base_mode_generation`; the reserved
`target_mode_generation`; one winning result; a terminal status; and its
audit references.**

**ONE OPERATION → ONE BASE → ONE RESERVED TARGET → ONE WINNING ACCESS
RESULT.** A target generation is **committed exactly once**, and **never
twice**. If another access change is needed, it is a **new operation**
with a **new operation id, new idempotency key, new base, and new
reserved target**. **Preparatory and cleanup stages are CHILD EVENTS —
they are not additional access-generation commits.**

**Opening lifecycle (resolving the two-commit ambiguity):**
**`personal_opening` is a PREPARATORY lifecycle state under the CURRENT
BASE generation — it does NOT commit the target.** While opening:
**effective mode permission remains Dry / no personal access**;
**retrieval and delivery fences remain closed**; **the reserved target
generation has NOT yet become the current generation**; and **preparation
records (the factor binding, the `activation_ready` event) may REFERENCE
the reserved target but never commit it.** The open operation then
**commits its target generation exactly once, into ONE final winning
outcome:** **`personal_active`**, **`personal_suspended` with zero
personal retrieval**, or a **blocked/failed Dry result**. **One target is
never committed first to `personal_opening` and then again to another
state.**

**Closing lifecycle:** **`personal_closing` is RESTRICTIVE CLEANUP AFTER
ACCESS HAS ALREADY BEEN REMOVED.** On **close admission**: **reserve the
close target generation**; **synchronously close delivery**; **commit the
target to the restrictive no-personal-access result**; and **defeat every
stale open, resume, upgrade, and delivery result**. Cleanup may then move
the session's lifecycle marker to `personal_closed`, but **this creates
no new access grant and does not reuse or recommit the target
generation**. **The live effective mode is Dry / no personal access
throughout cleanup.**

**Standardized generation fields, by stage (no bare `mode_generation`
where the stage matters):** **operation** → `base_mode_generation` +
`target_mode_generation`; **factor binding and `activation_ready`** →
the operation's **reserved target** + the operation reference;
**effective-access snapshot** → **`created_under_reserved_target_mode_generation`**
(it carries the RESERVED target, and becomes current-effective only when
the commit references it);
**transition event** → the **committed target** + operation and boundary
references; **delivery fence and indicator event** → the **committed
target**; **step-up observation** → the **committed generation under
which it was observed**; **recovery** → the **complete prior and new
epoch/generation pairs**.

**Allowed transitions, with preconditions and committed results (every
row additionally requires a current `base_mode_generation` and a
reserved `target_mode_generation` under the current epoch):**

| From → To | Precondition (all required) | Committed result |
|---|---|---|
| `dry` → `personal_opening` | Explicit opening action; trusted surface; stable open operation id; current epoch + generation recorded | Intent committed; **no access whatsoever** (`current_effective_access_ref` may be **null here, and permission is fixed at NO personal access**) |
| `personal_opening` → `personal_active` (**the open operation's ONE target-generation commit — which happens AFTER the opened event, not at it**) | Ordinary gate **accepted** (PIN, or the §5B purpose-bound fingerprint proof — **never voice alone**); a **fresh atomic SACL snapshot** (§12 record 5) that **can safely permit Ness-private use**; all bound to the same operation, session, boundary, **runtime epoch**, and the operation's **reserved target generation**; **a fresh effective-access snapshot is MANDATORY**; **owner truths re-verified at every §12B seam** | **In order (§5A):** runtime activation occurs with the fence **closed** → the **opened event is flushed under the RESERVED target** (it commits nothing) → **THEN the operation and its target generation COMMIT — once, to this one winning result, referencing that flushed event** → the fence is **released under the committed target** → the indicator updates → only then may retrieval begin. **The target is never committed before runtime activation and the opened-event flush.** |
| `personal_opening` → `personal_suspended` | Ordinary gate **accepted**, **but the current SACL result cannot safely permit Ness-private use** (§8) | The session exists **with ZERO private retrieval**; it waits for safety, honestly indicated |
| `personal_opening` → `dry` | Gate refused/absent/stale/unverifiable; untrusted surface; ambiguous action; SACL unavailable/conflicting; durable record unflushable | **Opening blocked**, recorded; **no access ever granted** |
| `personal_active` → `personal_suspended` | Any §8 **safety-loss** condition | Effective access reduces; **work above the new ceiling discarded before any output channel write** |
| `personal_active` → `personal_active` (**lower ceiling**) | An access **reduction** that does **not** end Ness-private safety (§8) | **The mode stays active**; only work **above the new ceiling** is discarded; a **lower snapshot** is committed; permitted work continues **only under the new epoch/generation-bound snapshot** |
| `personal_suspended` → `personal_active` | The **same still-valid** session; a **freshly verified** current SACL result that safely permits Ness-private use; no explicit close, restart, timeout, revocation, or newer restrictive transition intervening | **Only future operations proceed.** **Discarded work is never resumed or replayed.** **No new opening action** is required for a temporary SACL pause. **No top-security is restored** unless its complete separate conditions hold. |
| `personal_active` \| `personal_suspended` → `personal_closing` | Explicit close (or timeout/inactivity — **duration owned elsewhere**) | New private retrieval **stops immediately** |
| `personal_closing` → `personal_closed` / `dry` | Discard + release complete; step-up/top-security revoked or expired **by their accepted owners** | Live mode **Dry/closed**; indicator updates **after** the restrictive transition commits |
| **any** → `dry` | **Restart, crash, epoch mismatch, or unverifiable state** | **Fail closed to `dry`** (§10) |

**Forbidden transitions:** `dry` → `personal_active` (no opening
bypass); `personal_opening` → `personal_active` without **both** the
explicit action **and** an accepted gate **and** a fresh snapshot;
`personal_closed` → `personal_active` without a **new** explicit action
and a **new** gate; any transition that **widens** access from a stale
result; any transition **driven by a durable log** rather than live
committed authority; any transition granting **top-security** from mode
state.

## 8. ACCESS REDUCTION — A LOWER CEILING IS NOT A LOSS OF SAFETY

**On every access reduction (the accepted SACL behavior, applied):**

- **compare the new SACL ceiling with each in-progress operation's
  sensitivity** (SACL's own `SACL_session_state.in_progress_operations`
  is the accepted home of that list — consumed, not duplicated);
- **discard ONLY the work above the new ceiling — before any output
  channel is written — and ONLY among operations that depend on this
  mode session's authority (§9A); separately authorized background work
  is NOT cancelled by this signal;**
- **recompute and commit a lower effective-access snapshot;**
- **work still permitted by the lower ceiling may continue — but only
  under the new epoch/generation-bound snapshot** (§7A);
- **transient private buffers and zero-copy handles for discarded work
  are released safely;**
- **no withheld content — and no signal that additional content exists —
  is ever exposed** (§25.4's Guest rule: N.H never says "I cannot tell
  you" and never signals hidden material);
- **no completed private output is replayed later.**

**Personal Mode REMAINS `personal_active` when the ordinary mode session
remains valid** — a lower ceiling is not a loss of the mode. This
includes:

- **top-security falling back to `recognized_ness`;**
- **a step-up expiring or being revoked while normal Personal Mode
  remains valid;**
- **`imitation_risk` blocking top-security (Gate 1) while preserving
  recognized-Ness access** — per §25.4, the `imitation_risk` flag
  **blocks Gate 1 only and does not reduce Ness to guest**; natural
  divergence from stress, illness, or emotion produces it.

**Personal Mode becomes `personal_suspended` when Ness-private use is no
longer safely permitted.** This includes:

- **the current Ness stream becoming `guest`, unknown, or unresolved;**
- **a different person being the current addressed stream without a safe
  private Ness-only path;**
- **stale or failed SIA/SACL state;**
- **medium-or-higher acoustic spoofing suspicion** (SACL **Gate 0** →
  `guest`, plus its private Ness alert);
- **loss of the valid ordinary Personal Mode gate or session;**
- **an unverifiable mode / epoch / generation state.**

In `personal_suspended`: **no new private retrieval begins**; **the prior
explicit opening action is not treated as current identity proof**; and
**top-security authority is revoked wherever the accepted lease rules
require it.**

**If SACL later recovers during the same still-valid Personal Mode
session:** **only future operations may proceed**; **discarded work is
never resumed or replayed**; **the current SACL assessment must be
freshly verified**; **restoration must not override an explicit close,
restart, timeout, revocation, or newer restrictive transition**; **no new
opening action is required merely for a temporary SACL pause** if the
session remains valid under the accepted rules; and **this does not
restore top-security** unless its complete separate conditions also
hold.

## 9. EXPLICIT CLOSE

- Stable **`personal_mode_close_operation_id`** [proposed].
- **New private retrieval stops immediately.**
- **In-progress private work is discarded before output — scoped to work
  carrying the CURRENT mode-authority dependency (§9A, §12 record 9);
  independently authorized background work is not swept up by this.**
- **Transient handles and private buffers are released.**
- **Step-up and top-security authority are revoked or allowed to expire
  according to their accepted owners** (BAI/SACL) — B-INT-5 revokes
  nothing on their behalf; it **requests and records**.
- **The live mode becomes Dry/closed.**
- **The visible indicator changes only after the restrictive transition
  commits.**
- **Repeated close requests are absorbed safely**; **closing an
  already-closed session is idempotent.**
- **A late open result cannot reactivate a session after a newer
  close** (the generation fence, §11).

**Closing removes current access. It destroys no durable N.H record.**

### 9A. SCOPE OF CLOSE, SUSPEND, RESTART, AND CANCELLATION — BACKGROUND WORK IS NOT COLLATERAL

**Master §25.4 is explicit:** *"Background functions operate according to
their own purpose, authority, privacy, and function rules. They do not
become guest-level merely because no active speaker stream is present. A
background function authorized during a Ness session continues under
those rules unless a specific security event revokes that
authorization."* B-INT-5 therefore **scopes its signals precisely**:

- **B-INT-5's close, suspend, restart, and cancellation signals apply to
  the CURRENT INTERACTIVE Personal Mode session and to every operation
  that carries that mode session as an authority dependency** — each such
  operation carries a **`mode_authority_dependency_ref`** [proposed]
  naming the mode session it depends on.
- **A background operation with separate valid authority is NOT silently
  cancelled merely because Personal Mode closes or suspends.**
- **It remains governed by its own purpose, privacy, access, timeout, and
  revocation rules** — its owners, not the PMA.
- **A real security event may still revoke it when its owning rules say
  so** (e.g. Gate 0 spoofing suspicion, an explicit revocation) — B-INT-5
  **reports the event; it does not invent the revocation.**
- **Nothing a background operation produces may be exposed through the
  closed or downgraded interactive output path** — the delivery fence
  (§13) blocks it exactly as it blocks anything else.
- **B-INT-5 must NOT reinterpret Dry Mode as global blindness for
  independent background functions.**
- **The RESTART BOUNDARY — the final wording, with no overclaim in either
  direction:**
  - **Closing, suspending, or resetting Personal Mode is NOT itself
    authority to cancel independently authorized background work.**
  - **PMA restart handling cancels INTERACTIVE operations that depend on
    the dead Personal Mode epoch** (those carrying a
    `mode_authority_dependency_ref` on it — §12, record 9).
  - **B-INT-5 does NOT decide whether independent background work
    survives, retries, resumes, or fails after an actual application,
    process, or machine restart.**
  - **That outcome belongs to the background operation's OWNER and its
    recovery package.**
  - **Background results cannot enter a new interactive path without a
    CURRENT VALID delivery fence and CURRENT privacy/access checks**
    (§12A, §12B).
- **The exact background-function mechanics remain with their owning
  packages and later integration** — nothing here designs them.

## 10. RESTART AND CRASH BEHAVIOR — FAIL CLOSED TO DRY

**A process restart, application restart, machine restart, crash, or
unverifiable mode state fails closed:**

- **a NEW `mode_runtime_epoch_id` is minted** (§7A), and **effective mode
  starts as `dry`;**
- **no previous Personal Mode session is automatically restored;**
- **no previous PIN verification, explicit opening act, SACL assessment,
  fingerprint proof, step-up, BAI token, or top-security lease is
  reconstructed** (§25.6: BAI state is in-memory only);
- **historical logs remain history only** — including the old epoch,
  recorded **for provenance, never for authority**;
- **any non-terminal operation becomes TERMINAL as `failed`**, carrying
  the precise reason **`restart_interrupted`** or **`crash_interrupted`**
  — **the undeclared state `interrupted` is NEVER assigned** (§12,
  record 2), and a `personal_mode_recovery_event` records
  `action_taken = closed_for_restart` or `blocked_fail_closed` as
  **append-only history, never an authority**;
- **Ness must perform a new explicit opening action and satisfy the
  current ordinary gate** before Personal Mode becomes active again;
- **current SIA/SACL must be recalculated under their accepted startup
  rules;**
- **unknown mode state is never treated as active;**
- **no INTERACTIVE Personal-Mode output created under the DEAD EPOCH may
  be delivered through the NEW interactive path** — the epoch fence makes
  every such pre-crash result stale. **Independently authorized background
  work remains governed by its owners (§9A), and any later surfacing of
  anything still requires a NEWLY VALID delivery path and CURRENT
  privacy/access checks.**

| # | Crash boundary | Committed truth | Exact recovery action |
|---|---|---|---|
| 1 | **Before explicit intent is committed** | Nothing; mode is `dry` | Stay `dry`. Nothing recorded as an opening. |
| 2 | **After intent, before factor verification** | The intent record — **which grants no access** | New epoch; **operation → `failed` (`restart_interrupted`)**; recovery event `closed_for_restart`. **The intent is never later treated as identity proof.** New action required. |
| 3 | **After factor verification, before mode commit** (including **after a §5B token was consumed**) | The owner-held verification result / **BAI's durable audit record of the consumption** — **history and proof of what occurred, NOT authority** | **Fail closed to `dry`.** **The consumed token does NOT forward-complete or restore Personal Mode** (deliberately unlike B-INT-4's TSC path). **A new explicit action AND a new token are required.** Operation → `failed` (`crash_interrupted`). |
| 4a | **After `activation_ready` flushed, before runtime activation** | The **`activation_ready` event — which says ONLY that the checks passed and NEVER that the mode is open** | **Dry.** **No "mode opened" event exists**, because none was written. Operation → `failed` (`crash_interrupted`). |
| 4b | **After runtime activation, before the opened-event flush** | Volatile runtime state — **which does not survive** | **Dry.** **No private retrieval occurred: the fence stayed closed.** No durable event claims the mode opened. Operation → `failed`. |
| 4c | **After the opened-event flush, before the operation commits** | The **opened transition event** — **truthful history that runtime activation occurred UNDER THE RESERVED TARGET**; **the target was NEVER committed** | **Dry** (the runtime is gone). **No retrieval was released** — the fence was still closed. Operation → **`failed`** (`restart_interrupted`). The event stands as **honest history, not authority**, and **the reserved target dies uncommitted with its epoch**. |
| 4d | **After the operation commits, before fence release** | The committed operation + opened event | **Dry.** **The fence was never released, so nothing was ever deliverable.** |
| 4e | **After fence release, before the indicator update** | Committed operation, opened event, released fence | **Dry** — the new epoch invalidates the fence entirely. **Nothing formed under the dead epoch may be delivered**, and the indicator is recomputed from committed state. |
| 5 | **During private retrieval** | Whatever the owning stores committed | **Dry.** In-flight retrieval abandoned; **nothing retrieved under a dead epoch may be delivered**; buffers and zero-copy handles released. |
| 6 | **During output formation** | Nothing delivered | **Dry.** The formed output is **discarded, never delivered** — its epoch is dead (§7A, §13). |
| 7 | **During an access downgrade** | The **more restrictive** result, if committed; else nothing | **Dry** — and **the restrictive result always survives over the permissive one** (§11). |
| 8 | **During close** | Whatever the close committed | **Dry** (close and restart agree). The close's records are completed idempotently. |
| 9 | **During step-up** | The step-up authority's own committed state (**BAI/SACL own it**) | **Dry.** **No step-up survives restart**; B-INT-5's link was only an observation (§12, record 7). |
| 10 | **After step-up revocation, before the indicator updates** | The **revocation** | **Dry**; the indicator is recomputed from committed state and **never shows an authority that no longer exists**. |

**If runtime state and its required audit record cannot be reconciled →
fail closed to `dry`.**

## 11. CONCURRENCY, RACES, AND DUPLICATE PREVENTION

- **At most ONE nonterminal / open / live Personal Mode session per
  `mode_boundary_ref`, within the current `mode_runtime_epoch_id`** —
  **the uniqueness scope is the MODE BOUNDARY, never the session
  identity.** **`mode_session_id` identifies a session only AFTER
  admission; it is not the uniqueness key**, and **a duplicate can never
  bypass the rule by minting a new session id.** **Owner/enforcer: the
  PMA**, which admits at most one live session per boundary per epoch.
- **Stable operation identities** for **open, close, suspend, resume,
  and step-up** — each with an **idempotency key**; a replay is
  recognized, skipped, and recorded as duplicate-absorbed.
- **The fence, by stage** (§7A, §7B): **live state and live results use
  the `mode_runtime_epoch_id` + the `current_committed_mode_generation`**;
  **pending operations use the `mode_runtime_epoch_id` + their
  `base_mode_generation` + their reserved `target_mode_generation`.**
  **Any epoch mismatch is rejected outright**, and **any older generation
  within the same epoch is rejected**. **A number alone proves nothing
  across a restart.**
- **Concurrent opens:** **concurrent requests carrying the SAME
  `idempotency_key` return the existing parent result** (never a second
  parent operation). **Different keys racing on the SAME
  `mode_boundary_ref` still allow only ONE winner** — the loser is
  refused and recorded, **never a second live session**. **A close or a
  newer restriction defeats every older concurrent open.**
- **Duplicate indicator events** are absorbed (no second real
  operation).

**Binding rule: a more restrictive committed result always defeats a
stale less-restrictive result.** Therefore:

- **close defeats an older open;**
- **downgrade defeats an older access upgrade;**
- **restart mints a new epoch and invalidates ALL prior in-flight work**
  — no generation number from a dead epoch can ever match;
- **top-security revocation defeats a stale step-up success;**
- **a stale SACL result can never restore access.**

## 12. MODE RECORDS — B-INT-5-OWNED COORDINATION RECORDS ONLY

**Role check first:** **SIA** owns identity assessments; **SACL** owns
access decisions, levels, and PBRs; **BAI** owns tokens and the
top-security lease; **B7/§7Q** owns privacy decisions; the **audit
system** owns §0B events. **None of them owns the §9 mode session, the
mode generation, or the intent-plus-gate binding** — those are the gap
B-INT-5 fills, and **nothing below duplicates an accepted record.**

**Never stored in any record below:** **raw PIN**, **fingerprint image
or template**, **raw voice biometric**, **private retrieved content**,
**top-security secrets**, or **reconstructive protected content** —
**references to owner-held evidence only.** All records obey **§7Q and
§25 access rules**; corrections are **new linked records**, never
rewrites; `schema_version` required throughout.

**1. `personal_mode_session` [proposed]** — **the live mode state.**
Fields: `mode_session_id` (required);
**`mode_boundary_ref` (REQUIRED — the accepted local user/app session
boundary; the ONE-LIVE-SESSION uniqueness rule is enforced against THIS
boundary, never against a freshly minted `mode_session_id`, which a
duplicate request could otherwise trivially re-mint)**;
`state` (required; **live-state**; the §7 six values);
**`mode_runtime_epoch_id` (required)** and
**`current_committed_mode_generation` (required — the session's current
COMMITTED generation, never a reserved one. There is NO generic
`mode_generation` field here)**; `opened_by_operation_ref` (required from
`personal_active`); **`current_effective_access_ref`** (**may be null
ONLY while `personal_opening`, where effective permission is fixed at
NO personal access; a FRESH snapshot is MANDATORY before
`personal_active`, and NO retrieval may begin while this reference is
absent or stale**); `stepup_link_ref` (optional → record 7 — **an
observation, never authority**); `opened_at`, `terminal_at` (optional).
**Owner: the §9 PMA.** **Live-state in runtime authority — NEVER
restored from a log.** **Restart meaning: it does not survive; a new
epoch begins at `dry`.**

**2. `personal_mode_operation` [proposed]** — **one parent per
operation.** Fields: `operation_id` (required; unique);
**`idempotency_key` (REQUIRED — unique over
`mode_boundary_ref` + `operation_type` + the logical request; a repeated
request with the same key RETURNS THE EXISTING RESULT or is recorded as
`absorbed`, and NEVER creates a second parent operation)**;
`operation_type` (required; controlled: `open` | `close` | `suspend` |
`resume` | `step_up_request` | **`access_change`**); **`access_change_kind`
(required when `operation_type = access_change`; controlled:
`ceiling_reduction` | `ceiling_restoration` |
`step_up_attachment_affecting_access` |
`step_up_removal_affecting_access` |
`owner_state_invalidation_requiring_restriction`)**;
`mode_session_ref` (required);
**`mode_boundary_ref` (required — the accepted local user/app session
boundary)**; **`mode_runtime_epoch_id`** (required),
**`base_mode_generation`** (required) and **`target_mode_generation`**
(required — §7B); **for `open`: `trusted_surface_ref` (required),
`trusted_app_session_ref` (required), and
`device_or_keystore_boundary_ref` (required where applicable) — the
references that make the trusted-origin check PERFORMABLE, not merely
asserted; exact final implementation names remain open**;
`state` (required; **live-state until terminal**; controlled — **exactly
these seven, and no others**: `requested` | `intent_committed` |
`gate_pending` | `committed` | `blocked` | `failed` | `absorbed`);
**`terminal_reason`** (required when `failed`; controlled includes
**`restart_interrupted`**, **`crash_interrupted`**, `gate_refused`,
`untrusted_surface`, `sacl_unsafe`, `durable_write_failed`,
`epoch_mismatch`, `stale_generation`); `audit_event_refs` (required).
**Exactly one terminal parent record per logical operation**; stages and
retries are append-only child events. **Restart meaning: a non-terminal
operation becomes `failed` with `restart_interrupted` — the undeclared
value `interrupted` is NEVER used.**

**3. `personal_mode_transition_event` [proposed]** — **append-only
history** of committed transitions. Fields: `transition_event_id`;
`mode_session_ref`; **`operation_ref` (required)**;
**`mode_boundary_ref` (required)**; `from_state`, `to_state` (required);
`basis_ref` (required); **`mode_runtime_epoch_id`** and
**`reserved_target_mode_generation`** (required — **NOT a committed
generation: this event is flushed at §5A step 8, while the commit happens
at step 9**); `at`.

**What this event means, precisely:** it **truthfully records that
RUNTIME ACTIVATION OCCURRED under that reserved target**. **It does NOT
commit the operation or the generation, and it grants NO authority.**
**The later operation/target commit (§5A step 9) MUST reference this
successfully flushed opened event.** **Only after that commit** may the
session use the target as its **`current_committed_mode_generation`**,
and **only after that commit** may the delivery fence carry and release
under the **committed** target (§12A). **Append-only; history only. It is not authority: no
live access is ever derived from it** (§7, §10 boundary 4).

**4. `personal_mode_factor_binding` [proposed]** — **binds the explicit
intent and the accepted ordinary-gate proof to one operation, session,
runtime epoch, and RESERVED target generation.** Fields: `binding_id`;
`operation_ref` (required); `mode_session_ref`;
**`mode_runtime_epoch_id` (required)** and
**`reserved_target_mode_generation` (required — the OPEN operation's
reserved target; the binding is created BEFORE any commit and references
the already-existing snapshot of §5A step 3. There is NO generic
`mode_generation` field here)**; `explicit_action_ref` (required);
**`mode_boundary_ref`, `trusted_surface_ref`, `trusted_app_session_ref`,
and `device_or_keystore_boundary_ref` (where applicable) — all REQUIRED,
because the binding must PROVE (not merely assert) that its PIN or BAI
result belongs to the same operation, mode session, mode boundary,
trusted app/session, device boundary, epoch, generation, and purpose. A
result that cannot be tied to every one of these is REJECTED (§17)**;
`gate_factor_kind` (required; controlled: **`pin` | `fingerprint`** —
**`voice` is NOT a permitted value**); `gate_result_ref` (required — **a
reference to the owner-held verification result; never raw material**);
**`bai_purpose`** (required when `fingerprint`; **exactly
`extended:personal_mode_open:<personal_mode_open_operation_id>`**);
**`bai_proof_consumption_ref`** (required when `fingerprint` — BAI's
durable audit record of the **single** consumption);
`sacl_snapshot_ref` + `sacl_freshness_state` (required); `at`.
**Append-only.** **A factor result belonging to another session,
purpose, device boundary, epoch, or generation is REJECTED** (§17).
**Never stores raw PIN, template, or voice biometric.**

**5. `personal_mode_effective_access_snapshot` [proposed]** — **the
computed §4 intersection, bound to ONE exact SACL truth; the fence handed
to B-INT-6.** Fields: `snapshot_id`; `mode_session_ref`;
**`mode_boundary_ref`**; **`mode_runtime_epoch_id`** (required) and
**`created_under_reserved_target_mode_generation`** (required — **the
snapshot carries the RESERVED target BEFORE commitment; it does NOT carry
a committed generation, because none exists yet**); `mode_permission`
(required). **It grants NO authority by itself**, it is **append-only and
NEVER changed in place**, and it **becomes the session's CURRENT
effective-access snapshot only because the successful target-generation
commit references it** (§5A step 9). **It becomes stale the moment SACL
or observability owner state changes** (below).

**The atomic SACL binding — every stream fact below is DERIVED FROM ONE
COMMITTED MOMENT, never assembled from separate reads:**
- **`sacl_session_state_ref` (REQUIRED)** — the owner-held
  **`SACL_session_state`** itself (Master §25.4), and
  **`sacl_state_version_or_event_ref` (REQUIRED)** — its committed
  version / event identity.
- **`sacl_last_sia_event_id`** and **`sacl_last_audit_event_id`**
  (required) — **the SIA/SACL event identity establishing freshness.**
- **`active_stream_set_identity`** (required) — the identity of the
  **`stream_authorization_set`** as of that state.
- **`stream_entries`** (required) — one per relied-on active stream,
  **taken from that same state**: `stream_id`, `person_box_id`,
  `stream_access_level` (`top_security` | `recognized_ness` |
  `known_person` | `guest`), `stream_access_level_since`, **`pbr_version`**,
  **`ness_presence_satisfied`**, and `active_disqualifiers`.
- **`primary_addressed_stream_ref`** (required).
- **`ness_stream_authorization_ref`** (required where Ness-private use is
  contemplated).
- **`shared_output_level`** and **`shared_output_level_since`**
  (required) — **taken from that exact SACL-owned state (the minimum
  across all active streams). B-INT-5 NEVER recomputes or overrides
  SACL's own level.**
- **`pbr_version_refs`** (required where a known person is involved).

**Channel observability — owner-held, never self-declared:**
**`output_channel_ref`** (required), **`observability_classification_ref`**
(required), **`observability_owner`** (required), and
**`observability_version_or_event_ref`** (required — the owner's own
version/event identity, so a change to it is DETECTABLE and invalidates
this snapshot). **The PMA CANNOT
turn a shared path into a private path by writing a field** — the
classification is the owner's, and an individual stream's level may be
used **only where SACL already permits a genuinely private, unobservable
path**. **Shared or observable output uses `shared_output_level`**, and
**all active streams must be represented or covered by the authoritative
state reference whenever output is shared or observable.**

**Step-up / top-security owner set (§12, record 7):**
`stepup_owner_reference_set` (optional) — **owner references, never
copied authority.**

`effective_ceiling` (required — the most restrictive result);
`computed_at`. **Append-only.**

**THE INVALIDATION RULE — simple and complete:** **ANY change to the
relied-on owner-held SACL state version, OR to the channel-observability
version, invalidates this snapshot.** No exceptions, and no need to
enumerate before acting. The change set includes, at minimum: **any new
SIA/SACL assessment superseding the relied-on assessment**; a
**freshness or stale-state change**; an **access upgrade or downgrade**;
an **active-disqualifier change**; a **stream join** or **departure**; a
**speaker change**; an **active-stream-set change**; a
**`primary_addressed_stream` change**; a **`shared_output_level`
change**; a **PBR version or category change**; a **Ness-presence
satisfaction change**; a **Gate 0, Gate 1, Gate 2, or Gate 3 result
change**; an **output-channel change**; an **observability-classification
change**; an **observability-owner version/event change**; and a
**step-up or lease-owner change affecting effective access**.

**Each invalidation ADVANCES the PMA generation (whenever it changes
effective access or makes the old delivery fence unsafe) and CANCELS
stale delivery** (§7B). **A single cached level NEVER replaces the
current SACL-owned stream set.** **B-INT-5 never recomputes SACL's result
and never declares channel observability itself.** **It records §7Q's
applicability but never decides §7Q eligibility** (§13). **Never reused
across an epoch.**

**6. `personal_mode_recovery_event` [proposed]** — **recovery as one
recorded, append-only history event.** Fields: `recovery_operation_id`;
`recovered_operation_ref` / `recovered_session_ref`;
**`mode_boundary_ref`** (required); **the COMPLETE four-field fence:
`prior_mode_runtime_epoch_id` and `prior_mode_generation` (PROVENANCE
ONLY — they describe the dead runtime and grant nothing), and
`new_mode_runtime_epoch_id` and `new_mode_generation` (the FRESH Dry
runtime)** — **no old generation ever transfers into the new epoch, and
the old pair can never be revived**;
`crash_boundary` (required; **controlled — exactly these fourteen
values**: `1` | `2` | `3` | `4a` | `4b` | `4c` | `4d` | `4e` | `5` | `6` |
`7` | `8` | `9` | `10`);
`committed_truth_found` (required); `action_taken` (required;
controlled: **`closed_for_restart`** | **`blocked_fail_closed`** |
`absorbed_duplicate`); `at`. **Append-only history — NOT another
operation authority, never evidence weight, and never a source of live
access.**

**7. `personal_mode_stepup_link` [proposed]** — **a REFERENCE/HISTORY
observation of the separately owned step-up / top-security authority. It
is NOT a second live authority.** Fields: `stepup_link_id`;
`mode_session_ref`; `mode_boundary_ref`; **`mode_runtime_epoch_id`** and
**`observed_under_committed_mode_generation`** (required); `purpose`
(required); **`observed_at`** (required).

**The COMPLETE owner-reference set — top-security needs BOTH truths, so
a single `authority_ref` cannot represent it:**
- **`bai_lease_ref` (required for top-security)** — the **actual BAI
  lease**, owned by BAI;
- **`sacl_gate1_decision_ref` (required for top-security)** — the
  **current SACL Gate 1 decision**, owned by SACL;
- **`authority_state_event_refs` (required)** — the owners' own events;
- **`observed_authority_state` (required)** — **an OBSERVATION, never
  authoritative**; controlled: **`requested` | `observed_active` |
  `observed_expired` | `observed_revoked` | `observed_refused`**;
- **for a non-top-security step-up type:** its **own exact accepted owner
  set**, carried the same way — **no new authority is invented.**

**Binding rules:** **both owner truths must be CURRENT and MUTUALLY
COMPATIBLE at use time** — a lease without a current Gate 1 decision, or
a Gate 1 decision without a live lease, **grants nothing**. **No copied
`observed_active` value grants access.** **The effective-access snapshot
references the complete owner set (record 5), never copied authority.**
**Expiry, revocation, restart, a SACL downgrade, or an owner failure wins
IMMEDIATELY.** **The indicator verifies both owner truths and can never
rely on an observation alone** (§15). **Changes are append-only
observations — they never rewrite a second live authority.**

**8. `personal_mode_activation_ready_event` [proposed]** — **the durable
PREPARATION receipt. It grants NO authority and does NOT mean the mode is
open.** Fields: `activation_ready_event_id` (required);
`open_operation_ref` (required); `mode_session_ref` and
`mode_boundary_ref` (required); `trusted_surface_ref`,
`trusted_app_session_ref`, `device_or_keystore_boundary_ref` (required
where applicable); **`mode_runtime_epoch_id`** (required);
**`base_mode_generation`** and **the operation's RESERVED
`target_mode_generation`** (required — **referenced, NOT committed**);
`factor_binding_ref` (required — **which already links the
already-existing snapshot, §5A steps 3–4**); **`sacl_session_state_ref` +
`sacl_state_version_or_event_ref`** (required — the exact atomic SACL
truth); **`observability_classification_ref` +
`observability_version_or_event_ref`** (required);
`effective_access_snapshot_ref` (required); `created_at` and
**`flushed_at`** (required); `result` (required; **controlled: exactly
one value — `activation_ready`** — **it can say nothing else, and
explicitly cannot say "open"**). **Idempotency meaning:** one per open
operation; a replay is absorbed and **never re-opens anything**.
**Restart meaning: it does NOT survive as authority — a new epoch begins
Dry, and this event remains preparation history only.** **Append-only
preparation history, never live authority. It states only that ALL
PERMISSION CHECKS PASSED.**

**9. `mode_authority_dependency_ref` [proposed]** — **the record that
makes the dependency boundary ENFORCEABLE.** Fields:
`dependency_ref_id` (required); **`dependent_operation_ref`** (required);
**`operation_owner`** (required); **`purpose`** (required);
**`depends_on_interactive_personal_mode`** (required; boolean — **the
whole point: an operation either depends on the interactive Personal Mode
session or it does not**); `mode_session_ref` and `mode_boundary_ref`
(required when dependent); **`mode_runtime_epoch_id`** and **the
committed generation** (required when dependent);
`effective_access_snapshot_ref` (required when dependent);
`cancellation_signal_ref` (optional); **`output_delivery_path_ref`**
(required); `dependency_state` (required; live-state; controlled:
`active` | `cancelled` | `completed` | `independent`);
`correction_or_supersession_ref` (optional); `at`. **Restart meaning: a
dependent interactive operation dies with its epoch; an INDEPENDENT
operation's fate belongs to ITS OWNER (§9A).**
**Rules:** **every interactive retrieval, reasoning, output, or step-up
operation whose permission depends on Personal Mode MUST carry this
dependency**; **close, suspend, downgrade, and restart cancel ONLY
matching dependent operations**; **cancellation is never applied to
unrelated operations merely because they existed during the same
conversation**; **an independently authorized background operation carries
its OWN authority references rather than pretending to depend on Personal
Mode**; **its owner — not the PMA — decides its continuation, retry,
recovery, timeout, and revocation**; **a real security event may still be
delivered to its authority owner for THAT OWNER's decision**; and
**nothing produced by background work may enter a closed, stale, or
downgraded interactive delivery path.**

## 12A. THE RETRIEVAL/DELIVERY FENCE CONTRACT [PROPOSED]

**`personal_mode_delivery_fence` [proposed]** — the object B-INT-5
supplies to B-INT-6 (**without completing B-INT-6**). **The PMA OWNS the
live fence.**

**Fields:** `fence_ref` (required); `mode_session_ref` and
`mode_boundary_ref` (required); **`mode_runtime_epoch_id`** (required);
**`committed_target_mode_generation`** (required); **`state`** (required;
**controlled: `closed` | `released`**); **`fence_state_version`**
(required — monotonic within the epoch, so a stale writer is detectable);
**`idempotency_key`** (required — **scope: `mode_boundary_ref` + epoch +
`committed_target_mode_generation` + the requested state**);
**`release_operation_ref`** (required when `released` — **the
successfully committed open operation**);
**`restrictive_close_operation_ref`** (required when closed by a
restriction — the close / suspend / downgrade / invalidation operation);
**`last_authoritative_state_change_ref`** (required — the last change the
**PMA** actually committed); `at`.

**Rules, binding:**
- **The PMA owns the live fence** — no other component sets it.
- **Every new runtime epoch BEGINS CLOSED.**
- **No released fence is ever restored from history** — a durable record
  never re-releases anything.
- **A repeated identical release is ABSORBED** (idempotency key) — and
  **two releases can never create two live fences.**
- **Only the successfully committed open operation may release it** (§5A
  step 10).
- **Closing an already-closed fence is IDEMPOTENT.**
- **A newer restrictive close DEFEATS every older release.**
- **Old-epoch or old-generation releases are REJECTED** outright.
- **Audit records describe fence changes but NEVER grant or reopen
  access.**
- **Restriction applies IMMEDIATELY, even if its audit event must be
  written later** — the fence closes first; the record follows.

## 12B. OWNER-TRUTH REVALIDATION SEAMS

**The exact `sacl_session_state_ref` (+ version/event) and the
`observability_classification_ref` (+ version/event) must STILL MATCH
CURRENT OWNER TRUTH at each of these seams:**

1. **before `activation_ready` is written;**
2. **immediately before runtime activation;**
3. **before the opened event is flushed;**
4. **before the retrieval/delivery fence is released;**
5. **at each later retrieval or output operation under B-INT-6.**

**If either owner reference changed:** **the old snapshot is stale**;
**the open or delivery attempt CANNOT proceed**; **a restrictive
generation wins**; **stale output is cancelled**; and **B-INT-5 never
recomputes SACL's result and never declares channel observability
itself.** **After activation, an owner-version change ADVANCES the PMA
generation whenever it changes effective access or makes the old delivery
fence unsafe.**

## 13. RETRIEVAL AND OUTPUT HANDOFF (THE B-INT-6 BOUNDARY)

**B-INT-5 supplies to retrieval/output coordination — and stops there:**

- the **current mode-session reference**;
- the **committed mode state**;
- **the `mode_runtime_epoch_id` and the `current_committed_mode_generation`**;
- the **current effective access ceiling**;
- **the complete current SACL multi-speaker shape** (never one cached
  level): the **addressed stream identity**
  (`primary_addressed_stream`); the **current Ness-stream authorization
  reference**; the **per-stream access levels needed for the
  operation**; the **current `shared_output_level`** (the **minimum
  across active streams**); **whether the output channel is
  shared/observable or genuinely private and unobservable**; the **PBR
  references and category limits**; the **Ness-presence requirement**
  where applicable; and the **SACL assessment identity and freshness for
  EVERY relied-on stream**;
- the **current step-up / top-security OWNER reference** where required
  (**never a copied authority** — §12, record 7);
- an **access-reduction cancellation signal** (epoch- and
  generation-bound);
- a **do-not-deliver fence tied to the current epoch AND the committed
  target generation**, carrying the **`mode_boundary_ref`**;
- the **`sacl_session_state_ref` + state version/event reference** — **the
  ONE committed SACL truth every stream fact came from** (§12, record 5);
- the **owner-held channel-observability references**
  (`output_channel_ref`, `observability_classification_ref`,
  `observability_owner`) — **the PMA cannot declare a path private**;
- the **complete step-up owner set** where required
  (**`bai_lease_ref` AND `sacl_gate1_decision_ref`**) — **owner
  references, never copied authority**;
- the **`mode_authority_dependency_ref` scope** — **which operations this
  mode session's cancellation actually governs (§9A): separately
  authorized background work is NOT cancelled, though nothing it produces
  may be delivered through the closed or downgraded interactive path.**

**Output-path rules, supplied as boundaries:**

- **Shared or observable output uses `shared_output_level`.**
- **An individual stream's level may be used ONLY where SACL already
  permits a genuinely private, unobservable output path.**
- **Personal Mode NEVER turns a shared output path into a private one.**
- **A single cached level must never replace the current SACL-owned
  stream set.**

**And B-INT-5 states, without completing B-INT-6:**

- **Dry Mode prevents personal retrieval except where §9 explicitly
  allows otherwise** (its accepted exceptions, including the exact-quote
  exception for Ness's own original words, apply exactly as §9 states
  them);
- **Personal Mode does not itself decide §7Q privacy eligibility;**
- **SACL does not itself decide §7Q privacy eligibility;**
- **the §7Q-first / SACL-second delivery sequence remains B-INT-6's
  separate package — it is NOT completed here;**
- **any access reduction invalidates in-progress output above the new
  ceiling before delivery;**
- **output formed under an older epoch or generation cannot be delivered
  under a newer or more restrictive state.**

## 14. TEMPORARY STEP-UP AND TOP-SECURITY — CONNECTION ONLY

- **Personal Mode may request a separate step-up operation.**
- **The step-up uses the accepted strongest-factor and §25/BAI rules** —
  including SACL **Gate 1**'s complete conditions for top-security
  (biometric verified within timeout; Ness's Person-Box at high
  certainty; sufficient score separation; **no spoofing suspicion**;
  **no `imitation_risk` flag**; no active disqualifiers) — **all
  consumed, none redesigned.**
- **Its authority is purpose-bound, session-bound, time-bounded, and
  revocable according to its accepted owner.**
- **The step-up never rewrites the underlying Personal Mode session**,
  and **B-INT-5 creates NO second step-up authority**: its
  `personal_mode_stepup_link` is a **reference/history observation only**
  (§12, record 7). **Top-security requires BOTH owner truths — the actual
  `bai_lease_ref` AND the current `sacl_gate1_decision_ref` — and BOTH
  must be current and mutually compatible AT USE TIME.** **A stale
  `observed_active` never defeats expiry, revocation, restart, a SACL
  downgrade, or an owner failure.** **Attaching or removing a step-up
  advances the generation whenever it changes effective access** (§7B).
- **When step-up ends, effective access falls back to the still-valid
  Personal Mode / SACL / §7Q intersection.**
- **If Personal Mode or identity access is also lost, access falls to
  the more restrictive state.**
- **Step-up success cannot be reused to silently open a future Personal
  Mode session.**
- **No exact timeout, threshold, biometric algorithm, or BAI token
  purpose is invented here.**

## 15. INTERFACE INDICATORS — SEMANTIC STATES ONLY

**Required semantic states:** **Dry**; **Personal Mode opening**;
**Personal Mode active**; **Personal Mode suspended/restricted**;
**step-up / top-security active**; **closing / closed**; **error or
unverifiable state**.

**The indicator:** **reflects committed state only**; **never grants
authority**; **never relies on the step-up link alone** — a step-up /
top-security indication requires the **owner-verified** current lease
and Gate 1 result (§12, record 7); **never changes before the underlying
restrictive transition commits**; **must not expose private content or reveal that
hidden content exists**; **must be understandable in plain language**;
and **must remain accurate after downgrade, close, crash, or restart**.

**Left open for later interface work:** exact label text, icon, color,
placement, animation, and command/button wording.

## 16. FULL-TRANSPARENCY LOGGING (§0B / B-INT-11)

**One real operation → exactly one operational record.** Stages,
retries, and recovery actions are **append-only child events** under
their parent operation — never second parent truths.

| Operation | The one record |
|---|---|
| Personal Mode open requested | `personal_mode_operation` (`open`, `requested`) |
| Explicit opening intent committed | operation → `intent_committed` + stage event |
| Ordinary factor requested | stage event (`gate_pending`) |
| Ordinary factor accepted / refused | `personal_mode_factor_binding` (accepted) **or** operation → `blocked` (refused) |
| SACL snapshot used | `personal_mode_effective_access_snapshot` (referencing SACL's own assessment — **never duplicating it**) |
| Permission checks passed (**not yet open**) | **`personal_mode_activation_ready_event`** (§12, record 8) — its `result` can say **only `activation_ready`**; **it grants no authority and never claims the mode is open** |
| Mode opened (**after runtime activation actually occurred**) | `personal_mode_transition_event` (`personal_opening` → `personal_active`), appended **after** activation and **before** the retrieval fence opens |
| Retrieval/delivery fence released | `personal_mode_delivery_fence` → `released` (§12A) — **only the successfully committed open operation may do this** |
| Fence closed by restriction | `personal_mode_delivery_fence` → `closed` — **committed BEFORE any stale output may deliver, even if logging then fails** |
| Opening blocked | operation → `blocked` + transition event (→ `dry`) |
| Personal Mode suspended | transition event (→ `personal_suspended`) |
| Access reduced | new `..._effective_access_snapshot` (lower ceiling) |
| In-progress work discarded | discard event under the **operation that formed it** (no content, references only) |
| Mode resumed after fresh access recovery | transition event (`personal_suspended` → `personal_active`) with the **freshly verified** SACL reference |
| Explicit close requested | `personal_mode_operation` (`close`) |
| Mode closed | transition event (→ `personal_closed`/`dry`) |
| Step-up requested | `personal_mode_operation` (`step_up_request`) + `personal_mode_stepup_link` |
| Step-up accepted / refused | **the AUTHORITATIVE change happens in BAI/SACL** (their lease / Gate 1 decision and their own events); B-INT-5 appends an **observation** with the exact value **`observed_active`** or **`observed_refused`** |
| Step-up expired / revoked | **BAI/SACL own the change**; B-INT-5 appends the observation **`observed_expired`** or **`observed_revoked`** — **an observation never changes an authority** |
| Ordinary factor accepted via §5B fingerprint | `personal_mode_factor_binding` with the **exact `extended:personal_mode_open:<id>` purpose** + BAI's own durable consumption record (**referenced, never duplicated**) |
| Crash / restart recovery | `personal_mode_recovery_event` (**`closed_for_restart` / `blocked_fail_closed`**; the operation itself goes **`failed` + `restart_interrupted`/`crash_interrupted`** — **never `interrupted`**) |
| Stale operation rejected | rejection event under the operation (**epoch mismatch or older generation within the epoch**) |
| Duplicate absorbed | duplicate-absorbed event (**no second parent truth, no evidence weight**) |
| Indicator changed | indicator event (after the committed transition only) |
| Fail-closed halt | operation → `blocked`/`failed` + its stage event |

**Every record carries the runtime epoch and the exact generation field
appropriate to its stage: base, reserved target, committed target, prior,
or new-restart generation.**

**Log rules, binding:** logs **carry references, not secrets or private
payloads**; they **obey §7Q and §25**; they **add no evidence weight**;
**no record logs "the log was logged"** as a new real operation; all are
**append-only**; and **no log ever becomes current access authority
merely because it persists.**

## 17. FAIL-CLOSED REQUIREMENTS

**Stop, suspend, close, or reduce access safely** when: **explicit
opening intent is absent or ambiguous**; **the request comes from an
untrusted surface**; **the normal gate is missing, failed, stale,
conflicting, or unverifiable**; **voice is the only offered factor**;
**current SACL state is unavailable, stale, conflicting, suspicious, or
lower than required**; **§7Q authorization cannot be determined**; **the
current mode epoch or generation is unknown or mismatched**; **a
transition record conflicts with live state**; **a required durable
record cannot be written and flushed** (§5A); **runtime state and its
required audit record cannot be reconciled**; **an open races with a
close**; **an upgrade races with a downgrade**; **a factor result belongs
to another session, purpose, device boundary, epoch, or generation**;
**a BAI proof carries any purpose other than the exact
`extended:personal_mode_open:<open_operation_id>`**; **a factor result
cannot be tied by reference to the operation, mode session,
`mode_boundary_ref`, trusted surface/app session, device boundary, epoch,
generation, and purpose**; **a base generation is no longer current**;
**the SACL facts cannot be bound to ONE committed `SACL_session_state`
(or its version/event reference is missing)**; **channel observability
cannot be established from its owner**; **a required durable
`activation_ready` or transition record cannot be flushed** (§5A);
**top-security lacks EITHER the current BAI lease OR the current SACL
Gate 1 decision, or the two are mutually incompatible**; **restart or crash
status is uncertain**; **a step-up or top-security lease is absent,
expired, revoked, wrong-purpose, or unverifiable at use time**;
**required audit history cannot be written**; or **any authority owner
REQUIRED FOR THE CURRENT OPERATION is unavailable** — **an unrelated BAI
outage must NOT block a PIN-only ordinary opening, while BAI
unavailability MUST block any fingerprint or top-security path that
requires BAI.**

**Never treat unknown as success. Never deliver output first and
correct the access state afterward.**

## 18. MUST-NEVERS

B-INT-5 must never: merge §9 and §25 into one authority; let
recognition silently open Personal Mode; let voice alone open Personal
Mode; let a factor event from another purpose open Personal Mode; make
`recognized_ness` a universally mandatory opening factor; declare PIN,
voice, fingerprint, or any single factor universally sufficient;
displace the settled factor hierarchy; let Personal Mode unlock
top-security; let fingerprint alone restore top-security under
unresolved identity; allow mode state to widen SACL or §7Q permission;
allow SACL to widen §7Q permission; restore Personal Mode automatically
after restart; resume or replay discarded private output; treat durable
logs as live access authority; retain raw PIN or biometric material;
expose private content in errors, indicators, or logs; destroy durable
memory when closing mode; **accept a BAI artifact of any other purpose
as a Personal-Mode opening proof, or let a Personal-Mode opening proof
unlock top-security; forward-complete or restore Personal Mode from a
consumed token after a crash; treat the step-up link's observed state as
authority; assign the undeclared operation state `interrupted`; reuse a
generation number across epochs; replace the current SACL stream set with
a single cached level; **write a durable event claiming a state that
never existed; declare a channel private by writing a field rather than
reading its owner's classification; enforce the one-live-session rule
against a freshly minted session id instead of the `mode_boundary_ref`;
grant top-security from a lease without a current Gate 1 decision (or
the reverse); or cancel separately authorized background work merely
because Personal Mode closed (§9A);** complete B-INT-6, B-INT-7, or B-INT-8; claim
CY-I or Bundle 5 complete; edit or integrate the Map or Master; or begin
implementation.

## 19. EXPLICITLY OPEN AFTER THIS CANDIDATE

ChatGPT's independent audit; any real correction it finds; Ness's later
acceptance; accepted-source placement and a closure receipt; the **exact
PIN implementation**; the **exact fingerprint implementation**; the
**exact trusted-device/app mechanism**; **exact timeout and inactivity
durations**; **exact retry/attempt counts** (accepted B9 owns retry
classification; **no value is invented here**); **exact UI wording and
visual design**; **exact serialization and technology**; **B-INT-6**;
**B-INT-7**; **B-INT-8**; **CY-I consolidation**; **Bundle 5 final
consistency review and closure**; later versioned **Map/Master
integration**; and **all code, databases, schemas, migrations, tests,
runtime work, and live-disk changes.**

## 20. DRAFTING CHECKS (NOT INDEPENDENT CERTIFICATION)

These are the drafter's own consistency checks — **not independent
verification, not certification, not proof of enforcement**:

- **A26 preserved exactly** — all six points carried verbatim in §3;
  recognition ≠ opening; explicit opening required; §7Q unchanged
  inside authenticated Personal Mode; Personal Mode ≠ top-security;
  uncertainty reduces access — consistent in drafting.
- **§9 and §25 kept separate** — two layers, one intersection, neither
  widening the other (§4) — consistent in drafting.
- **The settled factor hierarchy preserved** — PIN the ordinary gate;
  fingerprint strongest and may satisfy it where permitted; voice
  convenience-only (§6) — consistent in drafting.
- **Both explicit intent AND an accepted ordinary gate are required**
  (§5, §6, §7) — consistent in drafting.
- **Recognition is neither mandatory nor sufficient by itself** (§6) —
  consistent in drafting.
- **Voice stays convenience-only and never a hard lockout** (§6) —
  consistent in drafting.
- **SACL preserved as the continuous access ceiling** — its Gates 0–3
  and four levels consumed, not redesigned (§4, §6, §14) — consistent
  in drafting.
- **§7Q preserved as a separate privacy authority** — mode and SACL
  decide none of it (§4, §13) — consistent in drafting.
- **Top-security preserved as a separate gate** — Gate 1's complete
  conditions plus the BAI lease; never granted by mode (§6, §14) —
  consistent in drafting.
- **Fails closed on uncertainty** (§8, §17) — consistent in drafting.
- **In-progress private work discarded before output on reduction**
  (§8, §13) — consistent in drafting.
- **Resets to Dry after restart**, with nothing reconstructed and no log
  granting authority (§10) — consistent in drafting.
- **The generation fence is fully implemented, not just declared** — the
  PMA is the **sole allocator**; every access-affecting operation carries
  `base_mode_generation` + `target_mode_generation` + the epoch; a
  transition commits **only if its base is still current**; **one target
  generation has one winning result**; **close/downgrade advance the
  restrictive fence before stale permissive work may deliver**; upgrades
  and resumes cannot commit after a newer restriction; and the recovery
  record carries the **complete four-field prior/new pair**, with the old
  pair **provenance only** (§7B, §12 records 2 and 6) — consistent in
  drafting.
- **Duplicate and trusted-boundary checks are RECORDABLE, not merely
  asserted** — `mode_boundary_ref` runs through the session, every
  operation, factor bindings, snapshots, recovery events, and delivery
  fences; **the one-live-session rule binds to the BOUNDARY, not a fresh
  session id**; every operation carries a required `idempotency_key`; and
  open operations and bindings carry `trusted_surface_ref`,
  `trusted_app_session_ref`, and `device_or_keystore_boundary_ref` so the
  cross-device/session rejection can actually be performed (§12 records
  1, 2, 4; §11, §17) — consistent in drafting.
- **The SACL handoff is bound to ONE committed SACL truth** — the
  snapshot references the owner-held `SACL_session_state` with its
  version/event identity, `last_sia_event_id`, `last_audit_event_id`,
  active-stream-set identity, per-stream `pbr_version` and
  `ness_presence_satisfied`, and its `shared_output_level` **taken from
  that same state**; **B-INT-5 never recomputes or overrides SACL's
  level**; and stream joins/departures/speaker changes/addressed-stream
  changes/PBR changes/Ness-presence changes/downgrades **invalidate the
  snapshot, advance the generation, and cancel stale delivery** (§12
  record 5, §13) — consistent in drafting.
- **Channel observability is owner-held** — `output_channel_ref`,
  `observability_classification_ref`, `observability_owner`: **the PMA
  cannot turn a shared path private by writing a field** (§12 record 5,
  §13) — consistent in drafting.
- **Activation records are truthful** — `activation_ready` says only that
  the checks passed; the `personal_active` event is appended **after
  runtime activation actually occurred**, with the retrieval fence still
  closed until it flushes; **no durable event claims a state that never
  existed**; and a **restrictive transition never waits in a permissive
  state because logging failed** (§5A, §10, §16) — consistent in
  drafting.
- **The step-up model is complete and non-authoritative** — top-security
  carries **both** `bai_lease_ref` **and** `sacl_gate1_decision_ref`,
  both **current and mutually compatible at use time**; the logging table
  uses the **exact observation values** and states that the authoritative
  change happened **in BAI/SACL**; expiry, revocation, restart, downgrade,
  or owner failure **wins immediately** (§12 record 7, §14, §15, §16) —
  consistent in drafting.
- **Separately authorized background work is protected** — per Master
  §25.4, background functions run under their own rules and **do not
  become guest-level merely because no active speaker stream is
  present**; B-INT-5's signals reach only the interactive session and
  operations carrying a `mode_authority_dependency_ref`, while **nothing
  a background operation produces may be delivered through the closed or
  downgraded interactive path**, and **Dry Mode is never reinterpreted as
  global blindness** (§9A, §8, §13) — consistent in drafting.
- **The stale fence is restart-safe** — `mode_runtime_epoch_id` (fresh,
  non-reused, per startup) **+** `mode_generation` (monotonic within the
  epoch) travel with every operation, record, snapshot, signal, formed
  output, and delivery fence; **any epoch mismatch or older in-epoch
  generation is discarded**; **no old output is delivered merely because
  a number matches in a new epoch** (§7A, §11, §12, §13) — consistent in
  drafting.
- **Crash terminal states are valid** — a non-terminal operation becomes
  **`failed`** with `restart_interrupted` / `crash_interrupted`; the
  undeclared `interrupted` is **never** assigned; the recovery event is
  **append-only history, not an authority** (§10, §12 records 2 and 6) —
  consistent in drafting.
- **The SACL multi-speaker shape is carried whole** — addressed stream,
  Ness-stream authorization, per-stream levels, `shared_output_level`
  (the minimum across active streams), channel observability, PBR refs
  and limits, Ness-presence, and per-stream assessment identity and
  freshness; **shared/observable output uses `shared_output_level`**, an
  individual level only where SACL already permits a genuinely private,
  unobservable path, and **Personal Mode never converts a shared path
  into a private one** (§12 record 5, §13) — consistent in drafting.
- **A lower ceiling is distinguished from a loss of safety** — only work
  **above** the new ceiling is discarded; the mode **stays
  `personal_active`** for top-security fallback, step-up expiry, and
  `imitation_risk` (which blocks Gate 1 only); it **suspends** only when
  Ness-private use is unsafe (§8) — consistent in drafting.
- **The fingerprint gate has a real purpose-bound proof** —
  `extended:personal_mode_open:<open_operation_id>` from Master §25.6's
  existing vocabulary, bound before the OS prompt, verified against
  purpose/requester/operation/session/epoch/generation/validity, consumed
  once; **no other-purpose artifact can open Personal Mode and this proof
  cannot unlock top-security**; a crash after consumption leaves the mode
  **Dry** (§5B, §6, §10 boundary 3, §12 record 4) — consistent in
  drafting.
- **No second step-up authority exists** — the link is
  reference/history only, its observed state never authoritative, and
  current access verifies the **actual** BAI lease and **current** SACL
  Gate 1 result (§12 record 7, §14, §15) — consistent in drafting.
- **ONE possible opening order, with no forward references** — intent →
  factor proof → **snapshot created under the RESERVED target** → binding
  (**linking an already-existing snapshot**) → `activation_ready` flushed
  → **owner recheck** → runtime activation with delivery closed → truthful
  opened event flushed → **operation and target commit (the snapshot
  becomes current-effective only because this commit references it)** →
  fence released → indicator → retrieval. **No claim survives that the
  snapshot carries a committed generation before the commit**, and **the
  binding never references a record that does not yet exist** (§5A, §12
  records 4, 5, 8) — consistent in drafting.
- **Every generation change has ONE parent operation** — including the new
  **`access_change`** type with its controlled `access_change_kind`; **no
  generation advances without a parent** carrying id, idempotency key,
  boundary, epoch, base, reserved target, one winning result, terminal
  status, and audit refs; generation fields are standardized per record
  (§7B, §12) — consistent in drafting.
- **Fence and recovery are complete** — the PMA owns the live fence; every
  new epoch begins **closed**; no released fence is restored from history;
  repeated releases are absorbed and **two releases cannot create two live
  fences**; closing is idempotent; **a newer restrictive close defeats
  every older release**; old-epoch/old-generation releases are rejected;
  **audit never grants or reopens access**; and **restriction applies
  immediately even if its audit event is written later**. The recovery
  record carries the **exact fourteen** `crash_boundary` values (§12A, §12
  record 6) — consistent in drafting.
- **The background restart boundary is honest** — closing/suspending/
  resetting Personal Mode is **not** authority to cancel independent
  background work; PMA restart cancels only **interactive** operations
  bound to the dead epoch; **B-INT-5 does not decide** whether independent
  work survives, retries, resumes, or fails — that belongs to its owner;
  and background results need a **current valid fence and current
  privacy/access checks** to reach a new interactive path (§9A, §12A) —
  consistent in drafting.
- **The activation order is truthful and stated identically everywhere**
  — durable intent → **factor proof → atomic SACL snapshot → factor
  binding** →
  **`activation_ready` flushed (which claims ONLY that the checks passed)**
  → **runtime activation WITH THE FENCE CLOSED** → **the opened event
  appended and flushed (only after activation truly occurred)** →
  operation `committed` → **fence released** → indicator → retrieval.
  **No durable event says the mode opened unless it did; no delivery
  happens merely because activation occurred** (§5, §5A, §7 table, §10
  seams 4a–4e, §12A) — consistent in drafting.
- **One operation → one base → one reserved target → ONE winning access
  result** — `personal_opening` prepares under the base (Dry, fences
  closed, target reserved but uncommitted); the target commits **exactly
  once**; `personal_closing` is restrictive cleanup **after** access is
  gone and **never recommits**; generation fields are standardized per
  stage (§7B) — consistent in drafting.
- **Uniqueness binds to the mode boundary, not the session id** — at most
  one live session per `mode_boundary_ref` per epoch, PMA-enforced; a
  duplicate cannot mint its way past it (§11, §12 record 1) — consistent
  in drafting.
- **Invalidation is complete and revalidation is explicit** — ANY change
  to the relied-on SACL state version or observability version
  invalidates the snapshot, advances the generation, and cancels stale
  delivery; owner truths are re-verified at all five seams (§12 record 5,
  §12B) — consistent in drafting.
- **The background boundary is enforceable and honest** —
  `mode_authority_dependency_ref` is a defined record; cancellation
  reaches only matching dependents; **B-INT-5 neither cancels
  independently authorized background work nor guarantees its survival
  across a real restart** — that belongs to its owner (§9A, §12 record 9)
  — consistent in drafting.
- **Stale and duplicate operations cannot reopen access** — the
  epoch+generation fence and the restrictive-wins rule (§11) —
  consistent in drafting.
- **Complete operation identities, crash boundaries, and logging**
  (§7, §10, §12, §16) — consistent in drafting.
- **B-INT-6 and all implementation left open** (§13, §19) — consistent
  in drafting.

---

*End of `NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
— `CANDIDATE — NOT ACCEPTED — NOT ADOPTED — NOT BUILT`, awaiting
ChatGPT's independent audit of this actual file and Ness's later
acceptance. N.H may know that it is Ness; only Ness opens his private
N.H — and even then, only what the ceiling, the privacy rules, and the
separate higher gate all permit. When certainty falls, the door closes
before a word escapes; when the machine restarts, it wakes up dry.*
