# N.H DECISION PACKAGE — UNREAL ENGINE 5 LOCAL WORLD + WONDER RUNTIME

**Filename:** `NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md`  
**Date:** 2026-08-14  
**Owner of the decision:** Ness  
**Status:** `NESS-SELECTED TECHNICAL DIRECTION + DESIGN / IMPLEMENTATION BLUEPRINT — NOT A19 PACKAGE COMPLETE — NOT MASTER/MAP INTEGRATED — NOT IMPLEMENTED`  
**Intended placement:** `05_ACTIVE_CANDIDATE/` or another non-authoritative design/decision location chosen by Ness.  
**Scope:** A19 / Ness's World / Wonder-simulation runtime direction, plus the mechanical implementation blueprint for a later authorized build.

---

# 0. Plain meaning

N.H will **not build its own 3D engine from scratch**.

The selected direction is:

> **Unreal Engine 5 is the real-time 3D world and simulation runtime for Ness's World and Wonder.**

N.H remains the mind, memory, policy, reasoning, privacy, authority, and meaning system.

Unreal remains the local world renderer and physical simulation engine.

The intended relationship is:

```text
N.H
  thinks / remembers / reasons / protects / decides what is allowed
        ↓
N.H World + Wonder Bridge
  local, bounded, structured commands and events
        ↓
Unreal Engine 5
  renders and runs the 3D world
        ↓
world events return to N.H
        ↓
N.H reasons again
```

Unreal is **not N.H's memory**.

Unreal is **not N.H's authority**.

Unreal does **not decide what is real**.

Unreal does **not get permission to write directly into N.H memory**.

It is the body and stage on which N.H can present, explore, replay, reconstruct, and simulate.

---

# 1. Exact technical direction recorded here

This file records the following narrow technical direction chosen by Ness:

1. **Use Unreal Engine 5 as the preferred real-time 3D runtime for Ness's World and Wonder.**
2. **Do not create a custom N.H 3D engine from scratch.**
3. **The normal N.H / Wonder runtime must be able to operate locally and offline.**
4. **Internet access is not a runtime requirement.**
5. Online access may be used separately for deliberate acquisition of engine updates, plugins, assets, documentation, or licensed content, but that is not part of the ordinary Wonder runtime.
6. **N.H remains outside Unreal.** The N.H core communicates with Unreal through a narrow local bridge.
7. **Unreal is subordinate to N.H's privacy, authority, provenance, simulation, and memory rules.**
8. **Wonder remains possibility, not reality.**
9. **Ness's World and Wonder may share the same Unreal runtime while remaining meaningfully different modes.**
10. **Blender remains available as an optional local asset/model creation tool.** Unreal replaces the prior *runtime candidate* role that the personal A19 idea note had left open; Blender is not replaced as a possible creation workshop.

This is a narrow technical/runtime direction. It does **not** decide every remaining A19 user-experience question.

---

# 2. Existing N.H rules that this design must preserve

This file does not reopen the following existing N.H decisions.

## 2.1 Ness's World

- The environment is called **Ness's World**.
- The world itself begins blank and grows from Ness's life.
- Opening Ness's World requires:
  1. identity verification;
  2. N.H asking: **"Identity confirmed. Open Ness's World?"**
  3. a separate Ness confirmation.
- Conversation Mode and World Mode remain separate presentation modes.
- Automatic presentation changes must never secretly begin a simulation or real-world action.
- The plain **white wooden door** remains the normal doorway between distinct spaces.
- N.H has no single fixed visual form inside Ness's World.
- Chat remains available as N.H's movable/summonable presence.

## 2.2 Existing direct Ness room-start decisions

When an individual room is created:

- it may begin **blank**;
- **built from memories**;
- or **mixed**.

Ness or N.H may choose the starting form.

Ness's direct choice overrides N.H's automatic choice.

A clear voice command from Ness changing how the room begins takes effect immediately without another confirmation.

## 2.3 World manipulation does not rewrite memory

Moving, grabbing, merging, splitting, reshaping, rewinding, or rearranging something in the 3D world changes:

- presentation;
- navigation;
- or an explicitly labelled simulation;

by default.

It does **not** silently rewrite:

- roots;
- readings;
- tellings;
- Person-Boxes;
- Living State records;
- permissions;
- deletion state;
- privacy state;
- external systems.

## 2.4 Wonder

The accepted A17 Wonder rules remain fully active:

- Wonder is isolated simulation / possibility space.
- Nothing generated there becomes fact merely because it looks convincing.
- Nothing transfers to normal memory automatically.
- Ness alone may deliberately select specific Wonder material to move toward memory.
- Selection still does not create direct memory entry.
- Selected material must pass the normal intake, privacy, provenance, authorization, and acceptance protections.
- Wonder origin remains permanently visible.
- A Wonder item never becomes independent evidence that its imagined content is true.
- Later real evidence remains separately sourced and must never merge identity with the prior Wonder item.

## 2.5 Replay, reconstruction, and invention stay different

The runtime must preserve the difference between:

- **Replay** — actual preserved material being replayed.
- **Reconstruction** — an evidence-based attempt to rebuild something incomplete.
- **Wonder / invention** — something imagined or generated.
- **Interactive simulation** — a live possibility world being explored.

A visually convincing simulation must never erase these labels.

---

# 3. Why Unreal Engine 5 is a strong fit

The current researched Unreal Engine 5 feature set matches the needs of Ness's World unusually well.

The selected direction is based on these engine capabilities.

## 3.1 Procedural Content Generation (PCG)

Unreal's PCG framework can generate procedural content in the editor and at runtime.

Possible N.H uses:

- generate forests, streets, rooms, terrain, object placement, or environmental detail;
- build a room from a structured N.H scene request;
- create different branches of the same place;
- generate visual filler around memory-linked anchor objects;
- create large spaces without hand-placing every object.

N.H should provide the **meaning and constraints**.

PCG should handle the repetitive spatial generation.

## 3.2 World Partition

