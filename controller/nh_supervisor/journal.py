#!/usr/bin/env python3
"""Section 4.1 -- the version-dependent authenticated journal format.

The format functions here are the production ones: ``nh_loop.py`` uses them for
its own installed interview journal, so the supported versions cannot drift and
no stored version-4 or version-5 byte is ever rewritten.

The validated version sequence is MONOTONIC: it may hold still or move forward,
and a later event carrying a LOWER version than one already validated is a
version rollback and is refused.

Two storage backends implement the same ``JournalGateway`` contract:

* ``NhLoopJournalGateway`` -- the installed authenticated interview journal.
  This is the production binding and the only one a real installation uses.
* ``DisposableFileJournal`` -- a bounded, anchored, locked, fsynced,
  HMAC-authenticated journal used ONLY inside a disposable rehearsal, and only
  when ``NH_SUPERVISOR_DISPOSABLE_JOURNAL=1`` is set.  It is never installed and
  is never authority for anything outside that rehearsal.
"""

from __future__ import annotations

import errno
import fcntl
import hmac
import hashlib
import json
import os
import stat

from . import constants
from .canonical import canonical_json, is_hex64, sha256_hex

INTERVIEW_AUTH_LABEL = "nh-interview-event-auth-v1"

ENVELOPE_KEYS = frozenset(
    (
        "journal_version",
        "event_seq",
        "prev_event_sha256",
        "event_sha256",
        "event_auth_sha256",
        "type",
    )
)


def event_digest(event):
    body = {key: value for key, value in event.items() if key != "event_sha256"}
    return sha256_hex(canonical_json(body))


def auth_material(event):
    """Version-dependent bound material.

    Each event's HMAC is taken over its OWN ``journal_version``.  Every existing
    record carries numeric 4 and the installed controller also authenticated it
    with numeric 4, so its HMAC input is exactly unchanged.
    """
    bound = {
        key: value
        for key, value in event.items()
        if key not in ("event_sha256", "event_auth_sha256")
    }
    return canonical_json(
        [INTERVIEW_AUTH_LABEL, event["journal_version"], bound]
    ).encode("utf-8")


def event_auth(key, event):
    if not key:
        return None
    return hmac.new(key, auth_material(event), hashlib.sha256).hexdigest()


def event_auth_ok(key, event):
    if not key:
        return False
    recorded = event.get("event_auth_sha256")
    if not is_hex64(recorded):
        return False
    return hmac.compare_digest(recorded, event_auth(key, event))


class JournalSchemaError(ValueError):
    """A version/type pair has no exact schema, or a body key set is wrong."""


def highest_journal_version(events):
    """The highest journal version among ``events``, or 0 when there is none.

    Non-integer and boolean versions are ignored here rather than compared:
    such an event fails closed on its own in ``validate_event``, and this
    helper must not raise before that refusal is reached.
    """
    versions = [
        event["journal_version"]
        for event in events
        if isinstance(event, dict)
        and isinstance(event.get("journal_version"), int)
        and not isinstance(event["journal_version"], bool)
    ]
    return max(versions, default=0)


