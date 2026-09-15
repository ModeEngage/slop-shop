# Slop Shop

A repository for skills intended to work with `workslop`.

The `funnel` plugin provides skills for planning Linear projects, writing implementation and exploratory issues,
breaking large implementation issues into sub-issues, and executing research, interviews, prototypes, and permanent
implementations.

## Workflow

1. Use `plan-project` to turn an idea into a Linear project, or `write-issues` to draft or create individual issues.
   Both use `write-issues` guidance to add the execution marker as an existing label or a standalone description line.
2. Use `execute-issue` with the issue to run the matching execution skill. It asks for clarification when the marker
   is missing or conflicting.

| Marker | Execution workflow |
| --- | --- |
| `slop:implementation` | Get approval of criteria, tests, and a plan, then use red-green-refactor. |
| `slop:prototype` | Build an artifact and iterate on feedback until the human confirms completion. |
| `slop:research` | Investigate assigned questions and record answers, evidence, and unresolved gaps. |
| `slop:interview` | Clarify decisions with the user and record the confirmed synthesis. |

Use `break-down-implementation` when a permanent implementation issue is too large for one agent session.
Planning and breakdown do not start execution. Each execution skill defines its own completion requirements.

## Installation

### `codex`

```sh
codex plugin marketplace add https://gitlab.com/ModeEngage/slop-shop.git
codex plugin add funnel@slop-shop
```

### cursor
