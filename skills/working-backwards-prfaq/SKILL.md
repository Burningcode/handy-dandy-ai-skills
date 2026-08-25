---
name: working-backwards-prfaq
description: Create, critique, or reverse-engineer a Working Backwards PRFAQ that clarifies the customer, future experience, evidence, trade-offs, risks, and decisions before a team commits to building. Use for PRFAQs, future press releases, internal FAQs, product narratives, or sanitized pattern extraction from reference documents.
---

# Working Backwards PRFAQ

Write the smallest PRFAQ that can expose whether a product direction deserves investment. The press release should make the future customer value concrete; the internal FAQ should make weak assumptions and difficult decisions impossible to hide.

Use [the PRFAQ template](references/prfaq-template.md) for a full document. Read [the sanitized examples](references/sanitized-examples.md) only when the user asks for an example or the draft needs a concrete quality reference.

## Choose the mode

- **Draft:** turn research, strategy, or a product idea into a new PRFAQ.
- **Critique:** identify unsupported claims, generic customer language, missing decisions, weak differentiation, and hidden operational or technical risk before rewriting.
- **Reverse-engineer:** infer a reusable structure and decision standard from one or more reference PRFAQs, then rebuild from the current project's evidence.
- **Sanitize:** create a public-safe fictional composite that demonstrates the method without presenting private facts as shipped work.

Do not use a PRFAQ as post-hoc justification for a decision that the team refuses to pressure-test.

## Evidence and privacy boundary

Classify inputs as:

- **Fact:** directly supported by an identified source.
- **Inference:** a reasoned interpretation that must be labeled.
- **Recommendation:** a proposed choice and its trade-off.
- **Open question:** missing evidence or an unresolved decision.

Do not invent customer research, market size, product performance, launch dates, owners, costs, legal conclusions, or quotes from real people. Customer and leader quotes in a future press release are illustrative; label them as such in working drafts.

When reverse-engineering a private reference:

1. Extract the document's purpose, section pattern, question types, decision gates, and quality bar.
2. Discard names, companies, products, links, numbers, customer data, proprietary mechanisms, and distinctive phrasing.
3. Rebuild using only the new project's sources.
4. If publishing an example, use an explicitly fictional composite with synthetic names, facts, metrics, and timelines.

## Start with the decision

Before drafting, state:

1. The decision this PRFAQ must unlock.
2. The decision-maker and intended decision date, if known.
3. The customer behavior the product must create.
4. The strongest reason to do nothing or choose another path.
5. The smallest evidence needed to move forward.

If these are unknown, preserve them as visible open questions rather than smoothing them over with narrative.

## Press release quality bar

Write from a believable future in plain customer language. Include:

- A specific customer and high-value job.
- The current problem and why it matters now.
- The product and how the experience changes.
- Benefits expressed as customer or business outcomes, not a feature inventory.
- A short how-it-works journey that proves the concept is coherent.
- The most credible differentiation from the status quo and alternatives.
- A clear next step for the customer.

Avoid superlatives, category-creation claims, unsupported market statistics, and promises that the FAQ cannot operationally defend.

## Internal FAQ quality bar

Answer the questions that could change the investment decision:

- Who is the initial customer, user, buyer, and beneficiary? Where do their incentives diverge?
- What evidence shows the problem is frequent, painful, and worth solving now?
- What behavior changes if the product works?
- What does the status quo do well, and why will users switch?
- What is the smallest lovable or learnable scope? What is explicitly out?
- What could disappoint, harm, confuse, or exclude the customer?
- How will customers discover, adopt, trust, and repeatedly use it?
- How will success be measured: formula, population, baseline source, target, time window, and decision rule?
- What are the economics, operational burden, dependencies, and scaling constraints?
- What are the value, usability, feasibility, viability, trust, security, legal, and marketplace-balance risks?
- What is the most contentious decision and strongest counterargument?
- What must be true at each rollout gate? What triggers rollback, revision, or stopping?

Do not answer every possible question. Include the questions whose answers can change scope, sequence, funding, or the decision itself.

## AI and agentic extension

For products that reason, call tools, or change state, also define:

- The agent's bounded job and the user intent it serves.
- Authoritative state, allowed data, permitted tools, and prohibited actions.
- Actions allowed automatically versus preview, confirmation, approval, or escalation.
- Quality floor, target, and delight level.
- Evaluation set, grader or review method, segment thresholds, and silent failure detection.
- Recovery, idempotency, auditability, human override, privacy, security, and prompt-injection controls.
- End-to-end cost, latency, and quality trade-offs.

Adoption is not sufficient evidence of agent quality. Connect tool execution and evaluation results to authoritative product state and the intended business outcome.

## Milestones

Use milestones as learning and decision gates, not a feature wish list. For each milestone, specify:

- Hypothesis or risk being tested.
- Smallest scope.
- Evidence and success threshold.
- Owner and dependency, if known.
- Decision enabled: continue, expand, revise, partner, or stop.

Separate discovery estimates from committed delivery forecasts.

## Review passes

Repair the PRFAQ through four lenses:

1. **Customer:** Is the problem recognizable and the benefit meaningful without internal context?
2. **Executive:** Is the strategic fit, investment case, trade-off, and requested decision explicit?
3. **Builder:** Can Product, Design, Engineering, Data, Security, Operations, Support, and GTM see the implications without inventing requirements?
4. **Skeptic:** Which claim, incentive, dependency, failure mode, or operational cost is underweighted?

End with decisions made, decisions requested, open questions with validation methods, and next actions. Keep detailed research, schemas, and test matrices in appendices.