def validate_event(event, index, previous_digest, body_key_table, auth_key=None,
                   highest_version_seen=0):
    """Structural, chain and authentication validation of ONE event.

    Returns the list of failure strings.  An unsupported version, a
    version/type pair with no exact schema, and a VERSION ROLLBACK each fail
    closed.

    ``highest_version_seen`` is the highest journal version already validated
    earlier in this same history (0 before the first event).  A validated
    version sequence may hold still or move forward, never back: 4 -> 4 -> 5 ->
    5 -> 6 -> 6 is valid, while 4 -> 5 -> 4, 4 -> 5 -> 6 -> 5 and 6 -> 4 are
    each refused.  The rule is stated once, over the versions themselves, so it
    stays true of every version this controller ever supports.  It does not
    require the first event to carry any particular version.
    """
    errors = []
    label = "journal record %d" % (index + 1)
    if not isinstance(event, dict):
        return ["%s is not a JSON object" % label]
    missing = sorted(ENVELOPE_KEYS - set(event))
    if missing:
        return ["%s is missing envelope keys: %s" % (label, ", ".join(missing))]

    version = event["journal_version"]
    if version not in constants.INTERVIEW_JOURNAL_SUPPORTED_VERSIONS:
        return ["%s carries unsupported journal version %r" % (label, version)]
    if version < highest_version_seen:
        return [
            "%s carries journal version %r after version %r was already "
            "validated: version rollback is refused"
            % (label, version, highest_version_seen)
        ]

    kind = event["type"]
    expected = body_key_table.get((version, kind))
    if expected is None:
        return [
            "%s has no schema for the pair (version %r, type %r)" % (label, version, kind)
        ]
    body_keys = set(event) - ENVELOPE_KEYS
    body_missing = sorted(expected - body_keys)
    body_extra = sorted(body_keys - expected)
    if body_missing:
        errors.append("%s is missing body keys: %s" % (label, ", ".join(body_missing)))
    if body_extra:
        errors.append("%s carries undefined body keys: %s" % (label, ", ".join(body_extra)))
    if errors:
        return errors

    if event["event_seq"] != index + 1:
        return ["%s carries the wrong event_seq" % label]
    if event["prev_event_sha256"] != previous_digest:
        return ["%s does not link to the previous event" % label]
    if not is_hex64(event["event_sha256"]) or event_digest(event) != event["event_sha256"]:
        return ["%s does not match its own recorded digest" % label]
    if not is_hex64(event["event_auth_sha256"]):
        return ["%s carries a malformed controller authentication" % label]
    if auth_key and not event_auth_ok(auth_key, event):
        return ["%s does not carry this controller's authentication" % label]
    return []


def upgrade_version4_candidate_event(event):
    """Map a version-4 candidate event in memory (Section 4.1).

    Stored version-4 bytes are never rewritten; this is the in-memory meaning.
    """
    from .identity import batch_triple

    if event.get("journal_version") != 4:
        return event
    if event.get("type") not in (
        "candidate_write_ahead_recorded",
        "candidate_write_ahead_aborted",
        "candidate_custody_recorded",
    ):
        return event
    lifetime = event.get("correction_round")
    mapped = dict(event)
    triple = batch_triple(lifetime)
    mapped["correction_round_lifetime"] = triple[0]
    mapped["correction_batch_number"] = triple[1]
    mapped["correction_round_in_batch"] = triple[2]
    return mapped


class JournalGateway:
    """The storage contract the engine is written against."""

    def read(self):
        raise NotImplementedError

    def append(self, body):
        raise NotImplementedError

    def snapshot(self):
        """ONE stable authenticated snapshot: ``(events, head)``.

        Section 11.2 of the accepted acceptance design needs the event tail and
        all eight authenticated head fields to describe the SAME instant.  Read
        without the storage lock they can be sampled across a concurrent
        append, and a binding assembled from a head that never existed is worse
        than a stale one.

        This is a READ.  It takes the backend's OWN EXISTING exclusive lock for
        exactly the snapshot and releases it; it performs NO tail recovery, NO
        truncation, NO fsync, NO mark write, and NO append.  A second lock, a
        second reader, and a second recovery authority are all forbidden here
        (Section 9.6).

        The default raises: a gateway that cannot prove one stable snapshot
        must say so rather than return an unstable one.
        """
        raise NotImplementedError

    def write_transaction(self):
        """The one write-capable E1-E5 transaction, as a context manager.

        It holds this backend's OWN EXISTING exclusive lock continuously from
        the recovery-enabled read, through the authenticated re-read of the
        journal and the complete head, through whatever the caller must prove,
        to the append itself -- so there is NO check-then-write window in which
        another writer could move the tail out from under a validated binding.

        The object it yields exposes ``events``, ``head``, ``reread()`` and
        ``append(body)``.  ``append`` reaches the SAME single writer every
        ordinary caller reaches; it is not a second append path.

        The default raises: a gateway that cannot hold one continuous
        transaction must say so rather than pretend it did.
        """
        raise NotImplementedError

    @property
    def state_dir(self):
        raise NotImplementedError

    def recover_stranded_candidate_custody(self, expected, lock_held=False):
        """Commit ONE stranded promoted candidate through the EXISTING recovery.

        ``lock_held`` says only WHO OWNS the one candidate-transaction lock, and
        nothing else.  False is the ordinary case and is unchanged.  True means
        the caller already holds that exact lock for this whole transaction, so
        this must not try to take it a second time.

        This is a NARROW ADAPTER and never a second recovery model.  It owns no
        rule of its own: it hands the decision to the one implementation the
        installed controller already has, and then checks that what landed is
        exactly the pending intent this caller named.

        ``expected`` is that pending intent's whole identity -- package, parent,
        candidate, round triple, branch, HEAD, source binding and the journal
        position of the write-ahead itself.

        Returns the appended ``candidate_custody_recorded`` event, or ``None``
        when this gateway binds no candidate-transaction recovery at all, which
        the caller must treat as a refusal rather than as a success.
        """
        return None


