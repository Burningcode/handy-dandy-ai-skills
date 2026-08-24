---
name: agentic-product-documentation
description: Turn product ideas, research, technical context, or reference PRDs into concise product briefs and decision-ready PRDs. Use when a team needs an executive summary, problem framing, goals and non-goals, metrics, requirements, agent behavior, evaluation, risks, rollout, or acceptance criteria. Do not use to invent evidence or expose private reference facts.
---

# Agentic Product Documentation

Create a document that helps leaders make a decision and builders produce the intended outcome. Preserve useful structure from references without carrying their product names, people, links, metrics, assumptions, or confidential implementation details into unrelated work.

## Choose the smallest useful mode

- **One-page brief:** early problem, prioritization, or discovery decision.
- **Full PRD:** a selected direction needs requirements, measurement, delivery, and launch clarity.
- **Reference reverse-build:** infer a reusable document pattern from an example, then rebuild it from the current project's evidence.
- **Critique:** identify decision gaps, unsupported claims, hidden risks, and unnecessary detail before rewriting.

If the requested decision can be made with a brief, do not manufacture a long PRD.

## Evidence and privacy boundary

Classify working inputs as:

- **Fact:** directly supported by a source.
- **Inference:** a reasoned interpretation that must be labeled.
- **Recommendation:** a proposed choice and its trade-off.
- **Open question / TBD:** information the team still needs.

Do not invent metrics, thresholds, research findings, technical constraints, dates, owners, or customer claims. A reference document may supply structure and quality cues without supplying facts. Remove private names, internal URLs, credentials, customer data, proprietary schemas, and employer-specific process language from public outputs.

## Product judgment first

Before drafting, answer or surface as open questions:

1. What behavior are we trying to create?
2. Who benefits immediately?
3. Who experiences new friction?
4. What second-order effects should we expect?
5. What feedback loop changes?
6. What assumption deserves explicit pushback?

Then identify the decision the document needs to unlock, the decision-maker, and the smallest evidence required.

## Drafting workflow

1. **Create the executive frame.** State the decision, problem, target user, why now, proposed direction, expected value, key trade-off, and requested action in language that can be understood without reading the rest.
2. **Define outcomes.** Specify the user behavior and business outcome. For an experiment, include the hypothesis, primary metric, success threshold, time window, population, and decision rule. If a value is unknown, leave a visible TBD with a named validation method.
3. **Set boundaries.** List goals, non-goals, users, use cases, assumptions, constraints, and the minimum viable scope. Explain why excluded work can wait.
4. **Compare credible options.** Include the status quo when it is viable. Evaluate value, usability, feasibility, viability, time to learning, operational complexity, and reversibility. Recommend one option and name the strongest counterargument.
5. **Describe the experience.** Use jobs-to-be-done, workflows, edge cases, user stories, and acceptance criteria only to the depth needed for the current decision and build stage.
6. **Make the system observable.** Define authoritative product state, events, metric formulas, dashboards, evaluation data, segment checks, and alert or review ownership.
7. **Plan delivery and learning.** Identify dependencies, risk owners, rollout, rollback, support readiness, instrumentation, decision gates, and the post-launch learning plan.
8. **Close with decisions.** Separate decisions made, decisions requested, open questions, owners, and next actions.

## AI and agentic product extension

When software can reason, call tools, or change state, explicitly define:

- User intent and the agent's bounded job.
- Data it may observe and the authoritative systems it may trust.
- Tools and actions it may use automatically.
- Actions requiring preview, confirmation, approval, or escalation.
- State transitions, idempotency, recovery, and auditability.
- Quality floor, target, and delight level.
- Silent failure modes and how users or operators discover them.
- Evaluation set, grader or review method, and segment-specific thresholds.
- Cost, latency, and quality trade-offs for the end-to-end workflow.
- Privacy, security, retention, prompt-injection, and least-privilege controls.
- Human override, appeal, fallback, and incident response.

Adoption alone is not evidence of agent quality. Connect experience signals and tool execution to authoritative product state, evaluation results, and business outcomes.

## Requirement quality

Every requirement should be:

- Traceable to a user, business, risk, or system need.
- Observable through an acceptance check, event, evaluation, or state transition.
- Clear about the happy path, material edge cases, and failure behavior.
- Explicit about ownership and external dependencies when those change delivery risk.

Avoid vague requirements such as “make it intuitive,” “use AI,” or “support scale.” Convert them into a target behavior, constraint, or measurable quality expectation.

## Review gates

Before handoff, critique and repair the draft from three lenses:

### Executive product leader

- Is the decision and why-now clear in the first screen?
- Is the strategic fit stronger than the strongest alternative use of the resources?
- Are value, user friction, second-order effects, and the feedback loop explicit?
- Are the recommendation, trade-offs, and requested decision unambiguous?

### Builder

- Can Product, Design, Engineering, Data, Security, Support, and GTM identify what they own?
- Are scope, states, interfaces, dependencies, acceptance criteria, instrumentation, rollout, and rollback concrete enough for the current stage?
- Could an agent act without inventing missing authority or requirements?

### Skeptic

- Which claims lack evidence?
- Which metric definitions, populations, denominators, time windows, or sources are missing?
- What user harm, operational burden, abuse path, failure mode, or incentive is underweighted?
- What should be simplified, tested first, or stopped?

## Output

Use [the PRD template](references/prd-template.md) for a full PRD. Omit sections that genuinely do not affect the decision; do not hide unavailable information by deleting a relevant section. Lead with the answer, keep the main narrative concise, and move detailed schemas or test matrices to appendices.

