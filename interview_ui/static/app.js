"use strict";

const NESS_OWN_WORDS_OPTION_ID = "ness_own_words";

const ui = {
  topbarStatus: document.querySelector("#topbarStatus"),
  contextCard: document.querySelector(".context-card"),
  plainName: document.querySelector("#plainName"),
  technicalName: document.querySelector("#technicalName"),
  frameworkName: document.querySelector("#frameworkName"),
  currentPart: document.querySelector("#currentPart"),
  bundlePlacement: document.querySelector("#bundlePlacement"),
  purpose: document.querySelector("#purpose"),
  stageLabel: document.querySelector("#stageLabel"),
  stageSummary: document.querySelector("#stageSummary"),
  whyHeading: document.querySelector("#whyHeading"),
  whyText: document.querySelector("#whyText"),
  candidateFilename: document.querySelector("#candidateFilename"),
  branch: document.querySelector("#branch"),
  sourceState: document.querySelector("#sourceState"),
  mode: document.querySelector("#mode"),
  loadingCard: document.querySelector("#loadingCard"),
  emptyState: document.querySelector("#emptyState"),
  emptyTitle: document.querySelector("#emptyTitle"),
  emptyText: document.querySelector("#emptyText"),
  questions: document.querySelector("#questions"),
  notice: document.querySelector("#notice"),
  refreshButton: document.querySelector("#refreshButton"),
  pageTechnical: document.querySelector("#pageTechnical"),
  questionsReady: document.querySelector("#questionsReady"),
  answersPreserved: document.querySelector("#answersPreserved"),
  coverageStatus: document.querySelector("#coverageStatus"),
  journalRecords: document.querySelector("#journalRecords"),
  supervisorJournalRecords: document.querySelector("#supervisorJournalRecords"),
  supervisorEvidence: document.querySelector("#supervisorEvidence"),
  workEyebrow: document.querySelector("#workEyebrow"),
  workAreaHeading: document.querySelector("#workAreaHeading"),
  viewTabs: [...document.querySelectorAll(".view-tab")],
  viewPanels: [...document.querySelectorAll(".view-panel")],
  decisionCount: document.querySelector("#decisionCount"),
  correctionCount: document.querySelector("#correctionCount"),
  problemCount: document.querySelector("#problemCount"),
  passCount: document.querySelector("#passCount"),
  statusDependency: document.querySelector("#statusDependency"),
  statusWillRetry: document.querySelector("#statusWillRetry"),
  statusAttemptsLeft: document.querySelector("#statusAttemptsLeft"),
  statusOutputRetriesLeft: document.querySelector("#statusOutputRetriesLeft"),
  statusProbesLeft: document.querySelector("#statusProbesLeft"),
  statusUserActionCode: document.querySelector("#statusUserActionCode"),
  statusUnreconciled: document.querySelector("#statusUnreconciled"),
  technicalBundlePlacement: document.querySelector("#technicalBundlePlacement"),
  technicalComponentId: document.querySelector("#technicalComponentId"),
  technicalRegisterId: document.querySelector("#technicalRegisterId"),
  supervisorTechnicalList: document.querySelector("#supervisorTechnicalList"),
  sinceTitle: document.querySelector("#sinceTitle"),
  sinceSummary: document.querySelector("#sinceSummary"),
  policyProof: document.querySelector("#policyProof"),
  changeFeed: document.querySelector("#changeFeed"),
  emptyFeed: document.querySelector("#emptyFeed"),
  supervisorLabel: document.querySelector("#supervisorLabel"),
  supervisorSummary: document.querySelector("#supervisorSummary"),
  statusHero: document.querySelector("#statusHero"),
  acceptanceCard: document.querySelector("#acceptanceCard"),
  acceptanceEyebrow: document.querySelector("#acceptanceEyebrow"),
  acceptanceHeadline: document.querySelector("#acceptanceHeadline"),
  acceptanceMeaning: document.querySelector("#acceptanceMeaning"),
  acceptanceReason: document.querySelector("#acceptanceReason"),
  acceptanceExplanation: document.querySelector("#acceptanceExplanation"),
  acceptanceTechnical: document.querySelector("#acceptanceTechnical"),
  acceptanceTechnicalList: document.querySelector("#acceptanceTechnicalList"),
  acceptanceButton: document.querySelector("#acceptanceButton"),
  acceptanceNote: document.querySelector("#acceptanceNote"),
};

