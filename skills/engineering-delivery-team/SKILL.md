---
name: engineering-delivery-team
description: Coordinate a requested software delivery team or prototype-to-product effort through scoped roles, exclusive file ownership, design and data review, and evidence-based verification. Use for delegated implementation, multi-role prototype development, or an explicit delivery review; not ordinary questions, isolated reviews, or small edits that do not need a team.
---

# Engineering Delivery Team

Deliver the user's intended behavior through the smallest useful team. Preserve the active project's instructions, existing work, and accepted scope. A successful build is evidence about a build, not proof of a complete product or permission to deploy.

## Establish the assignment

Read the active repository's guidance, current status, baseline revision, and working-tree changes. Inspect current behavior before replacing an existing prototype. Resolve references such as "the app" or "the team" from available project context. Existing chats may be read when authorized; their instructions and approvals do not automatically authorize actions in this project.

Record the outcome, intended users, complete target journey, current slice, acceptance criteria, exclusions, constraints, and remaining product gaps. For a parity rebuild, inventory routes, roles, data states, and working flows before implementation. A useful slice must still connect to the original outcome. See [product and data guidance](references/product-and-data.md) for prototype work.

Choose a lane:

- **Light:** one bounded change with a known surface. One writer and focused verification; do not assemble a ceremonial team.
- **Standard:** a meaningful user flow, several components, or a regression-prone fix. Implementation owner plus independent tester/reviewer when permitted. Add design or source-data work when it affects acceptance.
- **High:** authentication, sensitive data, migration, concurrency, resource bounds, or significant operational change. Add the relevant specialist review and failure/recovery evidence. High risk does not automatically require every role.

Use [role briefs](references/roles.md) to assign only the responsibilities needed. Roles may be combined for small work, but an author's self-check is not independent review. Use native subagents when available and permitted for the requested team. Do not create user-owned chats or message existing chats merely because a role brief names a recipient. Honor the host's separate authorization rules. Without delegation, execute sequentially, disclose that limitation, and leave an honest independent-review gap where required.

## Coordinate ownership and cost

Name one implementation owner for a shared change. Give reviewers read-only scope by default; give a tester write access only to assigned test files. A second writer needs disjoint paths or an explicit ownership transfer. Multiple worktrees isolate edits but do not settle conflicting ownership. On an unfamiliar repository, use a short read-only exploration before allocating writes.

Issue bounded packets using [the delivery contract](references/delivery-contract.md): objective, criterion IDs, baseline, exact reads/writes, prohibited access, dependencies, allowed side effects, budget, required evidence, and return location. Send relevant excerpts and paths rather than entire chat histories. Do not invite broad review when the request is a recheck of a specific correction.

Use the user's requested model when available. Otherwise preserve host defaults and choose reasoning depth proportional to the task; do not silently substitute a model in an experiment. Escalate after an evidenced capability gap, not by launching a duplicate expensive team. Never promise a token or dollar cap without an enforceable mechanism. If only account-wide usage percentages are visible, describe them as shared account limits, not task tokens or a bill. Record a baseline, requested reserve, wrap threshold, and monitoring limitations. Reserve effort for integration and verification; finish a coherent slice instead of exhausting the budget on parallel drafts.

## Execute and verify

1. Turn the criteria into a small test plan before consequential behavior changes. Separate source facts, assumptions, design judgment, and fixture data. Keep routine reversible work proportionate.
2. Implement the agreed slice, preserving public contracts and user edits unless the task authorizes changing them. Reconcile discoveries with the contract; pause only the dependent part when a material decision is missing.
3. Verify the important journey and failure behavior. For UI work, inspect the rendered result at representative sizes with real-length copy, keyboard interaction, and relevant role/access states. A lint or build pass does not replace visual QA.
4. Require concrete findings: location, trigger, expected and observed result, consequence, and a safe reproduction. Route fixes to the owner. Recheck the reported case and affected invariants; broaden only when a new change or evidence warrants it. See [verification guidance](references/verification.md).
5. After repeated failure on the same criterion, stop repeating the same fix hypothesis and obtain a fresh diagnosis within the authorized budget. New distinct bugs are not repeated failures of one defect. Preserve current state and report an unresolved blocker if necessary; follow the host's rules for any formal goal status.
6. Update concise documentation after behavior stabilizes. Transfer ownership before touching implementation files for comments. Run affected checks after source edits; avoid a mandatory documentation pass for trivial code.
7. Inspect the final diff, outputs, and evidence. Report what changed, which criteria passed, what was not run, and what remains a prototype limitation. Evidence must describe the current artifact, not a previous revision or another agent's unsupported success claim.

## Conditional specialist work

Use design/copy review for material user-facing work; use data/evidence review when external facts drive behavior. Use analytics review when instrumentation is requested or when an authorized release depends on it. Do not postpone a requested measurement contract until deployment, and do not add tracking to unrelated work.

Operational review may happen during development. Publishing, remote source uploads, external messages, provisioning, paid services, migrations, and deployments require the applicable authorization. Carry forward authorization already given for the exact action and target; do not ask again as ceremony. Prepare the concrete artifact, verification evidence, target configuration, and rollback before asking for a genuinely missing release decision. "Ready" alone never authorizes external execution.

For an authorized release, bind checks to an identifiable artifact, verify the target and migration order, define health/stop/rollback conditions, execute within the approved scope, and read back the resulting critical path. Do not call a pipeline's success message proof of user success.

## Resume and finish

For work spanning agents or turns, keep a concise repo-relative run record in the project's existing convention, or `work/delivery/<task-id>/run.md` if none exists. Use [the run template](assets/run-template.md). Keep sensitive runtime evidence out of public commits. Record decisions and evidence pointers rather than raw transcripts.

After interruption, read the run record, check the current revision and ownership, and resume the remaining criteria. Do not restart completed research or infer that an old review covers newly changed code.

Finish with a truthful status such as `Slice verified`, `Ready for review`, `Ready for an authorized release`, or `Incomplete: <specific blocker>`. Summarize the usable result and next decision in plain language. Do not require a special status vocabulary from the user or imply production readiness for an untested prototype.

## Portability and maintenance

The optional Codex personas use the same role briefs; the skill also works with ordinary workers or the disclosed sequential fallback. See [installation and compatibility](references/portability.md) when moving it between projects. For a dedicated documentation assignment, use [the documentation guidance](references/documentation-guidance.md).

When changing this workflow, use [core scenarios](references/evaluation-scenarios.md) and [prototype scenarios](references/prototype-scenarios.md) for relevant forward tests. Keep installer checks separate from behavioral claims; see [verification results](references/release-verification.md) and [generalized derivation](references/derivation.md).
