# Concise code documentation guidance

Read this reference for a Code Documenter task packet or when the Coordinator defines a documentation contract.

## Outcome

Help a younger or less-familiar developer build an accurate mental model of the finalized code without increasing maintenance burden. Use plain, direct language without talking down to the reader. Define unavoidable domain terms once and preserve precise technical meaning.

Document the finalized change surface by default. A whole-repository documentation sweep requires explicit scope.

## Documentation hierarchy

Use the closest durable location that fits the knowledge:

1. **Names and structure** should communicate ordinary behavior. Do not add a comment when a clearer existing name already makes the code obvious; the Documenter cannot refactor finalized code and should report a naming concern instead.
2. **Inline comments** explain local intent, invariants, counterintuitive ordering, compatibility constraints, or why the obvious alternative is unsafe.
3. **Docstrings/API comments** explain a public or reusable unit's purpose, meaningful inputs and outputs, failure behavior, side effects, and non-obvious constraints. Do not repeat type annotations or the function name in prose.
4. **Module or developer docs** explain boundaries, data flow, setup, extension points, and relationships spanning multiple symbols or files.
5. **Small examples** are appropriate only when they clarify a tricky contract or edge case more efficiently than prose. Keep them executable or easy to verify when project conventions support that.

## What deserves explanation

- Why the component exists and where it fits.
- Domain rules that are not obvious from the programming language.
- Preconditions, postconditions, invariants, ownership, and lifecycle.
- Failure, fallback, retry, cancellation, or last-known-good behavior.
- Non-obvious algorithms, data structures, complexity tradeoffs, or ordering requirements.
- Compatibility constraints and intentionally preserved behavior.
- Trust boundaries and the reason for validation, bounds, or cycle detection.
- Extension points and the smallest safe way to add another implementation.

## What to omit

- Line-by-line narration such as “increment the counter” or “loop over items.”
- Boilerplate docstrings for obvious private helpers, getters, setters, or thin wrappers.
- Prose that duplicates types, tests, or the code without adding intent.
- Long tutorials, decorative headings, copied requirements, or generated API encyclopedias.
- Change history, author commentary, speculative future design, apologies, or stale TODOs.
- Examples that are harder to maintain than the behavior they explain.
- Comments that compensate for a possible bug or unclear contract; report the issue instead.

## Behavior freeze

The Code Documenter may edit only packet-owned comments, docstrings, and developer-facing documentation. Do not change executable statements, imports, dependencies, signatures, types, schemas, configuration values, generated files, vendored files, formatting across unrelated lines, or tests.

Docstrings can be runtime-visible through reflection and can affect package size or generated API output. When that matters to the interface or resource contract, prefer a non-runtime comment or external developer documentation and report the choice.

If accurate documentation requires guessing, stop and return the ambiguity with file-and-line evidence. If the implementation needs a refactor or behavior correction to become explainable, return `revision_required` to the Coordinator. After product changes, repeat affected reliability/regression gates and the documentation pass.

## Quality check

For each addition, ask:

- Does this teach something the code does not already say clearly?
- Is it close to the behavior it describes?
- Does it explain `why`, a contract, or a safe mental model?
- Is every statement true for the finalized implementation and tests?
- Could it be shorter without losing the important constraint?
- Will it remain useful after a small internal refactor?

Prefer no new comment over a redundant or speculative one.
