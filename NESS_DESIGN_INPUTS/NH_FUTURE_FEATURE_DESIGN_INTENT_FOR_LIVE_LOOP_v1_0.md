# N.H — Future Feature Design Intent for the Live Design Loop

**Filename:** `NH_FUTURE_FEATURE_DESIGN_INTENT_FOR_LIVE_LOOP_v1_0.md`  
**Status:** NESS FEATURE-INTENT INPUT — NOT AN AUTHORITY FILE, NOT AN ACCEPTED DESIGN, NOT IMPLEMENTATION AUTHORIZATION  
**Purpose:** One self-contained file Ness can give to the future N.H live design loop when it asks what additional capabilities Ness wants brought into the N.H design.

---

# 0. How the live design loop must use this file

This file records **what Ness wants N.H to eventually be able to do in several feature areas that are not yet fully represented as completed N.H designs**.

It is **design input**, not a finished architecture.

When this file is supplied to the N.H live design loop, the loop must:

1. Read the current N.H governing files first.
2. Check every feature below against:
   - Master V10;
   - the current Design and Wiring Map;
   - adopted Decision Defaults;
   - current `cursorrules`;
   - accepted standalone packages;
   - closure/receipt records;
   - later accepted work;
   - earlier Ness decisions relevant to that feature.
3. Determine what is:
   - already fully designed;
   - already partially designed;
   - mechanically implied by existing design;
   - genuinely new;
   - dependent on another unfinished component;
   - a genuine meaning/policy choice for Ness;
   - later implementation work.
4. **Do not create a duplicate subsystem** when an existing N.H component can naturally own the capability.
5. Preserve every already-settled N.H rule.
6. Ask Ness only about genuinely open meaning/policy choices that cannot be derived from current authority.
7. Turn the unlocked work into proper **new versioned design candidate(s)**.
8. Run the normal independent audit/correction loop.
9. Do not mark anything accepted or adopted until Ness separately accepts it.
10. Do not begin implementation merely because the design becomes complete.

## Authority rule

This file is below all current N.H authority and accepted design.

If anything written here conflicts with adopted N.H rules, the live design loop must **surface the conflict and preserve the higher authority** rather than silently changing N.H.

This file is not permission to:
- overwrite an authority file;
- edit an accepted design in place;
- remove history;
- change privacy/security rules;
- build code;
- create production stores;
- integrate into Master or Map without the normal versioned process;
- accept or adopt anything for Ness.

---

# 1. Overall intent

I want N.H to grow beyond being only a memory-and-conversation system.

I want it to also become a system that can:

- experience and work with media with me;
- understand how music and media connect to my own inner meaning and creative work;
- understand the branching structure of how I think and converse;
- simulate possible next thought/conversation branches without pretending predictions are reality;
- help me navigate and understand the physical world in real time in a much later stage;
- become a serious creation workspace where I can actually make things with it;
- let me search my entire N.H memory through one powerful human-facing search surface.

These additions must still behave like N.H:

**N.H is my helper, not my decider.**

It may understand, connect, predict, simulate, prepare, search, compare, and suggest.

It must not silently turn:
- prediction into memory;
- interpretation into fact;
- similarity into identity;
- a draft into an accepted decision;
- a creation into an adopted rule;
- a media association into objective meaning;
- a proposed connection into a confirmed connection;
- a tool result into proof of success.

---

# 2. FEATURE FAMILY A — Personal Media Meaning and Live Media Experience

## 2.1 The basic idea

I want media to become a first-class part of my interaction with N.H.

This is not merely:

> upload an audio file and get a summary.

I want to be able to **experience music or other media while I am actively talking and thinking with N.H**, and I want N.H to understand the media at a much deeper level than title/lyrics/topic.

Music is especially important because I often connect songs, exact musical moments, emotional changes, beats, drops, vocal changes, and structure to:

- my memories;
- how I understand my own life;
- scenes I imagine;
- characters;
- character arcs;
- story structure;
- creative projects;
- emotional ideas;
- visual ideas;
- personal meanings that may be very different from the song's public or intended meaning.

N.H should be able to work with those connections without confusing my personal meaning with objective fact about the song.

---

## 2.2 Media-service connection

I want N.H eventually to be able to connect to a media service such as **Spotify**, and potentially other authorized media services later.

The exact providers are not the important concept.

The important capability is:

