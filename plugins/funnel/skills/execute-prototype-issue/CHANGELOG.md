# Changelog

## 0.1.1 - 2026-09-27

- **What**: Add rules for prototype code: no test-driven development or merge quality gates, tests only where they
  make the artifact cheaper to build or check, and code on a local branch unless the assignment or the human asks
  otherwise. These rules take precedence over general or repository test-first rules. Linear findings attach a
  source bundle, run instructions, and output snapshots as the durable artifact.
- **Why**: The skill did not say how to test prototype code or where to keep it, so the agent asked each time.
  Repository instructions that require test-first development and merge gates also conflicted with the purpose of a
  learning artifact.
- **Evidence**: During a TUI prototype, the agent asked about test discipline and artifact location. The user
  answered both questions, then asked for these answers to become the skill's defaults.
- **Impact**: Prototype execution no longer asks about test discipline or artifact location. Repository test-first
  rules no longer block prototype code. The artifact stays available after the local branch is gone.
- **Reference**: User decisions in this session. An earlier TUI prototype attached source, snapshots, and run
  instructions to its issue in the same way.

## 0.1.0 - 2026-09-13

- **What**: Import `execute-prototype-issue` and its supporting files. Start a new change history.
- **Why**: Add issue execution to the `funnel` plugin.
- **Evidence**: The user requested the execution skills from the same source directory.
- **Impact**: The skill is bundled for all three agents. Its source instructions are preserved.
- **Reference**: Imported from `~/dotfiles/_ai/skills/execute-prototype-issue` at the user's request in this session.