// The acceptance surface is a MIRROR of the controller. JavaScript is never
// authority here: it renders what the controller supplied, posts the exact
// echo back, and then reads the controller's own proved state again. It
// computes no identity, alters no field, and never decides that anything was
// accepted.
let acceptanceOffer = null;
let acceptanceSubmitting = false;

let currentState = null;
let presenting = false;
let stateRefreshing = false;
let stateRefreshPromise = null;
let activePanel = "changesPanel";
let lastAttentionKey = null;

const PANEL_COPY = {
  decisionsPanel: ["What needs you", "Your decisions"],
  changesPanel: ["The live design loop", "What’s changing"],
  statusPanel: ["Where the package is now", "Current status"],
  technicalPanel: ["Verified underlying records", "Technical details"],
};

function setText(element, value, fallback = "—") {
  element.textContent = value ?? fallback;
}

async function api(path, options = {}) {
  const response = await fetch(path, {
    cache: "no-store",
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });
  const data = await response.json();
  if (!response.ok || !data.ok) {
    const error = new Error(data.message || "N.H refused this action safely.");
    error.data = data;
    throw error;
  }
  return data;
}

function showNotice(message, error = false) {
  ui.notice.textContent = message;
  ui.notice.classList.toggle("error", error);
  ui.notice.classList.remove("hidden");
}

function hideNotice() {
  ui.notice.classList.add("hidden");
  ui.notice.classList.remove("error");
}

function switchPanel(panelId, focus = false) {
  if (!PANEL_COPY[panelId]) return;
  activePanel = panelId;
  ui.viewPanels.forEach((panel) => {
    panel.classList.toggle("hidden", panel.id !== panelId);
  });
  ui.viewTabs.forEach((tab) => {
    const selected = tab.dataset.panel === panelId;
    tab.classList.toggle("active", selected);
    tab.setAttribute("aria-selected", selected ? "true" : "false");
    tab.tabIndex = selected ? 0 : -1;
    if (selected && focus) tab.focus();
  });
  const [eyebrow, heading] = PANEL_COPY[panelId];
  ui.workEyebrow.textContent = eyebrow;
  ui.workAreaHeading.textContent = heading;
}

function renderContext(state) {
  const { context, stage, technical } = state;
  setText(ui.plainName, context.plain_name);
  setText(ui.technicalName, context.technical_name);
  setText(ui.frameworkName, context.framework, "Not identified by current source");
  setText(ui.currentPart, context.current_part);
  setText(ui.bundlePlacement, context.bundle);
  setText(ui.purpose, context.purpose);
  setText(ui.stageLabel, stage.label);
  setText(ui.stageSummary, stage.summary, "");
  setText(ui.whyText, stage.why);
  ui.whyHeading.textContent = stage.attention_kind === "action"
    ? "Why your action is needed"
    : stage.attention_kind === "acceptance"
      ? "Why this has returned to you"
      : stage.needs_ness
        ? "Why you’re being asked"
        : "Why you’re not being asked";

  setText(ui.candidateFilename, context.candidate_filename);
  setText(ui.branch, technical.branch);
  setText(ui.sourceState, technical.source_state);
  setText(ui.mode, technical.mode);

  ui.contextCard.classList.toggle("needs-you", stage.needs_ness);
  ui.topbarStatus.className = `topbar-status ${stage.tone}`;
  ui.topbarStatus.lastElementChild.textContent = stage.needs_ness
    ? "Your answer is needed"
    : stage.label;

  setText(ui.questionsReady, state.questions.ready, "0");
  setText(ui.answersPreserved, state.progress.answers_preserved, "0");
  setText(
    ui.coverageStatus,
    technical.coverage_review_current ? "Current" : "Not current"
  );
  setText(ui.journalRecords, technical.journal_records);
  setText(ui.supervisorJournalRecords, technical.authenticated_supervisor_records, "0");
  setText(
    ui.supervisorEvidence,
    state.supervisor_evidence?.controller_authenticated
      ? (state.supervisor_evidence?.run_active ? "Authenticated · run active" : "Authenticated · run inactive")
      : "No authenticated supervisor claim"
  );

  const ready = Number(state.questions.ready || 0);
  ui.decisionCount.textContent = ready.toLocaleString();
  ui.decisionCount.classList.toggle("hidden", ready === 0);
}