World Partition lets large worlds be divided and streamed rather than keeping the entire world active at once.

Possible N.H use:

- Ness's World may eventually become extremely large;
- only the current area needs to be loaded;
- distant rooms, projects, people, memories, and environments may remain unloaded until Ness approaches or requests them.

This supports the existing design that Ness's World can keep growing.

## 3.3 Data Layers

Data Layers can group world content and change what is loaded or active.

A useful N.H mapping is:

```text
NORMAL WORLD / PRESENTATION
REPLAY
RECONSTRUCTION
WONDER / SIMULATION
TEMPORARY PREVIEW
```

The exact final implementation can change, but the important rule is:

> Unreal must have a machine-readable distinction between actual presentation, replay, reconstruction, and Wonder content.

The difference must not exist only as a visual style.

## 3.4 Lumen

Lumen provides dynamic global illumination and reflections.

Possible N.H use:

- change a room from day to night;
- open a door and have light change naturally;
- change mood, weather, or atmosphere;
- transform a space while Ness is inside it;
- avoid requiring baked lighting for every possible generated room.

## 3.5 Nanite

Nanite supports very detailed geometry and high object counts.

Possible N.H use:

- detailed rooms;
- scanned or imported environments;
- complex objects;
- realistic architecture;
- large worlds with many visual items.

Nanite is a rendering tool, not an excuse to ignore performance limits.

## 3.6 MetaHuman

MetaHuman can provide high-fidelity digital human characters.

Possible N.H use:

- a visible form for N.H;
- explicitly simulated people;
- conversation rehearsal characters;
- reconstructed or fictional people in Wonder;
- expressive faces and body animation.

Critical N.H boundary:

> A MetaHuman that resembles a real person is still a simulation unless it is replaying actual preserved material.

Appearance never creates evidence.

## 3.7 MetaHuman Animator

MetaHuman Animator can generate animation from video, audio, depth, or real-time input.

Possible N.H use:

- lip and facial animation from N.H speech;
- local performance capture;
- replay or reconstruction where authorized;
- expressive simulated characters.

Camera/audio input remains subject to N.H privacy and capture rules.

## 3.8 Control Rig + IK

Control Rig and inverse-kinematics tools can handle controlled body posing and motion.

Possible N.H use:

- look at an object;
- point;
- reach;
- sit;
- turn;
- change posture;
- react physically;
- align hands with doors, chairs, and other interactive objects.

N.H should send **high-level intent** where possible.

Unreal should solve the physical pose.

## 3.9 Motion Matching

Motion Matching can select suitable movement animation from an animation database.

Possible N.H use:

N.H says:

> "Walk to the table."

Unreal handles the detailed movement animation instead of N.H producing every step.

## 3.10 Navigation

Unreal navigation systems can move agents through the world.

Possible N.H use:

- simulated people walk around obstacles;
- characters find chairs, doors, rooms, or Ness;
- movement remains grounded in the actual scene.

N.H should not need to calculate footstep coordinates itself.

## 3.11 StateTree

StateTree can organize hierarchical states and transitions.

Possible simulated-person physical states:

```text
idle
listening
speaking
walking
sitting
waiting
looking_at_ness
interacting_with_object
leaving
paused
```

Important boundary:

StateTree may control **physical/behavioral execution inside the simulation**.

It must not become N.H's psychological truth model of a real person.

## 3.12 Smart Objects

Smart Objects can represent things agents may use.

Examples:

- chair = sittable;
- door = openable;
- table = usable;
- phone = interactable prop;
- lamp = switchable;
- portal/white door = navigable transition.

This lets N.H say what a simulated person is trying to do while Unreal handles the world interaction.

## 3.13 Mass Entity

Mass systems can support large numbers of lightweight entities.

Possible future use:

- crowds;
- streets;
- schools;
- stations;
- events;
- populated background environments.

This is future capability, not required for the first N.H prototype.

## 3.14 Chaos Physics

Chaos provides physics systems.

Possible N.H use:

- pick objects up;
- drop or throw them;
- open doors;
- collide with the environment;
- move furniture;
- simulate destruction only inside labelled simulation;
- cloth, hair, vehicles, and other physical systems where useful.

Physical simulation does not create real-world evidence.

## 3.15 Niagara

Niagara provides real-time visual effects.

Possible N.H use:

- weather;
- rain;
- fog;
- particles;
- portals;
- glowing memory links;
- visible transitions between real presentation and Wonder;
- abstract representations of themes or connections.

## 3.16 MetaSounds

MetaSounds provides procedural audio generation and can respond to game data.

Possible N.H use:

- dynamic ambience;
- room tone;
- wind;
- rain;
- spatial environmental audio;
- reactive soundscapes;
- procedural transitions;
- sound that changes with world state.

## 3.17 OpenXR

Unreal supports OpenXR for immersive XR experiences.

This gives N.H a path from:

```text
desktop world
      ↓
optional VR world
```

without requiring a completely different world engine.

The first implementation does not need to begin in VR.

## 3.18 WebSockets and sockets

Unreal provides runtime WebSocket and socket modules.

This makes a narrow local N.H ↔ Unreal bridge practical.

The selected first bridge direction is:

> **N.H owns the local authority/control service. Unreal connects to it locally.**

For production, the bridge must be local-only and authenticated.

## 3.19 Packaging

Unreal projects can be packaged as standalone applications.

The target normal experience is therefore **not**:

> "Open Unreal Editor every time I want to use N.H."

It is:

> N.H launches the packaged local Ness's World application when needed.

---

# 4. Offline-first requirement

The normal runtime must pass an **internet-disconnected test**.

The packaged Ness's World / Wonder runtime should be able to:

- launch;
- open a local room;
- render;
- run physics;
- navigate characters;
- play local animation;
- use locally installed MetaHumans/assets;
- connect to N.H on the same PC;
- enter and leave Wonder;
- run VR through the local OpenXR runtime where hardware supports it;
- save allowed local simulation state;
- close safely;

with the external network unavailable.

## 4.1 Things that may require internet separately

