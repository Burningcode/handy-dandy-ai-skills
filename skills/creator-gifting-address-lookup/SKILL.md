---
name: creator-gifting-address-lookup
description: Example operational automation that enriches a requester-supplied creator gifting worklist through a read-only Amazon Athena MCP connector, preserves the source population, creates a reviewable output, and drafts a handoff. Use to demonstrate or adapt an Athena-backed MCP workflow; it is not a turnkey production integration.
---

# Example: Athena-backed Creator Gifting Address Lookup

This skill is a public portfolio example of a bounded operational automation. It demonstrates how an agent can coordinate a source spreadsheet, a read-only Amazon Athena MCP connector, deterministic reconciliation, and a verified handoff.

It does **not** contain a real organization's tools, table names, schemas, channels, campaign identifiers, creator records, permissions, or credentials. The SQL and configuration are placeholders. Adapt them to an authorized environment and its privacy, security, and retention policies before use.

## What the example demonstrates

```text
Requester-supplied worklist
        ↓
Google Sheets MCP: read and validate population
        ↓
Athena MCP: execute approved read-only enrichment queries
        ↓
Deterministic merge: preserve rows, surface duplicates and missingness
        ↓
Google Sheets MCP: create a fresh review artifact and read it back
        ↓
Drafted handoff: send or share only after explicit authorization
```

The source worklist defines who is in scope. Athena provides authorized enrichment data. The generated sheet is a review artifact, not a new system of record.

## Example versus production

Use this skill to inspect, discuss, prototype, or adapt the operating pattern. Before a production run, provide an environment-specific configuration derived from [the example configuration](internal-config.example.md) and confirm:

- The requester is authorized to access the source and requested fields.
- The Athena MCP connector uses approved identity, region, catalog, database, workgroup, and output controls.
- Queries are read-only and limited to the supplied population.
- The destination, recipients, retention period, and deletion process are approved.
- External sharing, permissions, and messages require separate action-time authorization.

Do not query real personal information merely to demonstrate the example.

## Bounded job

The automation may:

- Read the user-supplied worklist and its metadata.
- Validate headers, row counts, identifiers, accepted-state filters, and duplicates.
- Use the configured Athena MCP connector to execute approved `SELECT` queries.
- Poll query state, retrieve all result pages, and record query identifiers and provenance.
- Reconcile results to the exact source rows.
- Create and verify a new review artifact.
- Draft a concise handoff.

It may not:

- Add creators who are absent from the source worklist.
- Guess missing names, addresses, or identity matches.
- Update Athena-backed data, source systems, or the original worklist.
- Broaden queries to unrelated populations.
- Share files, change permissions, or send messages without explicit authorization.

## Required inputs

- Source spreadsheet and tab.
- Header mapping for creator identifier, campaign or worklist identifier, handle, state, and accepted flag.
- Athena MCP server and tool names.
- Approved catalog, database, workgroup, output location, tables, and fields.
- Authorized output fields and data classification.
- Output destination, recipients, and retention expectation.

If the configuration is missing or still contains placeholders, remain in demonstration mode. Do not attempt a live query.

## MCP connector contract

The Athena connector should expose the equivalent of:

1. `start_query_execution` — submit a read-only query with the configured workgroup and query context.
2. `get_query_execution` — poll until `SUCCEEDED`, `FAILED`, or `CANCELLED`.
3. `get_query_results` — retrieve every result page using the returned pagination token.
4. Optional `stop_query_execution` — cancel a runaway or no-longer-authorized query.

Tool names may differ. Discover the configured MCP tools rather than inventing them. Never print credentials or connector secrets.

Record query ID, state, scanned-data metadata when available, result-page count, and the configuration version used. Stop on failure or cancellation; do not silently return partial data.

## Workflow

