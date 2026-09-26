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

## Define the Plan

Before writing project content or selecting issues, read
[project and issue content](references/project-and-issues.md). It defines the description sections, findings entries,
issue types, and the rules for work that is not yet specified. Use the linked write-issues skill for assignments.

Create only work that can be specified with confidence. Create permanent implementation issues only when their
scope and acceptance decisions are settled. Keep unclear work in Not yet specified. Create issues directly in the
project, without new organizational parents or sub-issues. Preserve existing parent relationships.

Do not load break-down-implementation unless the task includes implementation breakdown. Broad implementation
issues do not prevent planning completion; that separate skill owns their division.

## Maintain the Plan

Before setting dependencies or refining existing work, read
[dependencies and replanning](references/replanning.md). It defines blocking relationships, cancellation handling,
and the update sequence for new findings.

Block work on unresolved prerequisites that can change its assignment. Revise implementation assignments when their
defining decisions are no longer settled. Keep valid existing work and check dependency direction and cycles.
Report conflicts with work in progress; an issue edit or blocker does not stop an active agent.

## Apply and Hand Off

Before Linear writes or a planning handoff, read [verification and handoff](references/handoff.md). It defines write
authorization, verification, recovery from partial updates, exit criteria, and the final report.

A draft request authorizes drafting. A request to create or maintain a project authorizes the corresponding updates
once material content and metadata decisions are resolved. Do not add approval for routine authorized updates.

Planning is complete only when all remaining issues are permanent implementations with settled scope and verifiable
acceptance criteria, no exploratory or unspecified work remains, issues cover all unmet success criteria, and
dependencies show the required work order. Report Planning awaits findings only when all currently definable work
is recorded and further planning needs exploratory results. Report other handoff blockers explicitly.

Project completion requires evidence that its success criteria are met. Closed issues or an empty issue list are
not sufficient. Return the linked project and the verified planning status, changes, available and blocked work,
remaining questions, active-work conflicts, and incomplete updates. Stop after the planning handoff.
