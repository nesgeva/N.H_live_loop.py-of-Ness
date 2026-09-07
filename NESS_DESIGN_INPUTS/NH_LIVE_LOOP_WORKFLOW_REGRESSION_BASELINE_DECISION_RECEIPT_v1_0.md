# N.H — Live-Loop Workflow Regression Baseline Decision Receipt v1.0

**Filename:** `NH_LIVE_LOOP_WORKFLOW_REGRESSION_BASELINE_DECISION_RECEIPT_v1_0.md`  
**Decision owner:** Ness  
**Decision date:** 2026-08-29  
**Record type:** append-only operational decision receipt and regression reference  
**Status:** NESS-ACCEPTED WORKFLOW BASELINE — LIVE LOOP FROZEN  
**Intended location:** `/home/ness/NH_CLAUDE_CODEX_DESIGN_LOOP/NESS_DESIGN_INPUTS/`  

## 1. Scope and authority boundary

This record preserves Ness's explicit decision to accept the currently proved
N.H live-loop workflow behavior as the regression baseline for future live-loop
repairs.

This record is **not** a new authority tier, does not adopt or accept any design
candidate, does not modify Master V10, the Design and Wiring Map, Decision
Defaults, `cursorrules`, the Companion, any accepted package, or any prior
record. It gives no implementation or package-continuation authorization. It
records an operational baseline only.

## 2. Exact authenticated freeze point

- Authenticated event sequence: `1545`
- Authenticated tail/event SHA-256:
  `1ea5cd5154ccb45c2b9c460205931eaa71e7180be1c2009ca46906345fab6912`
- Authenticated head-auth SHA-256:
  `d59e90edcde07383d4604889bf2772f50eea2ed7abba509e3b36aecd1867f669`
- Event-1545 type: `question_authority_audit_recorded`
- Event-1545 package: `A19`
- Event-1545 recorded controller identity:
  `6be9a04f4d3266a204aaeb78e9014b457c4a1a2dbfbdd83ebfe86dafc496aedf`
- Installed controller executable identity at freeze:
  `a03de7533fb14d3cbf4de31f8ecf449b7ae2aa8b35035bff577b4015bc20c34a`
- Installed `controller/nh_loop.py` SHA-256:
  `744eef776ffb7872c4e06cee8d659ba0633ec3d774d9f061577db92f7548750d`
- Installed source-state currentness projection: `false`

The different event-recorded and installed controller identities, and the
`false` source-currentness projection, are preserved as facts. This receipt
does not claim that event 1545 authenticated later installed bytes. It binds
both the proved journal frontier and the exact installed file baseline without
conflating them.

## 3. Frozen operational truth

- Loop state: `LOOP_NEEDS_NESS_DECISION`
- Loop detail: the proved frontier is a genuine Ness question; independent
  question validation and coverage are current, so the automatic loop stops
  rather than launching another provider call.
- Loop next command: `null`
- Loop transition working: `false`
- Supervisor workflow state: `ACCEPTED_FOR_DESIGN_ONLY`
- Supervisor next command: `null`
- Open provider request count: `0`
- Open result custody count: `0`
- Lease state: `ABSENT_PROVED`
- Lease live proved: `false`
- Worker running: `no`
- Claude/Codex provider running: `no`
- Existing maintenance pause: requested and active
- Ness question answered by this freeze: `no`
- Next package started by this freeze: `no`

The maintenance pause is the existing N.H scheduling gate. This receipt did not
append an interview-journal event, acquire a lease, run a worker, launch a
provider, answer a question, or start a package.

## 4. Ness-accepted workflow behavior

The regression baseline is:

1. N.H performs mechanically executable work automatically.
2. Claude may perform authorized mechanical writing or fixes.
3. Codex independently validates or audits where the controller genuinely
   requires it.
4. Real mechanical bugs are diagnosed, fixed, tested, and resumed without
   making Ness solve technical work.
5. Saved provider work and authenticated history are preserved; provider work
   is not duplicated or conveniently rerun.
6. Retries remain bounded and owned.
7. Provider-free checks are used when a provider call is unnecessary.
8. Repeated or semantically equivalent concerns converge instead of creating
   endless validation/coverage cycles.
9. Settled Ness decisions are not reopened as new questions.
10. Duplicate questions, false choices, mechanics, implementation details, and
    already-settled matters are filtered before Ness is asked.
11. Every genuinely open Ness decision remains preserved.
12. At the genuine Ness-question boundary, automatic worker/provider activity
    stops and control returns to Ness.
13. N.H does not continue package-to-package after reaching that Ness boundary.
14. After Ness answers, only the work unlocked by those answers may continue
    through the same governed workflow.

## 5. Regression use

Future live-loop repairs must compare their behavior against this receipt. A
repair must not regress durable custody, no-duplicate dispatch, bounded retry,
provider-free convergence, filtering of settled or duplicate questions,
preservation of genuine open questions, or the stop-at-Ness-boundary behavior.

This receipt does not make the listed files immutable. It records their exact
freeze identities so later authorized changes can be compared honestly.

## 6. Protected live-loop file manifest

