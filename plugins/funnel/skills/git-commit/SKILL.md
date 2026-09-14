---
name: git-commit
description: >-
  Review changes and create a safe, well-formed Git commit. Load before any Git commit operation, including commits made
  as part of a larger task or before opening a pull request.
---

# Git commit

Commit only on an explicit user request. Loading this skill does not authorize commits, pushes, PR creation, or
repository configuration changes. Never push to a protected default branch. Force-push or rewrite shared history only
with explicit user authorization.

For an authorized combined request, use [git-pr](../git-pr/SKILL.md) to apply its issue and review-state requirements,
push, and submit the work.

## Inspect and select a branch

Before staging, inspect working tree and untracked-file status, staged and unstaged diffs, recent commit subjects,
current branch, upstream, and default branch. Review all staged changes, including work staged before the request. In a
repository with no commits, inspect the index and working tree without relying on `HEAD`.

Keep an existing feature branch. On the default branch, create and switch to a feature branch before staging or
committing. Follow repository naming conventions; otherwise use `<issue-id>/<description>`. Ask if HEAD is detached or
the correct branch is uncertain.

Find the issue ID in conversation context, then the branch name, then repository plans, commits, or documentation that
clearly links the work to an issue. If a new branch needs an ID and none is available, ask; never invent one. A commit
does not otherwise require an issue link.

## Stage, validate, and commit

Follow repository instructions and templates. Stage only intended files; never use broad staging that could include
unrelated work. Exclude secrets, credentials, tokens, private keys, secret environment files, and unintended large or
generated binaries. Recheck the staged diff for the complete intended change before committing.

Do not create an empty commit. If no relevant changes exist, report that; continue with git-pr only for an authorized PR
request with existing work to submit.

Follow repository commit-message conventions; otherwise use `<type>(<optional scope>): <imperative summary>`. Types are
`build`, `chore`, `ci`, `docs`, `feat`, `fix`, `perf`, `refactor`, `revert`, `style`, and `test`. Keep the subject
concise. Add a body when useful to explain motivation and notable behavior. Pass multiline messages safely to prevent
shell interpolation. Add assistant or tool attribution only if the user or repository requires it.

Run relevant, proportionate validation before committing, or before pushing when the repository workflow requires it.
Report checks not run and why. Never bypass hooks (`--no-verify`). Fix hook failures and retry normally; do not amend a
failed commit. Amend a successful local commit only to include necessary hook-generated changes when repository policy
permits it.

## Verify and report

Confirm success and inspect the remaining working tree. Report the commit subject, validation results, and checks not
run. For an authorized combined request, continue with git-pr and include these details in the final report.
