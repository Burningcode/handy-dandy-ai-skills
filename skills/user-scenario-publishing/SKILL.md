---
name: user-scenario-publishing
description: Author and publish structured user-scenario Markdown through a deterministic document pipeline by defining a source contract, validating parser-sensitive structure, rendering to a reviewable document, comparing source coverage, and preserving links, acceptance criteria, and version provenance. Use for documentation-as-code and generated product artifacts.
---

# User Scenario Publishing

This hypothetical example generalizes an internal Markdown-to-document publishing workflow. All paths, identifiers, domains, and examples are fictional.

## Treat the source and renderer as one system

The Markdown contract and publisher cannot be designed independently. If the renderer keys on headings, labels, or list syntax, deviations can silently drop stories, flatten acceptance criteria, or break tables.

Keep the Markdown source canonical. Treat the rendered document as a generated, reviewable artifact unless the workflow explicitly supports safe round-trip editing.

## Example source contract

```markdown
# DEMO-100: Guided Setup — User Scenarios

**Companion brief:** [Guided Setup](../briefs/guided-setup.md)
**Owner:** [Role or name]
**Version:** 1.0 — [change summary]

## Epic 1 — Publish a first item

> **Job:** A new seller publishes a valid first item without support.

### Story 1.1 — Identify required fields · NEW

**Persona:** New seller
**Surface:** Catalog setup

> As a new seller, I want to see which fields are required so that I can publish successfully.

**Acceptance Criteria:**

- Given an incomplete item, when I review setup, then required fields are distinguishable.
- Given a missing requirement, when I attempt to publish, then focus moves to an actionable error.

## Open questions

1. Which fields vary by category, and who owns that rule?
```

The ticket, product, and scenario are fictional.

## Contract rules

Define and version:

- accepted heading hierarchy;
- story identifier pattern;
- allowed status tags;
- required metadata blocks and order;
- narrative and acceptance-criteria syntax;
- table, link, and nested-list handling;
- escaping rules;
- behavior for unknown or malformed sections.

Fail visibly on invalid structure. Do not silently omit content.

## Publishing workflow

1. Read the source and publisher configuration.
2. Validate structure before rendering.
3. Count epics, stories, acceptance criteria, tables, and links.
4. Render to a new review artifact or versioned destination.
5. Read the rendered document back.
6. Compare source and destination counts and identifiers.
7. Inspect representative formatting, nested lists, links, and tables.
8. Publish or replace the canonical rendered artifact only after verification.
9. Record source revision, renderer version, render time, and destination link.

## Verification report

| Check | Source | Rendered | Result |
| --- | --- | --- | --- |
| Epic count | [N] | [N] | Pass or fail |
| Story IDs | [List] | [List] | Pass or fail |
| Acceptance criteria | [N] | [N] | Pass or fail |
| Links | [N] | [N] | Pass or fail |
| Tables | [N] | [N] | Pass or fail |

Also inspect text that could be lost through Unicode normalization, Markdown parsing, or rich-text conversion.

## Change safety

- Render to a draft or new version before replacing a shared artifact.
- Preserve unrelated comments, permissions, and document topology when editing an existing destination.
- Do not update the source and rendered copy independently without recording which is canonical.
- If users edit the generated document, define a reconciliation policy rather than silently overwriting their work.

## Hypothetical failure example

The source contains six stories, but the rendered document contains five because one heading uses an en dash while the parser expects an em dash. The correct behavior is to fail validation with the exact story heading, not to publish a plausible-looking incomplete document.

## Permission and privacy boundary

Read and validate within scope. Confirm before replacing a shared document, changing permissions, or publishing externally unless explicitly authorized. Do not include private product links, real ticket domains, customer data, or internal owner names in a public example.

