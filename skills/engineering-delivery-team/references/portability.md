# Installation and compatibility

The skill's Markdown role briefs are the portable source of guidance. Native custom-agent support is optional, and no model or reasoning setting is pinned by this package. Host capabilities, project instructions, and the user's model choice still apply.

## Skill-only installation

Copy the complete `engineering-delivery-team` folder into your agent's skill directory, or use the repository's Skills CLI instructions. The Python installer requires Python 3.10 or newer. From the repository root:

```sh
python skills/engineering-delivery-team/scripts/install.py --project /path/to/project --dry-run
python skills/engineering-delivery-team/scripts/install.py --project /path/to/project
```

The project must exist. Use `--personal` instead of `--project` for `CODEX_HOME/skills`, or `~/.codex/skills` when unset. Quote paths with spaces. This installer copies only the skill; bundled persona files remain assets and are not installed into the host's agent configuration directory.

It refuses to overwrite a different existing installation, treats an identical one as a no-op, rejects symlinks, and verifies a staged copy before publishing it as one directory. If it reports a conflict, compare the installed customization with the new package before choosing an update. It never edits other skills, `AGENTS.md`, or `config.toml`.

## Existing PowerShell installation option

The established entrypoint and six persona filenames remain available:

```powershell
.\skills\engineering-delivery-team\scripts\Install-EngineeringDeliveryTeam.ps1 -TargetProject 'C:\work\your-project' -WhatIf
.\skills\engineering-delivery-team\scripts\Install-EngineeringDeliveryTeam.ps1 -TargetProject 'C:\work\your-project'
```

Use `-Personal` for the personal Codex locations. This option copies the skill and the six custom-agent files. It refuses existing destinations unless `-Force` is supplied; review and preserve customizations before using that override. Its copy behavior is different from the Python installer's staged publication. Neither installer changes model settings or grants publishing authority.

Existing agent names remain `project_coordinator`, `repository_explorer`, `staff_engineer`, `senior_tester`, `sre_guardian`, and `code_documenter`. Their prompts load the current shared role briefs, which also describe optional design/copy, data/evidence, and analytics assignments. Create only the roles warranted by the work; do not launch six or nine agents automatically. Reload the host after installation if required by that host.

## Verification

From the repository root:

```sh
node scripts/validate-skills.mjs
python -B -m unittest discover -s skills/engineering-delivery-team/tests -v
```

Installer tests use isolated temporary projects and personal homes. Behavioral scenarios require a separate execution and evaluation; neither package validation nor parsing persona files proves an agent follows their instructions.
