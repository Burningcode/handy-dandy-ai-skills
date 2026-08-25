# Delivery contract and evidence gates

Read this reference when coordinating a Standard or High delivery, or when a Light change exposes interface, resource, or ownership risk.

## Coordinator contract

Record the following before implementation:

```yaml
task:
  id: <stable-short-id>
  outcome: <user-visible or system outcome>
  risk_lane: light | standard | high
  risk_reasons: []
  base_commit: <sha-or-not-a-git-repository>
  baseline_status: <clean-or-exact-pre-existing-changes>
  constraints: []
  non_goals: []
  assumptions: []

acceptance_criteria:
  - id: AC-1
    behavior: <observable result>
    implementation_owner: <one persona>
    verifier: <different persona when independence is required>
    evidence_required: []

interface_contract:
  immutable_names: []
  signatures: []
  return_shapes: []
  exceptions: []
  serialization: []
  side_effects: []
  scaffolding: []
  known_consumers: []
  authorized_migrations: []

resource_contract:
  input_bounds: []
  termination_mechanisms: []
  timeout_or_cancellation: []
  expected_memory_behavior: []
  overload_behavior: []
  rollback_or_last_known_good: []

documentation_contract:
  audience: <junior-or-project-specific-reader>
  finalized_change_surface: []
  public_or_reusable_surfaces: []
  domain_terms_to_define: []
  invariants_and_constraints: []
  preferred_locations: []
  generated_or_vendored_exclusions: []
  post_documentation_checks: []

ownership:
  - paths: []
    writer: <one persona>
    reviewers: []
    transfer_condition: <optional>

verification:
  required_commands: []
  generated_artifacts_to_inspect: []
  unavailable_checks: []
```

Do not invent interface details. Use Explorer evidence, existing tests, callers, documentation, and the provided scaffold. If a field is unknown and material, resolve it before implementation or record it as a blocking decision.

## Coordinated task packet

The Coordinator issues one packet per persona. Packets share the same contract version and name dependencies on other packets so work can be sequenced without losing the original requirements.

```yaml
packet:
  id: <task-id>/<persona>/<sequence>
  contract_version: <integer>
  role: <persona>
  objective: <bounded assignment>
  risk_lane: light | standard | high
  acceptance_criteria: []
  constraints: []
  non_goals: []
  interface_contract: <relevant fields or reference>
  resource_contract: <relevant fields or reference>
  writable_paths: []
  read_only_paths: []
  base_commit: <sha>
  baseline_status: <pre-existing changes that must be preserved>
  evidence_inputs: []
  required_commands_or_checks: []
  depends_on_packets: []
  blocks_packets: []
  correction_round: 0
  return_to: project_coordinator
```

Give each persona only the context needed for its assignment, but never omit its objective, assigned criteria, exact writable paths, applicable contracts, baseline state, evidence required, dependencies, or correction round. Reissue a packet with an incremented `contract_version` when the user changes scope or a resolved discovery changes the contract; do not let personas work from conflicting versions.

Two personas may work concurrently only when their writes are disjoint or all but one are read-only. If ownership must move, the Coordinator records the transfer before the new writer edits the path. The Code Documenter receives write ownership only after the affected executable behavior passes its regression gate.

## Handoff receipt

Require this structure from every role:

```yaml
role: <persona>
packet_id: <task-packet-id>
contract_version: <integer>
status: complete | revision_required | blocked
acceptance_criteria: []
base_commit: <sha>
head_commit_or_worktree: <sha-or-uncommitted>
files_changed: []
files_reviewed: []
decisions: []
commands:
  - command: <exact-command-or-safe-summary>
    exit_code: <integer-or-not-run>
    observed: <result-not-success-claim>
defects: []
residual_risks: []
unverified_assumptions: []
```

Tester handoffs also state `contract_compatibility: passed | failed | not_applicable` and `termination_verified: passed | failed | not_applicable`. SRE handoffs distinguish measurements from estimates. Code Documenter handoffs also state `behavior_changed: false`, documentation added or updated, intentionally undocumented areas with reasons, and post-documentation checks.

## Gates

1. **Specification and compatibility gate**
   - Every acceptance criterion is observable and assigned.
   - The interface contract reflects actual callers and scaffolding.
   - Any intentional contract change has explicit authorization, affected consumers, and migration evidence.
   - The early test plan can prove the important behavior.

2. **Implementation gate**
   - The diff stays within owned paths and requested scope.
   - Relevant existing checks pass with recorded exit codes.
   - Defensive behavior is proportional to real trust-boundary and termination risks.

3. **Reliability gate** when SRE is required
   - Failure, overload, concurrency, security, observability, resource, rollback, and deployment risks are reviewed in proportion to the change.
   - CPU, memory, file descriptor, connection, task, retry, queue, fan-out, and buffering growth are bounded or explicitly justified.
   - Blocking findings are corrected by the proper owner and re-reviewed.

4. **Independent regression gate**
   - The Tester runs executable unit/integration/system checks appropriate to the change.
   - Relevant malformed, cyclic, type-wrong, extreme, repeated, partial-failure, and massive-input cases are exercised safely.
   - Skipped, filtered, flaky, or unavailable checks are not reported as passes.

5. **Documentation clarity gate** for finalized executable changes
   - The documented change surface matches the final implementation and tests.
   - Comments and docstrings explain purpose, contracts, invariants, or non-obvious choices instead of narrating syntax.
   - Public and reusable behavior has the concise developer documentation required by project conventions.
   - No executable behavior, interface, dependency, schema, test, generated file, or unrelated formatting changed.
   - Targeted syntax, lint, build, or test checks pass after source documentation edits.

6. **Final acceptance gate**
   - Inspect the final diff and generated artifacts.
   - Map actual evidence to every acceptance criterion.
   - Confirm no ownership violation, stale documentation, unresolved requested revision, blocking risk, or missing required check remains.

## Bounded correction protocol

- **First failure:** return the exact criterion, evidence, and expected behavior to its owner.
- **Second failure:** include the minimal reproduction and challenge whether the implementation or contract assumption is wrong.
- **Before the third attempt:** obtain a fresh read-only root-cause analysis from Explorer or another independent reviewer who has not authored the fix.
- **After a third failed verification:** stop, report `Blocked`, preserve the ledger, and name the decision, authority, or new evidence needed to continue.

## Lightweight run ledger

For durable runs, update `.codex/runs/<task-id>/run.md` after contract approval, each task-packet issue or version change, each ownership transfer, each gate, and each correction round. Keep the latest state plus concise evidence pointers; do not paste large logs. Suggested sections are `Contract`, `Task Packets`, `Ownership`, `Current Gate`, `Revision History`, `Evidence`, and `Open Risks`.