- I can choose media from inside the N.H experience;
- N.H knows which item is playing;
- N.H can understand the playback position;
- I can talk to N.H while the media is playing;
- media playback does not force me to leave the N.H conversation;
- the conversation and the media experience can happen together.

Possible later examples:

- "Play this song."
- "Pause."
- "Go back to that part."
- "What happened musically right there?"
- "This part is what I imagine for this character."
- "Remember how I connect this exact moment to that scene."
- "Compare this drop with the other song I connected to the same project."

Actual playback actions must obey the normal N.H permission/tool rules.

A media integration must never become a hidden shortcut around N.H's authentication, privacy, external-action, or recordkeeping rules.

---

## 2.3 Conversation while media keeps playing

I want N.H to support a genuine combined experience:

**media + conversation at the same time.**

For example:

1. I start a song.
2. The song continues playing.
3. I talk to N.H while it plays.
4. I refer to what I am hearing now.
5. N.H can understand that I mean the current or recently played part.
6. I may pause, rewind, jump, or replay a section.
7. N.H can discuss the exact musical moment with me.
8. The conversation remains a normal N.H conversation rather than changing into a separate "media analyzer" app.

This should eventually be possible for other time-based media too, such as video, where appropriate.

The design must define how N.H anchors statements such as:

- "this part";
- "that beat";
- "the drop";
- "when her voice changed";
- "right before the chorus";
- "the scene at 02:14";

to an actual media position without guessing.

---

## 2.4 Deep musical understanding

I do not want N.H's understanding of a song to stop at lyrics.

I want it to be able to reason about the actual musical experience, including where technically practical:

- melody;
- rhythm;
- tempo;
- harmony;
- instrumentation;
- vocals;
- vocal intensity;
- changes in delivery;
- buildup;
- release;
- beat;
- drop;
- silence;
- transition;
- structure;
- repetition;
- dynamic changes;
- contrast between sections;
- emotional movement suggested by the sound;
- the relation between lyrics and the musical arrangement.

The important part is not that N.H must produce a music-theory lecture every time.

The important part is that the **sound itself can be meaningful evidence in the conversation**, not only the written words.

---

## 2.5 Exact-moment meaning

A major capability I want is meaning attached to **specific moments inside media**.

An association should be able to refer to:

- the whole song;
- a range;
- an exact timestamp;
- a beat;
- a drop;
- a lyric line;
- a vocal change;
- a transition;
- a scene in a video;
- another identifiable media segment.

Example:

> "The drop at 02:14 feels like the exact moment this character stops being afraid and chooses to fight."

N.H should preserve that as **my interpretation / creative association**, not as an objective statement that the artist intended that meaning.

Later I may say something different.

The old association must not be overwritten merely because my interpretation changes.

---

## 2.6 Personal Media Meaning

I want N.H to be capable of learning and retrieving **what media means to me personally**.

This may include connections such as:

- song → memory;
- song → life period;
- song → person;
- song → emotion;
- song → project;
- song → character;
- song → scene;
- song → visual concept;
- song → theme;
- song → a particular internal feeling;
- exact timestamp → a particular creative beat;
- one song section → another media reference.

These are not universal facts.

N.H must keep the difference between:

1. **source facts**  
   Example: title, artist, album, duration, published lyrics, release metadata.

2. **N.H interpretation**  
   Example: N.H thinks the arrangement creates rising tension.

3. **outside/public interpretation**  
   Example: an interview or source says what the artist intended.

4. **my personal meaning**  
   Example: I experience the drop as the emotional turning point of one of my characters.

5. **my creative use**  
   Example: I want that exact section as a reference for Scene 23 of a project.

They may connect, but they may never silently collapse into one claim.

---

## 2.7 Media-to-creative-project linking

Media should be able to participate in my creation system.

I want to connect a song, video, or exact segment to:

- a project;
- series;
- film;
- episode;
- chapter;
- scene;
- character;
- relationship;
- character arc;
- emotional arc;
- visual sequence;
- animation idea;
- pacing reference;
- editing reference;
- creative note.

This should allow a project to later show:

> Media references connected to this project

and allow a media item to show:

> Creative ideas / scenes / characters I connected to this media.

The design should reuse N.H's existing provenance, connection, creation, and project concepts rather than inventing an unrelated media-memory database if those systems can own the relationships.

---

## 2.8 Media reference without copying the whole media

I want N.H to be able to remember a useful reference to media even when it should not or cannot permanently store a copyrighted full media file.