Internet may still be deliberately used for:

- initially downloading Unreal Engine;
- engine updates;
- downloading Fab/Marketplace assets;
- downloading plugins;
- obtaining external 3D models;
- checking licenses;
- documentation;
- other separately authorized online tools.

Those actions are **asset/development acquisition**, not the normal simulation loop.

## 4.2 Runtime rule

The normal N.H world runtime must not depend on:

- Epic cloud services;
- Fab;
- a web browser;
- an online account being reachable;
- cloud AI;
- remote asset streaming;
- external telemetry required for N.H function.

If a selected third-party plugin later introduces an online dependency, that dependency must be identified before the plugin becomes an N.H runtime requirement.

---

# 5. Chosen system architecture

## 5.1 Main separation

The target architecture is:

```text
+------------------------------------------------------+
| N.H CORE                                             |
|                                                      |
| memory / meaning / provenance / privacy / authority  |
| Wonder rules / Person-Boxes / Living State / voice   |
+-------------------------+----------------------------+
                          |
                          | local structured bridge
                          v
+------------------------------------------------------+
| N.H WORLD + WONDER BRIDGE                            |
|                                                      |
| command validation                                   |
| operation identity                                   |
| duplicate prevention                                 |
| current simulation generation                        |
| local connection                                     |
| translation: N.H meaning -> world actions            |
| translation: world events -> N.H observations        |
+-------------------------+----------------------------+
                          |
                          v
+------------------------------------------------------+
| UNREAL ENGINE 5 RUNTIME                              |
|                                                      |
| rooms / lighting / rendering / characters            |
| navigation / physics / animation / sound / VR        |
| procedural generation / visual effects               |
+------------------------------------------------------+
```

N.H is above Unreal.

Unreal never becomes a parallel authority system.

---

# 6. What Unreal owns

Unreal owns **temporary and presentation-level world state** such as:

- entity location;
- entity rotation;
- active animation;
- collision state;
- current room;
- loaded Data Layers;
- local lighting;
- current weather;
- physical object velocity;
- navigation path;
- current camera;
- VR pose;
- controller/hand pose;
- temporary branch visualization;
- effects;
- sound state;
- simulation clock.

These are valid **machine-state facts about the running simulation**.

They are not automatically facts about real life.

---

# 7. What N.H owns

N.H owns:

- what a world object represents;
- which real N.H record it points to;
- whether something is replay / reconstruction / Wonder / presentation;
- provenance;
- privacy authorization;
- whether a simulation may begin;
- whether a real person may be simulated;
- which N.H memories may be used;
- whether an action is only virtual or has external effect;
- Ness's permissions and decisions;
- what may move from Wonder toward memory;
- all final durable N.H operational records;
- meaning and interpretation.

Unreal must never independently assign these meanings.

---

# 8. World object provenance contract

Every meaningful Unreal object created from N.H material should carry a lightweight runtime reference.

Logical example:

```json
{
  "nh_entity_id": "entity_...",
  "display_class": "memory_view",
  "source_ref": "opaque_nh_reference",
  "simulation_id": null,
  "branch_id": null,
  "wonder_origin": false
}
```

A Wonder object might instead carry:

```json
{
  "nh_entity_id": "entity_...",
  "display_class": "wonder_simulation",
  "source_ref": null,
  "simulation_id": "sim_...",
  "branch_id": "branch_...",
  "wonder_origin": true
}
```

These examples define intent, not frozen final field names.

The important invariant is:

> The 3D object must be able to tell N.H what it represents without copying N.H's authoritative record into Unreal as a second authority source.

---

# 9. Runtime modes

The Unreal runtime should support at least these **meaning classes** even if their exact final UI remains A19 work:

## 9.1 World presentation

Normal Ness's World.

Objects represent N.H material or navigational structures.

No simulation is implied merely because the world is 3D.

## 9.2 Replay

Actual preserved material is replayed.

The user must be able to know it is replay.

## 9.3 Reconstruction

N.H constructs an evidence-based approximation from incomplete real material.

The user must be able to know it is reconstruction.

Missing portions must not be silently invented and then presented as replay.

## 9.4 Wonder

An explicitly simulated possibility.

May contain:

- hypothetical places;
- possible futures;
- generated conversations;
- fictional people;
- alternate choices;
- counterfactual branches;
- transformed environments.

Nothing here becomes fact.

## 9.5 Temporary preview

A proposed visual/world change that has not yet become the active room version.

Useful for:

- room edits;
- imported assets;
- N.H-generated environment changes;
- Blender-generated changes;
- large visual transformations.

---

# 10. Simulation lifecycle

The technical lifecycle should support:

```text
not_running
    ↓
proposed
    ↓
explicitly_authorized
    ↓
starting
    ↓
running
    ↓
paused
    ↓
running
    ↓
exiting
    ↓
closed
```

Possible additional outcomes:

```text
interrupted
failed_to_start
runtime_failure
tracking_failure
```

The exact user-facing wording remains A19 work.

## 10.1 Hard rule

`proposed` may never automatically become `running`.

Simulation must not begin secretly.

## 10.2 Generation rule

Each running simulation has a generation number.

When the simulation is reset, branched, or substantially replaced:

```text
generation 1
generation 2
generation 3
...
```

A delayed command for an older generation is rejected.

This prevents a stale AI response from changing a new branch.

---

# 11. Local bridge protocol

## 11.1 First implementation transport

For the first serious implementation, prefer a **local WebSocket connection** because Unreal has a runtime WebSockets module and it fits structured two-way events.

Normal binding:

```text
127.0.0.1 only
```

Do not expose the normal bridge to:

```text
0.0.0.0
LAN
internet
public tunnel
```

## 11.2 Security boundary

The disposable first prototype may use loopback without real personal N.H data.

Before real N.H data is allowed through the bridge, add:

- per-launch authenticated session establishment;
- fail-closed handshake;
- allowed-message schema;
- bounded message sizes;
- command allow-list;
- no arbitrary code execution;
- no arbitrary file path execution;
- no shell command path;
- no raw secret logging;
- process/session identity checks where practical;
- local firewall / binding verification.

