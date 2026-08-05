# Roadmap

> Schema: `product-canon-roadmap/v1`
>
> Authority: the complete product route plus user-approved delivery outcomes, order, dependencies, status, and Spec handoff.

## Product route

`UNKNOWN — record the confirmed product phases, capability scope, sequence, and open route decisions here.`

This layer preserves the complete product journey. It does not create Specs.

## Spec handoff rules

- Record vertical, independently demonstrable user outcomes; do not split by technical component.
- `Spec` means the approved delivery specification or equivalent technical specification. Speckit is one optional consumer, not a universal requirement.
- Only explicit approval of the exact user outcome, boundary, and acceptance may move an entry to `APPROVED`.
- One `APPROVED` entry maps to one Spec by default.
- Splitting or merging entries requires a ROADMAP change and explicit user approval.
- The next entry is the first `APPROVED` row whose dependencies are all `ACCEPTED`.
- A ROADMAP ID is product-owned and is never derived from a Spec directory number.
- An empty handoff table is valid; never turn the product route into speculative Spec rows.

## Spec handoff

Only rows in this table are eligible for specification workflows.

| ID | User outcome | Boundary | Dependencies | Acceptance | Status | Spec |
| --- | --- | --- | --- | --- | --- | --- |

## Allowed statuses

`PROPOSED` · `APPROVED` · `SPECIFIED` · `IMPLEMENTING` · `BLOCKED` · `ACCEPTED`
