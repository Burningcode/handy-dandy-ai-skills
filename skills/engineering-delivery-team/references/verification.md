# Verification and correction

Read for test planning, independent review, or a final acceptance pass. Select checks from actual risks rather than applying every category mechanically.

## Evidence contract

For each criterion, record the tested artifact/revision, environment, command or interaction, observed result, and remaining uncertainty. Distinguish:

- source inspection;
- synthetic/in-memory behavior;
- isolated integration tests;
- rendered UI and manual interaction;
- approved live integration or production read-back.

An assertion about one category does not prove another. A mocked payment is not a charge, an emitted analytics event is not a conversion, and a successful pipeline is not a working deployed journey. Historical chat claims are leads until current evidence is checked.

## Risk examples

| Risk | Decisive evidence |
| --- | --- |
| Stateful user decisions or generated replacements | Stable identity across wording/order changes; human edits and review/lifecycle state survive; ambiguous matches are surfaced rather than silently reactivated. |
| Background work beside an interactive task | Explicit capture/job lifecycles; bounded concurrency; start/stop guards; failed launch releases its claim; display failure cannot strand durable work; shutdown/restart recovery. |
| Retried mutations | Defined idempotency; partial failure reported truthfully; persisted state checked before retry; recovery preserves last-known-good data. |
| Source-backed recommendations | Current provenance, freshness/conflict handling, no unsupported availability claim, stale/missing source states. |
| Permissions and onboarding | Correct identity/tenant boundaries, access denial, meaningful empty/setup states, operator recovery. |
| Layout and copy | Actual rendered path with long text, representative viewport/zoom, keyboard access, and readable errors. |
| AI output | Grounding and omission cases, quality fallback, current source/version identity, preserved supported content after repair, honest output/readiness labels. |
| External release | Exact approved target/artifact, appropriate checks, rollback, post-release critical-path verification. |

Use bounded simulations for concurrency, cancellation, cyclic input, large inputs, and injected failures. Do not endanger a live process or inspect private recordings merely to make a test realistic. Read a test's setup before running it when it could touch actual data, devices, services, or model inference.

## Findings and rechecks

A finding states severity, location, trigger, expected behavior, observed behavior, consequence, and a safe reproduction. Distinguish an actionable bug from an optional improvement. Do not claim a path fails solely because it could be imagined to fail.

Track each finding by ID and affected criterion. The implementation owner receives the reproduction and scope; reviewers remain read-only unless ownership explicitly changes. Recheck the latest source before repeating a finding while another worker is editing it. After correction, rerun the reproduction and affected invariants. Preserve unaffected passes when the artifact has not changed in ways that invalidate them.

Repeated failure of the same criterion calls for a different diagnosis. Several distinct findings are not one repeatedly failed fix. Do not run unlimited review loops, but do not mark the deliverable complete to avoid reporting unresolved work. If budget or external access prevents a required check, preserve the artifact and state the precise limitation.

## Final acceptance

Inspect the diff and any generated deliverable, including documentation edited after a test pass. Reconcile implemented behavior with the original outcome and approved slice. Report current evidence, skips, residual risks, and what a user can actually do. A test fixture failure caused by deliberately mismatched provenance must not be solved by weakening the product's provenance check.
