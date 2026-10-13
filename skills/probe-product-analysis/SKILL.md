---
name: probe-product-analysis
description: Apply the PROBE sequence—Purpose, Reality, Obstacles, Bets, and Experiments—to clarify a product problem, separate external and internal constraints, generate obstacle-specific hypotheses, design the smallest useful learning loop, and produce a decision-ready analysis plus a one-page canvas. Use for product strategy, initiative framing, problem analysis, discovery planning, and stalled or ambiguous product work.
---

# PROBE Product Analysis

Use PROBE to turn an ambiguous product situation into a purpose-aligned learning loop:

```text
Purpose -> Reality -> Obstacles -> Bets -> Experiments -> updated Reality
```

This skill is an original, agent-ready operationalization inspired by licensed PROBE materials created by Ethan Tan / Exponentially.io and copyrighted by Pureplay Studios Ltd. It does not reproduce the course worksheets, canvas files, or examples. Do not add private source files or Drive links to a public artifact.

## Choose the analysis depth

- **Quick probe:** clarify an immediate choice, message, or small delivery problem.
- **Initiative probe:** frame a product opportunity, recovery plan, or discovery sequence.
- **Strategic probe:** connect a portfolio choice to vision, customer segments, and measurable outcomes.

Use the smallest depth that can change the decision. Do not turn a small problem into a strategy exercise.

Match the canvas to the depth: use a compact canvas for a quick probe and the full decision canvas for initiative or strategic work.

## P — Purpose

Define the destination before diagnosing the route:

- What should be different for the user or affected party?
- Why does that outcome matter now?
- What behavior needs to change?
- By when must useful progress be visible?
- Which broader product or business objective does it support?
- How will success and unacceptable harm be measured?

Write the purpose as an outcome, not a feature or task list. If the purpose is still broad, distinguish vision, strategic direction, and the near-term objective.

## R — Reality

Describe current conditions with evidence. Separate:

- **External reality:** customer behavior, journey, alternatives, market conditions, partner constraints, regulation, and observed outcomes.
- **Internal reality:** capabilities, incentives, decision rights, process, architecture, data quality, team capacity, and recurring behavior.

Label each statement as:

- fact with source and date;
- evaluation judgment with rubric and confidence;
- inference;
- assumption or unknown.

Actively seek contradictory evidence. Do not let an attractive purpose distort the description of reality.

## O — Obstacles

Identify what prevents reality from becoming the purpose:

1. Place each obstacle at the point where it exerts force.
2. Separate customer or ecosystem obstacles from internal organizational or technical obstacles.
3. Distinguish root causes from visible symptoms.
4. Estimate impact, evidence strength, controllability, and uncertainty.
5. Select the few obstacles whose removal would create the most progress.

Use this obstacle statement:

```text
[Actor or system] cannot or does not [needed behavior] because [mechanism],
which prevents [purpose-linked outcome]. Evidence: [source]. Confidence: [level].
```

Do not rank an obstacle highly merely because it is easy for the team to discuss or fix.

## B — Bets

Generate multiple solution hypotheses tied to specific priority obstacles. Include product, communication, policy, process, data, and operating-model responses when relevant.

For each bet, state:

- obstacle addressed;
- causal mechanism;
- expected behavior change;
- affected users and new friction;
- key assumption;
- impact, effort, confidence, and reversibility;
- reason it may fail or create a second-order effect.

Diverge before converging. Do not treat the first plausible feature as the strategy. Prefer a portfolio of complementary bets only when each has a distinct role in the causal chain.

## E — Experiments and execution

Turn the riskiest assumption into the smallest credible learning or delivery step.

Every experiment needs:

- hypothesis and decision it will change;
- eligible population and unit of analysis;
- treatment, prototype, operational change, or test;
- primary signal with a metric contract;
- success threshold and guardrails;
- expected result if the bet is correct;
- result that would weaken or invalidate the bet;
- owner, timing, cost boundary, and stopping condition;
- authoritative verification source.

Build less when a smaller test can acquire the necessary evidence. Break execution into increments that deliver value or reduce material uncertainty.

## Iterate from results

After an experiment or action:

1. Record the result and evidence quality.
2. Update Reality.
3. Re-rank Obstacles.
4. Continue, modify, or stop each Bet.
5. Revisit Purpose only when evidence or strategy genuinely changes it.

PROBE is a loop, not a stage-gate checklist. Preserve what was learned so the team does not reset to its original assumptions.

## Required outputs

Unless the user explicitly asks for prose only, deliver both:

1. a decision-ready narrative that explains the reasoning; and
2. a one-page **PROBE Decision Canvas** that makes the relationships scannable.

Read [the original public canvas specification](references/probe-decision-canvas.md) before producing the canvas. The canvas is a decision surface, not a poster: it must preserve the links from purpose to evidence, priority obstacles, bets, experiment, and the next update to reality.

When the environment can create an in-conversation visual or interactive canvas, use that capability and also include the compact Markdown version for portability. Otherwise, produce the Markdown canvas directly. Never present the public canvas as the licensed course template or reproduce a private source canvas.

### Decision-ready narrative

```markdown
## Bottom line
[Purpose, priority obstacle, recommended bet, and next experiment]

## Purpose
- Outcome:
- Behavior:
- Timeframe:
- Success and guardrails:

## Reality
### External
- [Evidence-labeled statements]
### Internal
- [Evidence-labeled statements]

## Priority obstacles
| Obstacle | Mechanism | Evidence | Impact | Confidence |
| --- | --- | --- | --- | --- |

## Bets
| Bet | Obstacle addressed | Expected change | Key assumption | Reversibility |
| --- | --- | --- | --- | --- |

## First experiment
- Hypothesis:
- Method and population:
- Primary metric and threshold:
- Guardrails:
- Owner and timing:
- Decision rule:

## Learning log
- Result:
- Reality updated:
- Next decision:
```

### Canvas quality gate

Before delivering, confirm that the canvas:

- names one decision, owner, timeframe, and confidence level;
- expresses Purpose as an outcome and behavior change rather than a feature;
- separates external from internal Reality and labels evidence quality;
- connects every priority Obstacle to a mechanism and purpose-linked impact;
- connects every Bet to a named obstacle and risky assumption;
- defines one smallest credible experiment with a threshold and decision rule;
- shows how the result will update Reality and change the next decision; and
- contains no invented evidence, private links, confidential identifiers, or decorative scoring.

## Hypothetical example

**Fictional situation:** Orbit Market wants to improve first-listing completion for new sellers.

- **Purpose:** More eligible new sellers publish one accurate listing during their first setup session without increased support demand.
- **Reality:** Completion falls most sharply after category selection; required attributes vary; support cases mention uncertainty; mobile rendering has not been reconciled with transactional outcomes.
- **Priority obstacle:** Sellers cannot predict which attributes are required for their category before attempting publication.
- **Bets:** Progressive requirements guidance, category-specific examples, or a simplified starter flow.
- **First experiment:** Prototype progressive guidance for one high-volume category, verify completion from the catalog system, and monitor incorrect-data and support-contact guardrails.

The organization and facts are fictional placeholders.

## Agent and permission boundaries

Use authorized connectors for read-only evidence gathering when useful. Do not invent sources, findings, thresholds, or agreement. Confirm before changing roadmaps, tickets, experiments, production settings, or stakeholder communications unless the user explicitly requested that action. After any authorized write, read the resulting artifact or product state back and verify it.
