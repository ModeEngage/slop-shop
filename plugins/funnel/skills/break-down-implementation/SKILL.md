---
name: break-down-implementation
description: >-
  Divide or revise a permanent implementation Linear issue into independently verifiable sub-issues, with native
  dependencies and complete coverage of the parent outcome. Use when the user requests an implementation breakdown.
  Does not implement or dispatch work.
---

# Break Down Implementation

Divide a decided implementation issue into clear outcomes. The parent remains the feature contract.
Stop after a verified breakdown. Do not implement, assign agents, or dispatch work.

## Establish the Contract

Read the issue, project, descendants, dependencies, and linked decisions. Inspect relevant code, tests, and
documentation read-only. Keep durable links and paths for later sessions.

Confirm settled scope and verifiable acceptance criteria. Do not invent criteria or make suggested implementation
details mandatory.
If a material choice about how to divide settled work needs user input, use the [interview skill](../interview/SKILL.md).
Send unresolved product or design decisions, or research gaps that affect scope or criteria, to
[plan-project](../plan-project/SKILL.md), or to the user without a project. Explain the gap and affected work before
wider project planning resumes. Do not hide gaps in sub-issues; ordinary implementation choices need no planning
round. If no useful separate outcomes can be defined, report that no breakdown is needed. Do not create a single
leaf merely to make a hierarchy.

## Divide the Outcome

Preserve the parent's problem, intent, scope, and criteria. Split by verifiable outcomes or subsystems; keep coupled
edits together. Each leaf includes implementation, tests, and documentation. Use no fixed count or depth. Prefer
direct children. Add an intermediate parent only when its combined outcome needs division. Its criteria summarize
its children; it has no separate execution assignment.

Each leaf needs an observable permanent outcome, settled criteria, relevant inputs, constraints, code paths or
references, and validation expectations. Give it enough context for an agent to start without prior chat history.
Name required outputs, handoffs, and constraints on using prerequisite results. Ready leaves must run in parallel
without conflicting edits or unstated coordination. Split, merge, or clarify leaves until this holds. Put detail in
its owning leaf; link shared decisions instead of copying. Do not split by predicted session length. Revise the
breakdown if execution reveals new boundaries.

Map every parent criterion to children. Assign integration and end-to-end validation to a suitable leaf, or a separate
integration leaf when needed. Finished leaves alone do not prove the parent outcome.

## Map Dependencies

Build the dependency graph before presenting the breakdown. Use parent links for scope and native blockers for work
order; nesting is not a prerequisite. For each blocker, name the required output and why the dependent issue needs
it. Combine conflicting work or add a blocker with a handoff. Leave independent leaves unblocked.

Read the parent's external blockers and dependents. Apply external blockers to affected leaves; a parent blocker does
not constrain children by itself. Keep consumers of the full feature dependent on the parent. Narrow a dependency
only when one child's result suffices and scope permits it. Never block a child on its parent.

Check the full graph for missing or unnecessary edges, reversed directions, and cycles. Confirm which leaves can
start without waiting. Tracker edits do not stop active agents; report conflicts with active assignments.

## Write and Apply the Breakdown

When writing issue bodies or choosing metadata, read [write-issues](../write-issues/SKILL.md) and its
[permanent implementation reference](../write-issues/references/permanent-implementation.md) for content and metadata.
Before revising an existing issue, also read its [update guidance](../write-issues/references/update-existing-issue.md).
Use the approval sequence below for the breakdown.

Present the complete proposed hierarchy with linked existing issues and temporary keys for new ones. Include issue
bodies, every blocker edge and its reason, ready and blocked leaves with prerequisites, parent-criteria coverage,
edits, and material metadata. Ask the user to approve the breakdown. If it changes materially, present the revision
for approval. Do not write to Linear until the user approves the proposal. After approval, apply it without a second
confirmation.

Use the parent's team and project and established metadata conventions. Leave new issues unassigned unless requested;
do not copy execution state. Reuse valid children; preserve completed work and unrelated edits. Cancel an unstarted
child made unnecessary by revision, record the reason on it, and repair dependencies. Report work-in-progress conflicts.

Create parents before children and map temporary keys to returned IDs and URLs. Add blockers after creation. If a
result is uncertain, inspect the parent's children before retrying. Resume partial work from the mapping.

## Verify and Hand Off

Before approval, check coherent leaves, criteria and integration coverage, relationships, metadata, and settled
requirements. After applying, read back issue content, parent links, project membership, metadata, and every native
blocker edge and direction. Do not close the parent before implementation and validation. Report partial updates as
incomplete.

Return the linked parent, concise hierarchy, ready leaves, blocked leaves with prerequisites, and gaps or incomplete
operations. Use linked issue titles in user-facing text.
