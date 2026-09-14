# Changelog

## 0.1.0 - 2026-09-14

- **What**: Import `git-pr` from `commit-and-pr` into the `funnel` plugin.
  Split commit preparation from PR submission and add operation-based discovery descriptions.
  Wrap Markdown prose and frontmatter at 120 characters for source readability.
  Require user approval or a request for creation.
  Keep descriptions current after additional commits are pushed to PRs owned by the authenticated hosting account.
  Combine repeated safeguards and workflow steps. Require ASD-STE100 simplified technical English in PR/MR descriptions.
- **Why**: Keep Git skills beside the other Funnel skills so they can use relative references.
  Load the relevant instructions before each Git commit or PR operation.
  Reduce the context needed and use clear language in review descriptions.
- **Evidence**: The user requested 120-character line wrapping, including frontmatter, and two skills with the source
  behavior preserved, then specified creation approval and automatic description updates limited to the session's
  authenticated account.
  The user also requested shorter skills and simplified technical English for PR descriptions.
- **Impact**: Keep feature branches, validation, issue links, and push safety rules.
  Existing PR descriptions stay current without separate approval when the authenticated account owns the PR.
  Other authors or unknown account identity require explicit authorization.
  Description updates preserve the base branch and review state. Descriptions use simplified technical English.
- **Reference**: Imported from `~/dotfiles/_ai/skills/commit-and-pr` at the user's request in this session.
  The user requested that both Git skills belong to Funnel. Start a new change history.