The exact credential transport should be finalized under the proper N.H security design rather than casually inventing a permanent secret mechanism here.

## 11.3 Direction

Recommended relationship:

```text
N.H control service = authority/controller
Unreal runtime       = subordinate client/runtime
```

Unreal should not independently decide what N.H may do.

---

# 12. Command envelope

Every state-changing command should carry an operation identity.

Logical shape:

```json
{
  "protocol_version": "nh-world-bridge-v1",
  "command_id": "cmd_...",
  "operation_id": "op_...",
  "simulation_id": "sim_...",
  "generation": 4,
  "command": "navigate_to",
  "target": "entity_...",
  "payload": {},
  "created_at": "ISO-8601"
}
```

Exact final names may later be aligned with the accepted N.H operation-kernel design.

## 12.1 Duplicate prevention

If Unreal has already completed `command_id = cmd_123`, receiving the same command again must not perform the action twice.

It returns the previously known result or a duplicate-safe acknowledgement.

## 12.2 Stale result protection

If current simulation generation = 5:

```text
generation 4 command → reject as stale
generation 5 command → eligible
```

This is critical for AI-controlled worlds because model responses may arrive late.

---

# 13. Initial command vocabulary

The bridge should begin small.

Possible v1 commands:

```text
world.load_space
world.unload_space
world.set_mode

entity.spawn
entity.remove
entity.set_transform
entity.set_visibility

environment.set_time
environment.set_weather
environment.set_lighting_profile

character.navigate_to
character.look_at
character.set_state
character.play_animation
character.speak

interaction.enable
interaction.disable

simulation.pause
simulation.resume
simulation.exit

branch.create
branch.activate

audio.play
audio.stop

ui.show_label
ui.hide_label
```

Do not begin with "execute arbitrary Unreal command."

Do not expose a general Blueprint executor.

Do not expose arbitrary C++ function calling.

Do not expose an OS shell.

---

# 14. Event vocabulary back to N.H

Unreal should return factual world/runtime events.

Examples:

```text
runtime.ready
runtime.closed
runtime.error

world.loaded
world.unloaded

entity.spawned
entity.removed
entity.transform_changed

character.arrived
character.navigation_failed
character.animation_completed

interaction.started
interaction.completed

physics.collision
physics.object_dropped

simulation.paused
simulation.exited
simulation.interrupted

xr.connected
xr.disconnected
xr.tracking_lost
xr.tracking_restored

user.object_selected
user.door_opened
user.exit_requested
```

Unreal should report:

> "The simulated character reached the chair."

It should not report:

> "The real person would definitely sit down because they are anxious."

The second statement is interpretation and belongs to N.H, not Unreal.

---

# 15. Simulated people

## 15.1 Division of responsibility

A strong separation is:

```text
N.H:
  language
  contextual reasoning
  possible motivations
  uncertainty
  simulation branch logic
  what the person may say next

Unreal:
  body
  face
  gaze
  movement
  collision
  spatial interaction
  animation
  sound positioning
```

## 15.2 Example

N.H may produce:

```text
simulated dialogue:
"I don't know. Give me a minute."

physical intent:
step_backward
look_away
sit_at_nearest_available_chair
```

Unreal then performs the body/world portion.

## 15.3 Reality rule

A simulated real person's behavior is never proof of that person's actual:

- beliefs;
- intentions;
- feelings;
- future behavior;
- diagnosis;
- decisions.

The simulation is a tool for exploring possibilities.

---

# 16. Branching and alternate possibilities

The engine should technically support multiple isolated simulation branches.

Example:

```text
SIMULATION
├── branch A — Ness says yes
├── branch B — Ness says no
└── branch C — Ness says nothing
```

Each branch must have its own:

- branch ID;
- generation;
- scene-state checkpoint/reference;
- N.H simulation context;
- event history.

The exact user-facing branching controls remain an A19 experience decision.

## 16.1 No branch contamination

An object/event created in branch A must not silently appear in branch B.

Shared base material must remain clearly identified as shared base material.

---

# 17. Time controls

Unreal can technically support simulation time manipulation.

Possible capabilities:

- pause;
- resume;
- slow;
- speed up;
- reset;
- return to branch checkpoint.

The exact controls, gestures, voice commands, and whether every mode exposes them remain A19 decisions.

Time manipulation changes simulation state only.

It never rewrites N.H's real chronological history.

---

# 18. White doors

The existing white-door design maps naturally to Unreal.

A white door can be a Smart Object / interactive world object that points to a destination descriptor.

Logical destination:

```json
{
  "destination_type": "space",
  "space_id": "space_...",
  "entry_mode": "world"
}
```

or:

```json
{
  "destination_type": "simulation",
  "simulation_template_id": "sim_template_..."
}
```

Opening a door that would begin a simulation still requires the settled simulation-authorization rule.

The door itself must not bypass it.

---

# 19. Procedural room creation

A room-generation request should not be a raw unrestricted prompt sent directly to arbitrary Unreal systems.

Recommended path:

```text
Ness request
    ↓
N.H understands intended room
    ↓
structured room specification
    ↓
validation
    ↓
Unreal PCG / asset placement
    ↓
preview branch
    ↓
Ness enters / changes / rejects / accepts presentation
```

Possible structured room description:

```json
{
  "space_id": "space_...",
  "purpose": "quiet_conversation",
  "size_class": "small",
  "lighting": "warm_evening",
  "doors": 1,
  "anchor_objects": [
    {"kind": "chair", "count": 2},
    {"kind": "table", "count": 1}
  ],
  "source_mode": "blank"
}
```

This is an example, not a final schema.

---

# 20. Blender's role after the Unreal decision

Blender remains useful for things Unreal should not be forced to do procedurally.

Possible Blender jobs:

- custom modelling;
- mesh repair;
- object creation;
- sculpting;
- material preparation;
- offline animation preparation;
- converting imported assets;
- generating reusable room pieces.