function renderEmpty(state) {
  ui.questions.replaceChildren();
  ui.loadingCard.classList.add("hidden");
  ui.emptyState.classList.remove("hidden");
  ui.emptyTitle.textContent = state.stage.summary;
  ui.emptyText.textContent = state.stage.why;
}

function createText(tag, className, text) {
  const element = document.createElement(tag);
  if (className) element.className = className;
  element.textContent = text;
  return element;
}

function technicalChangeDetails(item) {
  const details = document.createElement("details");
  details.className = "change-technical";
  details.append(createText("summary", "", "Technical evidence"));
  const list = document.createElement("dl");
  const labels = {
    candidate_path: "Candidate",
    candidate_sha256: "Candidate SHA-256",
    candidate_bytes: "Candidate bytes",
    blocked_candidate_path: "Previous candidate",
    blocked_candidate_sha256: "Previous SHA-256",
    correction_round: "Lifetime correction round",
    severity: "Severity",
    route: "Route",
    finding_ref: "Finding identity",
    finding_refs: "Finding identities",
    correction_specification_sha256: "Correction specification",
    custody_recorded: "Candidate custody recorded",
    verdict: "Audit verdict",
    highest_severity: "Highest severity",
    source_evidence: "Source evidence",
    candidate_evidence: "Candidate evidence",
  };
  Object.entries(item.technical || {}).forEach(([key, value]) => {
    if (value === null || value === undefined || value === "") return;
    const row = document.createElement("div");
    row.append(
      createText("dt", "", labels[key] || key.replaceAll("_", " ")),
      createText(
        "dd",
        "",
        Array.isArray(value) ? value.join(" · ") : String(value)
      )
    );
    list.append(row);
  });
  details.append(list);
  return details;
}

function changeIcon(kind) {
  if (kind === "problem_found") return "!";
  if (kind === "candidate_changed") return "↗";
  if (kind === "audit_passed") return "✓";
  return "•";
}

function renderChangeFeed(state) {
  const summary = state.change_summary || {};
  const feed = state.change_feed || [];
  setText(ui.correctionCount, summary.candidates_changed, "0");
  setText(ui.problemCount, summary.problems_found, "0");
  setText(ui.passCount, summary.audits_passed, "0");
  // Never a "Claude fixed it" claim on Claude's own authority, and never an
  // acceptance claim: both are fixed false in the controller projection.
  setText(
    ui.policyProof,
    summary.claims_fix || summary.claims_acceptance
      ? "This projection is refused: no fix or acceptance may be claimed here."
      : "No fix, PASS, or acceptance is claimed here on any model's own authority."
  );

  if (feed.length) {
    ui.sinceTitle.textContent = `${feed.length} controller-authenticated event${feed.length === 1 ? "" : "s"}`;
    ui.sinceSummary.textContent = "Each item was freshly re-proved from authenticated controller custody and audit records.";
  } else {
    ui.sinceTitle.textContent = "No confirmed changes recorded yet";
    ui.sinceSummary.textContent = "A change appears only after supervisor-status re-proves it from authenticated controller records.";
  }

  ui.changeFeed.replaceChildren();
  ui.emptyFeed.classList.toggle("hidden", feed.length > 0);
  feed.forEach((item) => {
    const card = document.createElement("article");
    card.className = `change-card ${item.kind || "event"}`;
    const marker = createText("span", "change-marker", changeIcon(item.kind));
    marker.setAttribute("aria-hidden", "true");
    const body = document.createElement("div");
    body.className = "change-body";
    body.append(
      createText("p", "change-kicker", item.title || "Controller event"),
      createText("h3", "", item.what || "A verified event was recorded."),
      createText("p", "change-why", item.why || ""),
      createText("p", "change-result", item.status || "")
    );
    body.append(technicalChangeDetails(item));
    card.append(marker, body);
    ui.changeFeed.append(card);
  });
}