A durable reference may include appropriate items such as:

- provider/source;
- title;
- artist/creator;
- stable service identifier where available;
- URL/reference;
- exact timestamp or range;
- my note;
- my personal meaning;
- linked project/scene/character;
- source metadata;
- what evidence was actually available;
- whether N.H could later re-open the original.

The design must distinguish:

**remembering my relationship to a media item**  
from  
**copying/owning the media itself.**

If the original later becomes unavailable, N.H must not pretend it still possesses content it never stored.

---

## 2.9 Media history

My media-related meaning can evolve.

I may connect one song to one idea today and something else later.

N.H should preserve:

- original associations;
- later associations;
- corrections;
- abandoned creative uses;
- changed interpretations;
- the date/context in which each association was made.

The newest association must not erase the older one.

---

## 2.10 Boundaries that must remain true

This feature must never:

- claim my personal interpretation is the artist's intent;
- claim a model's emotional read is objective fact;
- copy restricted media merely because N.H can access it;
- silently publish or share my private media associations;
- convert media playback permission into broader account permission;
- treat a similar song as the same song;
- lose timestamps/provenance;
- silently save simulated creative associations as confirmed ones;
- use outside metadata as authority over my own personal meaning;
- hide uncertainty when the exact media segment cannot be reliably identified.

---

# 3. FEATURE FAMILY B — Branches Simulation and Thought-Branch Navigation

## 3.1 The basic idea

A large part of how I think is not linear.

A conversation may start with one subject, split into another, return to the first one, open a third idea, pause it, and later continue from somewhere much earlier.

I want N.H to understand this structure as **branches**, rather than forcing my thinking into one flat sequence.

There are two related but different capabilities:

1. **Branch Navigation** — understanding the branches that actually happened.
2. **Branches Simulation** — temporarily exploring where a branch might go next.

They must remain separate.

---

# 3A. Branch Navigation — the branches that actually happened

## 3A.1 Actual conversation/thought structure

N.H should be able to recognize and preserve structures such as:

- current branch;
- parent branch;
- child branch;
- sibling branch;
- temporarily paused branch;
- unresolved branch;
- returned branch;
- completed branch;
- abandoned branch where that status is actually known;
- branch reopened much later.

A branch may contain another branch, which can itself contain another branch.

The goal is to preserve the **real shape of the conversation and my thinking**, not just the chronological order of messages.

Chronology must still remain intact underneath.

Branch structure must be an additional connected view, not a rewrite of the original conversation.

---

## 3A.2 Returning to old branches

N.H should be able to understand things such as:

- "going back to what I said before";
- "about the other thing";
- "continue the earlier idea";
- "not this branch, the previous one";
- "we'll come back to this";
- a natural return to an older unresolved subject even without exact wording.

N.H may use evidence to propose that I returned to an earlier branch.

If it is uncertain, it must remain uncertain rather than forcing a merge.

---

## 3A.3 Several branches can stay alive

Leaving a subject does not necessarily mean I finished it.

The system should allow several branches to remain open simultaneously.

A branch should not be marked resolved simply because:
- time passed;
- another topic appeared;
- I stopped mentioning it;
- a model predicts that I am done.

This is especially important for long creative, emotional, technical, and planning conversations.

---

## 3A.4 Branch view

Eventually I want the user-facing system to be capable of showing the branch structure in a useful form.

That may later connect naturally to:
- the normal chat;
- memory browser;
- Ness's World;
- project views;
- creation views.

The exact visual form is not decided by this file.

The live design process should decide only what is necessary to make the capability coherent and leave presentation choices to the proper interface package where required.

---

# 3B. Branches Simulation — possible future branches

## 3B.1 Purpose

I want N.H to be able to temporarily explore **possible next branches** of a live conversation or thought process.

The purpose is to help N.H stay mentally ahead without pretending it can predict me.

It may use the confirmed current context to consider possibilities such as:

- I may continue the current subject;
- I may return to an older branch;
- I may need context from another project;
- a particular question may become relevant;
- two branches may be about to connect;
- information can be prepared in case the next confirmed turn needs it.

This is preparation and simulation.

It is not reality.

---

## 3B.2 Critical reality/simulation boundary

A predicted branch is NEVER my actual thought merely because N.H predicted it.

A prediction must not become:

- a real conversation event;
- a root representing something I said;
- a belief attributed to me;
- a confirmed creation;
- a decision;
- evidence that I intended something;
- a Person-Box fact;
- a real branch in conversation history.

