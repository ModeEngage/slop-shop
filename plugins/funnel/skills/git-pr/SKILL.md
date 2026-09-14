---
name: git-pr
description: >-
  Push a feature branch and open or update a pull request or merge request. Load before PR or MR creation or updates,
  and when pushing additional commits to a branch with an existing PR or MR.
---

# Git PR

## Authorization

Create a PR or MR only on a user request or approval; a commit or push request does not authorize creation. Loading this
skill does not authorize pushes or repository configuration changes. For authorized commits, first use
[git-commit](../git-commit/SKILL.md); do not commit solely because a PR was requested.

After each authorized push of additional commits, keep the existing PR description current without separate approval if
its author matches the hosting account authenticated for this repository. Verify that account through this session's
hosting integration or CLI, not Git author settings, commit authors, or a local username. Require explicit authorization
to edit another author's PR or when the authenticated account is unknown.

## Inspect, validate, and push

Inspect working tree and untracked-file status, branch, upstream, default branch, recent commit subjects, and the full
PR diff and commits against its base. In a repository with no commits, inspect the index and working tree without
relying on `HEAD`. If there is no work to submit or authorized work to commit, report that; do not create an empty
commit or PR.

Keep an existing feature branch. On the default branch, create and switch to a feature branch before staging,
committing, or pushing. Follow repository naming conventions; otherwise use `<issue-id>/<description>`. Ask if HEAD is
detached or the correct branch is uncertain.

Run relevant, proportionate validation if not already run for these changes or required by repository workflow. Report
checks not run and why. Never bypass hooks, stage unrelated files, or commit secrets, credentials, tokens, or private
keys.

Push the feature branch to its intended remote; set upstream only if needed. Never push to a protected default branch.
Force-push or rewrite shared history only with explicit user authorization and a safe target.

After a successful push, find the open PR for the pushed source repository and branch through the hosting integration or
CLI. Resolve multiple possible matches before editing. If no integration is available, ask whether to continue manually;
do not guess URLs or API behavior. If no PR exists, apply the creation authorization rule.

## Link the issue

Find the issue ID in this order:

1. User request and conversation context.
2. Branch name, using the repository's issue-ID pattern.
3. Repository plans, commits, or documentation that clearly links the work to an issue.
4. Existing PR description and linked issues.

Ask for a missing ID before creating or updating the PR; never invent one. Include it in the description using the
tracker's linking syntax. The commit subject and PR title need it only if repository conventions require it.

For Linear, put a magic word directly before each ID, without intervening punctuation, and repeat it for each issue:

- **Closing**: `Fixes`, `Closes`, `Resolves`, `Completes`, or `Implements`, as in `Fixes <issue-id>`. Use only when
  merge into the default branch should complete the issue.
- **Non-closing**: `References`, `Related to`, or `Part of`, as in `Part of <issue-id>`. Use for partial or related
  work.

If completion is uncertain, use `Part of` or ask.

## Create or maintain the PR

Follow repository instructions. Look for PR/MR templates in standard hosting-platform locations and repository
documentation; preserve required sections and checkboxes.

For a new PR, determine the base from clear repository conventions or the default branch; otherwise ask. Ask about draft
versus ready status if the user request and context do not resolve it. Retain an existing PR's base and review state
unless the user requests a change.

Use a concise title that follows repository conventions; otherwise match the commit subject with `<type>(<optional
scope>): <imperative summary>`. Types are `build`, `chore`, `ci`, `docs`, `feat`, `fix`, `perf`, `refactor`, `revert`,
`style`, and `test`.

Write PR and MR descriptions in ASD-STE100 simplified technical English. Use short sentences, direct verbs, and
consistent terms. Include the problem or intent, a focused change summary, a concrete test plan, automated validation
already run, and the required issue link. Describe only pushed changes.

For an existing PR, read its author, title, body, base, and review state, then apply the author and authorization rules.
Compare the description with the full pushed diff and commits. Update stale summaries, test plans, validation results,
and issue completion claims. Preserve relevant context, template sections, checkboxes, and user-authored content. Leave
an accurate description unchanged.

## Verify and report

Confirm the branch is pushed and the PR has the intended base and review state. Read back description edits to verify
they reflect the pushed changes. Report the PR URL, commit subject, validation results, checks not run, and whether the
description was updated, already current, or left unchanged because authorization or author checks failed. Report update
failures; do not claim a failed update is current.