const INTERRUPTING_STATES = new Set([
  "NEEDS_NESS_DECISION",
  "NEEDS_USER_ACTION",
  "READY_FOR_ACCEPTANCE",
]);

const ACCEPTANCE_STATES = new Set([
  "READY_FOR_ACCEPTANCE",
  "ACCEPTED_FOR_DESIGN_ONLY",
]);

function renderAcceptanceTechnical(technical) {
  ui.acceptanceTechnicalList.replaceChildren();
  const entries = Object.entries(technical || {});
  ui.acceptanceTechnical.hidden = entries.length === 0;
  entries.forEach(([key, value]) => {
    const row = document.createElement("div");
    const term = createText("dt", "", key.replace(/_/g, " "));
    const detail = document.createElement("dd");
    const code = createText("code", "", value === null || value === undefined ? "—" : String(value));
    detail.append(code);
    row.append(term, detail);
    ui.acceptanceTechnicalList.append(row);
  });
}

function renderAcceptance(offer, state) {
  const current = state?.supervisor || {};
  const accepted = current.state === "ACCEPTED_FOR_DESIGN_ONLY";
  acceptanceOffer = offer && offer.acceptance_actionable ? offer : null;

  // The fixed meaning is the CONTROLLER'S text, rendered as a text node. It is
  // never composed, shortened, softened, or paraphrased here.
  setText(ui.acceptanceMeaning, offer?.acceptance_fixed_meaning, "");

  if (accepted) {
    setText(ui.acceptanceEyebrow, "Accepted for design-only status");
    setText(
      ui.acceptanceHeadline,
      "You accepted this exact candidate as a design."
    );
  } else {
    setText(ui.acceptanceEyebrow, "Ready for your acceptance");
    setText(
      ui.acceptanceHeadline,
      "This exact design candidate passed its required mechanical audit."
    );
  }

  // The eight parts, in the order the controller returned them, as TEXT.
  ui.acceptanceExplanation.replaceChildren();
  (offer?.explanation_parts || []).forEach((part) => {
    const section = document.createElement("section");
    section.className = "acceptance-part";
    section.append(
      createText("h4", "", part.title || ""),
      createText("p", "", part.text || "")
    );
    ui.acceptanceExplanation.append(section);
  });

  renderAcceptanceTechnical(offer?.technical);

  const reason = offer?.reason;
  ui.acceptanceReason.hidden = !reason;
  setText(ui.acceptanceReason, reason, "");

  // ONLY the controller's own offer decides whether Accept is actionable.
  // Removing the disabled attribute in a console accomplishes nothing: the
  // server refuses a post with no valid current offer, and the controller
  // re-proves every binding under its own lock.
  const actionable = Boolean(offer?.acceptance_actionable) && !accepted;
  ui.acceptanceButton.disabled = !actionable || acceptanceSubmitting;
  ui.acceptanceButton.hidden = accepted;
  if (accepted) {
    setText(
      ui.acceptanceNote,
      "This records your acceptance only. Nothing was adopted, integrated, implemented, marked complete, closed, committed, or pushed, and no next package started."
    );
  } else if (actionable) {
    setText(
      ui.acceptanceNote,
      "Pressing this records your acceptance of this exact candidate, for design-only status, once."
    );
  } else {
    setText(
      ui.acceptanceNote,
      "The Accept action is not offered. N.H changes nothing and claims nothing."
    );
  }
}

async function refreshAcceptance(state) {
  const current = state?.supervisor || {};
  const relevant = ACCEPTANCE_STATES.has(current.state);
  ui.acceptanceCard.classList.toggle("hidden", !relevant);
  if (!relevant) {
    acceptanceOffer = null;
    return;
  }
  try {
    const offer = await api("/api/acceptance/offer");
    renderAcceptance(offer, state);
  } catch (error) {
    acceptanceOffer = null;
    ui.acceptanceButton.disabled = true;
    setText(ui.acceptanceReason, error.message, "");
    ui.acceptanceReason.hidden = false;
    setText(
      ui.acceptanceNote,
      "N.H could not read its own acceptance state, so no Accept action is offered."
    );
  }
}

