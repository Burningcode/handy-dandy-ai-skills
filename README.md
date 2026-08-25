# Handy Dandy AI Skills

Public-safe, reusable skills for product leadership and operational workflows. Each skill is written to make decision boundaries, verification, and private configuration explicit.

## Install a skill

Copy a skill folder into the skills directory used by your agent or editor. For Cursor:

```bash
mkdir -p ~/.cursor/skills
cp -R skills/<skill-name> ~/.cursor/skills/
```

Then reload the application.

## Included skills

| Skill | Category | What it demonstrates |
| --- | --- | --- |
| [`working-backwards-prfaq`](skills/working-backwards-prfaq/SKILL.md) | Product strategy | Creates, critiques, or reverse-engineers decision-ready PRFAQs while separating evidence from assumptions and sanitizing private references into fictional composites. |
| [`agentic-product-documentation`](skills/agentic-product-documentation/SKILL.md) | Product delivery | Turns messy product context into an executive-ready brief or decision-ready PRD, with explicit evidence, risks, metrics, evaluation, rollout, and agent-specific quality boundaries. |
| [`executive-decision-brief`](skills/executive-decision-brief/SKILL.md) | Executive decision example | Frames an outcome, challenges a foundational assumption, compares viable options across four product risks, and ends with a clear recommendation and decision gate. |
| [`product-discovery-coach`](skills/product-discovery-coach/SKILL.md) | Product discovery example | Operates as both builder and coach: diagnoses weak opportunity framing, gathers evidence, tests assumptions, and produces an outcome-oriented discovery brief. |
| [`next-gen-product-analytics`](skills/next-gen-product-analytics/SKILL.md) | AI product analytics | Connects agent experience, tool execution, authoritative state, evaluations, durable outcomes, and business value into decision-ready measurement systems. |
| [`metric-root-cause-investigation`](skills/metric-root-cause-investigation/SKILL.md) | Analytics investigation | Locates funnel and product-quality failures through metric contracts, positional hypotheses, segmented evidence, contrastive traces, and explicit confidence. |
| [`marketplace-offer-funnel-analysis`](skills/marketplace-offer-funnel-analysis/SKILL.md) | Marketplace analytics example | Demonstrates a fictional warehouse-backed offer lifecycle analysis while keeping real schemas, identifiers, and data in private configuration. |
| [`cross-functional-status-synthesis`](skills/cross-functional-status-synthesis/SKILL.md) | Operating system | Synthesizes distributed program evidence into an executive readout, communications-readiness assessment, draft updates, and prioritized chase list. |
| [`program-update-communications`](skills/program-update-communications/SKILL.md) | Stakeholder communication example | Routes launches, decisions, scope locks, blockers, and holding patterns into concise main messages, evidence-rich threads, and action-shaped replies. |
| [`async-work-burndown`](skills/async-work-burndown/SKILL.md) | Agentic operations example | Prepares multi-system work asynchronously, separates drafted actions from approval gates, and verifies every authorized execution. |
| [`backlog-grooming-prep`](skills/backlog-grooming-prep/SKILL.md) | Product delivery example | Classifies backlog readiness, elevates material risks, identifies exact ticket gaps, and designs a focused grooming working session. |
| [`jira-ticket-quality`](skills/jira-ticket-quality/SKILL.md) | Delivery quality example | Scans for duplicates before creation and turns partial input into reproducible bugs or outcome-oriented stories with testable criteria. |
| [`user-scenario-publishing`](skills/user-scenario-publishing/SKILL.md) | Documentation-as-code example | Defines and validates a parser-sensitive Markdown contract, renders a review artifact, and verifies source-to-document coverage. |
| [`multi-repository-knowledge-sync`](skills/multi-repository-knowledge-sync/SKILL.md) | Knowledge operations example | Demonstrates check, dry-run, scoped sync, secret exclusion, and remote verification across a fictional documentation portfolio. |
| [`creator-gifting-address-lookup`](skills/creator-gifting-address-lookup/SKILL.md) | Operational automation example | Demonstrates a bounded automation that enriches a source worklist through a read-only Amazon Athena MCP connector, preserves source rows, verifies a fresh review artifact, and keeps distribution human-controlled. |

The product-documentation skill also includes a [copy/paste prompt](prompts/build-a-decision-ready-prd.md) for tools that do not support skills. The PRFAQ skill includes a [decision-ready template](skills/working-backwards-prfaq/references/prfaq-template.md) and [fictional sanitized examples](skills/working-backwards-prfaq/references/sanitized-examples.md).

These are not prompts dressed up as process. Each skill defines an operating contract: what evidence to gather, how to reason about it, what the agent may change, how to verify the result, and where human judgment remains accountable.

Several skills are explicitly labeled as examples. They preserve reusable operating patterns while replacing real organizations, projects, people, systems, schemas, paths, ticket keys, and metrics with fictional placeholders. The examples are starting points for authorized adaptation, not claims about a current employer or turnkey production integrations.

## Public-safety principles

- Keep employer-specific systems, table names, channel IDs, customer data, credentials, and private examples in ignored local configuration.
- Separate source facts, inferences, recommendations, and open questions.
- Require explicit authorization before external writes, messages, releases, or irreversible actions.
- Read back and verify created artifacts rather than trusting a success message alone.

## Adapting the operational example

The gifting lookup is intentionally an example rather than a turnkey production integration. It excludes company schemas, table names, accounts, channels, campaign IDs, creator data, and credentials. To adapt the operating pattern in an authorized environment, copy its non-functional example configuration:

```bash
cp skills/creator-gifting-address-lookup/internal-config.example.md \
  skills/creator-gifting-address-lookup/internal-config.md
```

Fill in `internal-config.md` locally and do not commit it.

