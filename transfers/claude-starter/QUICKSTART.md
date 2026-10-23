# Claude Code quick start

Use the approved work account, project, and import process. The pack grants no additional tool access. Do not change managed settings, add connectors, bypass permissions, or install a runtime to make it work without the required approval.

## 1. Download and inspect

Download [claude-code-starter.zip](https://github.com/Burningcode/handy-dandy-ai-skills/raw/refs/heads/main/transfers/claude-starter/claude-code-starter.zip). Extract it into a separate staging directory, not over an existing project. It contains:

```text
claude-code-starter/
  .claude/skills/<skill-name>/SKILL.md
  .claude/skills/<skill-name>/<supporting resources>
  CLAUDE.md
  .gitignore
  QUICKSTART.md
```

There are 19 skills: nine foundations, Art of Product Strategy, and nine complete paid product packages. All paid supporting files are preserved. The two Python helpers are optional local calculators, not installation scripts. No script runs on extraction.

## 2. Merge deliberately

- Copy the selected complete skill folders into the approved project's `.claude/skills/`. Start with Mary, executive communication, memory, and the workbench relevant to your immediate task; the rest can be installed now or later.
- Compare any same-named existing folder before replacing it. Preserve its local changes.
- Review and merge the supplied [CLAUDE.md](CLAUDE.md) into the project's instruction system. Do not overwrite an existing file or weaken team/managed rules.
- If the project already relies on `AGENTS.md`, confirm that those instructions remain loaded before introducing another instruction file.
- Merge relevant ignore entries; do not overwrite the project's `.gitignore`. An ignored folder prevents accidental Git tracking, not unauthorized access or retention.
- Do not configure a remote pointing back to this public transfer repository from the work project.

Project skills live under `.claude/skills/<skill-name>/SKILL.md` and can be invoked as `/skill-name`. Personal skills affect multiple projects, so project-local is the default here. See [Claude Code skill locations](https://code.claude.com/docs/en/skills).

## 3. Give Claude Code this setup request

Paste this after extraction in the approved work project:

> Inspect the extracted starter and this project's existing instruction files first. Show any conflicts, duplicate skill names, and proposed changes before modifying existing configuration. Help me merge the complete selected skill folders into this project's .claude/skills and integrate the working agreement without overwriting existing instructions. Preserve team and managed rules, including any AGENTS.md behavior. Do not change permissions, install dependencies, add network integrations, commit, or push. After approved local changes, verify the installed files and tell me which skills are available. Keep all work context in this approved environment.

Review the proposed changes before authorizing the merge. The prompt is not permission to bypass an organizational restriction.

## 4. Begin with Mary and one task

Start or restart Claude Code from the project root and try:

```text
/mary-design-partner Review this journey. Give me your strongest concern, a concrete next version, and what still needs real user evidence.
```

Use [Mary's guide](https://github.com/Burningcode/handy-dandy-ai-skills/blob/main/transfers/claude-starter/MARY-START-HERE.md) for voice calibration. The guide and catalog remain in the public transfer directory rather than inside the installed project; save a permitted local copy before the transfer folder is removed, or retain the full transfer archive.

Useful next commands:

- `/executive-communication-partner` for a clear, natural recommendation and ask.
- `/art-of-product-strategy` for a strategic choice, contradictory evidence, strongest alternative, and defensible argument.
- `/product-prd-workbench` for a selected direction that needs scope and delivery clarity.
- `/executive-decision-brief-workbench` for an investment decision and alternatives.
- `/customer-research-synthesis-workbench` for supplied research.
- `/metric-drop-investigator` for an unexplained metric movement.

Do not load all skill bodies into the standing instructions. Apply the relevant workflow on demand. The [catalog](https://github.com/Burningcode/handy-dandy-ai-skills/blob/main/transfers/claude-starter/SKILL-CATALOG.md) explains the full selection.

## 5. Establish private continuity

Use `/portable-project-memory` to propose a compact project record after the first useful session. Choose an approved private destination before saving. Keep project facts, decisions, collaboration preferences, and reusable design craft distinct. Retain source, owner, date, status, and what would change a decision.

Review the instance's actual memory behavior with its supported controls; these files do not configure or disable automatic memory. Instructions and saved memory are context, not an enforcement mechanism. See [Claude Code instructions and memory](https://code.claude.com/docs/en/memory).

Do not copy a personal memory directory, earlier conversations, or work-generated content back into the public pack.

## 6. Verify before relying on it

Run a small fictional exercise from a selected workbench, then the relevant [practice checks](https://github.com/Burningcode/handy-dandy-ai-skills/blob/main/transfers/claude-starter/SMOKE-TESTS.md). Check:

- The intended skill and its supporting references are available.
- Fictional examples remain fictional; no baseline, approval, source, or result is invented.
- Mary offers a point of view and a concrete change, not just a checklist.
- The answer sounds conversational while preserving evidence and caveats.
- A fresh session can recover a saved, approved handoff without claiming unseen history.

Optional Python helpers require an already approved Python environment; they read an explicitly named local CSV and print calculations. Do not install Python or relax execution policy merely to run them. Manual calculations or the agent's approved tools are alternatives.

**Not yet verified:** behavior in the organization's managed Claude Code build. If skills are unavailable or blocked, ask the administrator; do not work around the restriction.