class NhLoopJournalGateway(JournalGateway):
    """The production binding: the installed authenticated interview journal."""

    def __init__(self, loop_module, state_dir):
        self._loop = loop_module
        self._state_dir = state_dir

    @property
    def state_dir(self):
        return self._state_dir

    def read(self):
        errors = []
        _path, events = self._loop.read_interview_journal(errors)
        if events is None:
            raise JournalSchemaError("; ".join(errors) or "the journal could not be read")
        return [upgrade_version4_candidate_event(event) for event in events]

    def write_transaction(self):
        """The installed E1-E5 transaction, adapted to the gateway contract."""
        return _NhLoopWriteTransaction(self)

    def snapshot(self):
        """The installed lock, the installed reader, tail recovery disabled."""
        errors = []
        events, head = self._loop.read_interview_journal_snapshot(errors)
        if events is None:
            raise JournalSchemaError(
                "; ".join(errors) or "the journal could not be read"
            )
        return [upgrade_version4_candidate_event(event) for event in events], head

    def append(self, body):
        errors = []
        _path, events = self._loop.read_interview_journal(errors)
        if events is None:
            raise JournalSchemaError("; ".join(errors) or "the journal could not be read")
        state = self._loop.replay_interview_state(events, errors)
        if state is None:
            raise JournalSchemaError("; ".join(errors) or "the journal could not be replayed")
        appended = self._loop.append_interview_event(
            events, state["standing_chain_sha256"], body, errors
        )
        if appended is None:
            raise JournalSchemaError("; ".join(errors) or "the event could not be appended")
        return appended

    def recover_stranded_candidate_custody(self, expected, lock_held=False):
        """The installed controller's OWN write-ahead recovery, and nothing else.

        ``nh_loop.commit_promoted_candidate_custody()`` runs entirely inside the
        candidate-transaction lock, re-reads the world inside it, re-verifies
        every already-held candidate from its real bytes, and commits custody
        only when the promoted file is byte-for-byte the identity the pending
        write-ahead named before that file existed.  None of those proofs is
        repeated, relaxed or replaced here; this only invokes it and then
        refuses anything that is not the exact record the caller expected.
        """
        notes = []
        errors = []
        # ONE recovery implementation, reached two ways that differ ONLY in who
        # already owns the single candidate-transaction lock.  The lock-held form
        # is the same function body: no second recovery model, no relaxed proof,
        # no second lock.  Taking the same flock again from inside the holder,
        # on a different open file description, is not a re-entrant acquire and
        # is what would wedge a supervisor B8.
        if lock_held:
            committed = self._loop.commit_promoted_candidate_custody_locked(
                notes, errors
            )
        else:
            committed = self._loop.commit_promoted_candidate_custody(notes, errors)
        if committed != 1:
            raise JournalSchemaError(
                "; ".join(errors + notes)
                or "the existing candidate transaction recovery committed nothing"
            )
        events = self.read()
        appended = events[-1] if events else None
        if not isinstance(appended, dict) or appended.get("type") != (
            "candidate_custody_recorded"
        ):
            raise JournalSchemaError(
                "the candidate transaction recovery did not leave one custody "
                "record as the newest authenticated event"
            )
        for key, value in expected.items():
            if key == "intent_event_seq":
                continue
            if appended.get(key) != value:
                raise JournalSchemaError(
                    "the recovered custody record is not the pending intent this "
                    "transaction named: %s differs" % key
                )
        return appended


