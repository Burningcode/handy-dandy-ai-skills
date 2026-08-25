---
name: program-update-communications
description: Draft concise program-channel updates by selecting the right communication archetype, separating the scannable main message from supporting detail, making actions and deadlines explicit, and preserving evidence and decision provenance. Use for launches, decisions, scope locks, blockers, holding patterns, and stakeholder status posts.
---

# Program Update Communications

This is a public-safe example derived from a structured internal channel-update runbook. It produces reviewable drafts for hypothetical or real authorized programs. It does not post automatically.

## Choose one archetype

| Archetype | Use when | Action shape |
| --- | --- | --- |
| Status update | Pure information; no response required | FYI |
| Decision request | One unresolved choice | Decide or approve by a stated deadline |
| Multi-decision | Two or three coupled choices | Numbered questions with one response window |
| Scope lock | Alignment already exists and needs a final objection window | Review; silence may equal consent only with adequate notice |
| Holding pattern | Stakeholders are waiting but the evidence is not ready | Not ready; name the next milestone |
| Blocker or chase | One owner has the next move | Exact action and due date |

Do not mix archetypes in one main message. Split them when the audience must respond differently.

## Verify before drafting

For decisions, scope locks, and blockers:

- check the latest decision record or meeting note;
- confirm the owner, scope, and date are current;
- surface discrepancies before writing authoritative language.

Never create a scope lock from stale framing.

## Main message contract

Keep the main channel scannable:

```text
**[Program or initiative]**

TL;DR: [What changed and why it matters]

Action Needed: [FYI / Review / Decide / Approve] — [specific response]
Deadline: [date, time, timezone]
Owners: @[Decision owner] @[Required reviewer]

Details and sources are in the thread.
```

Use placeholders instead of real handles in a draft. Never invent approval or commitment.

## Thread contract

Include only useful sections:

- **Goal:** behavior or outcome the work should create.
- **What changed:** shipped work, evidence, and impact.
- **Decisions:** what is decided, by whom, and when.
- **Still open:** owner, consequence, and whether it blocks.
- **Blockers:** specific constraint and needed action.
- **Next steps:** owner and date.
- **Sources:** full links to the brief, design, work item, metric, or decision record.

For a scope lock, separate **locked decisions** from **open items that do not gate the lock**.

## Make replies decision-shaped

Use a constrained menu when it improves closure:

- Yes / No / Workshop
- Approved / Approved with edits / Workshop
- Acknowledge / Need a different timeline

Avoid open-ended “thoughts?” when a specific decision is required.

“Silence equals consent” requires at least one business day, ideally two, plus a clear list of what will lock. Do not use it for genuinely unresolved or high-risk decisions.

## Hypothetical example

```text
**Aurora checkout — digital-wallet experiment**

TL;DR: The fictional experiment has completed its first guardrail review with no critical incidents.

Action Needed: Approve expansion from the pilot cohort to the next test cohort.
Deadline: Thu May 14, 5:00 PM ET
Owners: @[Product owner] @[Engineering owner]

Details and source links are in the thread.
```

Thread outline:

- Goal: shorten checkout without increasing payment errors.
- Evidence: fictional pilot results; insert verified metric contracts and links.
- Decided: keep one platform out of scope until accessibility review completes.
- Open: finance reconciliation test, owned by the payments lead.
- Next: expand only if the verified error-rate guardrail remains below the agreed floor.

All names and facts above are fictional placeholders.

## Quality gate

- Archetype, action, owner, deadline, and timezone are explicit.
- The main message contains no deep detail.
- Facts link to current sources.
- Planned, shipped, observed, and recommended work remain distinct.
- Draft is labeled for review.
- No message is sent without explicit authorization.