Only what actually happens may become the real branch history.

The simulation may be wrong, completely.

That is normal.

---

## 3B.3 Unsent typing

The current N.H design must be checked carefully here.

My feature intent is **not permission for N.H to secretly read unfinished typing**.

Branches Simulation should work from confirmed, authorized context unless a separate later design explicitly establishes an opt-in draft/simulation surface.

The live loop must preserve any already-settled rule that unfinished typing is not observable.

Do not infer permission to inspect keystrokes, drafts, deleted text, or unsent messages from this feature.

---

## 3B.4 Temporary preparation

Branches Simulation may allow N.H to prepare temporary material such as:

- likely relevant context;
- candidate questions;
- possible connections;
- retrieval candidates;
- alternate response directions;
- reminders of unresolved parent branches.

Temporary preparation should disappear or remain simulation-only when it is not used, except for whatever minimal operational record N.H's general transparency rules require.

Simulation output must not gain evidentiary weight simply because it was generated.

---

## 3B.5 Prediction must not distort conversation

N.H must not try to force me toward the branch it predicted.

It must not:

- answer a question I did not ask;
- finish my thought for me as if known;
- treat its prediction as my intention;
- steer conversation merely to make its prediction correct;
- repeatedly surface predicted branches I ignored;
- claim it "knew" what I was going to say.

Predictions are tools for readiness, not control.

---

## 3B.6 Branches and memory

The design should connect Branch Navigation and Branches Simulation to existing N.H systems where appropriate:

- live chat;
- context retrieval;
- creation;
- attention/relevance;
- Living State Web;
- operational logging;
- Wonder/simulation boundary;
- memory browser;
- projects.

But it must preserve the core distinction:

**actual branch history = what happened**  
**branch simulation = what might happen**

---

# 4. FEATURE FAMILY C — Live Physical-World Assistance Using Phone Camera + Location

## 4.1 Status and timing intent

This is a **far-future feature**.

It should not jump ahead of the current N.H build order.

I want it preserved in the design so it is not forgotten, but I do not want it to become a reason to derail or delay the core N.H system.

When this stage is eventually reached, I want the design process to be collaborative rather than an AI unilaterally filling in the experience.

---

## 4.2 Core capability

I want to be able to deliberately open a live session where my phone gives N.H temporary access to information such as:

- the current camera view;
- current location/GPS;
- possibly orientation/movement or other phone context if later justified and authorized.

Then N.H can help me understand or navigate the physical situation I am in.

Examples of the kind of experience I mean:

- "Where am I going?"
- "Which direction should I walk?"
- "What am I looking at?"
- "Where is the entrance?"
- "Which object is the one I need?"
- "Help me navigate this place."
- "Read/understand what is in front of me."
- "Stay with me while I move through this environment."

These are examples of capability, not a settled UI or autonomous-action policy.

---

## 4.3 Deliberate live session, not silent surveillance

The feature must be explicitly activated.

I do not want "camera access" to become:

- permanent background surveillance;
- hidden continuous recording;
- automatic uploading;
- automatic memory ingestion;
- silent location tracking.

A live assistance session and persistent recording are different permissions.

If N.H can answer a real-time question without permanently saving raw video/location history, that should remain a valid design direction.

---

## 4.4 Privacy of other people and places

The camera may see:

- strangers;
- family;
- private homes;
- documents;
- screens;
- addresses;
- faces;
- conversations;
- children;
- sensitive locations.

Therefore live visual assistance needs strong privacy handling.

The eventual design must distinguish at least:

- using a frame temporarily to answer me;
- storing a frame;
- storing extracted information;
- linking information into memory;
- recognizing a person;
- sharing anything externally.

Permission for the first must not silently grant the others.

---

## 4.5 Location is sensitive

Location must remain protected information.

The system must not turn a one-time request like:

> guide me to this entrance

into standing permission to record where I go.

Any historical location feature would need its own deliberate design and permission.

---

## 4.6 No false certainty

N.H must be able to say:

- "I can't see enough";
- "GPS is uncertain";
- "I may be identifying the wrong entrance";
- "the camera view is blocked";
- "I cannot safely tell from this image."

It must not invent physical certainty.

High-impact situations must remain governed by the normal N.H safety and permission rules.

---

# 5. FEATURE FAMILY D — General-Purpose Creation Workspace

