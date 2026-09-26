# Changelog

## 0.1.1 - 2026-09-26

- **What**: Shorten the skill entrypoint while retaining its breakdown, dependency, update, and verification rules.
- **Why**: The entrypoint was too long for Codex to load in full.
- **Evidence**: The user reported that Codex truncates the skill during loading.
- **Impact**: The breakdown workflow uses less context when Codex loads it.
- **Reference**: This session's request and the existing `write-issues` guidance.

## 0.1.0 - 2026-09-15

- **What**: Add a skill to divide permanent implementation issues into self-contained sub-issues, maintain native
  dependencies, preserve the parent contract, and verify coverage before handoff.
- **Why**: Features that exceed one agent session need bounded assignments without repeating project discovery.
- **Evidence**: The user requested an implementation sub-issue skill based on their Cursor `linear-wayfinder` skill.
- **Impact**: Large implementation issues can be prepared for separate sessions without dispatching execution.
  Unsettled requirements return to project planning, and integration work remains part of the breakdown.
- **Reference**: The user's `linear-wayfinder` skill and this session's agreed boundary between project planning and
  implementation decomposition; the bundled `write-issues` skill.
