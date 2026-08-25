---
name: outcome-goal-metric-design
description: Turn a product purpose into a focused outcome, observable behavior change, metric contracts, thresholds, guardrails, and review decisions. Use for product goals, OKRs, initiative success measures, goal trees, metric selection, and plans that confuse outputs, activities, or revenue with user outcomes. Do not use as the primary workflow for investigating an unexpected metric drop.
---

# Outcome, Goal, and Metric Design

Design goals that focus a cross-functional team and metrics that change decisions rather than decorate a dashboard.

This is an original, public-safe operationalization inspired by licensed product-objective and measurement materials from Ethan Tan / Exponentially.io and Pureplay Studios Ltd. It does not reproduce their worksheets or examples.

## Start with the decision and outcome

Define the planning horizon, decision owner, target population, and business context. Write one qualitative objective describing the user or system outcome that matters now. Then identify the observable behavior that would demonstrate progress.

Do not use shipping, adoption alone, revenue alone, or a task list as the objective. If the team has multiple unrelated objectives, expose the resource trade-off rather than hiding it in a long scorecard.

## Build the outcome chain

Trace a falsifiable chain:

```text
team intervention -> user experience -> user behavior -> durable user outcome -> business outcome
```

Label each causal link as evidence, inference, or assumption. Name external conditions that could move the metric without the intended behavior.

## Choose metric roles

Use only the roles needed for the decision:

- **Primary outcome:** best available evidence that the desired user or system outcome occurred.
- **Leading behavior:** earlier signal in the causal chain that can guide iteration.
- **Business consequence:** durable economic or strategic effect, usually lagging.
- **Guardrail:** harm, quality loss, cost, risk, or displaced behavior that must stay within a boundary.
- **Learning measure:** evidence collected to resolve a risky assumption before scale.
- **Health baseline:** ongoing reliability that requires a sufficient floor but is not the current differentiating goal.

Avoid selecting one metric from every framework category. Start with the intended behavior and the decision the measure will inform.

## Write metric contracts

For every retained quantitative metric, state:

- plain-language definition;
- numerator and denominator;
- event or authoritative state;
- population and exclusions;
- unit of analysis;
- time window and attribution window;
- segmentation required before aggregation;
- gross versus net treatment where relevant;
- baseline, target, and confidence;
- owner and review cadence; and
- known failure or gaming mode.

For qualitative evaluation, define the rubric, sample, evaluator, quality floor, target, delight level, and disagreement process.

## Set thresholds and decisions

Anchor targets in baseline evidence, user value, strategic necessity, or a justified model. Distinguish aspiration from commitment. Pair each threshold with the action it triggers and the guardrails that can override it.

For experiments, require a hypothesis, primary metric, success threshold, minimum credible exposure or evidence, and stopping rule. Do not declare success from a favorable but underpowered or selectively segmented result.

## Required outputs

Deliver:

1. a concise outcome and metric recommendation;
2. a completed [Outcome and Metric Decision Canvas](references/outcome-metric-decision-canvas.md); and
3. unresolved instrumentation or evidence gaps with owners.

## Quality gate

Confirm that the goal is shared across Product, Design, Engineering, and relevant business partners; metrics map to the causal chain; every metric has a contract; guardrails represent real harms; targets have a stated basis; segments reveal rather than hide mix shift; and the review cadence ends in explicit continue, modify, scale, or stop decisions.
