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

| Skill | What it does |
| --- | --- |
| [`working-backwards-prfaq`](skills/working-backwards-prfaq/SKILL.md) | Creates, critiques, or reverse-engineers decision-ready PRFAQs while separating evidence from assumptions and sanitizing private references into fictional composites. |
| [`agentic-product-documentation`](skills/agentic-product-documentation/SKILL.md) | Turns messy product context into an executive-ready brief or decision-ready PRD, with explicit evidence, risks, metrics, evaluation, rollout, and agent-specific quality boundaries. |
| [`creator-gifting-address-lookup`](skills/creator-gifting-address-lookup/SKILL.md) | Demonstrates a bounded operational automation that enriches a source worklist through a read-only Amazon Athena MCP connector, preserves source rows, verifies a fresh review artifact, and keeps distribution human-controlled. |

The product-documentation skill also includes a [copy/paste prompt](prompts/build-a-decision-ready-prd.md) for tools that do not support skills. The PRFAQ skill includes a [decision-ready template](skills/working-backwards-prfaq/references/prfaq-template.md) and [fictional sanitized examples](skills/working-backwards-prfaq/references/sanitized-examples.md).

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