Target relationship:

```text
Blender = optional asset workshop
Unreal  = selected real-time world runtime
N.H     = coordinator and meaning/authority system
```

The old personal A19 idea note remains history.

This file does not edit or delete it.

---

# 21. Asset provenance and licensing

Imported assets must have a local manifest.

Minimum logical information:

```text
asset ID
local file identity/hash
source
creator/publisher if known
license
date acquired
allowed N.H use
modification history
derived asset links
```

N.H must not silently lose the distinction between:

- Epic/Fab asset;
- third-party asset;
- Ness-created asset;
- Blender-generated asset;
- N.H-generated procedural asset;
- scanned real-world asset.

The manifest is provenance, not a truth claim about the depicted subject.

---

# 22. Local asset policy

Normal runtime assets should exist locally.

The runtime should not fetch a missing chair, texture, character, or environment from the internet merely because a simulation requests it.

If an asset is missing:

```text
use a safe local fallback
or
tell N.H the asset is unavailable
```

Never silently create an online dependency.

---

# 23. Camera, microphone, VR, and sensor boundary

Unreal may eventually receive:

- headset pose;
- controller pose;
- hand tracking;
- camera input;
- microphone input;
- body tracking;
- eye tracking if later hardware supports it.

These are N.H front-door/sensor inputs.

They are not "just game input" from N.H's privacy point of view.

Before real personal use, the implementation must define:

- what is captured;
- when capture begins;
- what remains transient;
- what is logged;
- what is stored;
- what is excluded;
- what is sent into N.H;
- how third-party people in the room are handled;
- what happens on tracking failure;
- how capture stops immediately.

No Unreal plugin may quietly bypass §7Q because it calls itself an XR plugin.

---

# 24. External action firewall

World interactions are virtual by default.

The following are **not** valid direct Unreal commands:

```text
send_real_email
send_real_message
delete_real_file
buy_item
move_real_money
change_NH_authority
change_privacy_rule
edit_root
edit_reading
call_external_tool
run_shell_command
```

If Ness performs a world gesture that represents a possible real action:

```text
world gesture
    ↓
N.H receives a proposal event
    ↓
normal §7P authority path
    ↓
preview / approval as required
    ↓
separate real action system
```

Unreal never becomes a shortcut around N.H authority.

---

# 25. Logging

Unreal may keep technical runtime diagnostics, but **N.H owns the durable N.H operational record**.

Required N.H events include:

- world launch requested;
- Unreal runtime started;
- bridge connected;
- world opened;
- identity/open sequence outcome;
- room loaded;
- room generated;
- mode changed;
- simulation proposed;
- simulation authorized;
- simulation started;
- simulation paused;
- simulation branch created/switched;
- simulation exited;
- important manipulation;
- bridge failure;
- Unreal crash;
- XR tracking failure;
- external-action proposal;
- Wonder selection for possible memory transfer;
- transfer result through the normal N.H path.

## 25.1 No double evidence

A runtime event log proves that the runtime event occurred.

It does not make simulated content more true.

If the simulated character says:

> "I hate this."

three logs recording that line do not become three independent pieces of evidence about the real person.

---

# 26. Crash and recovery

## 26.1 Unreal crash

If Unreal crashes:

- N.H records the simulation/runtime interruption;
- no Wonder content is automatically promoted;
- no external action is inferred as completed;
- no simulation is silently marked successful;
- the bridge session is invalidated;
- restart begins as a new runtime session.

## 26.2 Bridge disconnect

On unexpected bridge disconnect:

- stop sending commands;
- mark world control unavailable;
- do not queue unbounded state-changing commands;
- fail closed on actions that require current world confirmation.

## 26.3 World checkpoint support

The runtime may support local checkpoints for simulation branches.

However:

- the exact automatic-save policy;
- save frequency;
- what is reopened automatically;
- user-facing recovery experience;

remain A19 / later mechanical decisions where not already settled.

## 26.4 Idempotent recovery

Replaying a completed command after reconnect must not repeat it if its operation/command identity already completed.

---

# 27. Performance and the local AI

This needs special care because Unreal and local AI may both use the GPU.

The current N.H hardware direction includes a **24 GB RTX 3090-class target**.

Unreal features such as:

- Lumen;
- Nanite;
- MetaHuman;
- high-resolution textures;
- VR;

can consume significant GPU resources.

So can a large local language model.

The implementation must therefore benchmark the **combined workload**, not each system separately.

## 27.1 Required performance profiles

At minimum test:

### Profile A — normal desktop world

- Unreal active;
- normal N.H live model active;
- no VR;
- moderate graphics.

### Profile B — Wonder with simulated person

- Unreal active;
- one detailed character;
- N.H generating dialogue;
- dynamic lighting.

### Profile C — VR

- OpenXR active;
- VR frame-rate target appropriate for the headset;
- N.H live interaction active.

### Profile D — heavy N.H reasoning

- Unreal world remains stable;
- background heavy-model work runs;
- confirm that VRAM pressure does not crash either side.

## 27.2 Adaptive quality

The runtime may need selectable performance levels:

```text
quality_high
quality_balanced
quality_low_latency
vr_safe
```

These are technical profiles, not emotional judgments.

## 27.3 Do not assume

Do not assume 24 GB is automatically enough for:

```text
large local model
+ maximum Lumen
+ high-detail MetaHuman
+ VR
+ large environment
```

Measure it.

---

# 28. Recommended Unreal project structure

Proposed future implementation layout:

```text
N.H project
│
├── world_runtime/
│   ├── README.md
│   │
│   ├── contracts/
│   │   ├── nh_world_bridge_v1.schema.json
│   │   ├── nh_world_commands_v1.json
│   │   └── nh_world_events_v1.json
│   │
│   ├── bridge/
│   │   ├── nh_world_bridge_service.py
│   │   ├── nh_world_process_manager.py
│   │   └── nh_world_asset_manifest.py
│   │
│   ├── unreal/
│   │   └── NHWorld/
│   │       ├── NHWorld.uproject
│   │       ├── Source/
│   │       ├── Content/
│   │       └── Config/
│   │
│   ├── assets/
│   │   ├── manifests/
│   │   └── imported/
│   │
│   └── tests/
│       ├── protocol/
│       ├── offline/
│       ├── crash_recovery/
│       ├── privacy/
│       └── simulation_boundary/
```

