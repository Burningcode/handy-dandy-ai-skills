# PROBE Decision Canvas

This is an original, public-safe output template for the `probe-product-analysis` skill. It is not a reproduction of a licensed course worksheet or canvas.

## Output contract

Keep the completed canvas to one scannable page or screen. Use short evidence-backed statements, not paragraphs. Preserve the causal chain:

```text
Purpose -> Reality -> Obstacles -> Bets -> Experiment -> updated Reality
```

Every obstacle must connect to the purpose, every bet to an obstacle, and the experiment to the riskiest assumption. Add source labels and confidence where evidence is incomplete.

## Portable Markdown canvas

```markdown
# PROBE Decision Canvas — [initiative or decision]

| Decision | Owner | Timeframe | Last updated | Confidence |
| --- | --- | --- | --- | --- |
| [Decision this analysis must change] | [Name or role] | [Window] | [Date] | [High / medium / low + why] |

## Purpose and success

| Desired outcome | Behavior change | Why now | Success threshold | Guardrails |
| --- | --- | --- | --- | --- |
| [User or business outcome] | [Observable behavior] | [Trigger or opportunity] | [Metric, population, window, target] | [Harms or regressions to prevent] |

## Reality

| External evidence | Internal evidence | Unknowns or contradictions |
| --- | --- | --- |
| [Fact / evaluation / inference + source and date] | [Fact / evaluation / inference + source and date] | [Assumption to resolve] |

## Priority obstacles

| # | Type | Obstacle and mechanism | Purpose-linked impact | Evidence | Confidence |
| --- | --- | --- | --- | --- | --- |
| O1 | External / internal | [Actor or system cannot do X because Y] | [What progress it prevents] | [Source] | [H / M / L] |

## Bets

| # | Obstacle | Bet and causal mechanism | Expected behavior change | New friction / second-order effect | Riskiest assumption | Reversibility |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | O1 | [Response and why it should work] | [Observable change] | [Who pays a cost] | [What must be true] | [High / medium / low] |

## First experiment

| Hypothesis | Population and method | Primary metric | Threshold | Guardrails | Owner and timing |
| --- | --- | --- | --- | --- | --- |
| [If B1, then behavior changes because mechanism] | [Smallest credible test] | [Definition, numerator, denominator, window, source] | [Decision-changing result] | [Limits] | [Owner, duration, cost boundary] |

**Stopping rule:** [When to end or invalidate the test]  
**Verification source:** [Authoritative product or data state]  
**Decision rule:** [Continue / modify / stop conditions]

## Learning loop

| Result | Reality update | Obstacle reprioritization | Bet decision | Next decision |
| --- | --- | --- | --- | --- |
| [Observed result + evidence quality] | [What is now true or less certain] | [What moves up or down] | [Continue / modify / stop] | [Named decision and owner] |
```

## Visual or interactive rendering

If a visual-capable environment is available, render the same content as one accessible decision surface:

- Put the decision metadata and Purpose across the top.
- Place external and internal Reality side by side.
- Show numbered Obstacles between Reality and Bets.
- Use the obstacle IDs to make each Bet's causal link explicit.
- Give the first Experiment one dominant block beneath the selected Bet.
- Close with a Learning Loop that visibly returns the result to Reality.
- Reflow into a vertical sequence on narrow screens; do not shrink the text to force a desktop grid.

The visual may support selection or expansion, but its first view must be useful without interaction. Do not add decorative scores, generic status cards, or colors that imply evidence strength without a text label.

## Compact version for a quick probe

For a small decision, use six lines rather than leaving a large canvas mostly empty:

```markdown
# Quick PROBE Canvas — [decision]
- **Purpose:** [outcome, behavior, timeframe]
- **Reality:** [strongest external evidence] / [strongest internal evidence]
- **Obstacle:** [mechanism preventing progress]
- **Bet:** [response, expected change, risky assumption]
- **Experiment:** [smallest test, metric, threshold, owner]
- **Learning loop:** [result that causes continue / modify / stop and updates Reality]
```
