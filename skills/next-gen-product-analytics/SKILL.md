---
name: next-gen-product-analytics
description: Design, audit, or investigate product analytics for AI agents and agentic workflows by linking experience signals, tool execution, authoritative product state, evaluations, and business outcomes. Use for agent metric systems, instrumentation plans, dashboard or experiment specs, production-quality investigations, and questions about measuring AI product quality beyond adoption, retention, and revenue.
---

# Next-Generation Product Analytics

Help product teams determine whether an agent understood the job, performed it correctly, created a verified state change, and produced durable user value. Keep ordinary adoption, retention, revenue, cost, and risk metrics; connect them to the mechanics of agent experience rather than replacing them with one opaque quality score.

Operate as both:

1. **Practitioner:** answer the product question, design the measurement system, or diagnose the change.
2. **Coach:** briefly explain the non-obvious measurement principle behind important choices.

Lead with the decision or finding.

## Start with the decision

Establish or safely infer:

- the behavior the product should create;
- the immediate beneficiary and business outcome;
- the decision the analysis will change, its owner, and timing;
- the eligible population and unit of analysis: user, account, task, workflow, session, turn, tool call, or business object;
- the autonomy mode: advisory, supervised, or autonomous;
- the authoritative system that proves whether the requested work happened.

Push back when a request starts with a dashboard but does not name a decision. Do not invent access, schemas, baselines, thresholds, or quantitative results.

## Use the outcome evidence chain

Analyze the full chain:

```text
eligible need -> expressed intent -> understood intent -> proposed plan
-> tool/API execution -> authoritative state change -> verification
-> durable user outcome -> business outcome
```

An assistant message, `resolved=true`, successful tool call, HTTP 2xx response, approval click, or offline evaluation is evidence about one link. It is not proof of the final outcome.

Prefer a post-action read from the authoritative system and, when durability matters, a delayed check. Keep these states distinct:

- attempted;
- technically acknowledged;
- state-confirmed;
- user-valued;
- durable.

## Measure five complementary layers

| Layer | What to measure |
| --- | --- |
| Business health | Eligible adoption, qualified use, retention, revenue, cost, and risk |
| Experience | Effort, turns to intent, redundant clarification, workarounds, scope narrowing, and abandonment |
| Execution | Tool selection, technical success, recovery, latency, and action provenance |
| Verified outcome | Claim-to-state agreement, completion coverage, correction, reversal, and durability |
| Trust and learning | Acceptance, material edits, overrides, escalation, repeated delegation, and eval-to-production gaps |

Do not optimize friction signals in isolation. Clarification can improve safety, scope narrowing can be responsible, human intervention can be healthy supervision, and fast completion can conceal failure.

## Build a quality case, not a vanity score

For material rollout or autonomy decisions, test seven claims separately:

1. **Goal validity:** Was this the right, feasible, permitted job with valid success criteria?
2. **Outcome effectiveness:** Did the requested goal become true, complete, and useful?
3. **Process integrity:** Was the path authorized, safe, recoverable, and proportionate?
4. **Experience efficiency:** What total effort accompanied each outcome state?
5. **Appropriate reliance:** Did people accept, verify, override, and escalate appropriately?
6. **Reliability:** Does quality hold across repeated runs, segments, versions, and realistic conditions?
7. **Durable net value:** Did the benefit persist and exceed the best credible counterfactual after costs and corrections?

For each material claim, define a **floor**, **target**, and **delight level**. Do not average a critical integrity or safety failure into a passing composite.

## Join behavioral, transactional, and evaluation evidence

Correlate conversations, sessions, agent traces, tool calls, transactional records, supervision actions, evaluations, and downstream outcomes with durable identifiers whenever possible. Timestamp joins are a labeled fallback.

Keep user, long-lived agent instance, conversation, session, durable task, execution trace, transaction, and affected entity as separate identities. Use pseudonymous identifiers, least privilege, retention limits, and deletion propagation. Do not copy raw conversation text into broad analytics tables unless it is authorized and necessary.

For supervised flows, capture the proposal, accept/edit/reject action, material diff, approval time, execution, and verified post-state. For autonomous flows, capture the completion claim, provenance, verification read, uncertainty, recovery, and escalation.

## Write a metric contract

For every quantitative metric, state:

| Field | Requirement |
| --- | --- |
| Decision | Choice it informs, owner, and timing |
| Behavior | User or system behavior the team wants to create |
| Definition | Plain-language meaning |
| Formula | Numerator and denominator |
| Unit | User, account, task, workflow, session, turn, call, or object |
| Eligibility | Who or what can reasonably enter the denominator |
| Window | Event, reporting, and outcome-lag windows |
| Source | Authoritative event, table, API, or system and freshness |
| Join | Identifiers, deduplication, retry, and correction rules |
| Segments | Required cuts before interpretation |
| Guardrails | Quality, safety, latency, cost, trust, and gaming risks |
| Threshold | Hypothesized floor, target, or decision rule and its evidence |
| Coverage | Observable share of the eligible population and blind spots |

Segment before counting. Separate population mix shift from within-segment change. Use distributions and tails when averages hide failure.

## Diagnose from population to mechanism

1. Start with global experience and verified-outcome measures across the eligible population.
2. Locate concentration by outcome state, intent, task complexity, scope change, autonomy mode, surface, tool, cohort, and version.
3. Inspect contrastive traces or replay from relevant cells, including successes and failures.
4. Name the failure mechanism and responsible layer: task definition, interaction, orchestration, tool or data, model, supervision, policy, or measurement.
5. Test the trace-derived explanation against population data before calling it a pattern.
6. Use a causal design before claiming product impact, then add confirmed failures to a held-out regression suite.

Traces explain how a pattern happens. Population analysis establishes how often and where it happens. Experiments establish contribution.

## Produce the smallest decision-ready artifact

Choose the output that matches the decision:

- **Measurement strategy:** behavior, evidence chain, metric tree, leading and lagging indicators, guardrails, and learning plan.
- **Metric contract:** exact definition, eligibility, sources, joins, segments, owner, threshold hypothesis, and failure modes.
- **Instrumentation plan:** events, states, identifiers, verification reads, privacy constraints, QA, and rollout.
- **Investigation:** finding first, segmented diagnosis, competing hypotheses, confidence, impact, and next test.
- **Dashboard spec:** decisions supported, audience, comparisons, alerts, drill paths, and freshness.
- **Experiment spec:** hypothesis, treatment, primary metric, threshold, guardrails, power assumptions, and decision rule.

Always distinguish **instrumented facts**, **evaluation judgments**, **inferences**, and **recommendations**. If data access is unavailable, deliver executable metric and query specifications instead of fabricated results.

## Permission and privacy boundaries

Prefer read-only inspection. Confirm authorization before writing events, changing schemas, editing dashboards, or modifying external systems unless the user explicitly requested the action. Keep credentials, sensitive content, unnecessary personal data, and private company details out of the artifact.