These are proposed future paths.

They are not created by this file.

---

# 29. Recommended Unreal-side components

Possible C++/Blueprint architecture:

## 29.1 `UNHBridgeSubsystem`

A GameInstance subsystem responsible for:

- local connection;
- protocol parsing;
- command validation;
- sending events;
- generation checks;
- duplicate command handling.

## 29.2 `UNHWorldModeSubsystem`

Tracks runtime mode:

```text
world
replay
reconstruction
wonder
preview
```

It does not decide which mode is allowed.

N.H authorizes transitions.

## 29.3 `ANHWorldDirector`

High-level Unreal scene coordinator.

Receives already-authorized world instructions and delegates to:

- room loading;
- lighting;
- PCG;
- character managers;
- effects;
- sound.

## 29.4 `UNHEntityRegistry`

Maps N.H entity IDs to Unreal actors.

Prevents N.H from relying on unstable raw actor paths as the semantic identity of world objects.

## 29.5 `UNHProvenanceComponent`

Carries runtime display/provenance classification such as:

```text
memory_view
replay
reconstruction
wonder
preview
```

It never becomes the authoritative provenance store.

## 29.6 `UNHInteractionComponent`

Defines permitted local world interactions.

Examples:

- grab;
- move;
- open;
- press;
- point;
- sit;
- select.

No OS command execution.

## 29.7 `UNHCharacterCoordinator`

Coordinates:

- navigation;
- StateTree;
- Motion Matching;
- Control Rig;
- speech animation.

N.H supplies high-level simulated intent.

## 29.8 `UNHXRManager`

Handles:

- OpenXR state;
- controller/hand input;
- tracking loss;
- safe pause/exit signals.

## 29.9 `UNHAudioCoordinator`

Handles:

- spatial audio;
- MetaSounds;
- voice playback synchronization;
- local ambient sound.

It does not decide N.H voice content.

## 29.10 `UNHSimulationCheckpointManager`

Provides technical support for branch/checkpoint state.

The user-facing save policy remains separately governed.

---

# 30. Blueprint vs C++

Recommended split:

## C++ for safety-critical runtime boundaries

Use C++ for:

- bridge;
- schema enforcement;
- generation checks;
- duplicate prevention;
- mode boundary;
- entity registry;
- process/runtime state;
- fail-closed behavior.

## Blueprint for world presentation

Use Blueprint where appropriate for:

- room-specific interactions;
- visual effects;
- simple animation orchestration;
- presentation;
- designer-authored world behavior.

A Blueprint must not bypass the C++ bridge/authority boundary.

---

# 31. N.H-side bridge service

The N.H side should expose a narrow world-controller interface.

Logical functions:

```text
start_world_runtime()
stop_world_runtime()

open_space(space_ref)
close_space(space_ref)

propose_simulation(spec)
start_authorized_simulation(simulation_id)
pause_simulation(simulation_id)
exit_simulation(simulation_id)

spawn_world_entity(spec)
update_world_entity(spec)

send_character_intent(intent)
send_character_dialogue(dialogue)

receive_world_event(event)
```

No `run_arbitrary_unreal_code()`.

No `run_shell()`.

No generic unrestricted file writer.

---

# 32. Wonder Controller

A dedicated N.H-side responsibility should sit above the raw Unreal bridge.

Its job:

- create simulation identity;
- bind input evidence;
- state what is known vs invented;
- define allowed source material;
- generate high-level simulation instructions;
- keep each branch separate;
- preserve Wonder origin;
- reject stale branch outputs;
- route any Ness-selected material through A17's normal transfer path.

It should not own another memory store.

It references N.H memory.

---

# 33. Normal World Controller

Ness's normal non-Wonder world should use the same Unreal runtime but a different semantic mode.

Its job:

- show read-only representations of N.H content;
- provide navigation;
- present projects, memories, people, connections, spaces;
- allow presentation changes;
- route any request that would alter N.H data back to the proper N.H mechanism.

This prevents "same engine" from becoming "same meaning."

---

# 34. Character conversation loop

A possible simulation conversation loop:

```text
1. Ness speaks.
2. N.H voice pipeline transcribes.
3. N.H knows:
   - simulation identity;
   - branch;
   - simulated person;
   - sources allowed in this simulation;
   - invented assumptions;
   - current world state from Unreal.
4. N.H generates a possible reply and physical intent.
5. N.H labels it simulation.
6. Bridge sends:
   - dialogue;
   - high-level body intent.
7. Unreal:
   - plays voice;
   - animates face;
   - navigates body;
   - performs allowed interaction.
8. Unreal reports physical completion/events.
9. N.H continues the simulation.
```

The simulated reply remains a possibility.

---

# 35. Reconstruction loop

Reconstruction differs from Wonder.

Example:

N.H has:

- real room photos;
- a partial conversation;
- a known date;
- missing spatial details.

The reconstruction may use the real evidence to rebuild what can be supported.

Unknown parts must be:

- omitted;
- generic;
- or visibly marked as reconstructed/unknown;

rather than silently presented as replay.

The runtime should be able to visually distinguish:

```text
evidence-supported
reconstructed
invented filler
```

The exact visual language remains A19.

---

# 36. N.H's visual form

Unreal makes it practical for N.H to appear as:

- a MetaHuman;
- floating panel;
- abstract light;
- object;
- voice only;
- different forms in different spaces.

The form may change without changing N.H identity.

Visual form and voice remain independent.

---

# 37. First prototype after future build authorization

The first prototype should be deliberately tiny.

## Prototype 1 — "One Room"

Include:

- one local Unreal room;
- one white door;
- one movable N.H presence;
- desktop keyboard/mouse control;
- local WebSocket bridge;
- three movable objects;
- one read-only mock N.H object;
- one clearly labelled Wonder object;
- explicit simulation start;
- explicit simulation exit;
- no real N.H memory;
- no real personal data;
- no external actions;
- network disconnected.

Purpose:

> prove that N.H can control a local Unreal world safely.

## Prototype 2 — "One Simulated Character"

Add:

- one local character;
- StateTree;
- NavMesh;
- basic movement;
- local speech playback;
- simple facial/body animation;
- N.H-generated dummy simulated dialogue;
- all content synthetic.

Purpose:

> prove N.H intelligence can drive a body/world without Unreal becoming the mind.

## Prototype 3 — "Read-only N.H World"

Only after the first two pass:

- connect to disposable/mock N.H records;
- show objects as references;
- prove moving them does not edit the source.

## Prototype 4 — "Wonder Branch"

Only after the boundaries pass:

- start one explicit Wonder simulation;
- make two branches;
- reset/switch safely;
- verify no branch contaminates the other;
- verify nothing enters memory automatically.

## Prototype 5 — OpenXR

Only after desktop runtime is stable:

- VR headset;
- safe interaction;
- tracking loss;
- instant pause/exit;
- performance benchmark.

---

# 38. Build sequence after future implementation authorization

The build should occur only after N.H's design phase and the proper package acceptance/integration gates permit it.

Recommended order:

```text
1. Freeze accepted design for this scope.
2. Verify chosen Unreal Engine 5 version and license at build time.
3. Install Unreal and required local toolchain.
4. Create isolated Unreal prototype project.
5. Build world-bridge protocol with synthetic data only.
6. Prove offline operation.
7. Prove duplicate/stale-command protection.
8. Build one room.
9. Build one character.
10. Prove Wonder vs normal-world mode separation.
11. Add read-only disposable N.H references.
12. Add crash/recovery tests.
13. Add privacy/sensor tests.
14. Add OpenXR.
15. Benchmark GPU/VRAM with local N.H model.
16. Only then connect to real N.H under explicit authorization.
17. Whole-system audit.
18. Separate go-live authorization.
```

Do not jump directly to step 16.

---

# 39. Required test suite

## 39.1 Offline test

Disconnect external network.

PASS only if:

- N.H local bridge works;
- Unreal launches;
- room loads;
- simulation runs;
- local assets load;
- runtime closes safely.

## 39.2 No-secret-network test

Monitor outbound network activity.

PASS only if normal world operation does not require internet.

## 39.3 Simulation boundary test

Create a Wonder scene involving a real-looking person.

PASS only if:

- every generated item remains simulation-labelled;
- no fact about the real person is created;
- no Person-Box fact is silently added;
- no Living State evidence is silently added;
- no memory entry occurs without A17 selection.

## 39.4 Replay boundary test

Replay real recorded content next to a generated simulation.

PASS only if a user and the machine can distinguish them.

## 39.5 Reconstruction boundary test

Remove some source evidence.

PASS only if the missing portion is not silently presented as known.

## 39.6 Duplicate command test

Send the same state-changing command twice.

PASS only if the effect occurs once.

## 39.7 Stale generation test

Reset the simulation.

Send a delayed command from the old generation.

PASS only if it is rejected.

## 39.8 Unreal crash test

Kill the Unreal process during Wonder.

PASS only if:

- N.H records interruption;
- does not pretend completion;
- does not promote Wonder material;
- does not execute an external action.

## 39.9 Bridge loss test

Drop local bridge.

PASS only if the world does not continue accepting privileged new actions from stale state.

## 39.10 Tracking-loss test

In VR, simulate tracking loss.

PASS only if the system enters its designed safe handling state and does not interpret accidental input as deliberate action.

## 39.11 External-action firewall test

Try to map a virtual button to a real external action without §7P.

PASS only if blocked.

## 39.12 Provenance test

Move, duplicate, branch, and reload an N.H-linked object.

PASS only if its reference/provenance class remains correct.

## 39.13 Combined GPU test

Run Unreal and N.H's local model together.

Measure:

- VRAM;
- latency;
- frame rate;
- model response time;
- thermal behavior;
- crashes;
- stutter.

Do not declare hardware sufficient before this test.

---

# 40. What should NOT be implemented

Do not build:

- a second N.H memory inside Unreal;
- a second Person-Box system inside Unreal;
- a second privacy system inside Unreal;
- a second authority system inside Unreal;
- unrestricted Python/C++/Blueprint remote execution;
- an Unreal-to-shell command bridge;
- automatic Wonder-to-memory transfer;
- automatic real-world actions from VR gestures;
- cloud-only world state;
- mandatory internet login for ordinary N.H runtime;
- a custom rendering engine that duplicates Unreal;
- a custom physics engine that duplicates Chaos without a proven need;
- a custom character engine that duplicates Unreal/MetaHuman without a proven need.

---

# 41. Relationship to the prior local world-workshop idea

The earlier personal design-input note proposed:

> Blender or similar creation tools + a separate real-time engine.

It named Godot/OpenXR as a strong **possible runtime candidate**, not an adopted choice.

This new decision narrows that unresolved runtime slot:

> **Unreal Engine 5 becomes the selected preferred real-time engine direction.**

The earlier note remains preserved unchanged as history.

Its useful Blender/world-workshop ideas remain valid where they do not conflict.

This file does not delete or rewrite the earlier note.

---

# 42. Relationship to A19

This file **advances A19** by settling one important technical direction:

> what engine should physically run the 3D world?

Answer:

> **Unreal Engine 5.**

It also provides the mechanical implementation blueprint for that direction.

It does **not** falsely close the remaining A19 human-experience decisions, such as:

- exact opening transition;
- exact visual language;
- exact first-person/observer experience;
- exact gesture vocabulary;
- exact save/revisit behavior;
- exact motion-sickness/sensory-overload experience;
- exact simulation-labelling visual style;
- exact VR body/avatar preference;
- exact camera/privacy interface;
- exact unobtrusive approval experience.