class _NhLoopWriteTransaction:
    """Adapts ``nh_loop.InterviewWriteTransaction`` to the gateway contract.

    It owns no rule of its own: the lock, the recovery, the readers and the
    writer are all the installed ones, and this only carries the caller's view
    of them across the one continuous hold.
    """

    def __init__(self, gateway):
        self._gateway = gateway
        self._loop = gateway._loop
        self._transaction = None
        self.events = None
        self.head = None

    def __enter__(self):
        try:
            self._transaction = self._loop.interview_write_transaction()
            self._transaction.__enter__()
        except Exception as exc:  # noqa: BLE001 -- reported as a journal refusal
            raise JournalSchemaError(str(exc)) from exc
        self._sync()
        return self

    def _sync(self):
        self.events = [
            upgrade_version4_candidate_event(event)
            for event in (self._transaction.events or [])
        ]
        self.head = self._transaction.head
        return self.events, self.head

    def reread(self):
        try:
            self._transaction.reread()
        except Exception as exc:  # noqa: BLE001
            raise JournalSchemaError(str(exc)) from exc
        return self._sync()

    def append(self, body):
        """E5 -- through the SAME writer, inside the lock already held."""
        errors = []
        raw = self._transaction.events
        state = self._loop.replay_interview_state(raw, errors)
        if state is None:
            raise JournalSchemaError(
                "; ".join(errors) or "the journal could not be replayed"
            )
        appended = self._transaction.append(
            raw, state["standing_chain_sha256"], body, errors
        )
        if appended is None:
            raise JournalSchemaError(
                "; ".join(errors) or "the event could not be appended"
            )
        return appended

    def __exit__(self, exc_type, exc, traceback):
        if self._transaction is not None:
            self._transaction.__exit__(exc_type, exc, traceback)
        return False


class _DisposableWriteTransaction:
    """The same continuous-hold contract over the disposable backend's own lock."""

    def __init__(self, gateway):
        self._gateway = gateway
        self._lock_fd = None
        self.events = None
        self.head = None

    def __enter__(self):
        self._lock_fd = self._gateway._lock()
        try:
            # E1 -- the same one-suffix tail recovery the installed backend
            # performs, run here because it requires exactly this lock and this
            # transaction already owns it.  It removes at most ONE unterminated
            # trailing suffix, only over a completely valid prefix, and never
            # touches a complete-but-malformed final line.
            self._gateway._recover_tail_locked()
            self.reread()
        except BaseException:
            self.__exit__(None, None, None)
            raise
        return self

    def reread(self):
        self.events = self._gateway.read()
        self.head = self._gateway._head_for(self._gateway._read_raw())
        return self.events, self.head

    def append(self, body):
        appended = self._gateway._append_locked(body)
        self.reread()
        return appended

    def __exit__(self, exc_type, exc, traceback):
        if self._lock_fd is not None:
            os.close(self._lock_fd)
            self._lock_fd = None
        return False