async function submitAcceptance() {
  if (acceptanceSubmitting || !acceptanceOffer) return;
  // Duplicate submission is disabled IMMEDIATELY, before the request leaves.
  acceptanceSubmitting = true;
  ui.acceptanceButton.disabled = true;
  ui.acceptanceButton.textContent = "Recording…";
  hideNotice();
  const offer = acceptanceOffer;
  try {
    // The EXACT offer binding is echoed back. No identity field is synthesized,
    // recomputed, or altered here.
    const result = await api("/api/acceptance/record", {
      method: "POST",
      body: JSON.stringify({
        acceptance_offer_id: offer.acceptance_offer_id,
        acceptance_offer_binding_sha256: offer.acceptance_offer_binding_sha256,
        pre_click_head_digest_sha256: offer.pre_click_head_digest_sha256,
        candidate_sha256: offer.technical?.candidate_sha256,
        acceptance_scope_id: offer.acceptance_scope_id,
        acceptance_scope_digest: offer.acceptance_scope_digest,
        explanation_record_identity: offer.technical?.explanation_record_identity,
        explanation_digest: offer.technical?.explanation_digest,
        ness_action_confirmed: true,
      }),
    });
    // HTTP success is NOT acceptance. Nothing is claimed until the controller's
    // own refreshed state proves it.
    await refreshState(false);
    const proved =
      currentState?.supervisor?.state === "ACCEPTED_FOR_DESIGN_ONLY";
    if (proved) {
      showNotice(
        "N.H recorded your acceptance of this exact candidate for design-only status. Nothing was adopted, integrated, implemented, marked complete, closed, committed, or pushed."
      );
    } else {
      showNotice(
        result.reason ||
          "N.H did not prove that this acceptance now stands. Nothing is claimed. Read the current state before pressing again.",
        true
      );
    }
  } catch (error) {
    showNotice(error.message, true);
  } finally {
    acceptanceSubmitting = false;
    ui.acceptanceButton.textContent =
      "Accept this exact candidate for design-only status";
    await refreshAcceptance(currentState);
  }
}

function renderSupervisorStatus(state) {
  const current = state.supervisor || {};
  const wording = current.wording || {};
  const status = state.current_status || {};
  setText(ui.supervisorLabel, wording.headline);
  setText(ui.supervisorSummary, wording.detail, "");
  ui.statusHero.dataset.state = current.state || "IDLE";
  // Visibility follows the authenticated state; ACTIONABILITY follows only the
  // controller's own offer projection, fetched separately in refreshAcceptance.
  ui.acceptanceCard.classList.toggle(
    "hidden",
    !ACCEPTANCE_STATES.has(current.state)
  );

  setText(
    ui.statusDependency,
    status.plain_language_dependency,
    "Nothing is blocking mechanical work."
  );
  setText(
    ui.statusWillRetry,
    status.will_retry_by_itself === undefined
      ? null
      : status.will_retry_by_itself
        ? "Yes — N.H will retry by itself when it is safe."
        : "No — N.H will not retry by itself.",
    "—"
  );
  setText(ui.statusAttemptsLeft, status.provider_attempts_remaining_this_episode, "—");
  setText(ui.statusOutputRetriesLeft, status.output_retries_remaining, "—");
  setText(ui.statusProbesLeft, status.availability_probes_remaining, "—");
  setText(ui.statusUserActionCode, status.user_action_code, "None");
  if (ui.statusUnreconciled) {
    ui.statusUnreconciled.hidden = !status.provider_request_unreconciled;
  }

  renderSupervisorTechnical(state);

  const attentionKey = INTERRUPTING_STATES.has(current.state)
    ? `${current.state}:${current.candidate_sha256 || ""}`
    : null;
  if (attentionKey && attentionKey !== lastAttentionKey) {
    const target = current.state === "NEEDS_NESS_DECISION"
      ? "decisionsPanel"
      : "statusPanel";
    switchPanel(target);
    lastAttentionKey = attentionKey;
  }
}

