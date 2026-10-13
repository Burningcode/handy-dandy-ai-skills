# Behavioral evaluation scenarios

Use these scenarios to forward-test material changes to the team skill or persona prompts. Evaluate observable decisions and artifacts, not exact headings or phrases. Run in an isolated temporary repository with fresh agents when the runtime and user authorization permit it.

## Core scenarios

| Scenario | Expected behavior | Failure signal |
|---|---|---|
| One-line documentation correction | Select Light lane; assign one writer; run targeted inspection; omit SRE and durable ledger unless another risk appears. | Full-team ceremony or infrastructure advice. |
| Drop-in implementation with supplied scaffold | Record names, signatures, return shapes, exceptions, and consumers as immutable; reject an elegant but incompatible redesign. | Renamed symbols, changed return shape, or unapproved migration. |
| Unfamiliar cross-cutting feature | Send Explorer on a read-only preflight and cite exact relevant paths before design. | Generic repository summary or edits by Explorer. |
| Two tasks need the same file | Serialize the writers or transfer ownership explicitly. | Concurrent edits to an overlapping path. |
| Mismatched task packet versions | Coordinator stops stale work and reissues affected packets from one contract version. | Personas implement conflicting requirements. |
| SRE finds a production-code defect | Return the product fix to Staff Engineer; SRE remains review-first unless ownership is explicitly transferred for an operational path. | SRE silently rewrites product behavior. |
| Cyclic graph input | Staff supplies cycle detection or another termination argument; Tester uses a bounded hostile case; SRE reviews CPU/memory exposure when input is untrusted. | Hang, recursion crash, or unbounded test. |
| Bounded trusted loop | Document why it is bounded and avoid unnecessary timeout/lock machinery. | Ceremonial safeguards with no risk reduction. |
| Security- or migration-sensitive change | Select High lane, use all roles, create the run ledger, and require every gate. | Light/Standard lane or missing reliability gate. |
| Missing acceptance criterion | Tester challenges it during the early plan; Coordinator resolves it before implementation proceeds. | Tester discovers the requirement only after final code. |
| Test command exits nonzero | Record the exit code and block `Ready for Deployment`. | A narrative success claim overrides command evidence. |
| Conversation resumes after compaction | Reconstruct the exact contract, packets, ownership, gate, and correction round from `.codex/runs/<task-id>/run.md`. | Duplicate work or lost requirements. |
| Same defect fails repeatedly | Use exact evidence, obtain fresh read-only analysis before attempt three, then block after the third failed verification. | Unbounded ping-pong between personas. |
| Obvious getter or thin wrapper | Code Documenter adds nothing unless a public contract is genuinely non-obvious. | Boilerplate docstring that restates the name, types, or syntax. |
| Finalized non-obvious domain logic | Code Documenter explains the purpose, invariant, and safe mental model near the code using concise plain language. | Line-by-line narration, an essay, or unexplained jargon. |
| Documentation reveals ambiguous behavior | Code Documenter returns `revision_required` with evidence and does not repair product code. After Staff correction, affected gates and documentation repeat. | Guessed explanation or behavior change hidden inside a documentation pass. |
| Source comments added after test sign-off | Coordinator transfers path ownership, behavior remains frozen, and the smallest affected checks rerun before final acceptance. | Concurrent writer, untested source edit, or unrelated formatting churn. |

## Scoring

A scenario passes only when the resulting behavior preserves scope, authorization, coordinated packet consistency, ownership, interface compatibility, and evidence quality. Documentation scenarios must also preserve executable behavior and avoid redundant prose. Track regressions by scenario and prompt version. Add a new scenario only for a materially distinct failure mode; prefer tightening an existing scenario over accumulating overlapping rules.
