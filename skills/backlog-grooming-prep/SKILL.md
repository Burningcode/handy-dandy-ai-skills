---
name: backlog-grooming-prep
description: Review a backlog before engineering grooming, group work into themes, classify readiness, elevate urgent or risky items, identify exact ticket gaps, and produce a focused working-session agenda. Use for backlog readiness reviews, grooming preparation, story refinement, and prioritization handoffs.
---

# Backlog Grooming Prep

This public-safe example generalizes an internal grooming runbook. Adapt field names and workflow states to the authorized work tracker; the example tickets are fictional.

## Goal

Turn a backlog into:

- themes that should be discussed together;
- work ready for estimation or engineering discussion;
- urgent or risky items that deserve early attention;
- exact gaps to close before the meeting;
- already-scored work that belongs in prioritization rather than grooming;
- a proposed agenda and follow-up checklist.

## Intake

Accept ticket URLs, keys, filters, epics, or pasted lists. Deduplicate before fetching. Gather, when available:

- summary, description, type, state, priority, owner, parent, and links;
- acceptance criteria or reproduction steps;
- comments and recent decisions;
- estimate, sprint, target date, and dependencies;
- relevant prior grooming notes.

Treat missing access as a visible limitation, not permission to infer fields.

## Readiness classes

| Class | Definition |
| --- | --- |
| Ready for grooming | Clear user or problem, outcome, boundaries, acceptance criteria or reproduction, and owner context |
| Needs quick cleanup | Mostly ready; one small field or decision is missing |
| Review first | Urgent, risky, ambiguous, disputed, dependency-heavy, or likely to consume the meeting without preparation |
| Prioritization candidate | Already sized and stable; needs sequencing rather than another grooming discussion |
| Not for grooming | Done, duplicate, obsolete, pure support action, or belongs in incident response |

State whether a classification comes from explicit evidence or a heuristic.

## Elevate material risk

Review first when work affects:

- payments, billing, permissions, privacy, safety, or data integrity;
- a time-sensitive launch or contractual commitment;
- repeated support volume or a known blast radius;
- a recently reopened or disputed decision;
- an active incident, customer escalation, or irreversible state change.

Urgency does not make an unclear ticket ready. It changes the order in which the gap should be resolved.

## Gap checklist

Name the smallest specific improvement:

- clarify user, problem, and expected outcome;
- add acceptance criteria or reproducible steps;
- define scope and non-goals;
- assign an owner or parent;
- size impact or blast radius;
- link dependencies and related work;
- separate discovery spike from implementation;
- decide manual workaround versus product fix;
- confirm that the workflow state is current.

## Working-session agenda

1. Material risks and time-sensitive blockers.
2. Tickets needing one product or technical decision.
3. Ready stories grouped by theme.
4. Stable scored items for prioritization.
5. Duplicates, obsolete work, and support-process handoffs.

Do not spend group time reconstructing context that can be prepared asynchronously.

## Output

1. **Bottom line:** overall readiness and the first recommended focus.
2. **Themes:** grouped ticket keys and readiness labels.
3. **Review first:** reason, missing decision, and owner.
4. **Ready or nearly ready:** items that can move efficiently.
5. **Prioritization candidates:** stable scored work.
6. **Agenda:** ordered working session.
7. **Draft team message:** concise handoff after tickets are updated.

## Hypothetical example

| Ticket | Fictional summary | Classification | Exact next action |
| --- | --- | --- | --- |
| DEMO-101 | Duplicate charge after retry | Review first | Add reproduction evidence and payment-state blast radius |
| DEMO-118 | Clarify empty-state guidance | Needs quick cleanup | Add accessibility acceptance criterion |
| DEMO-123 | Add export filter | Ready for grooming | Confirm estimate with platform team |
| DEMO-099 | Retired integration cleanup | Not for grooming | Close as superseded by DEMO-087 |

These identifiers and issues are fictional.

## Permission boundary

Read and prepare within scope. Confirm before editing tickets, moving workflow states, assigning people, or posting the team message unless explicitly authorized. After any authorized write, re-open the affected ticket and verify the result.