## 5.1 Why this is different from the existing Creation concept

N.H already has important Creation concepts around recognizing and preserving creations such as:

- designs;
- ideas;
- rules;
- names;
- decisions;
- provisional creations.

I want to go further.

I want N.H to become an actual **place where I make things with it**, not only a system that notices that I created an idea.

The Creation Store and the Creation Workspace may connect, but they are not necessarily the same responsibility.

The live design process should reuse existing Creation architecture rather than replacing it.

---

## 5.2 What I want to create with N.H

Examples include:

- notes;
- outlines;
- plans;
- explanations;
- letters;
- scripts;
- screenplays;
- stories;
- project documents;
- design documents;
- specifications;
- presentations;
- structured research outputs;
- diagrams;
- images where a capable tool is available;
- data/artifact files;
- eventually software/code where I separately authorize that kind of work.

The important idea is:

**N.H can help produce a real working artifact, not only talk about producing one.**

---

## 5.3 Workspace behavior

I want to be able to work iteratively:

1. create something;
2. inspect it;
3. ask for a change;
4. compare versions;
5. preserve earlier versions;
6. continue later;
7. connect the work to its project/context;
8. deliberately decide when something is final enough for its intended use.

A later revision should not silently destroy the earlier version.

---

## 5.4 Draft is not decision

This is critical.

A document N.H helps me draft is not automatically:

- my settled belief;
- a confirmed N.H design;
- an accepted N.H rule;
- an adopted policy;
- permission to act;
- permission to build;
- a real-world message that has been sent.

For N.H project work in particular:

**creating a design artifact is not the same as accepting the design.**

The workspace must preserve that distinction.

---

## 5.5 Artifact provenance

A created artifact should be able to preserve useful history such as:

- project it belongs to;
- why it was created;
- source material used;
- which parts came from me;
- which parts were proposed/generated by N.H or a tool;
- revisions;
- explicit decisions that shaped it;
- current status;
- links to predecessor/successor versions.

The exact schema belongs to design work.

The meaning requirement is that N.H must not erase authorship/provenance merely because the final artifact reads smoothly.

---

## 5.6 Working with existing files

Eventually I want N.H to be able to help me work on existing artifacts as well.

Examples:

- read a document;
- suggest edits;
- create a new version;
- transform format;
- compare versions;
- update a project artifact;
- create a derivative file.

Existing file protection/version rules must still apply.

No silent overwrite should become the default merely because the Creation Workspace exists.

---

## 5.7 Code and executable work

Eventually, the workspace may include coding/tool-assisted building.

But:

**designing the Creation Workspace is NOT blanket permission for N.H to execute code or change my machine.**

Writing code as an artifact, running code, changing N.H, committing Git changes, and affecting external systems are different permission levels.

They must remain governed by the normal N.H action/authority system.

---

## 5.8 Connection to projects

I want a project to become a real working context.

A project may connect:

- conversations;
- memories;
- research;
- media references;
- files;
- drafts;
- decisions;
- unresolved questions;
- tasks/actions;
- versions.

The Creation Workspace should make it practical to move from:

> "I have an idea"

to:

> "Here is the actual evolving work."

without breaking N.H's distinction between memory, interpretation, proposal, decision, and executed action.

---

# 6. FEATURE FAMILY E — Unified Faceted Memory Search

## 6.1 The basic idea

N.H already has memory retrieval, semantic/positional context, browsing concepts, Person-Boxes, project views, current/history views, and other ways of reaching information.

I also want **one direct human-facing search capability across the complete usable N.H memory**.

I should be able to deliberately search rather than waiting for N.H to surface something.

---

## 6.2 Search dimensions

I want to be able to search/filter by useful dimensions such as:

- person;
- event;
- date or period;
- source;
- conversation/thread;
- project;
- theme;
- status.

Where existing N.H design already defines another appropriate filter, the design may reuse it rather than inventing duplicate categories.

The important capability is that filters can work together.

Example:

> Show me things connected to [person], from [period], in [project], where the status is unresolved.

The exact query language/UI is open unless already settled elsewhere.

---

## 6.3 Search across different kinds of N.H material

A unified search should be able to lead me to appropriate accessible objects such as:

- original roots/source material;
- readings;
- historical readings;
- story-layer material;
- Person-Box material;
- projects;
- creations;
- accepted connections;
- unresolved/proposed connections;
- operational history where I am permitted to view it;
- media references;
- action/result history;
- other future N.H object types.