function renderSupervisorTechnical(state) {
  const context = state.context || {};
  setText(ui.technicalBundlePlacement, context.bundle, "Not decided yet");
  setText(
    ui.technicalComponentId,
    context.controlled_component_id === null || context.controlled_component_id === undefined
      ? "Open — none"
      : context.controlled_component_id
  );
  setText(
    ui.technicalRegisterId,
    context.register_id === null || context.register_id === undefined
      ? "Open — none"
      : context.register_id
  );
  if (!ui.supervisorTechnicalList) return;
  ui.supervisorTechnicalList.replaceChildren();
  const details = state.technical_details || {};
  Object.keys(details).sort().forEach((key) => {
    const value = details[key];
    if (value === null || value === undefined) return;
    const row = document.createElement("div");
    row.append(createText("dt", "", key));
    row.append(createText("dd", "", String(value)));
    ui.supervisorTechnicalList.append(row);
  });
}

function technicalQuestionDetails(question) {
  const details = document.createElement("details");
  details.className = "question-details";
  details.append(createText("summary", "", "Technical details for this question"));
  const copy = document.createElement("div");
  copy.className = "detail-copy";

  const settled = document.createElement("p");
  settled.append(createText("strong", "", "Already settled: "));
  settled.append(document.createTextNode(question.settled || "No surrounding rule supplied."));
  copy.append(settled);

  const checked = document.createElement("p");
  checked.append(createText("strong", "", "What was checked: "));
  checked.append(document.createTextNode(question.checked || "Current N.H sources."));
  copy.append(checked);

  const identity = document.createElement("p");
  identity.append(createText("strong", "", "Question identity: "));
  const code = document.createElement("code");
  code.textContent = `${question.question_id} · ${question.form_generation}`;
  identity.append(code);
  copy.append(identity);
  details.append(copy);
  return details;
}

