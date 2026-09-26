# Changelog

## 0.1.1 - 2026-09-26

- **What**: Shorten the entrypoint, replace session-size rules with verifiable outcomes, defer issue-writing guidance,
  use the interview skill for breakdown choices, and apply changes unless the user requests a draft.
- **Why**: Session duration is uncertain, early reference loading wastes context, and breakdown choices can need user
  input without reopening product design.
- **Evidence**: The user reported truncation and identified session-size, reference-loading, and draft-flow problems.
- **Impact**: The workflow uses less context, divides work by observable boundaries, and routes questions by type.
- **Reference**: This session's requests and the `write-issues`, `interview`, and `plan-project` skills.

## 0.1.0 - 2026-09-15

- **What**: Add a skill to divide permanent implementation issues into self-contained sub-issues, maintain native
  dependencies, preserve the parent contract, and verify coverage before handoff.
- **Why**: Features that exceed one agent session need bounded assignments without repeating project discovery.
- **Evidence**: The user requested an implementation sub-issue skill based on their Cursor `linear-wayfinder` skill.
- **Impact**: Large implementation issues can be prepared for separate sessions without dispatching execution.
  Unsettled requirements return to project planning, and integration work remains part of the breakdown.
- **Reference**: The user's `linear-wayfinder` skill and this session's agreed boundary between project planning and
  implementation decomposition; the bundled `write-issues` skill.
