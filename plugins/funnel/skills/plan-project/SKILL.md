---
name: plan-project
description: >-
  Create or refine a Linear project from a vague idea, with exploratory and implementation issues and maintained
  dependencies. Use for initial planning or replanning after findings arrive. Does not execute or dispatch work.
---

# Plan a Project

Turn an idea into a Linear project that can develop as questions are answered. Create only the work that can be
specified with confidence. Keep less defined work in the project description until findings make it clear enough
to assign. Support a new project, an empty project, and an existing project with work and findings.

This is a recurring planner. Do not execute issues, assign agents, or dispatch work.

## Establish Context

Read the available conversation, relevant repository material, and any referenced Linear project and issues.
For an existing project, inspect its description, issue states, dependencies, and relevant findings documents.
Follow links to detailed findings as needed to understand their effect on the plan.

Resolve the target project and team from available context. Ask when they cannot be inferred. Inspect available
metadata and use established conventions. Do not invent labels, deadlines, priorities, or assignments.

Use the [interview skill](../interview/SKILL.md) to establish the user's intent, desired outcome, scope, constraints,
and success criteria. Limit this planning interview to what is needed to define the project and initial assignments.
Put deeper questions into exploratory issues. Preserve settled decisions when returning to an existing project.

If findings require a material change to the desired outcome or scope, discuss that change directly with the user
before replanning affected work. Do not treat a research finding as a confirmed product decision.

## Project Description

Keep the description short enough to provide shared context for later sessions. Use these sections and omit empty
optional sections:

- **Intent**: Why the user wants the work. Use the user's stated motivation.
- **Desired outcome**: What the completed project achieves.
- **Success criteria**: Observable conditions that establish project completion.
- **Context and constraints**: Information relevant across the project, including repositories, systems, and durable
  reference links. Distinguish working assumptions from confirmed constraints.
- **Findings and decisions**: Short summaries linked to the issues that hold the details. Distinguish findings,
  confirmed decisions, and working assumptions.
- **Not yet specified**: In-scope work or questions that are not clear enough to assign.
- **Out of scope**: Explicit boundaries.

Keep detailed assignments and findings on their issues. Use linked issue titles in the description and in user-facing
summaries. Do not copy the full issue list into the description; project membership and dependencies show the work.

Add explicit entries in Findings and decisions for exploratory issues whose results will inform the project.
An open entry can state the question being investigated. The execution skills can then update that entry with a
short outcome and an issue link. Preserve the detailed findings in the document attached to the issue.

## Define Issues

Use [write-issues](../write-issues/SKILL.md) for issue bodies, type-specific requirements, metadata, and findings
recording. Use its four types:

| Type | Intended result |
| --- | --- |
| Research | Answers to factual questions through autonomous investigation |
| Interview | Decisions or refinement through human dialogue |
| Implementation: prototype | A rough artifact and human feedback that clarify a concept |
| Implementation: permanent | A decided change with settled scope and observable acceptance criteria |

Create as many issues as the work requires. Do not target a fixed count or create an issue of each type by default.
Each assignment must include enough durable context for a later session to understand and perform its work.

A question can become an exploratory issue when it can be stated precisely, even if another issue blocks its
execution. If its assignment cannot yet be defined, keep it in Not yet specified.

Create a permanent implementation issue only when the decisions that define its scope and acceptance criteria are
settled. Until then, keep the prospective change in Not yet specified and create the exploratory issues needed to
resolve those decisions. A decided implementation issue can still depend on other implementation work.

Create issues directly in the project. Do not create organizational parent issues or sub-issues. The separate
`break-down-implementation` skill divides permanent implementation issues that exceed one agent context window.
Do not load that skill during project planning. Load it only when the task includes breaking down implementation
issues. Do not force those issues into one session or perform that breakdown here. Preserve existing parent
relationships when refining a project.

## Maintain Dependencies

Use native blocking relationships when one issue cannot proceed without another issue's result. Link useful context
without a blocking relationship when it does not prevent work from proceeding.

Before leaving work available to start, check for unresolved research, interviews, prototypes, and prerequisite
changes that could alter its assignment. Block affected work on those prerequisites. If the defining decisions for
an implementation issue are no longer settled, revise the plan rather than leave an actionable assignment based on
assumptions.

Dependencies are the protection against starting work too early. Editing or cancelling an issue does not notify an
agent already executing it. If new findings conflict with work in progress, report that conflict explicitly; do not
claim that an issue edit or a new blocker has stopped the active work.

Check that dependencies have the intended direction and contain no cycles. Recheck dependencies after revisions or
cancellations. Cancellation does not supply the result that a dependent issue needed; remove, replace, or revise the
affected dependency according to the remaining assignment.

## Refine an Existing Plan

Compare new findings and confirmed decisions with the current project and issues:

1. Update the shared context and relevant findings summaries.
2. Create issues for work that is now clear enough to assign.
3. Remove entries from Not yet specified when issues replace them. Retain any portion that remains unclear.
4. Revise affected assignments and dependencies to reflect the supported plan.
5. Cancel work that is no longer needed. Record the reason on the cancelled issue and retain its history.
6. Record work excluded by a scope decision in Out of scope when it helps explain the project boundary.

Keep valid existing work. Do not recreate issues just to make their wording or structure uniform. Follow the
write-issues guidance for updates to existing issues.

## Planning Exit Criteria

Planning is complete when all of these conditions hold:

- Every remaining issue is a permanent implementation issue with settled scope and verifiable acceptance criteria.
- No unresolved research, interview, or prototype work remains. Relevant findings are reflected in the plan.
- Not yet specified has no remaining entries.
- The implementation issues cover every unmet project success criterion.
- Dependencies accurately describe the required work order.

Implementation issues do not need to fit one agent session for planning to be complete. The separate breakdown skill
owns that division. Planning completion is provisional; new findings can require further planning.

A planning session can end before planning is complete when all currently definable work is recorded and further
planning depends on exploratory findings. Report **Planning awaits findings** and identify the issues whose results
are needed. Do not use this status to leave work unspecified when it can already be assigned.

Distinguish **Planning complete** from **Project complete**. The project is complete only when its success criteria
are met. An empty issue list or the closure of all current issues does not establish completion. Identify unmet
outcomes and evidence gaps. If a missing decision or an incomplete update prevents a planning handoff, report that
blocker rather than claim planning is complete or awaits findings.

## Apply and Verify

A request for a draft authorizes drafting. A request to create or maintain the project authorizes the corresponding
Linear updates once material content and metadata decisions are resolved. Do not add a separate approval step for
routine updates already within the user's request.

Before updating the project description, read its current content and preserve unrelated edits. Resolve conflicting
changes before writing. Create issues before adding dependencies that require their identifiers.

If a create operation has an uncertain result, check the project for the intended issue before retrying. If updates
stop partway through, retain the mapping of completed operations and report the remaining work.

Verify project membership, issue content, and dependency relationships after writes. Confirm that cancellations have
recorded reasons and that affected dependencies still represent the intended prerequisites.

Return the linked project title and a concise summary of:

- What was created, revised, or cancelled, with reasons for material changes.
- Which issues can start and which are blocked, with their prerequisites.
- What remains unclear and any conflict with work already in progress.
- Whether planning is complete or awaits findings, with the relevant evidence or prerequisite issues.
- Whether the success criteria are met, when assessing project completion.
- Any updates that could not be completed or verified.

Stop after the planning handoff.
