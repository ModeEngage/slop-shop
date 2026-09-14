# Slop Shop

A repository for skills intended to work with `workslop`.

The `funnel` plugin provides `git-commit` for Git commits and `git-pr` for PR or
MR submission. Their descriptions tell agents to load them before the relevant
operation, including work within a larger task. PR creation requires a user request
or approval. After additional commits are pushed, `git-pr` keeps the description
current for PRs opened by the authenticated hosting account. Other authors require
explicit authorization. Automatic selection depends on the host agent.
PR and MR descriptions use ASD-STE100 simplified technical English.
Claude Code uses `/funnel:git-commit` and `/funnel:git-pr`.
