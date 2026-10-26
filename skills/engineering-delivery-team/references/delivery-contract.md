# Delivery contract

Use only fields that affect the assignment. Reuse existing project records instead of creating parallel documentation. This example is a schema guide; fill values from observed context, not assumptions disguised as facts.

```yaml
task_id: stable-short-name
contract_version: 1
outcome: user-visible result
full_journey: trigger through verified result
current_slice: what this increment delivers
remaining_product_gaps: []
risk_lane: standard
risk_reasons: []
baseline_revision: observed revision or no repository
pre_existing_changes: []
constraints: []
non_goals: []
decisions_and_assumptions: []
acceptance:
  - id: AC-1
    behavior: observable outcome
    owner: implementation owner
    verifier: assigned reviewer or self-check disclosed
    required_evidence: []
    result: pending
ownership:
  - writable_paths: []
    writer: one owner
    reviewers: []
    transfer_condition: none yet
interfaces:
  preserve: []
  authorized_changes: []
  consumers_and_migration: []
budget:
  requested_model: host default unless user chose otherwise
  measured_baseline: unavailable until observed
  scope_of_measurement: task or shared account or unavailable
  limit_and_units: user-provided or unbounded
  wrap_threshold: user-provided or agreed working checkpoint
  required_reserve: user-provided or none
  enforcement_and_blind_spots: []
external_actions:
  authorized: []
  exact_target_and_request_evidence: []
  pending_decisions: []
verification:
  commands_or_interactions: []
  data_and_side_effect_limits: []
  required_artifacts: []
  skipped_or_unavailable: []
```

## Task packet

Include the task/contract version, role, bounded objective, criterion IDs, baseline, allowed read paths, writable paths (empty for read-only), prohibited data, allowed tools/side effects, relevant contracts, dependencies, model/budget constraints, expected evidence, and return channel. The budget applies to nested work too. If a packet changes materially, reissue it and stop stale dependent work.

Return `complete`, `revision_required`, or a named dependency/blocker, plus observations, files changed/reviewed, checks and outcomes, decisions, and open risks. A role's claim that it is complete does not close acceptance criteria without the evidence required by the contract.

## Model-comparison contract

When explicitly comparing models, use the same task brief, baseline, tools, relevant data, and acceptance rubric. Isolate implementations and identify the authoring model and settings from actual runtime evidence. Choose success criteria before viewing results. Track quality, completion, defects, time, and measured cost/usage where available. Record unequal context, interventions, missing usage data, and other confounders. Do not declare a universal winner from one prototype or convert shared account usage into a fabricated per-model bill.

## Release supplement, when authorized

Record the authorization and exact environment, artifact identity, required checks, secret/configuration handling, migration order, health and stop conditions, rollback/last-known-good plan, and post-release result. Instrumentation requirements should identify behavior/decision, population, event semantics, authoritative sources, join keys, deduplication, retention, access, and known blind spots. Do not invent conversion thresholds or deployment requirements for an unrelated local change.
