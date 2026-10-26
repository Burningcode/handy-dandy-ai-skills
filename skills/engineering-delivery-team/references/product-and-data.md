# Product, data, and prototype guidance

Use this for a new prototype, a parity rebuild, or a meaningful product slice. Apply the relevant parts; do not impose a tourism or recording product's policies on an unrelated application.

## Preserve the outcome across slices

Write the original user outcome and one observable end-to-end journey before dividing work. Inventory the current screens, roles, working interactions, persistence, and unavailable integrations. Label behavior as implemented, simulated, planned, or unverified. Keep a parity matrix when rebuilding an existing app.

A successful subordinate feature may still miss the outcome. A directory is not a feasible itinerary; a redirect is not a confirmed conversion; a saved recording is not trustworthy notes. At each checkpoint, name what a user can now accomplish and the remaining gap. Use a competition rubric or executive demo as acceptance evidence without inflating scope to add features solely for the rubric.

Choose a coherent first slice, then improve it with actual operator/user feedback. Respect accepted scope changes and version the affected packets. Do not freeze an earlier pilot boundary after the user expands it, or carry a past approval to a new external target.

## Verify the complete experience

Follow the real click path, including entry, role or identity selection, navigation, state changes, result, and return/retry. Include operator setup, onboarding, budget/configuration changes, corrections, and moderation when they are part of the request. Verify that simulated selectors are not standing in for actual access control.

Check representative small and large viewports, zoom, long labels, card/table/dialog overflow, keyboard focus, touch targets, contrast, and meaningful loading/empty/error/permission states. Keep map and list selections and filters synchronized; retain a usable non-map path. For copy, make next actions, caveats, and success states specific. Keep uncertainty beside the decision it qualifies. Do not hardcode an aesthetic or technology stack from a past prototype.

## Make data trust visible and operable

For source-backed products, preserve the original claim, source identifier/URL, retrieval time, confidence or verification state, selected resolution, and unresolved conflict where relevant. Discovery leads are not verified live facts. A default merge key must reflect an explicit entity relationship, not name resemblance alone. Time windows and time zones must match the actual product promise; frozen demo snapshots must be disclosed and must not masquerade as a rolling live feed.

An operator should be able to inspect provenance, add sources/nodes, preview changes, validate required fields and links, and publish or restore within their permissions. Community signals and imported claims should not bypass the product's established moderation or authority model. For commercial surfaces, preserve the project's distinction between sponsored content and independently sourced facts; do not adopt another project's advertising policy automatically.

## Treat AI output as a versioned derivative

Keep source evidence, generated output, human edits, review decisions, and lifecycle state distinct. Model output should carry relevant source/version provenance. A ready label must correspond to the current durable artifact, not a stale file or successful model call. Preserve supported first-pass work during repair; bounded repair does not justify silently replacing valid content with weaker output. Make uncertainty and omitted content visible when they affect reliance.

For an AI feature, identify the quality floor, desired result, useful exceptional result, silent failures, and cost/latency tradeoff. Test quality claims on permitted data. Use synthetic fixtures for state/recovery tests; do not present those as proof of real-world model accuracy. Actual customer content or live capture requires its own access and processing authorization.

## Fit the host and leave a clean handoff

Inspect actual platform capabilities. If an app builder cannot run a requested backend, state that limitation and propose a compatible API boundary or a scoped alternative; never fabricate support. Do not force an unsupported stack for visual similarity.

Maintain a short reading order, current status, key decisions, data/source contracts, setup instructions, and verification evidence using the project's conventions. A handoff should let a new worker resume without replaying the entire conversation. Use a concise initial brief and separate detailed contracts when a builder has limited prompt capacity; confirm current platform behavior before making product-specific claims.
