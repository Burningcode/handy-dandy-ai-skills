# Creator Gifting Address Lookup — Internal Config

Copy this file to `internal-config.md` and fill it in locally. Do not commit real internal values.

## MCP Servers

- Slack MCP server: `<slack-mcp-server-name>`
- Google Workspace MCP server: `<google-workspace-mcp-server-name>`
- Athena / warehouse MCP server: `<warehouse-mcp-server-name>`

## Slack

- Request channel name: `<channel-name>`
- Request channel ID: `<channel-id>`
- Default requester / responder notes: `<optional>`

## Google Workspace

- Sheets read tool: `<tool-name>`
- Drive upload/import path available: `yes/no`
- Local auth command if Drive scope is needed: `<command>`

## Warehouse Tables

Use your internal table names here.

- Current campaign/collaboration table: `<database.schema.campaign_collaboration_table>`
- Creator address profile table: `<database.schema.creator_address_profile_table>`
- Primary creator name table: `<database.schema.creator_name_table>`
- Fallback contact/name table: `<database.schema.fallback_contact_table>`

## Required Columns

Source sheet:

- Campaign ID column: `<header>`
- Creator ID column: `<header>`
- Creator handle column: `<header>`
- Campaign title column: `<header>`
- State column: `<header>`
- Accepted flag column: `<header>`

Warehouse:

- Campaign ID field: `<field>`
- Creator ID field: `<field>`
- Collaboration state field: `<field>`
- Gifting address field: `<field>`
- Gifting address unit field: `<field>`
- First name field: `<field>`
- Last name field: `<field>`

## State Mapping

- Accepted source-sheet state: `<value>`
- Accepted source-sheet flag: `<value>`
- Accepted collaboration warehouse states: `<values>`

## Sharing Defaults

- Share generated Sheet with requester as: `writer/commenter/viewer`
- Share generated Sheet with cc users as: `writer/commenter/viewer`
- Send Slack message automatically: `yes/no`