The search system must not flatten all of these into the same thing.

A source record and an AI interpretation must remain visibly different types of result.

---

## 6.4 Exact source versus interpreted result

Search results should preserve the difference between:

- original material;
- N.H reading;
- human judgment;
- computed/current view;
- simulated material;
- unresolved material.

If I search for:

> "things where I felt abandoned"

N.H may find:
- exact statements where I said that;
- readings that infer something related;
- story-layer material;
- related events.

Those should not all be displayed as equally direct evidence.

---

## 6.5 Positional and semantic search remain distinct

The existing N.H distinction must remain:

- **positional context** = what actually occurred before/after/around an item;
- **semantic retrieval** = other things that appear related in meaning.

Unified search must not blur that.

If a result is semantically related, N.H should not present it as though it was part of the same original conversation.

---

## 6.6 Why a result matched

Where practical, I want the search experience to explain the basis of a result.

Examples:

- exact text match;
- person link;
- project link;
- date range;
- source;
- accepted connection;
- theme;
- semantic similarity;
- current computed relationship.

The system should not need to expose raw internal scoring.

The point is to avoid mysterious results that look authoritative merely because search returned them.

---

## 6.7 Privacy and permission before search

Search is not a bypass around privacy.

A powerful search interface must still obey:

- identity/access;
- private-material rules;
- sealed/restricted material;
- third-party protections;
- influence-removal rules;
- sensitive-data boundaries;
- explicit compartment rules.

"The information exists" does not automatically mean every search mode may display it.

---

## 6.8 Search must not change memory

Searching is read/retrieval behavior.

A search result must not become more true merely because it was retrieved.

Repeated searches must not turn one source into multiple independent pieces of evidence.

Opening a result must not silently accept, promote, merge, or confirm it.

---

## 6.9 Honest empty and failed searches

N.H must distinguish:

- nothing matched;
- results exist but are inaccessible under current permissions;
- search could not complete;
- an index/source is unavailable;
- only weak/uncertain semantic matches exist.

It must not fill an empty search with invented relevance.

---

# 7. Cross-feature connections I want preserved

The five feature families above should not become isolated apps inside N.H.

Where compatible with current architecture, I want them connected.

Examples:

## Media ↔ Creation

A musical moment can become a creative reference for a scene/project.

## Media ↔ Memory

A song may connect to a life period, person, event, or personal meaning.

## Media ↔ Search

I should eventually be able to find:
> songs/segments I connected to this character/project/theme.

## Branches ↔ Chat

The real branch structure comes from actual live conversation.

## Branches ↔ Search

I may want to find the point where one idea branched away from another.

## Branches ↔ Creation

A paused creative branch may later become a separate project idea or draft.

## Branches Simulation ↔ Attention/Context

Possible next branches may help N.H prepare context, but may never become facts.

## Camera/GPS ↔ Live Conversation

Physical-world assistance should feel like talking to N.H while N.H can temporarily see the same environment.

## Camera/GPS ↔ Memory

Persistent memory is a separate permission. A live visual assistance session does not automatically become a stored life record.

## Creation ↔ Search

I should be able to find drafts, versions, project artifacts, and the conversations/decisions that produced them.

---

# 8. Global rules these features must inherit

The live design process must preserve all relevant N.H rules, including at minimum:

## 8.1 Never-close-the-book

N.H interpretation remains revisable.

## 8.2 Ness is the decider

N.H may help, simulate, suggest, and prepare.

Ness owns meaning/policy/acceptance/adoption and real-world authorization where required.

## 8.3 Original material stays distinct from interpretation

A song, message, camera frame, conversation, or file must not be rewritten into an AI interpretation.

## 8.4 Simulation stays simulation

Predicted branches and imagined possibilities never become real events automatically.

## 8.5 Append/preserve history rather than silently overwrite

Changed meaning, changed drafts, changed associations, and corrections should preserve the earlier state where the governing system requires history.

## 8.6 Provenance matters

N.H should be able to answer:
- where this came from;
- who said it;
- what media/source it referred to;
- when the association was made;
- whether it was observed, imported, inferred, generated, simulated, or stated by Ness.

## 8.7 Privacy before convenience

A useful feature is not permission to weaken:
- identity;
- private access;
- third-party privacy;
- protected material handling;
- external-action authorization.

## 8.8 No permission expansion

Permission to:
- play media
does not mean:
- change my account.

