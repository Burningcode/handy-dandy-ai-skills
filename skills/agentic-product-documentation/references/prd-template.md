# Decision-ready PRD template

Use this template for a selected direction that needs cross-functional delivery clarity. Replace guidance text; do not leave generic placeholders in the final document.

## Document control

- Product / initiative:
- Owner:
- Status and last updated:
- Decision requested:
- Decision-maker and deadline:
- Source links:

## 1. Executive summary

In a short narrative, state:

- The user and business problem.
- Why the problem matters now.
- The recommended direction and minimum viable scope.
- Expected user behavior and business outcome.
- The most important trade-off or risk.
- The decision or action requested.

## 2. Problem and evidence

### Target users and jobs

Who has the problem? What are they trying to accomplish? What current behavior, workaround, or friction provides evidence?

### Evidence

Separate observed facts from inference. Include source, population, time window, and known limitations for quantitative claims.

### Why now

Explain the strategic trigger, changing constraint, opportunity cost, or learning window.

## 3. Outcomes and measurement

### Hypothesis

If we **[change the product or workflow]** for **[population]**, then **[target behavior]** will change, leading to **[business outcome]**, because **[mechanism]**.

### Primary outcome

- Metric and formula:
- Population and segmentation:
- Baseline and source:
- Success threshold:
- Time window:
- Decision rule:

### Guardrails

Include user harm, quality, reliability, cost, latency, security, support, or marketplace-balance metrics that could invalidate a nominal win.

## 4. Product boundaries

### Goals

List the outcomes this version owns.

### Non-goals

List tempting adjacent work that is intentionally excluded and why it can wait.

### Assumptions and constraints

Label each assumption with how and when it will be validated. Include technical, commercial, legal, privacy, operational, and accessibility constraints when relevant.

## 5. Options and decision

| Option | User value | Business value | Feasibility | Time to learn | Complexity and risk | Reversibility |
| --- | --- | --- | --- | --- | --- | --- |
| Status quo / do nothing |  |  |  |  |  |  |
| Option A |  |  |  |  |  |  |
| Option B |  |  |  |  |  |  |

State the recommendation, rationale, strongest counterargument, and evidence that would change the decision.

## 6. Experience and requirements

### Core workflow

Describe the beginning-to-end user and system flow, including entry, success, recoverable failure, hard failure, cancellation, and return visits.

### Requirements

| ID | Requirement | Rationale / source | Acceptance evidence | Priority |
| --- | --- | --- | --- | --- |
| R1 |  |  |  |  |

### Edge cases and accessibility

Include only material cases, but do not omit errors that could create user harm, corrupted state, lost money, security exposure, or silent failure.

## 7. AI / agent contract, if applicable

### Bounded job and permissions

- User intent the agent serves:
- Authoritative state and allowed data:
- Automatic tools/actions:
- Preview or confirmation actions:
- Human approval or escalation actions:
- Prohibited actions:

### Quality contract

| Level | Definition | Measurement / evaluation | Product response |
| --- | --- | --- | --- |
| Floor | Minimum acceptable behavior |  | Block, fall back, or escalate |
| Target | Sustained value threshold |  | Normal operation |
| Delight | Meaningfully better outcome |  | Learn and expand |

### Failure and recovery

Document silent failures, detection, retries, idempotency, rollback, user override, audit trail, abuse and prompt-injection risks, and incident ownership.

### Cost, latency, and quality

State the end-to-end budgets and which dimension may degrade first under load or uncertainty.

## 8. Technical and data considerations

Document system boundaries, integrations, data contracts, persistence, migration, identity and authorization, security and privacy, performance, observability, and known technical decisions. Link to the detailed technical design instead of duplicating it.

## 9. Rollout and operations

- Phases and target populations:
- Eligibility and feature controls:
- Go/no-go gate:
- Rollback or fallback:
- Monitoring and alerts:
- Support and operational readiness:
- Communications and enablement:

## 10. Risks and mitigations

| Risk | Type | Likelihood / impact | Early signal | Mitigation | Owner |
| --- | --- | --- | --- | --- | --- |
|  | Value, usability, feasibility, viability, trust, security, or operations |  |  |  |  |

## 11. Dependencies and delivery

List external teams, vendors, decisions, data, infrastructure, policy, staffing, or sequencing needs that can change scope or dates. Distinguish discovery estimates from committed delivery forecasts.

## 12. Decisions, questions, and next actions

### Decisions made

Record the decision, date, owner, and rationale.

### Decisions requested

Make the choice and deadline explicit.

### Open questions

Assign an owner and validation method. Do not use “TBD” as a substitute for ownership.

### Next actions

| Action | Owner | Due | Evidence of completion |
| --- | --- | --- | --- |
|  |  |  |  |

