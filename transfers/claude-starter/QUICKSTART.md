# Quick start

## First: keep the boundary clear

Use only your approved Claude account, workspace, and import process. Ask your administrator if skill upload or code execution is unavailable; do not work around a restriction. This pack needs no network connector or custom executable script.

Start with executive communication, Mary, and product critique. Install other skills when a real task calls for them.

## Claude browser / Desktop chat

1. Open the skill catalog and download the individual ZIPs you want.
2. In Claude, use **Customize → Skills → Add / Create skill → Upload a skill**, where enabled.
3. Upload one skill ZIP at a time and enable it.
4. Add the content of [CLAUDE.md](CLAUDE.md) to the relevant Project instructions, or paste it at the start of a chat if that is your approved route. Merely attaching a file does not establish a permanent instruction.
5. Try the fictional [practice checks](SMOKE-TESTS.md). Ask which skill was applied; also inspect the visible result.

If custom skills are unavailable, use the skill's Markdown as explicit task instructions only if your organization's policy permits it. Do not represent that as an installed skill. See [Claude's upload and organization controls](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Claude Code

1. Extract each selected skill ZIP.
2. Copy its entire skill folder into the approved project's `.claude/skills/` directory. For example: `.claude/skills/mary-design-partner/SKILL.md`.
3. Review and merge this pack's [CLAUDE.md](CLAUDE.md) into the project's existing instructions; never overwrite existing or managed rules.
4. Start a new session and invoke a skill, for example `/mary-design-partner`. Verify the expected behavior with the practice checks.
5. Use a user-wide installation only if you intentionally want the skill in other projects and policy permits it.

Claude documents [project and personal skill locations](https://code.claude.com/docs/en/skills) separately from [persistent instructions and memory](https://code.claude.com/docs/en/memory). These files guide behavior; they are not security enforcement.

## A useful first prompt

> Work with me as a product and engineering operating partner. Read the working agreement and use only the skills relevant to this task. First confirm which tools and approved sources you actually have. Keep facts, assumptions, and recommendations distinct. Do not import personal or prior-employer context. Let's start by defining the decision, the user behavior we want to change, and the most important evidence gap. Ask one useful question at a time.

## Set up continuity after the first useful session

Use **portable-project-memory** to propose a compact handoff. Choose an approved private destination before saving. Keep working style, project facts, and reusable lessons separate; retain source and status. In chat-only mode, ask for a handoff you can review and save yourself.

This is deliberate written continuity, not model training. Do not assume skills or memory settings transfer between Claude surfaces or accounts; verify the instance you use.

## A five-minute check

- Can Claude identify the right skill without applying every framework?
- Does it preserve uncertainty and refuse to invent sources?
- Does Mary offer a concrete change without claiming user research?
- Can it summarize a decision without claiming authority to approve it?
- Does a new session recover the approved handoff, rather than pretending to remember an unseen chat?

If any answer is no, narrow the instruction or fix the setup before importing more skills.

