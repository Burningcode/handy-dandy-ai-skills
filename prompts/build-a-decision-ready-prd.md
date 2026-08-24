# Prompt: build a decision-ready PRD

Copy the prompt below into an AI tool, then attach or paste the product context beneath it.

```text
Act as an executive product leader and a hands-on agentic product builder.

Turn the supplied context into the smallest product document that can unlock the next real decision. Use a one-page brief if the problem or direction is still being selected; use a full PRD only when a direction needs cross-functional delivery clarity.

First, critique the inputs. Separate:
- source-supported facts
- inferences
- recommendations
- open questions or missing evidence

Do not invent metrics, thresholds, research findings, dates, owners, technical constraints, or customer claims. Treat any reference PRD as a source of structure and quality cues, not as factual authority for this project. Remove private names, internal links, customer data, credentials, proprietary schemas, and employer-specific implementation details from public output.

Before drafting, determine:
1. The decision this document must unlock and who makes it.
2. The behavior we are trying to create.
3. Who benefits immediately and who experiences new friction.
4. The second-order effects and feedback loop that may change.
5. The assumption that most deserves pushback.
6. The smallest credible version and the strongest alternative, including doing nothing.

For the document:
- Lead with a concise executive summary: problem, why now, recommendation, expected value, key trade-off, and requested decision.
- Define goals and explicit non-goals.
- State the hypothesis, primary metric, metric formula, population, baseline source, success threshold, time window, and decision rule. Leave a visible, owned TBD when evidence is missing.
- Compare credible options across user value, business value, feasibility, time to learning, complexity, risk, and reversibility.
- Describe the end-to-end experience, requirements, material edge cases, failure behavior, and acceptance evidence.
- Identify dependencies, risk owners, instrumentation, rollout, rollback, support readiness, and post-launch learning.

If the product uses AI agents or tool-calling software, also define:
- the agent's bounded job
- authoritative product state and allowed data
- actions allowed automatically
- preview, confirmation, human approval, and prohibited actions
- quality floor, target, and delight level
- silent failure modes and how they become observable
- evaluation data, segments, thresholds, and review method
- recovery, override, auditability, privacy, security, and prompt-injection controls
- cost, latency, and quality trade-offs

End with:
- decisions made
- decisions requested
- open questions with owners and validation methods
- next actions with owners and evidence of completion

After drafting, run three short review passes and repair the document:
1. Executive: Is the decision, strategic value, trade-off, and requested action obvious?
2. Builder: Can each function and any coding agent act without inventing missing authority or requirements?
3. Skeptic: Which claim, incentive, failure mode, operational burden, or user harm is underweighted?

Keep the main narrative concise. Move detailed schemas, test matrices, or research notes to appendices only when they materially help execution.

PROJECT CONTEXT
[Paste the idea, research, user feedback, data, constraints, technical context, and reference links here.]
```

