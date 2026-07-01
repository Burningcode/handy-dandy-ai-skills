# Handy Dandy Cursor Skills

Reusable Cursor skills that can be installed by copying a skill folder into `~/.cursor/skills/`.

## Install A Skill

```bash
mkdir -p ~/.cursor/skills
cp -R skills/creator-gifting-address-lookup ~/.cursor/skills/
```

Then reload Cursor.

## Included Skills

| Skill | What it does |
| --- | --- |
| `creator-gifting-address-lookup` | Pulls creator names and gifting addresses for accepted campaign creators, generates a fresh Google Sheet, and drafts a Slack handoff. |

## Private Configuration

The gifting lookup skill is public-safe. It intentionally does not include private company table names, Slack channel IDs, campaign IDs, or example creator data.

To use it inside a company environment, copy:

```bash
cp skills/creator-gifting-address-lookup/internal-config.example.md \
  skills/creator-gifting-address-lookup/internal-config.md
```

Fill in the local `internal-config.md` with your private MCP server names, table names, Slack channels, and Google auth details. Do not commit that file.
