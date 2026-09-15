---
name: break-down-implementation
description: >-
  Break a permanent implementation Linear issue into self-contained sub-issues that each fit one agent session,
  with native dependencies and complete coverage of the parent outcome. Use when implementation work is too large
  for one session or an existing breakdown needs revision. Does not implement or dispatch work.
---

# Break Down Implementation

Divide a decided permanent implementation issue into work that independent agent sessions can complete. Preserve
the original issue as the feature's contract. Planning ends with a verified hierarchy and dependency relationships.
Do not implement the work, assign agents, or dispatch execution.

## Read the Assignment

Read the target issue, its project context when present, existing descendants, dependencies, and linked decisions.
Inspect relevant repository code, tests, and documentation to establish current behavior, conventions, and boundaries.
Investigation is read-only. Use durable links and paths for evidence needed by later sessions.

Use [write-issues](../write-issues/SKILL.md) and its permanent implementation reference for issue bodies and metadata.
Use its existing-issue update guidance when revising the parent or existing descendants.

Confirm that the parent has settled scope and verifiable acceptance criteria. Ask only for material information that
cannot be obtained from available context. Do not turn suggested implementation details into requirements.

If investigation exposes an unresolved product decision or research question that changes the assignment, identify
the gap and affected work. Return it to [plan-project](../plan-project/SKILL.md), or to the user when no project is
involved. Do not invent acceptance criteria or create exploratory sub-issues to conceal an unsettled requirement.
Ordinary implementation choices do not require a new planning round.

If the issue already fits one agent session, report that no breakdown is needed. Do not create a parent with a single
leaf solely to produce a hierarchy.

## Decompose the Outcome

Keep the parent's problem, intent, scope, and acceptance criteria as the overall contract. Children divide how that
contract will be delivered; they must not expand or weaken it.

Split along independently verifiable outcomes or subsystem boundaries. Keep tightly coupled edits together. Include
the implementation, relevant tests, and documentation needed to complete each outcome in its assignment. Avoid
separate coding and testing issues when neither is a useful deliverable alone.

Use as many sub-issues and nesting levels as the work requires, with no fixed count or depth. Prefer direct children.
Add an intermediate parent only when it represents a meaningful implementation outcome that itself needs division.
Its acceptance criteria describe the combined result of its children; it must not contain a second execution assignment.

Put detailed work specifications in the lowest issue that owns them. Retain enough context in each leaf to understand
its assignment without another session's chat history. Link shared decisions and explain their relevant constraints
rather than copying all parent material into each child.

Account for every parent acceptance criterion in the proposed children. Include integration and end-to-end validation
where child results must work together to satisfy the parent. Assign that responsibility to a suitable leaf or a
separate bounded integration issue when it is meaningful work. Do not assume that individually completed children
prove the parent outcome.

## Make Each Leaf Executable

Each leaf must:

- Describe a permanent implementation outcome with observable acceptance criteria.
- Provide its relevant inputs, constraints, code paths, references, and validation expectations.
- Fit one agent session, including the context needed to understand, implement, and verify the change.
- Identify prerequisite outputs and the constraints needed to use them.
- Be safe to execute alongside every other available leaf without conflicting edits or unstated coordination.

Judge session size from the actual scope, coupling, and context required. Do not impose a fixed token or file count.
Split, merge, or clarify leaves that fail these checks. A leaf may wait for a prerequisite implementation result, but
its intended behavior and acceptance criteria must already be settled.

## Wire Dependencies

Use native blocking relationships for work order and parent relationships for decomposition. Nesting alone does not
express execution prerequisites.

When leaves require conflicting edits or shared state, consolidate them or add an ordering dependency and describe
the handoff. Where work can proceed independently, do not add a blocker merely because the issues share a parent.

Read the parent's external blockers and dependents. Preserve their meaning after decomposition:

- Apply external prerequisites to affected leaves explicitly. Do not assume a blocker on the parent blocks children.
- Keep work that requires the complete feature dependent on the parent. Use a narrower dependency only when the
  consumer needs that child's result alone and the supported scope permits the change.
- Do not block a child on its own parent. The parent outcome depends on its descendants being delivered.

Check the complete dependency graph for cycles and missing prerequisites. An issue edit or new blocker does not
stop an agent already executing work; report any conflict with an active assignment explicitly.

## Draft or Apply the Breakdown

Present the hierarchy with linked existing titles and temporary keys for new issues. Include proposed issue bodies,
dependency edges and their reasons, the leaves that can start, and how children cover the parent acceptance criteria.
Identify changes to existing issues and material metadata choices.

A draft request authorizes drafting. A request to create or revise the breakdown authorizes the corresponding Linear
updates once material content and metadata questions are resolved. Do not require a second approval for clear updates
already requested by the user.

Use the parent's team and project when present, and established conventions for other metadata. Do not copy the
parent's assignee or execution state to new children. Leave new issues unassigned unless the user requests otherwise.

Reuse valid existing children. Preserve completed work and unrelated edits. If revising the breakdown makes an
unstarted child unnecessary, cancel it with the reason recorded on that issue and repair affected dependencies.
Identify conflicts with work in progress instead of claiming tracker updates have redirected active execution.

Create new issues parent-first and retain a mapping from temporary keys to returned identifiers and URLs. Add native
dependencies after all required issues exist. If a create result is uncertain, inspect the intended parent's children
before retrying. Resume partial work from the recorded mapping rather than recreate the tree.

## Verify and Hand Off

The breakdown is complete when:

- Every remaining leaf passes the executable checks and fits one agent session.
- The hierarchy covers the parent's full acceptance criteria, including integration and validation.
- Parent relationships, project membership, metadata, and dependency directions match the intended breakdown.
- No unresolved requirement is hidden in an implementation assignment.
- All requested writes have been verified. For draft-only requests, the proposed breakdown satisfies the checks above.

For applied changes, read the resulting descendants and dependencies to verify these conditions. Do not close the
parent because decomposition is complete; its acceptance criteria still require implementation and verification.
Report partial updates and unresolved gaps as incomplete breakdowns.

Return the linked parent, a concise hierarchy summary, leaves available to start, blocked leaves and their
prerequisites, and any unresolved gap or incomplete operation. Use linked issue titles in user-facing text.
Stop after the handoff.
