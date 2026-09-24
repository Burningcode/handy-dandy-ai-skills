---
name: job-hunt-automation
description: Set up and run a candidate-controlled job search, from preference intake and verified sourcing through application staging, authorized submission, and tracker reconciliation. Use for a new candidate's job-hunt workflow or an existing application batch; do not treat sourcing as permission to submit.
---

# Job Hunt Automation

Help a candidate run a high-quality search without losing control of identity, claims, consent, or submissions. Optimize for verified opportunities and confirmed outcomes, not raw application count.

## Choose the mode

- **Setup or changed preferences:** Read [references/intake.md](references/intake.md). Ask the relevant questions in small groups, record answers in a candidate-owned private profile, and identify what remains unknown. Do not run live applications from example or inferred answers.
- **Discovery and staging:** Use the profile, current tracker, and [references/run-state.md](references/run-state.md). Discover, verify, deduplicate, screen, and prepare role-specific materials. Staging is not submission.
- **Authorized application run:** Read [references/application-execution.md](references/application-execution.md). Operate only the named role or batch and the candidate-approved action scope. Check current posting and tracker state again at action time.
- **Reconciliation or recovery:** Read [references/run-state.md](references/run-state.md) and, if an employer form is involved, [references/application-execution.md](references/application-execution.md). Establish the last employer-confirmed state before retrying.

## Invariants

1. The candidate chooses the source of truth for profile, career evidence, application tracker, and artifact storage. Keep filled profiles, resumes, access tokens, screenshots containing personal data, and submission logs outside the public skill package. Never commit them with this skill.
2. A job board, email, recruiter message, or saved job is discovery evidence only. Before recommending or applying, open the exact current employer careers or official ATS posting; verify title, requisition, location eligibility, live Apply action, compensation as stated, and any AI-use restriction. Mark unresolved or closed roles accordingly.
3. Deduplicate against **all** relevant tracker records by exact requisition/ATS ID or canonical URL first, then normalized employer and title. Recheck immediately before packet work and submission. A refreshed date or repost is not a new role; a genuine scope change needs an explicit explanation. Keep distinct requisitions and legitimate reapplications distinct.
4. Screen with candidate-defined hard gates and soft preferences. Unknown pay, remote eligibility, or mandatory qualification remains unknown; do not invent an estimate or infer that “remote” includes the candidate's location. Do not use volume pressure to weaken gates. A stretch can proceed when the candidate's verified transferable evidence supports it and no hard gate fails.
5. Tailor only from verified career evidence. Do not inflate tenure, credentials, metrics, ownership, or referrals. Respect an employer's no-AI or candidate-original-answer rule; hand those fields to the candidate.
6. Ask for explicit authorization for the named role or bounded batch before transmitting candidate data or submitting. Standing preferences can help fill ordinary fields, but new legal/security declarations, sensitive disclosures, consent choices, signatures, assessments, passwords, one-time codes, and CAPTCHAs remain candidate-controlled unless clearly and specifically authorized where permissible. Do not bypass employer controls.
7. A click, upload, or browser success toast is not proof of application submission. Confirm the result on an employer confirmation page, candidate home, or receipt before counting it. If state is uncertain, inspect first and do not retry blindly.
8. Update the canonical tracker only with accurately labeled evidence and read the changed record back. Keep applied, staged, blocked, manual-only, rejected, closed, and withdrawn states distinct. Pause sourcing and submission when the candidate says the search is paused or an offer changes priorities.

## Output contract

For each role, provide the exact official URL and requisition, evidence-backed fit and main tradeoff, disposition, packet location, authorization state, last verified form state, required human action, and submission evidence. At batch end report verified submissions separately from attempts and open tabs; include a concise, resumable handoff. Use candidate-specific preferences only from the private profile, never from this skill's examples.
