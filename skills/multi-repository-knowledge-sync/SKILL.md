---
name: multi-repository-knowledge-sync
description: Design or operate a safe multi-repository knowledge sync that checks status before writing, supports dry-run and explicit sync modes, keeps destinations manifest-driven, excludes secrets, commits only scoped changes, verifies remote state, and reports clean, pushed, skipped, and failed repositories. Use as an example for source-controlled documentation automation.
---

# Multi-Repository Knowledge Sync

This public-safe example generalizes a personal documentation-backup runbook. The repositories, schedules, paths, and commands are fictional. Adapt the pattern without exposing private repository names or credentials.

## Operating modes

| Mode | Behavior |
| --- | --- |
| Check | Read-only: report dirty, ahead, behind, diverged, missing, and clean repositories |
| Dry run | Show the exact files and actions that a sync would perform |
| Sync | Commit and push only the explicitly approved repositories and paths |

Default to `check`. Do not treat “check my repositories” as authorization to commit or push.

## Manifest contract

Keep repository configuration in a local ignored file:

```yaml
repositories:
  - name: product-docs-example
    local_path: C:/example/product-docs
    remote: example-owner/product-docs
    branch: main
    allowed_paths:
      - decisions/
      - research/
  - name: playbooks-example
    local_path: C:/example/playbooks
    remote: example-owner/playbooks
    branch: main
    allowed_paths:
      - skills/
```

All entries are fictional. Never commit filled credentials, tokens, private remote names, home-directory inventories, or transcript snapshots.

## Pre-flight checks

For each repository:

1. Resolve and validate the exact local path.
2. Confirm it is a repository with the expected remote and branch.
3. Fetch safely when network access and authorization exist.
4. Report dirty, staged, untracked, ahead, behind, and diverged state.
5. Scan proposed files for secret-shaped content and excluded paths.
6. Stop on conflicts, divergence, unexpected remotes, or broad path expansion.

Never construct a destructive target from an unresolved variable or wildcard.

## Sync contract

When sync is explicitly authorized:

- stage only `allowed_paths`;
- show the staged diff summary;
- use a clear commit message that names the automation and time;
- do not include unrelated working-tree changes;
- push the expected branch only;
- verify the remote branch contains the new commit;
- preserve failed repositories for manual review instead of forcing.

Do not use destructive resets or history rewrites to make automation appear clean.

## Hypothetical example

```text
Repository                 State       Planned action
product-docs-example       dirty       Commit 2 approved Markdown files
playbooks-example          clean       No action
research-notes-example     diverged    Stop; needs human reconciliation
archive-example            missing     Report configuration gap
```

The agent should sync only `product-docs-example` after approval, then verify the remote commit. It should not auto-resolve the diverged repository.

## Report

Return:

- repositories checked;
- repositories already clean;
- exact files committed;
- commit identifiers and verified remote state;
- skipped repositories and reason;
- failures and next safe action;
- scheduler health only when the user asked about automation.

## Scheduler example

A scheduler may run read-only checks automatically and save a local report. Automatic commit or push should be separately configured, narrowly scoped, and auditable. Prefer a human review queue when repositories can contain sensitive product work.

## Quality and privacy gate

- No secrets or credentials in proposed changes.
- No transcripts, screenshots, customer data, or private identifiers unless explicitly authorized and appropriate.
- Remote and branch match the manifest.
- Only approved paths are staged.
- Push result is verified from remote state.
- Failures are visible; no force push or silent skip.

