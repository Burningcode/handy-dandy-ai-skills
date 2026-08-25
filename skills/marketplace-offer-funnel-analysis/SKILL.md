---
name: marketplace-offer-funnel-analysis
description: Analyze a hypothetical two-sided marketplace offer funnel by defining lifecycle states, reconciling delivery, impression, response, rescission, and completion evidence, segmenting before counting, and separating reusable query patterns from private schemas. Use for marketplace funnel analysis and warehouse-backed operational investigations.
---

# Marketplace Offer Funnel Analysis

This is a sanitized example of a warehouse-backed marketplace runbook. All organizations, schemas, tables, fields, volumes, and metrics below are fictional placeholders. Configure only against systems the user is authorized to access.

## Define the lifecycle

Use a generic state model and map it to the real product before querying:

```text
drafted -> sent -> viewed -> accepted or declined or expired or rescinded
-> active -> completed
```

Do not assume application state, event telemetry, notification delivery, and business completion use the same identifiers or timestamps.

## Write metric contracts

At minimum define:

- offers sent;
- notification delivered;
- offer viewed;
- response;
- acceptance;
- rescission;
- completion;
- time between each material transition.

For every rate, specify numerator, denominator, eligibility, time window, unit, source, deduplication, and exclusions. Keep event occurrence distinct from authoritative offer state.

## Use the evidence chain

```text
eligible recipient -> offer created -> offer sent -> notification queued
-> notification delivered -> destination reached -> offer rendered
-> impression recorded -> response recorded -> state verified
-> obligation completed -> downstream value
```

A notification issue can affect response without directly affecting an upstream list impression when users enter through a different route. Place hypotheses where they can exert force.

## Example source contract

Replace these fictional names in a private, ignored configuration file:

| Purpose | Fictional source |
| --- | --- |
| Offer and lifecycle state | `demo_marketplace.offer_facts` |
| Campaign or opportunity | `demo_marketplace.opportunity_dim` |
| Experience events | `demo_events.product_events` |
| Notification delivery | `demo_messaging.delivery_events` |
| Participant segment | `demo_analytics.participant_segments` |
| Completion or value | `demo_marketplace.outcome_facts` |

Never commit real account IDs, databases, schemas, workgroups, credentials, or customer data.

## Investigation cuts

- state distribution and transition rates by week;
- sent-to-viewed and viewed-to-response decomposition;
- rescinded-before-view versus rescinded-after-view;
- notification queued, delivered, clicked, and failed;
- participant activity, tenure, segment, and platform;
- opportunity type, value band, and source;
- timing buckets between send, view, response, and rescission;
- raw event versus materialized metric comparison;
- legacy versus current system separation.

Segment before counting. Distinguish mix shift from within-segment change.

## Vendor-neutral query pattern

```sql
-- Illustrative only; adapt syntax and fields to the authorized warehouse.
SELECT
  opportunity_type,
  COUNT(DISTINCT CASE WHEN sent_at IS NOT NULL THEN offer_id END) AS sent,
  COUNT(DISTINCT CASE WHEN viewed_at IS NOT NULL THEN offer_id END) AS viewed,
  COUNT(DISTINCT CASE WHEN accepted_at IS NOT NULL THEN offer_id END) AS accepted,
  COUNT(DISTINCT CASE WHEN rescinded_at IS NOT NULL THEN offer_id END) AS rescinded
FROM demo_marketplace.offer_facts
WHERE sent_at >= :window_start
  AND sent_at < :window_end
GROUP BY opportunity_type;
```

The query is non-functional example code. It does not describe a real company schema.

## Hypothetical example

Fictional observation: Orbit Market's sent-to-viewed rate declines while notification delivery and viewed-to-response remain stable.

Working interpretation:

- response quality among viewers is unchanged;
- the problem is likely before or at render, not in offer attractiveness;
- next tests should compare destination routing, eligibility, render success, and impression instrumentation by platform and cohort;
- a change in dormant-recipient mix must be decomposed before naming a product defect.

No quantitative conclusion should be stated until the fictional query results are replaced with authorized evidence.

## Output

Lead with the finding and confidence, then include metric contracts, trend, segment decomposition, lifecycle timing, hypothesis board, source caveats, and one discriminating next test. Put detailed SQL in an appendix.

## Permission boundary

Prefer read-only warehouse access through a narrowly scoped connector. Confirm the account, workgroup, cost boundary, and data policy before querying when they are not already established. Never mutate production data or export sensitive rows as part of an analysis.