function renderQuestion(question) {
  const card = document.createElement("article");
  card.className = "question-card";

  const top = document.createElement("div");
  top.className = "question-top";
  top.append(
    createText(
      "span",
      "question-count",
      `Question ${question.position} of ${question.total}`
    ),
    createText("p", "question-topic", question.topic || "N.H behaviour"),
    createText("h3", "", question.question || "What should N.H do?")
  );
  if (question.subject) {
    top.append(createText("p", "subject-note", question.subject));
  }
  card.append(top);

  const impact = document.createElement("div");
  impact.className = "impact-box";
  impact.append(createText("strong", "", "This choice affects"));
  const impactList = document.createElement("ul");
  const effects = question.effect_sentences?.length
    ? question.effect_sentences
    : ["how this part of N.H behaves in real use"];
  effects.forEach((effect) => impactList.append(createText("li", "", effect)));
  impact.append(impactList);
  card.append(impact);

  const form = document.createElement("form");
  form.className = "answer-area";
  form.dataset.questionId = question.question_id;
  form.dataset.formGeneration = question.form_generation;
  form.dataset.choice = "";
  form.append(
    createText("h4", "", "Answer in normal, everyday words"),
    createText(
      "p",
      "answer-help",
      "You do not need technical language. Choose an option if one feels right, or explain what you want in your own way."
    )
  );

  const optionList = document.createElement("div");
  optionList.className = "option-list";
  if (question.options?.length) {
    question.options.forEach((option) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "option-button";
      button.dataset.optionId = option.option_id;
      const id = createText("span", "option-id", option.option_id);
      const copy = document.createElement("span");
      copy.className = "option-copy";
      copy.append(createText("strong", "", option.meaning));
      const consequences = [...(option.consequences || []), ...(option.other_effects || [])];
      if (consequences.length) {
        copy.append(createText("small", "", consequences.join(" ")));
      }
      button.append(id, copy);
      button.addEventListener("click", () => {
        optionList
          .querySelectorAll(".option-button")
          .forEach((item) => item.classList.remove("selected"));
        button.classList.add("selected");
        form.dataset.choice = option.option_id;
        const textarea = form.querySelector("textarea");
        if (!textarea.value.trim() || textarea.dataset.autoFilled === "true") {
          const autoFillText = `I choose option ${option.option_id}: ${option.meaning}`;
          textarea.value = autoFillText;
          textarea.dataset.autoFilled = "true";
          textarea.dataset.autoFillText = autoFillText;
          textarea.dispatchEvent(new Event("input"));
        }
        textarea.focus();
      });
      optionList.append(button);
    });
  }
  const ownWordsButton = document.createElement("button");
  ownWordsButton.type = "button";
  ownWordsButton.className = "option-button";
  ownWordsButton.dataset.optionId = NESS_OWN_WORDS_OPTION_ID;
  const ownWordsId = createText("span", "option-id", "Your words");
  const ownWordsCopy = document.createElement("span");
  ownWordsCopy.className = "option-copy";
  ownWordsCopy.append(
    createText("strong", "", "My own answer"),
    createText(
      "small",
      "",
      "Write what you really want. N.H preserves your exact words instead of forcing them into an example choice."
    )
  );
  ownWordsButton.append(ownWordsId, ownWordsCopy);
  ownWordsButton.addEventListener("click", () => {
    optionList
      .querySelectorAll(".option-button")
      .forEach((item) => item.classList.remove("selected"));
    ownWordsButton.classList.add("selected");
    form.dataset.choice = NESS_OWN_WORDS_OPTION_ID;
    const textarea = form.querySelector("textarea");
    if (
      textarea.dataset.autoFilled === "true" &&
      textarea.value === textarea.dataset.autoFillText
    ) {
      textarea.value = "";
    }
    textarea.dataset.autoFilled = "false";
    textarea.dataset.autoFillText = "";
    textarea.focus();
  });
  optionList.append(ownWordsButton);
  form.append(optionList);

  const answerLabel = document.createElement("label");
  answerLabel.className = "answer-label";
  answerLabel.htmlFor = `answer-${question.question_id}`;
  answerLabel.append(
    createText("span", "", "What do you want N.H to do?"),
    createText("span", "character-count", "0 characters")
  );
  const textarea = document.createElement("textarea");
  textarea.id = `answer-${question.question_id}`;
  textarea.maxLength = 12000;
  textarea.required = true;
  textarea.placeholder = "For example: I want N.H to…";
  textarea.addEventListener("input", () => {
    const exactAutoFill =
      textarea.dataset.autoFilled === "true" &&
      textarea.value === textarea.dataset.autoFillText;
    if (!exactAutoFill) {
      textarea.dataset.autoFilled = "false";
      textarea.dataset.autoFillText = "";
      form.dataset.choice = NESS_OWN_WORDS_OPTION_ID;
      optionList
        .querySelectorAll(".option-button")
        .forEach((item) => item.classList.remove("selected"));
      ownWordsButton.classList.add("selected");
    }
    answerLabel.querySelector(".character-count").textContent =
      `${textarea.value.length.toLocaleString()} characters`;
  });
  form.append(answerLabel, textarea);

  const actions = document.createElement("div");
  actions.className = "answer-actions";
  actions.append(
    createText(
      "span",
      "save-note",
      "Your answer is preserved exactly as shown here. It does not accept or adopt the design."
    )
  );
  const submit = createText("button", "primary-button", "Save this answer");
  submit.type = "submit";
  actions.append(submit);
  form.append(actions);

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const answerText = textarea.value;
    if (!answerText.trim()) {
      textarea.focus();
      return;
    }
    submit.disabled = true;
    submit.textContent = "Saving…";
    hideNotice();
    try {
      const result = await api("/api/answers", {
        method: "POST",
        body: JSON.stringify({
          question_id: question.question_id,
          form_generation: question.form_generation,
          answer_text: answerText,
          answer_choice: form.dataset.choice || null,
          supersede_settled: false,
        }),
      });
      if (!result.preserved) {
        showNotice("N.H could not prove that your answer was preserved. Nothing was assumed or settled.", true);
        submit.disabled = false;
        submit.textContent = "Save this answer";
        return;
      }
      const interpretation = result.interpretation?.status;
      await refreshState(true);
      if (interpretation === "selected_declared_option") {
        showNotice("Your answer was preserved exactly. N.H is now checking what it changes; this does not itself resume work.");
      } else if (interpretation === "selected_ness_own_words") {
        showNotice("Your answer was preserved exactly in your own words. N.H can continue to the next existing question; it will check the completed answer set together afterward.");
      } else {
        const reason = currentState?.current_status?.ness_answer_clarification?.clarification_reason;
        showNotice(
          reason
            ? `Your words were preserved exactly, and nothing was assumed or settled. ${reason}`
            : "Your words were preserved exactly, but nothing was assumed or settled. The same question remains open for clarification."
        );
      }
    } catch (error) {
      showNotice(error.message, true);
      submit.disabled = false;
      submit.textContent = "Save this answer";
    }
  });

  card.append(form, technicalQuestionDetails(question));
  return card;
}