class DisposableFileJournal(JournalGateway):
    """A bounded authenticated journal for a DISPOSABLE rehearsal only.

    It is refused unless ``NH_SUPERVISOR_DISPOSABLE_JOURNAL=1`` is set.  It is
    never installed, never adopted, and never authority outside the rehearsal
    that created it.  It uses the identical canonical encoding, HMAC label,
    version-dependent auth material, hash chain, and body-key validation as the
    installed journal, so the engine above it runs the production path.
    """

    ENV_FLAG = "NH_SUPERVISOR_DISPOSABLE_JOURNAL"
    JOURNAL_BASENAME = "nh_interview_journal.jsonl"
    KEY_BASENAME = "nh_interview_authenticity.key"
    LOCK_BASENAME = "nh_interview_journal.lock"

    def __init__(self, directory, body_key_table, environ=None):
        environ = os.environ if environ is None else environ
        if environ.get(self.ENV_FLAG) != "1":
            raise JournalSchemaError(
                "the disposable rehearsal journal is refused unless %s=1" % self.ENV_FLAG
            )
        self._dir = str(directory)
        self._body_key_table = body_key_table
        os.makedirs(self._dir, mode=0o700, exist_ok=True)
        os.chmod(self._dir, 0o700)
        self._key = self._load_or_create_key()

    @property
    def state_dir(self):
        return self._dir

    def _path(self, basename):
        return os.path.join(self._dir, basename)

    def _load_or_create_key(self):
        path = self._path(self.KEY_BASENAME)
        try:
            fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
        except OSError as exc:
            if exc.errno != errno.ENOENT:
                raise
            key = os.urandom(32)
            temp = path + ".new"
            fd = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
            try:
                os.write(fd, key)
                os.fsync(fd)
            finally:
                os.close(fd)
            os.rename(temp, path)
            return key
        try:
            info = os.fstat(fd)
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                raise JournalSchemaError("the authenticity key is not a plain file")
            if stat.S_IMODE(info.st_mode) != 0o600 or info.st_uid != os.geteuid():
                raise JournalSchemaError("the authenticity key is not owner-only")
            return os.read(fd, 64)
        finally:
            os.close(fd)

    def _lock(self):
        fd = os.open(
            self._path(self.LOCK_BASENAME),
            os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW,
            0o600,
        )
        fcntl.flock(fd, fcntl.LOCK_EX)
        return fd

    def _read_raw(self):
        path = self._path(self.JOURNAL_BASENAME)
        try:
            with open(path, "rb") as handle:
                blob = handle.read()
        except FileNotFoundError:
            return []
        events = []
        for line in blob.decode("utf-8").splitlines():
            if not line.strip():
                continue
            events.append(json.loads(line))
        return events

    def read(self):
        events = self._read_raw()
        previous = None
        highest_version = 0
        for index, event in enumerate(events):
            problems = validate_event(
                event,
                index,
                previous,
                self._body_key_table,
                auth_key=self._key,
                highest_version_seen=highest_version,
            )
            if problems:
                raise JournalSchemaError("; ".join(problems))
            highest_version = max(highest_version, event["journal_version"])
            previous = event["event_sha256"]
        return [upgrade_version4_candidate_event(event) for event in events]

    HEAD_VERSION = "nh-interview-journal-head-v1"
    HEAD_LABEL = "nh-interview-journal-head-v1"

    def _head_for(self, events):
        """The eight-field authenticated head this disposable journal proves.

        The installed journal keeps two marks in a separate file because it
        writes a record between them.  This one appends under its own lock and
        fsyncs before it returns, so its intent and committed positions are
        always the same durable record -- and that is stated here as a fact
        about THIS backend rather than as a claim about the installed one.

        The field names, the field count, and the authentication label are the
        installed ones, so the code above this gateway compares exactly the
        same eight fields in a rehearsal as it does in production.
        """
        tail = events[-1]["event_sha256"] if events else None
        head = {
            "v": self.HEAD_VERSION,
            "intent_generation": 1,
            "intent_number": max(1, len(events)),
            "intent_event_seq": len(events),
            "intent_event_sha256": tail,
            "committed_event_seq": len(events),
            "committed_event_sha256": tail,
        }
        material = canonical_json(head)
        head["head_auth_sha256"] = hmac.new(
            self._key,
            (self.HEAD_LABEL + "|" + material).encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        return head

    def snapshot(self):
        """One stable snapshot under THIS backend's own existing lock."""
        lock_fd = self._lock()
        try:
            events = self.read()
            return events, self._head_for(self._read_raw())
        finally:
            os.close(lock_fd)

    def write_transaction(self):
        return _DisposableWriteTransaction(self)

    def _recover_tail_locked(self):
        """Remove ONE unterminated trailing suffix. The caller holds the lock.

        This mirrors the installed ``recover_interview_journal_tail`` exactly
        in what it will and will not do, so a rehearsal exercises the same
        rule the production backend enforces:

          * a journal whose last byte is a newline has no unterminated suffix,
            so a COMPLETE-BUT-MALFORMED final line is never touched -- that is
            corruption, not an interrupted write, and it fails closed;
          * the prefix before the suffix must itself be a completely valid,
            authenticated chain, or nothing is removed;
          * removal is a truncate to the proved length plus an fsync plus a
            byte-for-byte re-read.

        It is a repair, so it is a WRITE, and it is reached only from the
        write-capable transaction -- never from a read.
        """
        path = self._path(self.JOURNAL_BASENAME)
        try:
            with open(path, "rb") as handle:
                blob = handle.read()
        except FileNotFoundError:
            return False
        if not blob or blob.endswith(b"\n"):
            return False
        cut = blob.rfind(b"\n")
        proved_length = cut + 1 if cut >= 0 else 0
        prefix = blob[:proved_length]

        # The prefix must be a completely valid chain before anything is cut.
        events = []
        previous = None
        highest = 0
        for index, line in enumerate(prefix.decode("utf-8").splitlines()):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except ValueError as exc:
                raise JournalSchemaError(
                    "the interview journal prefix is not a valid chain, so its "
                    "unterminated tail is refused rather than removed: %s" % exc
                )
            problems = validate_event(
                event, index, previous, self._body_key_table,
                auth_key=self._key, highest_version_seen=highest,
            )
            if problems:
                raise JournalSchemaError(
                    "the interview journal prefix is not a valid chain, so its "
                    "unterminated tail is refused rather than removed: %s"
                    % "; ".join(problems)
                )
            highest = max(highest, event["journal_version"])
            previous = event["event_sha256"]
            events.append(event)

        fd = os.open(path, os.O_WRONLY | os.O_NOFOLLOW)
        try:
            os.ftruncate(fd, proved_length)
            os.fsync(fd)
        finally:
            os.close(fd)
        with open(path, "rb") as handle:
            restored = handle.read()
        if restored != prefix:
            raise JournalSchemaError(
                "the interview journal did not read back byte-for-byte after "
                "its unterminated tail was removed"
            )
        return True

    def append(self, body):
        """Take this backend's lock, then run the one append core below."""
        lock_fd = self._lock()
        try:
            return self._append_locked(body)
        finally:
            os.close(lock_fd)

    def _append_locked(self, body):
        """The ONE append implementation. The caller must already hold the lock.

        ``append()`` above takes the lock and calls this; a write transaction
        calls it while it already owns that same lock.  There is one
        implementation, and both reach it.
        """
        events = self._read_raw()
        event = dict(body)
        event["journal_version"] = constants.INTERVIEW_JOURNAL_CURRENT_VERSION
        event["event_seq"] = len(events) + 1
        event["prev_event_sha256"] = (
            events[-1]["event_sha256"] if events else None
        )
        event["event_auth_sha256"] = event_auth(self._key, event)
        event["event_sha256"] = event_digest(event)

        problems = validate_event(
            event,
            len(events),
            events[-1]["event_sha256"] if events else None,
            self._body_key_table,
            auth_key=self._key,
            highest_version_seen=highest_journal_version(events),
        )
        if problems:
            raise JournalSchemaError("; ".join(problems))

        line = (canonical_json(event) + "\n").encode("utf-8")
        path = self._path(self.JOURNAL_BASENAME)
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND | os.O_NOFOLLOW, 0o600)
        try:
            os.write(fd, line)
            os.fsync(fd)
        finally:
            os.close(fd)
        dir_fd = os.open(self._dir, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
        # Re-read and re-validate the whole history: the record is accepted
        # only if it is exactly the old one plus exactly this event, once.
        reread = self.read()
        if len(reread) != len(events) + 1:
            raise JournalSchemaError("the append did not produce exactly one record")
        return reread[-1]