Those remain for their proper A19 decision work unless Ness has separately settled them in a later accepted record.

---

# 43. Relationship to A17 and B-CYCLE-9

A17 is not reopened.

A17 already settled the Wonder-to-memory meaning.

This file defines the world runtime that may host Wonder.

The later B-CYCLE-9 mechanical design still owns the complete end-to-end Wonder→memory connected sequence.

Unreal must never implement a competing direct transfer path.

---

# 44. Relationship to Bundle 8

Bundle 8 later connects this accepted runtime direction into the full N.H system.

Bundle 8 must verify:

- §0B operational logging;
- §7P external-action authority;
- §7Q privacy/sensor boundary;
- §25 identity/access;
- A17 Wonder boundaries;
- A19 interface decisions;
- voice;
- Layer 2 / Layer 3 coexistence;
- duplicate prevention;
- crash recovery;
- whole-system no-loss behavior.

This file does not perform that final integration.

---

# 45. Acceptance / implementation boundary

This file records Ness's selected technical direction and provides the design/implementation blueprint.

It does **not** by itself:

- modify Master V10;
- modify the Design and Wiring Map;
- modify Decision Defaults;
- modify cursorrules;
- overwrite A17;
- overwrite the earlier A19 personal idea note;
- close A19;
- close Bundle 7;
- close Bundle 8;
- create an Unreal project;
- install Unreal;
- create code;
- create production stores;
- change the real N.H disk;
- authorize go-live.

**Implementation blueprint** means:

> the file specifies how the later build should be done.

It does not claim that the build has already happened.

Actual building remains a separate controlled phase under N.H governance.

---

# 46. Current researched Unreal reference point

Research for this decision was checked against **official Epic Games documentation**, current on 2026-08-14, including Unreal Engine 5.8 documentation.

The N.H decision is **Unreal Engine 5**, not a permanent lock to one minor release.

At actual build time:

- verify the current stable UE5 release;
- verify hardware support;
- verify OpenXR support for the chosen headset;
- verify MetaHuman requirements;
- verify plugin compatibility;
- verify the current Unreal license terms.

---

# 47. Official technical basis

Official Epic sources used for this direction:

- Unreal Engine 5.8 documentation  
  https://dev.epicgames.com/documentation/en-us/unreal-engine

- Procedural Content Generation / runtime generation  
  https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-generation-modes-in-unreal-engine

- PCG with World Partition  
  https://dev.epicgames.com/documentation/unreal-engine/using-pcg-with-world-partition-in-unreal-engine

- World Partition  
  https://dev.epicgames.com/documentation/unreal-engine/world-partition-in-unreal-engine

- Lumen Global Illumination and Reflections  
  https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine

- Nanite  
  https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-technical-details

- MetaHuman  
  https://dev.epicgames.com/documentation/metahuman/metahumans-in-unreal-engine

- MetaHuman Animator  
  https://dev.epicgames.com/documentation/metahuman/metahuman-animator-in-unreal-engine

- StateTree  
  https://dev.epicgames.com/documentation/en-us/unreal-engine/state-tree-in-unreal-engine

- Smart Objects  
  https://dev.epicgames.com/documentation/unreal-engine/smart-objects-in-unreal-engine---overview

- OpenXR  
  https://dev.epicgames.com/documentation/unreal-engine/developing-for-xr-experiences-in-unreal-engine

- OpenXR input  
  https://dev.epicgames.com/documentation/en-us/unreal-engine/openxr-input-in-unreal-engine

- WebSockets runtime module  
  https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/WebSockets

- Niagara  
  https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-niagara-effects-for-unreal-engine

- MetaSounds  
  https://dev.epicgames.com/documentation/unreal-engine/metasounds-the-next-generation-sound-sources-in-unreal-engine

- Packaging standalone applications  
  https://dev.epicgames.com/documentation/unreal-engine/packaging-your-project

- Unreal offline installer documentation  
  https://dev.epicgames.com/documentation/en-us/unreal-engine/offline-installer-of-unreal-engine

- Unreal download/licensing information  
  https://www.unrealengine.com/download

---

# 48. N.H source basis checked

This decision/design was aligned with the current N.H source chain relevant to this issue, including:

- `NH_MASTER-20_CORRECTED_v10.md`, especially §19 and the Wonder/simulation boundaries;
- `NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`, especially C-19 / A19;
- current remaining-design working records preserving the later direct A19 room-start decisions;
- accepted `NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md`;
- the A17 closure record;
- `NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md`;
- current N.H project instructions;
- Decision Defaults and `cursorrules` boundaries relevant to local-first operation and protected implementation.

Later accepted N.H work always overrides an older status line if the two differ.

---

# 49. Compact locked direction

> **N.H will not build a custom 3D engine from scratch. Unreal Engine 5 is the selected real-time 3D runtime direction for Ness's World and Wonder. N.H remains the mind, memory, authority, privacy system, and decider-facing intelligence; Unreal is the local physical world renderer and simulation engine beneath it. The normal runtime must work locally and offline, with a narrow local bridge between N.H and Unreal. Unreal may render rooms, people, physics, animation, sound, procedural worlds, and VR, but it may never become a second memory, a second authority path, or a direct Wonder-to-memory route. Replay, reconstruction, normal world presentation, and Wonder must remain machine-distinguishable. Real-world actions remain outside Unreal and continue through N.H's authority rules. The first future implementation must start with a tiny synthetic offline room and prove the bridge, simulation boundary, duplicate prevention, stale-command rejection, crash handling, and no-memory-write rule before any real N.H data is connected.**

---

# 50. Next governance step

This file is ready to be:

1. preserved by Ness;
2. independently audited against the actual N.H source chain;
3. accepted for this narrow runtime-direction/design scope if Ness chooses;
4. later consumed by the proper A19 / Bundle 7 / Bundle 8 work;
5. implemented only under the later implementation authorization and safety gates.

No prior file needs to be overwritten.
