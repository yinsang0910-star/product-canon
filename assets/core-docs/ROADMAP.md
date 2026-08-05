# Roadmap

> Schema: `product-canon-roadmap/v1`
>
> Authority: user-approved delivery outcomes, order, dependencies, status, and Spec handoff.

Product horizons, phases, explanations, and grouping may be added freely outside the delivery table. They provide context but do not create Specs.

## Rules

- Record vertical, independently demonstrable user outcomes; do not split by technical component.
- Only explicit user approval may move an entry to `APPROVED`.
- One `APPROVED` entry maps to one Spec by default.
- Splitting or merging entries requires a ROADMAP change and explicit user approval.
- The next entry is the first `APPROVED` row whose dependencies are all `ACCEPTED`.

## Delivery entries

Only rows in this table are eligible for specification workflows.

| ID | User outcome | Boundary | Dependencies | Acceptance | Status | Spec |
| --- | --- | --- | --- | --- | --- | --- |

## Allowed statuses

`PROPOSED` · `APPROVED` · `SPECIFIED` · `IMPLEMENTING` · `BLOCKED` · `ACCEPTED`