The manifest covers the installed controller, supervisor modules, worker,
launcher, read-only status projection, server, and browser assets that expose
the accepted behavior. The SHA-256 of the ordered `sha256sum` manifest itself is:

`e3a4832998cf4c07caa1fb9fbf8df2448e6dc96c2d672a7d179dc0956b3c3cab`

| File | SHA-256 |
|---|---|
| `controller/nh_loop.py` | `744eef776ffb7872c4e06cee8d659ba0633ec3d774d9f061577db92f7548750d` |
| `controller/nh_supervisor/__init__.py` | `dc384041332659dfbbdf70aa5fa91d4cd035677af187d7202cd6eb1f1326449b` |
| `controller/nh_supervisor/auditresult.py` | `eac748ec06e25baf280903dacb2f6e30ca891cf681b4c6bf4785378ec7b2de92` |
| `controller/nh_supervisor/canonical.py` | `4f4cad66fbfe57026848b08afffba1d55a779f14817493f3b62c13bbf3f29fa6` |
| `controller/nh_supervisor/capability.py` | `0ba770f9c2aad71922e6cdd777d7a82387631108d4611bbd934cd97f67e3e5e9` |
| `controller/nh_supervisor/classify.py` | `542f967139480f6024644c96c14295e54d8504017adfb6be9e11d46ada7aee4b` |
| `controller/nh_supervisor/commands.py` | `5ef4019359b22bec0933fd553d936da7b7fb6dece85c18934931c05d48560641` |
| `controller/nh_supervisor/constants.py` | `d989b32cf9681f3544acd4ea920e39221184022d4221aa56bd78bc657db491c0` |
| `controller/nh_supervisor/corrections.py` | `3f480faf2ac4ece33759361fd6e05654592741813ae97ae82ea1417bb358c107` |
| `controller/nh_supervisor/dependency.py` | `32dce1caaaabe040af0bac9d81b3496818527b60d5431bdae8ede9d41cbc8b7e` |
| `controller/nh_supervisor/engine.py` | `ea420a8709bcc3a3f9da7f69c1b19d628dcd06f93d44275b2c38c46f9d63cfc7` |
| `controller/nh_supervisor/feed.py` | `9142cb4a860ec26e20a68df0a640484322440cfc39882c2f316feb94cd376b63` |
| `controller/nh_supervisor/identity.py` | `62ced3a51032859707f6271732986ff3915f1b23e27acf332a5f9aa116e97072` |
| `controller/nh_supervisor/journal.py` | `b23967b6d6875f166229cc4539b801cd1fcae5f9504ada2a6a533b1ea9258cbe` |
| `controller/nh_supervisor/lease.py` | `073f7d28ce821fb04c13763bcf79f86029ce4e327a5555156c105f27d7217ce8` |
| `controller/nh_supervisor/provider.py` | `c51c7dddc1831c6f2ae965ab5b01d3796a0ba37b788a74084a17962b32b34c40` |
| `controller/nh_supervisor/replay.py` | `da12bddf8d1f8da60321a1c62a4aec771184d077f9bf4f37a33d525e5524e5e2` |
| `controller/nh_supervisor/runtime.py` | `7f20bd000eb91b4d489ce0f1a962c79493f23a134c6157ff53456b33d9326254` |
| `controller/nh_supervisor/scheduling.py` | `dd3f590b0730fe4e48fdefb6123b7ff10be10e62a5037809ce6f64bf1ba3d645` |
| `controller/nh_supervisor/schema.py` | `7a18d53376802f7d567465562ad9cc8234833bdfef5c3d1ca9c68797de069cb5` |
| `controller/nh_supervisor/status.py` | `805572f9f3fd3ff2b60a30b8417554e1b22202da731f36f6ac3b12c197642edf` |
| `interview_ui/production.py` | `7e1d1bbce973f9fce5555a9d9a90c1baefa090d149326fcb6697f4a38df69838` |
| `interview_ui/worker.py` | `dfe99be35be6dd9fad86b04f7db4a9ee3034d0a822a9b32653c85573f5aa956d` |
| `interview_ui/server.py` | `1c0a1c6a404581805a8c27b7d1e19e5817567f8e6014a4968ccff5b69ac4811a` |
| `interview_ui/progress_view.py` | `8be8648d5ea2fd4388bc5ddc3526f2c887fe269f08826781bb840f84c752ecdb` |
| `interview_ui/static/app.js` | `1aebf61085f7384f315f5bc8085071a14326715ba8b3379c556f9c80f5ae9f5a` |
| `interview_ui/static/index.html` | `fe4d04aab904f61660d38c591ae940f077f00ad533dc97603ab5cd53553f3fe0` |
| `interview_ui/static/styles.css` | `3ff65d231ce4e495fb5ea1ea3c82ac3237fdd5c6ed2f398f92151ac27ed2b904` |

## 7. Preservation statement

The authenticated journal remains frozen at event 1545. No source listed in
the manifest above was changed by creating this receipt. No authority, Map,
accepted package, prior decision input, package state, question answer, provider
custody, lease, or worker state was altered. This new versioned receipt is the
only authorized project-file addition made for the freeze.
