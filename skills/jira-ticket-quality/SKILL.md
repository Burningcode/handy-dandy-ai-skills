---
name: jira-ticket-quality
description: Improve issue quality by scanning for duplicates before creation, distinguishing bugs from user stories, preserving verified facts, and producing reproducible bug reports or outcome-oriented stories with testable acceptance criteria. Use when drafting, reviewing, or creating work-tracker issues.
---

# Jira Ticket Quality

This hypothetical example uses Jira terminology, but the pattern applies to any issue tracker. Replace the fictional project and fields with the authorized environment.

## Intake

Establish:

- bug, user story, spike, or task;
- working title and intended project;
- existing notes, evidence, or links;
- reporter intent: new work, known related item, or suspected duplicate;
- permission to search and, separately, to create or edit.

Do not invent missing facts. Mark unknowns as `TBD` or ask one focused question.

## Duplicate scan before creation

1. Extract distinctive product, symptom, error, endpoint, user, and outcome terms.
2. Search the target project, then adjacent projects if authorized.
3. Compare symptom, root cause, affected workflow, and likely fix area—not only the title.
4. Classify matches as likely duplicate, related, or distinct.
5. Report key, summary, state, date, and why it may match.

For a strong duplicate, recommend updating or linking the existing issue. Do not create a second issue unless the user explicitly overrides.

## Bug contract

```markdown
## Summary
[One sentence describing what is broken]

## Environment
- Surface or client:
- Version or build:
- User role or segment:

## Steps to reproduce
1.
2.
3.

## Expected result

## Actual result

## Evidence
- Screenshot, log, request ID, or `TBD`

## Scope and severity
[Affected population, frequency, reversibility, and business or safety impact]

## Related work
- [Ticket or incident]
```

Bar: another engineer can reproduce or rule out the problem without a meeting.

## User-story contract

```markdown
## Key user
- Primary user:
- Why they care:

## Problem and outcome
- Today:
- Desired behavior:

## Story
As a [specific user], I want [capability], so that [outcome].

## Acceptance criteria
### Scenario 1 — Primary path
- Given [context]
- When [action]
- Then [observable result]

### Scenario 2 — Edge or failure path
- Given
- When
- Then

## Out of scope
- [Explicit non-goal]

## Dependencies and evidence
- [Links]
```

Flag technical tasks disguised as user stories. Keep engineering subtasks linked under the user-valued outcome.

## Hypothetical example

Proposed issue: “Export is broken.”

Duplicate scan finds fictional `DEMO-204`, “Large CSV export times out after filter change.” The new report affects the same endpoint, user segment, and failure signature. Recommend adding the new evidence to `DEMO-204` instead of creating a duplicate.

If distinct, strengthen the new issue with:

- affected file size and filter state;
- reproducible steps;
- expected download behavior;
- observed timeout and request identifier;
- severity and workaround;
- explicit boundary for other export formats.

All identifiers and facts are fictional.

## Quality and permission gate

- Facts are traceable to the reporter or evidence.
- User and outcome are specific.
- Acceptance criteria are observable and include a failure case.
- Related issues are linked.
- Duplicate disposition is recorded.
- Creation or editing requires explicit authorization when not already requested.
- After a write, read the issue back and verify formatting and fields.

