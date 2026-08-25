---
name: metric-root-cause-investigation
description: Investigate funnel metric drops, analytics incidents, and product-quality inflections with positional hypotheses, metric contracts, segmented evidence, and explicit confidence. Use when a metric changes unexpectedly, dashboards disagree, instrumentation may be broken, or a team needs a decision-ready root-cause readout and next test.
---

# Metric Root-Cause Investigation

Use this skill to locate a measurable failure in the product system, not merely chart a decline. Lead with the current finding, confidence, business impact, and next decision.

## Evidence labels

Keep these distinct throughout the investigation:

- **Instrumented fact:** directly observed in an authoritative event, table, API, or log.
- **Evaluation judgment:** a human- or model-applied rubric with version and confidence.
- **Inference:** the most plausible explanation connecting observed evidence.
- **Recommendation:** a proposed test, fix, or operating decision.

Do not present an inference as a measured result.

## Step 1: Write the metric contract

Before querying, state:

- decision and owner;
- numerator and denominator;
- eligible population and exclusions;
- unit of analysis;
- time window and comparison window;
- event, table, API, or transactional source of truth;
- join, deduplication, retry, and correction logic;
- gross versus net treatment;
- expected segments and known blind spots.

Reconcile competing dashboard definitions before explaining the movement. A definition change can create a real chart inflection without a real behavior change.

## Step 2: Locate the inflection

Establish:

- first date the movement is statistically and operationally visible;
- whether it is sudden, gradual, periodic, or cohort-specific;
- absolute volume as well as rate;
- reporting latency and late-arriving data;
- relevant releases, experiments, incidents, campaigns, eligibility changes, and traffic shifts.

Use daily and weekly views when possible. Do not let smoothing obscure the first affected cohort.

## Step 3: Frame hypotheses by system position

Place every hypothesis where it could exert force:

```text
entry -> routing -> eligibility -> render -> instrumentation
-> pipeline -> verified outcome -> downstream value
```

Examples:

- **Entry:** Was the notification, task, recommendation, or deeplink created and delivered?
- **Routing:** Did the user reach the intended list, detail view, tab, or filtered state?
- **Eligibility:** Was the object available to this user at that timestamp?
- **Render:** Did the card, call to action, error, or empty state render?
- **Instrumentation:** Did the raw event fire with the expected properties?
- **Pipeline:** Did ingestion and transformation preserve the raw event?
- **Outcome:** Did the authoritative system record the response, conversion, or state change?
- **Value:** Did the verified outcome persist and create the intended downstream effect?

## Step 4: Maintain a hypothesis board

| Hypothesis | Positional fit | Evidence for | Evidence against | Rule-in test | Rule-out test | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| [Mechanism] | [Chain position] | [Observed] | [Observed] | [Test] | [Test] | Priority / plausible / ruled down |

Update verdicts as evidence arrives. Keep ruled-down hypotheses visible so the team does not reopen them without new evidence.

## Step 5: Test in triage order

1. Definition, eligibility, and reporting-window check.
2. Raw event versus transformed metric reconciliation.
3. Adjacent-event sanity check across the funnel.
4. Volume-versus-rate decomposition.
5. Mix shift versus within-segment change.
6. Cohort and release comparison around the inflection.
7. Qualitative replay, logs, support cases, or sampled records.
8. Code, routing, filter, eligibility, empty-state, and API-path inspection.
9. Authoritative outcome and delayed durability check.

Use aggregates to size the problem and appropriately stratified samples to explain mechanisms. A handful of dramatic traces proves existence, not prevalence.

## Required evidence cuts

Produce these when the sources allow:

- daily and weekly trends around the inflection;
- numerator and denominator separately;
- product type, platform, source, cohort, geography, and user-activity segments where relevant;
- release, incident, experiment, and policy timeline;
- entry-point or delivery volume;
- raw versus transformed event counts;
- adjacent funnel events;
- successful and failed trace or replay contrasts;
- authoritative post-state checks.

For each cut, state coverage, freshness, row or sample count, and important exclusions.

## Positional reasoning rules

- A downstream failure cannot directly explain an upstream event decline.
- A change deployed after the inflection cannot explain its start.
- If raw and transformed counts agree, rule down the pipeline.
- If adjacent metrics move together, investigate their shared upstream dependency.
- If composition does not explain the change, inspect within-segment behavior.
- If the rate changes while both numerator and denominator fall, explain both movements.
- If the chart recovers before the proposed fix, the fix is unlikely to be sufficient as the explanation.

## Deliver a decision-ready artifact

Use this order:

1. **Executive readout:** what changed, current theory, confidence, impact, and decision.
2. **Metric contract:** definition, population, windows, source, and coverage.
3. **Trend and inflection:** highest-signal chart or table.
4. **Hypothesis board:** current verdicts and evidence.
5. **Completed tests:** what was learned and ruled down.
6. **Next test:** one owner, action, expected discriminating result, and timing.
7. **Appendix:** detailed cuts, queries, trace references, and caveats.

Keep the main artifact decision-oriented. Move large tables and query text to the appendix.

## Executive update template

```text
Metric: [name and definition]

TL;DR: [movement, strongest current explanation, confidence, and what is ruled down]

Evidence:
- [trend, window, population, and source]
- [raw-versus-transformed or adjacent-event result]
- [segment or mix result]
- [release, incident, trace, or code-path result]

Decision / next test: [owner, action, expected result, timing]
```

## Common failure modes

- Treating a successful query as an answered question.
- Moving directly from correlation to a causal claim.
- Blaming source mix without decomposing within-segment rates.
- Trusting sparse identifiers or page views as proof of user behavior.
- Generalizing from only failed or only successful traces.
- Leaving stale dates, labels, denominators, or windows in the final artifact.
- Reporting huge tables without the decision they support.
- Modifying instrumentation or dashboards during diagnosis without authorization.

Prefer read-only investigation. Confirm before external writes, schema changes, dashboard edits, messages, or releases unless the user explicitly requested them.

