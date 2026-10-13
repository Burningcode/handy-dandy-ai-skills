# Handy Dandy AI Skills

A public catalogue of 19 reusable skills for product leadership and operational workflows, plus links to paid workbenches. Each skill is written to make decision boundaries, verification, and private configuration explicit.

## Paid workbenches on Agensi

For complete practice packages, visit [C.J. Burns on Agensi](https://www.agensi.io/creators/clay-burns). The paid editions add original fictional exercises, supporting resources and delivery reviews to the workflows. Listings include worked demonstrations so you can inspect the output before buying.

| Group | Bundle | Included workbenches | One-time price (USD) |
| --- | --- | --- | ---: |
| Product management | [Product Discovery and Decisions](https://www.agensi.io/bundles/product-discovery-and-decisions) | Working Backwards PRFAQ, Competitive Product Teardown, Executive Decision Brief | $25.74 |
| Product management | [Product Execution and Measurement](https://www.agensi.io/bundles/product-execution-and-measurement) | Product PRD, Product Outcomes and Metrics, Metric Drop Investigator, AI Agent Product Analytics | $35.10 |
| Career and interview practice | [Case Practice and Assessment](https://www.agensi.io/bundles/case-practice-and-assessment) | Executive Case Practice Studio, Timed Product Case Coach, Interview & Case Grader | $32.76 |

Each bundle is 35% below the combined individual prices. Check the linked listings for current contents, prices and availability. Individual skills are also available through the creator page.

Case Practice Studio creates and evaluates practice cases. Interview & Case Grader assesses supplied responses and interview turns, records interviewer assistance and distinguishes missing evidence from observed mistakes. Practice scores are diagnostic feedback, not predictions of hiring outcomes.

The supplied-context workflows were exercised in Codex with fictional evidence. Connected-service execution, other agent products and autonomous coordination across skills have not been independently validated. Paid source and release archives are maintained privately; purchases are delivered through Agensi.

### New workbenches submitted for review

Two additional standalone packages were submitted on October 13, 2026 and are awaiting Agensi review:

| Workbench | What it produces | One-time price (USD) |
| --- | --- | ---: |
| Customer Research Synthesis Workbench | Traceable findings, segment comparisons, contradictory evidence and a next research decision from supplied customer notes | $14.40 |
| Backlog Readiness Workbench | Ticket readiness assessment, relationship map, complete repair drafts and a focused grooming agenda from supplied exports | $14.40 |

Their fictional supplied-context exercises were completed in Codex. Live services and other agent products were not tested. These packages are not included in the three bundles above. Check the [creator page](https://www.agensi.io/creators/clay-burns) for approval and availability; submission is not a live listing.

### Athena analytics companion

An Athena MCP connector and setup kit is being evaluated to help buyers use the analytics workflows with their own authorized AWS data. It is not released or included in current purchases. The existing [Athena workflow example](skills/creator-gifting-address-lookup/SKILL.md) demonstrates the pattern with placeholders; it does not ship a production connector.

## Previously public workflows

Eight earlier source workflows are now maintained privately. Their public installation entries have been retired; see the [migration map](MIGRATED-SKILLS.md) for the corresponding paid editions. The free skills listed below remain available.

This public repository was rebuilt with fresh history on October 13, 2026. Previous repository history is preserved privately. If you maintain an older checkout, clone this repository again rather than merging or force-pushing the old history into it.

## Install with the Skills CLI

The repository is a discoverable skills package. List all available skills without installing them:

```bash
npx skills add Burningcode/handy-dandy-ai-skills --list
```

Install one skill globally for compatible agents, including Codex:

```bash
npx skills add Burningcode/handy-dandy-ai-skills \
  --skill engineering-delivery-team \
  --global \
  --yes
```

Install every skill for every supported agent:

```bash
npx skills add Burningcode/handy-dandy-ai-skills --all
```

Generate a prompt from one skill without installing it:

```bash
npx skills use Burningcode/handy-dandy-ai-skills@product-discovery-coach
```

Reload the target agent after installation. Each skill remains independently selectable through `owner/repo@skill-name`.

## Manual installation

Copy a skill folder into the skills directory used by your agent or editor. For Cursor:

```bash
mkdir -p ~/.cursor/skills
cp -R skills/<skill-name> ~/.cursor/skills/
```

Then reload the application.

## Package contract

- Put every distributable skill under `skills/<skill-name>/SKILL.md`.
- Set the frontmatter `name` to the exact folder name and provide a concise `description`.
- Keep supporting scripts, references, examples, and assets inside that skill folder.
- Do not add a repository-root `SKILL.md`; the Skills CLI must discover the individual folders.
- Run `node scripts/validate-skills.mjs` before pushing. GitHub Actions runs the same validation on pushes and pull requests.

The `engineering-delivery-team` skill also includes six Codex persona configurations and a PowerShell installer. Install the complete team into a project with:

```powershell
.\skills\engineering-delivery-team\scripts\Install-EngineeringDeliveryTeam.ps1 -TargetProject 'C:\work\your-project'
```

Use `-Personal` instead to install under `CODEX_HOME`, or under `~/.codex` when `CODEX_HOME` is unset.

## Included skills

| Skill | Category | What it demonstrates |
| --- | --- | --- |
| [`engineering-delivery-team`](skills/engineering-delivery-team/SKILL.md) | Engineering delivery | Risk-sizes work across a Coordinator, read-only Explorer, Staff Engineer, SRE, Senior Tester, and post-finalization Code Documenter using versioned task packets, exclusive file ownership, compatibility/resource contracts, and independent evidence gates. |
| [`probe-product-analysis`](skills/probe-product-analysis/SKILL.md) | Product analysis | Applies Purpose, Reality, Obstacles, Bets, and Experiments as an evidence-backed loop, producing both a decision analysis and a one-page decision canvas. |
| [`user-problem-outcome-journey`](skills/user-problem-outcome-journey/SKILL.md) | Experience strategy | Connects an evidence-backed user problem to as-is and to-be journeys, outcome intent, opportunities, end-to-end user stories, release slices, and a decision canvas. |
| [`product-system-leverage-map`](skills/product-system-leverage-map/SKILL.md) | Systems strategy | Maps actors, exchanges, internal health, constraints, delays, and feedback loops to identify a small, testable system leverage point. |
| [`product-vision-alignment`](skills/product-vision-alignment/SKILL.md) | Product vision | Creates or critiques an evidence-grounded future user transformation and pairs it with an original alignment canvas and stakeholder playback. |
| [`product-principles-decision-review`](skills/product-principles-decision-review/SKILL.md) | Leadership system | Turns product principles into observable rules for resolving recurring trade-offs, including boundaries, counterexamples, and conflict review. |
| [`product-process-improvement`](skills/product-process-improvement/SKILL.md) | Operating model | Maps actual demand-to-outcome flow, diagnoses waits and rework, and designs a reversible one-cycle process experiment with user-outcome guardrails. |
| [`market-and-gtm-strategy`](skills/market-and-gtm-strategy/SKILL.md) | Market and growth strategy | Connects decision-driven market research, segment selection, positioning, pricing, route to market, staged launch, and commercial learning into one evidence-backed operating contract. |
| [`collaborative-product-critic`](skills/collaborative-product-critic/SKILL.md) | Executive product coaching | Steelmans an idea, probes the highest-value assumption, applies product, strategy, system, commercial, and agentic lenses, and converts critique into stronger options and a bounded learning decision. |
| [`product-discovery-coach`](skills/product-discovery-coach/SKILL.md) | Product discovery example | Operates as both builder and coach: diagnoses weak opportunity framing, gathers evidence, tests assumptions, and produces an outcome-oriented discovery brief. |
| [`marketplace-offer-funnel-analysis`](skills/marketplace-offer-funnel-analysis/SKILL.md) | Marketplace analytics example | Demonstrates a fictional warehouse-backed offer lifecycle analysis while keeping real schemas, identifiers, and data in private configuration. |
| [`cross-functional-status-synthesis`](skills/cross-functional-status-synthesis/SKILL.md) | Operating system | Synthesizes distributed program evidence into an executive readout, communications-readiness assessment, draft updates, and prioritized chase list. |
| [`program-update-communications`](skills/program-update-communications/SKILL.md) | Stakeholder communication example | Routes launches, decisions, scope locks, blockers, and holding patterns into concise main messages, evidence-rich threads, and action-shaped replies. |
| [`async-work-burndown`](skills/async-work-burndown/SKILL.md) | Agentic operations example | Prepares multi-system work asynchronously, separates drafted actions from approval gates, and verifies every authorized execution. |
| [`backlog-grooming-prep`](skills/backlog-grooming-prep/SKILL.md) | Product delivery example | Classifies backlog readiness, elevates material risks, identifies exact ticket gaps, and designs a focused grooming working session. |
| [`jira-ticket-quality`](skills/jira-ticket-quality/SKILL.md) | Delivery quality example | Scans for duplicates before creation and turns partial input into reproducible bugs or outcome-oriented stories with testable criteria. |
| [`user-scenario-publishing`](skills/user-scenario-publishing/SKILL.md) | Documentation-as-code example | Defines and validates a parser-sensitive Markdown contract, renders a review artifact, and verifies source-to-document coverage. |
| [`multi-repository-knowledge-sync`](skills/multi-repository-knowledge-sync/SKILL.md) | Knowledge operations example | Demonstrates check, dry-run, scoped sync, secret exclusion, and remote verification across a fictional documentation portfolio. |
| [`creator-gifting-address-lookup`](skills/creator-gifting-address-lookup/SKILL.md) | Operational automation example | Demonstrates a bounded automation that enriches a source worklist through a read-only Amazon Athena MCP connector, preserves source rows, verifies a fresh review artifact, and keeps distribution human-controlled. |

The remaining product-framework skills include original public canvases that make evidence, causal links, trade-offs, and decision rules visible without reproducing private or licensed worksheets.

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
