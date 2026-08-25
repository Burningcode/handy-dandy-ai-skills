---
name: user-problem-outcome-journey
description: Turn any evidence-backed user problem into an as-is journey, outcome intent, to-be journey, prioritized opportunity map, end-to-end user stories, and smallest valuable release slices. Use for user journey mapping, scenario maps, story maps, service blueprints, IBM Enterprise Design Thinking-inspired framing, and teams moving from a problem to an outcome without jumping directly to features.
---

# User Problem-to-Outcome Journey

Create one causal canvas that connects a real user's current experience to a testable future outcome and an end-to-end delivery path.

This is an original, public-safe operationalization informed by IBM's publicly documented Enterprise Design Thinking framework and toolkit, including Hills, Playbacks, Sponsor Users, and As-Is and To-Be Scenario Maps. It is not an official IBM skill or reproduction of an IBM worksheet. When attribution matters, link to the [official framework](https://www.ibm.com/training/enterprise-design-thinking/framework) and [official toolkit](https://www.ibm.com/training/enterprise-design-thinking/toolkit).

## Ground the problem

Name the primary user, context, trigger, desired progress, observed problem, and decision the journey must change. Distinguish the end user from buyer, administrator, operator, and stakeholder. Do not create a persona biography when a role, situation, and behavior are enough.

Gather direct research, behavioral data, operational evidence, support signals, and prior decisions. Label every journey claim as observed, reported, inferred, or unknown. A stakeholder opinion is not a user observation.

## Map the as-is journey

Define the user's natural phases from trigger through attempted outcome. For each phase record:

- the job or progress sought;
- observable action and channel;
- expectation or mental model;
- emotional signal only when evidence supports it;
- friction, failure, delay, or workaround;
- system or human dependency; and
- evidence source and confidence.

Highlight moments that disproportionately determine success, abandonment, trust, or downstream work. Keep secondary actors in a dependency lane rather than replacing the primary user's journey.

## Define the outcome intent

Write a solution-independent intent with:

- **who:** the specific user and context;
- **outcome:** what they must be able to accomplish; and
- **differentiated proof:** the measurable or observable quality that makes the outcome meaningfully better.

Limit active outcome intents to the few a team can resource. Name foundational work separately so it does not masquerade as a user outcome.

## Design the to-be journey

For each phase, define the future user behavior, value realized, remaining or new friction, enabling product or service capability, and proof of success. Preserve the full outcome journey; do not turn the target state into a tour of screens or features.

Generate multiple opportunity responses before converging. Test desirability, usability, feasibility, viability, safety, accessibility, and operational support where relevant.

## Convert the journey into a story map

Use the journey phases as the horizontal backbone. Under each phase, describe user tasks as outcome-oriented stories. Organize vertically by necessity and learning value, not by stakeholder rank or implementation layer.

Create release slices that cross the full backbone and deliver a coherent user outcome. The first slice should be the smallest end-to-end experience that can test the riskiest assumption or provide real value. Put enabling technical work under the user outcome it supports or in a clearly named foundation lane.

## Keep users and stakeholders in the loop

Recruit representative design partners or sponsor users who are invested in the outcome and available to collaborate. Use playbacks to tell the end-to-end user story, expose misalignment, gather evidence, and record decisions. Do not treat a playback as a status presentation or substitute for broader research.

## Required outputs

Unless the user explicitly narrows the request, deliver:

1. a concise problem and outcome narrative;
2. a completed [Problem-to-Outcome Journey Canvas](references/problem-to-outcome-journey-canvas.md);
3. an end-to-end story map with release slices; and
4. a validation and playback plan.

When a visual-capable environment is available, render the canvas as an accessible left-to-right journey and include the compact Markdown version for portability. Otherwise, produce Markdown directly.

## Quality gate

Confirm that the canvas:

- follows one primary user in a real context;
- separates evidence from assumption;
- includes current behavior, not only pain-point labels;
- states a solution-independent outcome;
- makes new friction and secondary actors visible;
- links each story to a journey phase and user outcome;
- slices releases end to end rather than by component or function;
- defines success, guardrails, and the riskiest assumption; and
- names who will validate the journey and what decision the playback must change.

## Permission boundary

Use authorized sources for read-only research. Do not contact users, schedule sessions, change a backlog, or publish a roadmap without explicit authorization. Preserve anonymization and consent requirements for research evidence.