Permission to:
- use camera temporarily
does not mean:
- record continuously.

Permission to:
- create a draft
does not mean:
- send/publish it.

Permission to:
- write code
does not mean:
- execute or deploy it.

Permission to:
- search memory
does not mean:
- expose every protected record.

## 8.9 No hidden duplication

If current N.H architecture already has the correct owner for part of these features, extend/connect that owner.

Do not create a parallel:
- memory system;
- connection system;
- creation truth system;
- permission system;
- privacy system;
- Person-Box system;
- simulation-to-reality shortcut.

---

# 9. What I am NOT deciding in this file

This file intentionally does **not** settle technical architecture that should be designed only after the current N.H sources are checked.

It does not decide:

- database schemas;
- exact record names;
- controlled IDs;
- API/provider choices beyond examples such as Spotify;
- exact UI layout;
- exact search syntax;
- final visualization of branches;
- storage engine;
- embedding model;
- music-analysis model;
- camera model;
- GPS framework;
- background-process architecture;
- latency targets;
- exact retention periods;
- exact provider terms/copyright handling implementation;
- final package boundaries;
- final build order unless already required by N.H dependencies.

Those are design/mechanical questions for the proper package.

If one of them is actually already settled by current N.H authority, preserve the existing answer.

---

# 10. Earlier wellbeing/de-escalation ideas — explicitly NOT promoted by this file

Earlier project discussions also contained a set of AI-proposed wellbeing/de-escalation ideas, including things such as:

- physiological sensor fusion;
- a clearance-cue detector;
- safe-approach/ally prompting;
- graduated safe modes;
- a multi-checkpoint re-read logger;
- an arousal-cost dashboard;
- a partial-uncertainty shortcut;
- ally-feedback capture.

**Do not treat those as Ness-approved feature intent from this file.**

They were previously described as proposed ideas requiring evaluation, and some involve health/physiological inference that would require especially careful real-world validation.

If Ness later wants any of them, they must be brought forward separately and checked against the existing Wellbeing/BOP/privacy design.

This file does not authorize or request their design.

---

# 11. Requested live-loop behavior when I supply this file

When I give this file to the future live N.H design loop, interpret my request as:

> I want the feature intent in this file preserved and brought into the N.H design through the normal governed design process.
>
> First check the complete current N.H source and determine what is already present, what needs extension, what is genuinely new, and what depends on other unfinished work.
>
> Do not make me re-decide something already settled.
>
> Do not ask me to solve mechanical architecture.
>
> If there is a genuinely open choice that changes what the feature means, how it behaves for me, what it may do, what it protects, or what it prioritizes, explain that one choice to me plainly and ask it at the proper time.
>
> Otherwise complete the mechanical design automatically through Claude + independent Codex/ChatGPT-style audit according to the controller's current workflow.
>
> Work one package at a time.
>
> Preserve all existing N.H authority, accepted designs, history, privacy, security, simulation boundaries, and permission rules.
>
> Create new versioned candidates only.
>
> Nothing in this file is automatically accepted or adopted.
>
> Do not begin implementation unless I separately authorize building.

---

# 12. Feature-intent summary

The additional capability areas I want preserved for future N.H design are:

### A. Personal Media Meaning and Live Media Experience
A first-class music/media experience inside N.H: playback while talking, exact timestamp awareness, deep musical understanding, personal meaning, and project/scene/character links.

### B. Branches Simulation and Thought-Branch Navigation
Represent the real branching shape of my conversations and temporarily simulate possible next branches without treating prediction or unsent thought as reality.

### C. Live Physical-World Assistance
A far-future, deliberately activated phone-camera + location mode for real-time assistance in the physical world, with strict privacy and no silent persistent surveillance.

### D. General-Purpose Creation Workspace
A real place to make, revise, version, connect, and preserve documents and other artifacts with N.H, while keeping drafts separate from decisions, acceptance, execution, and authority.

### E. Unified Faceted Memory Search
One human-facing search surface over N.H that can combine person/event/date/source/conversation/project/theme/status and return original material, readings, projects, creations, and other accessible objects without flattening their meaning or authority.

---

# 13. Final intent sentence

**I want these features designed as natural extensions of N.H — not bolted-on apps — while keeping the same core N.H laws: preserve the real source, keep interpretations revisable, keep simulation separate from reality, protect privacy and permissions, connect everything honestly, and leave the final decisions to me.**
