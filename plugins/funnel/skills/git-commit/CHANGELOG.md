# Changelog

## 0.1.0 - 2026-09-14

- **What**: Import `git-commit` from `commit-and-pr` into the `funnel` plugin.
  Split commit preparation from PR submission and add operation-based discovery descriptions.
  Wrap Markdown prose and frontmatter at 120 characters for source readability.
  Combine repeated safeguards and workflow steps; remove the redundant commit example.
- **Why**: Keep Git skills beside the other Funnel skills so they can use relative references.
  Load the relevant instructions before each Git commit or PR operation.
  Reduce the context needed without changing the workflow rules.
- **Evidence**: The user requested 120-character line wrapping, including frontmatter, and two skills with the source
  behavior preserved.
  The user also requested shorter skills without loss of functionality.
- **Impact**: Keep explicit authorization, feature branches, validation, and safety rules.
  Keep staging and commit rules in `git-commit`; keep ticket links, push rules, and PR handling in `git-pr`.
  A combined request uses both skills.
- **Reference**: Imported from `~/dotfiles/_ai/skills/commit-and-pr` at the user's request in this session.
  The user requested that both Git skills belong to Funnel. Start a new change history.