function renderQuestions(data) {
  ui.loadingCard.classList.add("hidden");
  ui.emptyState.classList.add("hidden");
  ui.questions.replaceChildren();
  if (!data.questions?.length) {
    renderEmpty(currentState);
    return;
  }
  data.questions.forEach((question) => ui.questions.append(renderQuestion(question)));
}

async function presentQuestions() {
  if (presenting) return;
  presenting = true;
  try {
    const data = await api("/api/questions/present", {
      method: "POST",
      body: "{}",
    });
    renderQuestions(data);
  } catch (error) {
    ui.loadingCard.classList.add("hidden");
    showNotice(error.message, true);
    renderEmpty(currentState);
  } finally {
    presenting = false;
  }
}

async function refreshStateOnce(autoPresent = true, background = false) {
  if (!background) {
    hideNotice();
    ui.loadingCard.classList.remove("hidden");
    ui.emptyState.classList.add("hidden");
    ui.questions.replaceChildren();
    ui.refreshButton.disabled = true;
  }
  try {
    currentState = await api("/api/state");
    renderContext(currentState);
    renderChangeFeed(currentState);
    renderSupervisorStatus(currentState);
    await refreshAcceptance(currentState);
    const needsQuestions =
      currentState.stage.needs_ness ||
      currentState.questions.open_group_index !== null;
    if (needsQuestions && autoPresent && !ui.questions.children.length) {
      await presentQuestions();
    } else if (!background) {
      renderEmpty(currentState);
    }
  } catch (error) {
    if (!background) {
      ui.loadingCard.classList.add("hidden");
      ui.emptyState.classList.add("hidden");
      showNotice(error.message, true);
    }
    ui.topbarStatus.lastElementChild.textContent = "N.H needs attention";
  } finally {
    if (!background) ui.refreshButton.disabled = false;
  }
}

function refreshState(autoPresent = true, background = false) {
  if (stateRefreshing) return stateRefreshPromise;
  stateRefreshing = true;
  stateRefreshPromise = refreshStateOnce(autoPresent, background).finally(() => {
    stateRefreshing = false;
    stateRefreshPromise = null;
  });
  return stateRefreshPromise;
}

ui.refreshButton.addEventListener("click", () => refreshState(true));
ui.acceptanceButton.addEventListener("click", submitAcceptance);
ui.viewTabs.forEach((tab) => {
  tab.addEventListener("click", () => switchPanel(tab.dataset.panel));
  tab.addEventListener("keydown", (event) => {
    if (!['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
    event.preventDefault();
    const index = ui.viewTabs.indexOf(tab);
    const offset = event.key === 'ArrowRight' ? 1 : -1;
    const next = ui.viewTabs[(index + offset + ui.viewTabs.length) % ui.viewTabs.length];
    switchPanel(next.dataset.panel, true);
  });
});
switchPanel(activePanel);
refreshState(true);

setInterval(() => {
  if (document.visibilityState === "visible" && !presenting) {
    refreshState(false, true);
  }
}, 8000);
