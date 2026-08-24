# Handy Dandy Agent Skills

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
| [`agentic-product-documentation`](skills/agentic-product-documentation/SKILL.md) | Turns messy product context into an executive-ready brief or decision-ready PRD, with explicit evidence, risks, metrics, evaluation, rollout, and agent-specific quality boundaries. |
| [`creator-gifting-address-lookup`](skills/creator-gifting-address-lookup/SKILL.md) | Pulls creator names and gifting addresses for accepted campaign creators, generates a fresh Google Sheet, and drafts a verified handoff. |

The product-documentation skill also includes a [copy/paste prompt](prompts/build-a-decision-ready-prd.md) for tools that do not support skills.

## Public-safety principles

- Keep employer-specific systems, table names, channel IDs, customer data, credentials, and private examples in ignored local configuration.
- Separate source facts, inferences, recommendations, and open questions.
- Require explicit authorization before external writes, messages, releases, or irreversible actions.
- Read back and verify created artifacts rather than trusting a success message alone.

## Private configuration

The gifting lookup skill intentionally excludes company table names, Slack channel IDs, campaign IDs, and creator data. To use it in a company environment, copy its example configuration:

```bash
cp skills/creator-gifting-address-lookup/internal-config.example.md \
  skills/creator-gifting-address-lookup/internal-config.md
```

Fill in `internal-config.md` locally and do not commit it.

