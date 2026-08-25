---
name: async-work-burndown
description: Prepare an asynchronous work session by gathering read-only context, classifying each item as agent-executable, needs approval, or open, drafting exact actions for review, and executing only approved work with read-back verification. Use for todo burndowns, delegated prep, and multi-system working sessions.
---

# Async Work Burndown

This public-safe example generalizes a private multi-connector work loop. The agent does the legwork while the user is away, presents a reviewable action packet, and executes only authorized items.

## Operating contract

1. Gather context read-only unless a write was explicitly requested.
2. Take the smaller reasonable interpretation of ambiguity.
3. Run independent lookups in parallel when available.
4. Give every item a verdict.
5. Put the exact proposed action in the review packet.
6. Verify every approved write by reading the resulting artifact back.

## Task states

| State | Meaning |
| --- | --- |
| Prepared | Draft or exact action is ready; awaiting approval when required |
| Open item | Missing evidence, authority, or user judgment blocks a safe action |
| Approved | User authorized the exact action |
| Done | Action executed and verified |
| Removed | User chose to skip or handle it elsewhere |

Do not label an item done from an API success response alone.

## Gather the most authoritative evidence

Choose sources by task:

- latest explicit decision or meeting record for scope;
- work tracker for delivery state and ownership;
- product document for intended outcome and boundaries;
- design artifact for experience state;
- warehouse or transactional system for measured outcomes;
- conversation thread for recent context and unresolved debate;
- repository for source-controlled work and verification.

Label inaccessible sources and conflicting evidence.

## Action card

```markdown
### [Task]

Status: [Prepared / Open item]

Evidence:
- [Fact, source, date]

Recommended action:
[Exact draft, query, edit, or command]

Approval needed:
[Specific decision or “None; explicitly requested”]

Verification:
[How the result will be read back or tested]
```

## Review packet

1. **Bottom line:** task count, prepared count, and open-item count.
2. **When you return:** the smallest set of approvals or answers needed.
3. **Prepared actions:** exact reversible drafts or commands.
4. **Open items:** missing choice, evidence, authority, or dependency.
5. **Execution order:** highest value and dependency-clearing work first.
6. **Verification plan:** source-specific read-back checks.

## Hypothetical example

Fictional todo list:

| Item | Classification | Prepared result |
| --- | --- | --- |
| Draft launch update | Prepared | Unsent message with source links and verified date |
| Change launch date | Open item | Needs decision owner and downstream dependency check |
| Analyze onboarding drop-off | Prepared | Read-only metric contract and query specification |
| Close duplicate ticket | Open item | Candidate duplicate found; deletion or closure needs approval |

The scenario is fictional and contains no real systems or people.

## Execution loop

After approval:

1. Execute only the approved scope.
2. Read the affected message, ticket, document, repository, or dashboard back.
3. Compare the result with the approved draft.
4. Mark done only when verified.
5. Reclassify downstream tasks if the action changed their context.

## Boundaries

Never use a broad todo request as permission to send messages, edit tickets, publish documents, change access, commit unrelated files, or make irreversible decisions. Keep credentials, private identifiers, and raw sensitive content out of the review packet.