1. **Ground authority and scope.** Confirm the requested fields, source population, authorized destination, and whether the user wants a demonstration, dry run, or live execution.
2. **Read the full source.** Use spreadsheet metadata and bounded ranges. Preserve every original column and row.
3. **Validate the population.** Report total rows, eligible rows, unique creator identifiers, blank identifiers, duplicates, campaign or worklist counts, and excluded states.
4. **Preview the query plan.** Show the Athena catalog/database, logical tables, selected fields, population bound, and expected output without exposing credentials or real sensitive values.
5. **Run a coverage query.** Verify the eligible population and duplication behavior before retrieving personal fields.
6. **Run the enrichment query.** Query only the supplied identifiers, split large populations into bounded chunks, poll execution, and retrieve all result pages.
7. **Reconcile deterministically.** Join by the configured stable identifier. Preserve source row order and duplicate source rows. Flag one-to-many matches, missing values, and conflicting values.
8. **Create a fresh review artifact.** Append lookup status, provenance, notes, and query timestamp after the original columns.
9. **Read back and verify.** Confirm row count, column preservation, appended fields, missing/ambiguous flags, and output metadata.
10. **Draft the handoff.** Summarize coverage and exceptions. Share or send only after explicit authorization.

## Illustrative Athena query pattern

Use placeholders and the authorized environment's actual schema. Prefer parameterization when the connector supports it. Otherwise validate and quote identifiers as data, never as SQL syntax.

```sql
WITH source_ids (creator_id) AS (
  VALUES
    (CAST(? AS VARCHAR)),
    (CAST(? AS VARCHAR))
),
candidate_records AS (
  SELECT
    CAST(p.<creator_id_field> AS VARCHAR) AS creator_id,
    p.<first_name_field> AS first_name,
    p.<last_name_field> AS last_name,
    p.<gifting_address_field> AS gifting_address,
    p.<gifting_address_unit_field> AS gifting_address_unit,
    p.<updated_at_field> AS source_updated_at
  FROM <catalog>.<database>.<authorized_creator_profile_table> p
  JOIN source_ids s
    ON CAST(p.<creator_id_field> AS VARCHAR) = s.creator_id
)
SELECT *
FROM candidate_records
ORDER BY creator_id, source_updated_at DESC;
```

The `?` values represent positional execution parameters when the Athena MCP connector supports them. Otherwise, construct the `VALUES` rows from strictly validated data values using the connector's approved escaping method. For large lists, use configured chunk sizes or a temporary authorized input mechanism. Do not scan a full personal-data table when a bounded identifier lookup can perform the job.

## Output fields

After every original source column, append:

- `Lookup First Name`
- `Lookup Last Name`
- `Gifting Address`
- `Gifting Address Unit`
- `Address Status`
- `Lookup Source`
- `Lookup Notes`
- `Source Match Count`
- `Athena Query ID`
- `Lookup Pulled At`

Use statuses such as `FOUND`, `MISSING`, `AMBIGUOUS`, and `REVIEW_REQUIRED`. Never convert missingness into a guessed value.

## Synthetic example

Input:

| Worklist | Creator ID | Handle | Accepted |
| --- | --- | --- | --- |
| DEMO-01 | EX-1001 | example_one | Y |
| DEMO-01 | EX-1002 | example_two | Y |

Expected behavior:

- Query only `EX-1001` and `EX-1002` through the configured Athena MCP connector.
- Return a new two-row review artifact.
- Mark `EX-1001` as `FOUND` if the synthetic fixture has an address.
- Mark `EX-1002` as `MISSING` if it does not.
- Do not send, share, ship, or update any source system.

## Quality floor

A run fails if it has a silent row drop, an unbounded query, partial Athena results presented as complete, an unflagged one-to-many match, a guessed personal value, missing provenance, or an external handoff without authorization.

Before declaring success, verify:

- Output row count equals source row count.
- Every original source column remains intact and in order.
- Eligible unique identifiers equal queried unique identifiers.
- Athena reports `SUCCEEDED` and every result page was retrieved.
- Duplicate, missing, ambiguous, and unit-only records are explicit.
- Query ID and lookup timestamp are present.
- The created artifact can be read back.
- Sharing and messaging state are accurately reported.

## Draft handoff

```text
The Athena-backed enrichment example is ready for review.

- Source rows preserved: <rows>
- Eligible unique IDs queried: <ids>
- Found: <found>
- Missing: <missing>
- Ambiguous / review required: <review>
- Athena query status: SUCCEEDED (<query_id>)

Review artifact: <link>

No source records were changed. The artifact has not been shared or messaged beyond the currently authorized scope.
```

