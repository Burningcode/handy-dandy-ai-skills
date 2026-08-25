---
name: executive-decision-brief
description: Create an evidence-backed executive decision brief that frames the outcome, challenges a foundational assumption, compares viable options across value, usability, feasibility, and viability, and ends with a clear recommendation, owner, and decision date. Use for executive pre-reads, portfolio choices, investment decisions, and cross-functional alignment.
---

# Executive Decision Brief

This is a public-safe example playbook distilled from an internal decision-document workflow. Use only supplied, public, or authorized evidence. Replace the fictional scenario with the user's facts.

## Start with the decision

Establish:

- decision statement and decision owner;
- deadline and consequences of delay;
- behavior or business outcome the decision should create;
- immediate beneficiary and newly introduced friction;
- affected users, operators, partners, and systems;
- constraints, non-negotiables, and reversible assumptions.

Reject feature-only framing. Convert “Should we build X?” into “Which option best creates Y behavior for Z population within these constraints?”

## Build the evidence ledger

For each material claim, capture:

| Claim | Evidence | Source and date | Confidence | Gap |
| --- | --- | --- | --- | --- |

Separate facts, evaluation judgments, inferences, and recommendations. Quantitative claims require a definition, population, time window, source, and relevant calculation.

## Generate real options

Include at least three viable choices when the decision warrants them:

1. maintain or improve the current approach;
2. make a bounded change or staged investment;
3. pursue the full proposal;
4. partner, buy, or stop when genuinely viable.

Do not create a weak “do nothing” strawman merely to make the preferred option win.

## Evaluate the four product risks

For each option:

- **Value:** Will the intended user choose or benefit from it? What evidence exists?
- **Usability:** Can the user understand and complete the experience with acceptable effort?
- **Feasibility:** Can the system and team deliver it with known dependencies and reliability?
- **Viability:** Does it work for the business, policy, legal, support, and operating model?

Also name cost, latency, quality, reversibility, and second-order marketplace or ecosystem effects where relevant.

## Rank without false precision

Use a small comparison table:

| Option | Outcome potential | Evidence strength | Delivery effort | Risk | Reversibility |
| --- | --- | --- | --- | --- | --- |

Explain the reasoning behind any score. Do not hide uncertainty behind decimal precision or collapse a hard constraint into an average.

## Required pushback

Challenge at least one foundational assumption before recommending. Use this structure:

```text
Assumption: [what the proposal treats as true]
Why it matters: [what breaks if false]
Evidence: [what supports or weakens it]
Cheapest test: [how to learn before overcommitting]
```

## Decision brief structure

1. **Executive summary:** decision, recommendation, rationale, and immediate action.
2. **Outcome and context:** user behavior, business result, constraints, and why now.
3. **Evidence:** strongest facts, uncertainties, and source ledger.
4. **Options:** credible alternatives and trade-offs.
5. **Risk assessment:** value, usability, feasibility, and viability by option.
6. **Recommendation:** singular choice, conditions, and rejected alternatives.
7. **Implementation:** owner, milestones, dependencies, decision gates, and rollback.
8. **Success measures:** metric contracts, floor, target, and guardrails.
9. **Open questions:** owner and resolution date for each.

## Hypothetical example

**Fictional decision:** Should Orbit Market allow an AI service agent to approve low-value refunds without human review?

- Outcome: reduce customer resolution time without increasing improper refunds.
- Options: keep human approval, automate a narrow reversible segment, or automate all eligible refunds.
- Foundational pushback: “Low dollar value” does not necessarily mean low fraud or trust risk.
- Recommended evidence: eligible volume, current handling time, error severity, reversal rate, support effort, and audit coverage.
- Likely staged decision: narrow segment with a hard policy gate, authoritative post-state verification, weekly review, and rollback threshold.

The names and scenario are fictional. Do not carry them into a real brief.

## Permission boundary

Drafting and read-only evidence gathering are allowed when in scope. Confirm before editing an executive document, changing priorities, assigning people, publishing the recommendation, or modifying an external system unless the user explicitly requested that action.

