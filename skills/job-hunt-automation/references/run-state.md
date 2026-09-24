# Discovery, dedupe, and durable run state

## Tracker identity and two-pass dedupe

Read every populated row in each candidate-designated authoritative tracker table before evaluating new leads. Build a suppression index of normalized employer/title, exact requisition or ATS UUID, and canonical official URL (remove fragments, tracking parameters, and trailing slash). Normalize obvious aliases and ATS board names. A title variant at the same employer and function is `Possible duplicate` until resolved. Record the match basis and source row.

After discovery and official-page verification, reread the authoritative tables and check each surviving role again before packet generation or final recommendation. At submission time, check once more. Never use only the newest rows or a local snapshot as the index. If the tracker is unavailable, say so and do not claim that a role is net-new.

## Source and role assessment

Keep board coverage honest: results reviewed, pagination/batches, visible total, official-page verified, net-new, duplicate, stale/unverifiable, strong fit, and unreviewed backlog where measurable. A blocked or profile-gated board is not an exhausted board. Limit board work by the candidate's agreed search scope; do not substitute cached listing snippets for a live official application.

For a surviving role, retain exact title, employer, requisition, canonical official URL, posting date if shown, stated pay and pay type, work model, explicitly eligible locations, travel, required qualifications, AI-use rules, and discovery source. Label each main gap `hard`, `soft`, or `unknown`; explain the decision. A live posting is necessary but not sufficient: the application form must correspond to the same title/requisition.

## Batch manifest

Use a durable manifest with one record per employer-role-requisition and these fields: discovery source/date; official verification time; tracker duplicate check time/match; fit and hard-gate result; packet paths and QA state; batch approval scope/time; ATS/form stage; transmitted files and answers; exact blocker and owner; submit attempt time; employer receipt/state; tracker row and readback time; follow-up date. Do not store secrets or one-time codes.

Suggested states: `Discovered`, `Possible duplicate`, `Excluded`, `Review`, `Packet ready`, `Staged`, `Human action`, `Manual-only`, `Submitting`, `Submission uncertain`, `Employer confirmed`, `Tracker reconciled`. Only `Employer confirmed` or a clearly labeled candidate-confirmed submission may become `Applied`. A browser tab alone is not durable state; record the official link and exact remaining action so recovery survives a restart.

## Recovery and end of run

When a tab vanishes, upload fails, session expires, or a click times out, check candidate home and existing receipts before resubmission. Reopen the exact official requisition, revalidate that the role is live, and compare saved versus unsaved fields. A file chooser timeout is an access/UI failure, not evidence that an attachment uploaded; use the environment's documented recovery method and verify the attachment name. Never change browser security settings or evade an employer challenge as a workaround.

End with counts separated by state, confirmed evidence, tracker readback, and exact handoffs. If an offer arrives or the candidate pauses, leave queued roles as paused without sending further applications; discuss follow-up or withdrawal only under a new request.
