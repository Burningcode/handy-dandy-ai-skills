---
name: cross-functional-status-synthesis
description: Synthesize program status across work trackers, conversations, meeting notes, product documents, designs, and outcome data into an evidence-backed executive readout, communications-readiness assessment, draft updates, and prioritized chase list. Use for portfolio reviews, program updates, launch readiness, morning briefings, or cross-functional alignment when the truth is distributed across systems.
---

# Cross-Functional Status Synthesis

Turn fragmented operating evidence into a concise, honest status packet. This is an example playbook for multi-source operational automation: adapt the connectors and source hierarchy to the authorized environment.

The default output is a reviewable draft. Do not send messages, update tickets, publish documents, or change delivery plans unless the user explicitly authorizes that action.

## Define the decision first

Establish or safely infer:

- initiative or portfolio scope;
- reporting window;
- audience and decision they need to make;
- named owner and review time;
- systems available for read-only evidence gathering;
- whether the request is a fast pre-flight or a full synthesis.

Default to the smallest useful scope. If the audience only needs to know whether communications are ready, do not produce a full program review.

## Use the right source for each claim

No source is universally authoritative. Prefer:

| Claim type | Preferred evidence |
| --- | --- |
| Current scope or decision | Latest explicit decision record or approved product document |
| Delivery state | Work tracker plus linked code, design, or release evidence |
| User or business outcome | Authoritative product, warehouse, or financial system |
| Ownership and timing | Current plan, work tracker, or directly responsible owner |
| Rationale and unresolved debate | Meeting notes and conversation threads |
| Experience readiness | Designs, prototypes, test results, and acceptance criteria |

Use recency, specificity, approval state, and source authority together. A recent informal message may supersede an old document, but it should not silently override an approved decision. Surface the conflict.

## Gather evidence in parallel

When connectors are available, run independent read-only lookups together:

- work tracker: initiative, epic, story, bug, dependency, and blocker states;
- conversations: recent decisions, asks, and unresolved threads;
- meetings: explicit alignment, dissent, owners, and deadlines;
- product documents: intended outcome, scope, risks, and success measures;
- design: current experience and unresolved states;
- analytics or warehouse: observed outcomes and leading indicators;
- release or incident systems: shipped state and operational risk.

Do not claim access you do not have. If a source is unavailable, label the gap and continue with the available evidence.

## Normalize each claim

Capture a compact evidence ledger:

| Claim | Status | Source | Date | Owner | Confidence | Conflict or gap |
| --- | --- | --- | --- | --- | --- | --- |
| [Specific statement] | Fact / inference / recommendation | [Link or identifier] | [Date] | [Owner] | High / medium / low | [What remains unclear] |

For quantitative claims, record the metric definition, population, window, source, and whether the result is gross or net. Do not invent numbers or silently carry forward stale metrics.

## Assess communications readiness

Classify each initiative:

- **Ready:** message, evidence, decision, owner, and next step align.
- **Ready with caveats:** core message is stable; one or more caveats must remain explicit.
- **Not ready:** material facts, scope, evidence, or approvals are unresolved.
- **Blocked by decision:** execution may be understood, but a named decision owner must choose.

When an update is not ready, still produce useful holding language:

```text
We are not ready to communicate [commitment or date] yet because [specific unresolved evidence or decision]. We expect to be ready after [named milestone or decision], owned by [owner] and targeted for [timing if verified].
```

Never manufacture certainty to make the update feel more complete.

## Resolve contradictions explicitly

For each conflict:

1. State the competing claims and sources.
2. Identify which is newer, more specific, and more formally approved.
3. Determine whether one supersedes the other or whether a decision is still open.
4. Assign an owner and the smallest action needed to resolve it.
5. Keep external wording conservative until the conflict is closed.

Do not merge contradictory claims into vague consensus language.

## Produce the status packet

### 1. Executive readout

Start with:

- overall status and confidence;
- what materially changed in the reporting window;
- decisions or risks requiring attention;
- whether stakeholder communication is ready;
- one recommended next action.

### 2. Initiative table

| Initiative | Outcome | Delivery state | Evidence | Risk or blocker | Owner | Next milestone | Comms readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use plain status language. Avoid uncalibrated red/yellow/green labels unless definitions are provided.

### 3. Decision and risk register

For each material item, include:

- decision or risk;
- why it matters now;
- options or mitigation;
- owner and due date;
- consequence of no action.

### 4. Draft communications

Draft only the messages the audience needs. Each draft should include:

- what changed;
- why it matters;
- action needed, owner, and timing;
- supporting links;
- caveats or open decisions.

Clearly label drafts as unsent.

### 5. Prioritized chase list

Order by decision impact, dependency criticality, and timing:

| Priority | Person or team | Ask | Why now | Evidence | Due |
| --- | --- | --- | --- | --- | --- |

Make every ask answerable. Replace “follow up” with the exact decision, artifact, data, or approval needed.

## Fast pre-flight mode

When another skill needs only a freshness check:

1. Read the latest decision record or meeting note for the topic.
2. Read one recent program conversation or work-tracker update.
3. Return three to five bullets: decision, owner, date, source, and any discrepancy.

Do not build the full packet unless the discrepancy materially changes the draft.

## Quality gate

Before delivery, verify:

- every major claim has a source, date, or explicit uncertainty label;
- shipped, planned, explored, and proposed work are not conflated;
- outcome evidence is separated from activity;
- contradictions and stale sources are visible;
- owners and dates are verified rather than inferred where possible;
- drafts are concise and audience-specific;
- no internal data, identifiers, customer information, credentials, or private links are exposed outside the authorized context;
- no message or external update has been sent without permission.

After any authorized external write, read the resulting artifact back and verify it.

