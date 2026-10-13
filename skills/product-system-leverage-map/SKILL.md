---
name: product-system-leverage-map
description: Map a product as a system of users, buyers, partners, internal capabilities, flows, constraints, and feedback loops, then identify the smallest high-leverage intervention. Use for platform strategy, ecosystem analysis, operating-model diagnosis, portfolio framing, and problems that keep recurring despite local fixes.
---

# Product System Leverage Map

Use this skill when a product problem crosses actors, teams, incentives, or lifecycle stages and a feature-level answer would be premature.

This is an original, agent-ready operationalization inspired by licensed product-system materials from Ethan Tan / Exponentially.io and Pureplay Studios Ltd. It does not reproduce their worksheets, diagrams, or examples. Do not add private source files or Drive links to a public artifact.

## Frame the system

Name the decision, system boundary, time horizon, and primary user outcome. Distinguish the user from the economic buyer, administrator, operator, partner, regulator, and internal team. Include an actor only when they exchange value, information, authority, risk, or work with the system.

Map the current system rather than the org chart or intended process. Mark each statement as evidence, inference, or unknown.

## Trace the flows

For each meaningful actor, trace:

- the outcome they seek and the behavior the product needs from them;
- value, money, data, attention, trust, decisions, and work moving through the system;
- alternatives and workarounds available when the system fails;
- delays, queues, handoffs, and points where state becomes ambiguous; and
- reinforcing or balancing feedback loops.

Do not assume that value flows in the same direction as revenue or that the buyer experiences the user's friction.

## Separate external value from internal health

External value describes changes users or ecosystem actors experience. Internal health describes the capabilities required to produce that value reliably: direction, alignment, discovery, delivery process, measurement, architecture, data, and capacity.

Treat internal health as an enabling constraint with a sufficient baseline, not an unlimited end in itself. Make the trade-off explicit when a health investment competes with a near-term user outcome.

## Diagnose constraints and leverage

Locate the few constraints that cap system performance. Distinguish:

- a root constraint from a downstream symptom;
- a stock problem from a flow problem;
- missing capability from poor adoption or incentives;
- local optimization from system improvement; and
- an acute incident from a repeating structural loop.

Evaluate candidate leverage points by user-outcome impact, system reach, evidence strength, controllability, time delay, reversibility, and second-order effects. Prefer an intervention that changes a governing rule, information flow, incentive, or feedback loop when evidence shows that a local feature cannot resolve the constraint.

## Design the first intervention

State the mechanism, affected actors, new friction, leading signal, system guardrails, owner, and stopping rule. Define the smallest credible test that can distinguish a true leverage point from a plausible story.

## Required outputs

Unless the user asks for prose only, deliver:

1. an executive system diagnosis;
2. a completed [Product System Leverage Canvas](references/product-system-leverage-canvas.md); and
3. one recommended intervention with a verification plan.

When a visual-capable environment is available, render the canvas as an accessible system map and include the compact Markdown version. Otherwise, use Markdown directly.

## Quality gate

Before delivering, confirm that:

- the boundary and primary outcome are explicit;
- actors and flows are evidence-backed rather than decorative;
- user value and internal health are not conflated;
- at least one feedback loop or time delay is considered;
- the recommended leverage point resolves a named constraint;
- immediate beneficiaries, new friction, and second-order effects are named; and
- the intervention has a metric contract, decision rule, and authoritative verification source.

## Permission boundary

Use authorized sources for read-only evidence. Do not invent system behavior, metrics, or agreement. Confirm before changing roadmaps, team structures, production systems, or stakeholder communications unless the user explicitly requested that action.
