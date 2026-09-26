---
name: break-down-implementation
description: >-
  Break a permanent implementation Linear issue into self-contained sub-issues that each fit one agent session,
  with native dependencies and complete coverage of the parent outcome. Use when implementation work is too large
  for one session or an existing breakdown needs revision. Does not implement or dispatch work.
---

# Break Down Implementation

Divide a decided implementation issue into separate agent sessions. The parent remains the feature contract.
Stop after a verified breakdown. Do not implement, assign agents, or dispatch work.

## Establish the Contract

Read the issue, project, descendants, dependencies, and linked decisions. Inspect relevant code, tests, and
documentation read-only. Keep durable links and paths for later sessions.

Read [write-issues](../write-issues/SKILL.md), its permanent implementation reference, and its update guidance before
editing existing issues. Confirm settled scope and verifiable acceptance criteria. Ask only for material information
that context cannot supply. Do not make suggested implementation details mandatory. Send product or research gaps that
change the assignment to [plan-project](../plan-project/SKILL.md), or to the user without a project. Do not hide gaps
in sub-issues; ordinary implementation choices need no planning round. If one session can finish the issue, report
that no breakdown is needed. Do not create a single leaf merely to make a hierarchy.

## Divide the Outcome

Preserve the parent's problem, intent, scope, and criteria. Split by verifiable outcomes or subsystems; keep coupled
edits together. Each leaf includes implementation, tests, and documentation. Use no fixed count or depth. Prefer
direct children. An intermediate parent needs a combined outcome, with criteria summarizing its children and no
separate execution assignment.

Each leaf needs an observable permanent outcome, settled criteria, relevant inputs, constraints, code paths or
references, and validation expectations. It must fit one session, including context and verification. Name required
outputs and handoffs. Ready leaves must run in parallel without conflicting edits or unstated coordination. Split,
merge, or clarify leaves until this holds. Put detail in its owning leaf; link shared decisions instead of copying.

Map every parent criterion to children. Assign integration and end-to-end validation to a suitable leaf, or a bounded
integration leaf when needed. Finished leaves alone do not prove the parent outcome.

## Set Relationships

Use parent links for scope and native blockers for order; nesting is not a prerequisite. Combine conflicting work or
add a blocker and handoff. Leave independent leaves unblocked. Apply external parent blockers to affected leaves.
Keep consumers of the full feature dependent on the parent; narrow this only when one child's result suffices and
scope permits it. Never block a child on its parent. Check for cycles and missing prerequisites. Tracker edits do
not stop active agents; report conflicts with active assignments.

## Draft or Apply

Show linked existing issues and temporary keys for new ones, proposed bodies, blockers and reasons, ready leaves,
parent-criteria coverage, edits, and material metadata. A draft request authorizes a draft. A create or revise request
authorizes Linear updates once material questions are resolved; do not request a second approval for clear updates.

Use the parent's team and project and established metadata conventions. Leave new issues unassigned unless requested;
do not copy execution state. Reuse valid children; preserve completed work and unrelated edits. Cancel an unstarted
child made unnecessary by revision, record the reason on it, and repair dependencies. Report work-in-progress conflicts.

Create parents before children and map temporary keys to returned IDs and URLs. Add blockers after creation. If a
result is uncertain, inspect the parent's children before retrying. Resume partial work from the mapping.

## Verify and Hand Off

Check session size, criteria and integration coverage, relationships, metadata, and settled requirements. For applied
changes, read back descendants and dependencies to verify all writes; for drafts, verify the proposal. Do not close
the parent before implementation and validation. Report partial updates as incomplete.

Return the linked parent, concise hierarchy, ready leaves, blocked leaves with prerequisites, and gaps or incomplete
operations. Use linked issue titles in user-facing text.
