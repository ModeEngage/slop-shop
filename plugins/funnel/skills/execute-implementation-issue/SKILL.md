---
name: execute-implementation-issue
description: >-
  Deliver a permanent implementation after the user approves verification criteria, acceptance tests, and the
  implementation plan. Use to execute implementation work, including assigned issues; not to draft or break down
  an assignment, or build a prototype for learning.
---

# Execute an Implementation Issue

Deliver the agreed permanent change through red-green-refactor. Establish how to verify the result with the user
before writing implementation code.

## Planning Mode

If the host harness supports plan mode and permits the agent to enter it, enter that mode before clarification
and planning. Stay in plan mode until the user explicitly approves the verification criteria, acceptance tests,
and implementation plan. Then use the harness's supported transition to implementation mode before making changes.
Follow any host requirement for the user to make or approve that transition.

If plan mode is unavailable or the agent cannot activate it, follow the same planning and approval gate through
the conversation. Do not claim that the harness mode changed unless it did. A mode transition alone does not
replace approval of the tests and implementation plan.

## Read and Clarify

Read the assignment, linked decisions, and relevant repository instructions, code, tests, and documentation.
Identify the intended behavior, scope, constraints, dependencies, and current test methods. Use available context
before asking for missing information. Inspection and baseline checks can proceed before approval.

For an assigned issue, read its current description, relevant comments, parent, project context, and prerequisite
outputs. Confirm that required dependencies are satisfied before starting dependent work. Preserve the parent's
acceptance criteria and the assigned child's scope. Do not expand a child into the full parent implementation.

Treat implementation details as evidence and constraints, not a prescribed solution unless explicitly required.
Preserve confirmed decisions and accepted tradeoffs. Research findings and prototype feedback alone do not settle
a product decision. If the assignment is no longer a decided change, return the unresolved decision to the user or
the project's planning workflow before implementation. If the work needs decomposition, use
[break-down-implementation](../break-down-implementation/SKILL.md) when that breakdown is requested.

Ask clarifying questions whenever requirements are ambiguous. Do not replace an unresolved requirement with an
assumption. Resolve questions that affect scope, expected behavior, or verification before starting affected work.

## Establish Verification and Obtain Approval

Use [interview](../interview/SKILL.md) to resolve open requirements and establish the verification agreement with
the user. Keep the dialogue focused on the assigned change and preserve settled decisions. Use its question rounds
and summary confirmation rather than duplicate that procedure here. Establish:

1. **Verification criteria:** Measurable conditions that prove the deliverable is correct. State observable outcomes
   and relevant thresholds, including failure behavior and scope boundaries.
2. **Definition of done:** The complete set of acceptance tests needed to satisfy the assignment. Map each criterion
   to tests with clear inputs, expected results, and pass conditions. Include required documentation and other
   delivery conditions.
3. **Test plan agreement:** Specify the tests to add or change, relevant regression checks, and how to run them.
   Identify required environments, test data, and any manual checks. Resolve gaps in test coverage with the user.

Cover relevant modes, defaults, exceptions, runtime behavior, and compatibility. Include integration checks when
the assigned outcome combines prerequisite changes. For changes that can cause data loss, access-control failures,
production outages, or difficult migrations, carry forward the agreed rollback strategy or clarify it with the user.
Establish which review, merge, release, or deployment steps the assignment requires for completion.

Present these items with an implementation plan that explains the proposed changes and their order. Ask the user
to explicitly approve the tests and implementation plan. Wait for that approval before writing tests or implementation
code. An assignment to implement, silence, or approval of scope alone is not approval of the test and implementation
plan. Reuse explicit approval already present when it covers the same criteria, tests, and plan.

Include the criteria, acceptance tests, and implementation plan in the interview's final summary. Explicit approval
of that complete summary satisfies this gate; do not ask for a second approval of the same plan.

Do not begin implementation while verification criteria are unsettled or plan approval is pending. If a criterion
cannot be tested automatically, agree on a concrete verification method before proceeding. Do not claim that a
manual check provides evidence of a failing automated test.

## Implement Through Red-Green-Refactor

After approval, work in small increments:

1. **Red:** Write a test for the next agreed behavior and run it. Confirm that it fails because the behavior is
   missing or incorrect. Fix setup errors before treating the failure as evidence. If the test already passes,
   inspect why and determine whether it covers the intended change.
2. **Green:** Write the minimum implementation needed to make the test pass. Run the test and relevant existing
   tests. Do not weaken assertions or change expected behavior merely to obtain a passing result.
3. **Refactor:** Improve the implementation and tests as needed while preserving behavior. Run the affected tests
   again to confirm that they still pass.

Repeat until the agreed behavior is covered. Keep repository documentation accurate as the implementation changes.
For agreed manual checks, record the observed result and compare it with the approved pass conditions.

If new information makes requirements ambiguous, ask the user before implementing the affected behavior. If it
changes the verification criteria, acceptance tests, or implementation plan materially, present the revision and
wait for explicit approval before continuing affected work. Ordinary implementation choices within the approved
plan do not require another approval.

When resuming existing work, inspect the changes and available test evidence. Preserve valid work and apply the
approved test plan to remaining gaps. Do not claim that existing code was developed through a failing test unless
that evidence is available.

## Delivery

For authorized commits, use [git-commit](../git-commit/SKILL.md). For authorized pushes and pull or merge requests,
use [git-pr](../git-pr/SKILL.md). Follow their authorization and issue-linking rules. Plan approval does not expand
permission for delivery actions beyond the user's request.

## Verify and Report

Run the full agreed acceptance tests and required repository checks against the final change. Compare the results
with every verification criterion and definition-of-done condition. Report failed, blocked, or unrun checks as gaps;
do not treat them as passed or report the implementation as complete while required evidence is missing.

Record the changes, test results, manual evidence, and remaining limitations in the location specified by the
assignment. If none is specified, return them to the user. Include enough detail to repeat the checks.
Completion requires all agreed acceptance tests and delivery conditions to be satisfied.

For tracked work, keep the original assignment intact and link delivery artifacts and verification evidence from
the issue when issue updates are authorized. Read current content before edits, preserve unrelated changes, and
verify saved updates. Keep the issue incomplete while required review, merge, deployment, or checks remain pending.
Use closing PR links only when merge should complete the issue; use non-closing links for partial work.

Report the assigned outcome separately from parent or project completion. Completing a child does not prove that
the parent works; that requires evidence for the parent's full criteria, including integration checks.
