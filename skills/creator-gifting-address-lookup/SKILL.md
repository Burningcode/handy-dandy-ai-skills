---
name: creator-gifting-address-lookup
description: Pull creator names and gifting addresses for accepted non-Shopify gifting campaigns from a Google Sheet and warehouse tables. Use when a Slack or chat request shares a creator list spreadsheet and asks for gifting addresses, shipping addresses, or a creator address lookup.
---

# Creator Gifting Address Lookup

Creates a fresh Google Sheet containing every row and column from a requester-provided source sheet, plus appended lookup columns for creator name, gifting address, address status, source, and notes. Drafts a Slack handoff in the original request thread.

## Private Config

Before running, look for `internal-config.md` in this skill directory. If it is missing, ask the user for the private values or have them copy `internal-config.example.md` to `internal-config.md`.

Never commit real company table names, Slack IDs, source Sheet links, campaign IDs, creator data, or access tokens to a public repo.

## Inputs

Capture:

- Slack request channel and parent thread timestamp, if the request came from Slack.
- Requester user ID and cc user IDs.
- Google Sheet URL or spreadsheet ID.
- Linked tab/gid and actual tab title from sheet metadata.
- Source sheet headers and full row count.

## Workflow

1. Search Slack for the Sheet URL if only the Sheet URL was provided.
2. Read the request thread for context and cc users.
3. Read Google Sheet metadata to confirm the actual tab title and row/column count.
4. Pull the full source range. Preserve every original source column and row.
5. Parse by header names, not hardcoded column indices.
6. Validate the source population:
   - accepted row count
   - unique creator ID count
   - duplicate creator ID count
   - campaign ID/title counts
7. Query the warehouse for gifting addresses and primary names.
8. Query fallback contact/name data only for creator IDs missing a primary name.
9. Merge lookup data back onto the source sheet rows.
10. Generate a CSV/JSON payload with original columns plus appended lookup columns.
11. Create a fresh native Google Sheet from the generated CSV.
12. Share the Sheet with requester and cc users.
13. Re-read the generated Sheet to verify row count, original columns, and appended lookup columns.
14. Draft the Slack reply. Send only when explicitly asked.

## Source Sheet Rules

Use the source sheet as the source of truth. If the warehouse contains additional active creators for the same campaign IDs, do not add them unless the user asks.

Use header names from config, commonly:

- campaign ID
- creator/influencer ID
- creator handle / shop name
- campaign title
- state
- accepted flag

Only include rows that match the configured accepted state/flag.

## Warehouse Query Pattern

For current campaign systems, validate the campaign population before joining addresses:

```sql
SELECT state,
       COUNT(*) AS rows,
       COUNT(DISTINCT <creator_id_field>) AS unique_creators
FROM <campaign_collaboration_table>
WHERE <campaign_id_field> IN (<campaign_ids>)
GROUP BY state
ORDER BY state;
```

For large creator populations, split the query into modulo chunks to avoid row limits:

```sql
WITH accepted AS (
  SELECT DISTINCT CAST(<creator_id_field> AS VARCHAR) AS creator_id
  FROM <campaign_collaboration_table>
  WHERE <campaign_id_field> IN (<campaign_ids>)
    AND <state_field> IN (<accepted_states>)
    AND mod(<creator_id_field>, 4) = <0_to_3>
)
SELECT a.creator_id,
       addr.<gifting_address_field> AS gifting_address,
       addr.<gifting_address_unit_field> AS gifting_address_unit,
       names.<first_name_field> AS first_name,
       names.<last_name_field> AS last_name
FROM accepted a
LEFT JOIN <creator_address_profile_table> addr
  ON CAST(addr.<creator_id_field> AS VARCHAR) = a.creator_id
LEFT JOIN <creator_name_table> names
  ON CAST(names.<creator_id_field> AS VARCHAR) = a.creator_id
ORDER BY a.creator_id;
```

For smaller lists, it is fine to query by explicit source-sheet creator IDs.

## Fallback Names

Only query fallback contact data for creator IDs missing both first and last name from the primary source.

```sql
SELECT CAST(<fallback_creator_id_field> AS VARCHAR) AS creator_id,
       <fallback_first_name_field> AS first_name,
       <fallback_last_name_field> AS last_name
FROM <fallback_contact_table>
WHERE CAST(<fallback_creator_id_field> AS VARCHAR) IN (<missing_name_ids>);
```

Name priority:

1. Primary creator name table.
2. Fallback contact table when the candidate clearly matches the handle or there is one complete candidate.
3. Leave ambiguous values flagged in notes.

Do not treat multiple fallback contacts as certain. If ambiguous, add `Fallback returned multiple candidates; verify name against creator profile`.

## Output Columns

Append these columns after all original source columns:

- `Lookup First Name`
- `Lookup Last Name`
- `Gifting Address`
- `Gifting Address Unit`
- `Address Found`
- `Lookup Name Source`
- `Lookup Notes`
- `Duplicate Accepted Rows`
- `Lookup Pulled At`

Use `Address Found = Y` when either address or unit has content. Use `N` otherwise.

Recommended notes:

- `NEEDS MANUAL COLLECTION - no gifting address on file`
- `Address stored in unit field only - verify before shipping`
- `Name from fallback contact source`
- `Fallback returned multiple candidates; verify name against creator profile`
- `Creator appears in N accepted source rows`

## Fresh Google Sheet Creation

If the available Google Sheets tool can write ranges, create a new spreadsheet and write the full payload.

If Sheets write tools are unavailable but Drive upload is available, generate a CSV and import it as a native Google Sheet:

```text
POST https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart
metadata.mimeType = application/vnd.google-apps.spreadsheet
media Content-Type = text/csv
```

If local Google auth lacks Drive scope, ask the user before running a scoped login command such as:

```bash
gcloud auth login --enable-gdrive-access
```

Do not print access tokens. Capture tokens in-process only.

Share the created Sheet with requester and cc users using Drive permissions.

## Verification

Before declaring done:

- Output row count equals source row count.
- Output includes all original source columns.
- Output includes all appended lookup columns.
- Generated Google Sheet metadata can be read.
- A range spanning the last original column and appended columns reads back correctly.
- Sharing permissions were attempted and the result was recorded.
- Slack draft uses the fresh Sheet link and does not mention stale blockers.

## Slack Draft Format

Draft in the original request thread unless the user asks to send.

```text
Hi <@requester> - got it! Here are the <brand/campaign> creator addresses.

**Results:**
- <found> of <total> unique creator addresses found
- <missing> unique creators have no gifting address on file and need manual collection
- <unit_only> unique creators have addresses stored only in the unit field and should be verified before shipping
- <fallback_names> creator names used fallback; <ambiguous_names> creator names remain ambiguous and are flagged in the notes column

**Full address data:** <fresh_google_sheet_url>

The fresh Sheet includes all original source columns plus the appended lookup columns, and I shared it with you and <@cc_user> as writers.

**<missing> needing manual collection:**
| Handle | Creator ID | Name |
|---|---:|---|
| ... |

For future requests, tag <@owner> and we'll run the lookup.
```
