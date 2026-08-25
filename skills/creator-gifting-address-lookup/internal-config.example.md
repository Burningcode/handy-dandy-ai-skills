# Example configuration — Athena-backed gifting lookup

This file is intentionally non-functional. Copy it to `internal-config.md`, replace every placeholder using an approved environment, and keep the completed file out of version control.

## Execution mode

- Mode: `<demonstration | dry-run | live>`
- Configuration owner: `<team or role>`
- Configuration version / reviewed date: `<value>`

## MCP connectors

- Google Sheets MCP server: `<server-name>`
- Spreadsheet metadata/read tool: `<tool-name>`
- Spreadsheet create/write/read-back tools: `<tool-names>`
- Athena MCP server: `<server-name>`
- Athena start-query tool: `<tool-name>`
- Athena query-status tool: `<tool-name>`
- Athena results tool: `<tool-name>`
- Athena cancel tool: `<optional-tool-name>`

## Athena query context

- AWS region: `<region>`
- Workgroup: `<read-only-workgroup>`
- Catalog: `<catalog>`
- Database: `<database>`
- Query results location: `<approved-managed-location>`
- Maximum bytes scanned or cost guardrail: `<value>`
- Poll timeout and stopping rule: `<value>`
- Maximum identifiers per query chunk: `<value>`

## Authorized schema mapping

- Creator profile table: `<catalog.database.table>`
- Creator ID field: `<field>`
- First name field: `<field>`
- Last name field: `<field>`
- Gifting address field: `<field>`
- Gifting address unit field: `<field>`
- Source updated-at field: `<field>`

Do not add unrelated personal, financial, authentication, or behavioral fields.

## Source spreadsheet mapping

- Worklist / campaign header: `<header>`
- Creator ID header: `<header>`
- Creator handle header: `<header>`
- State header: `<header>`
- Accepted flag header: `<header>`
- Eligible state / flag values: `<values>`

## Output controls

- Authorized destination folder: `<folder>`
- Authorized recipients: `<people or groups>`
- Default access role: `<viewer | commenter | writer>`
- Retention period: `<value>`
- Deletion owner / process: `<value>`
- External sharing allowed: `<yes | no>`
- Message sending allowed without separate approval: `no`

## Privacy and security controls

- Data classification: `<classification>`
- Identity / role used by Athena MCP: `<approved role name, never credentials>`
- Required query tags or audit metadata: `<values>`
- Prohibited fields: `<values>`
- Prohibited destinations: `<values>`
- Incident / escalation owner: `<role>`

