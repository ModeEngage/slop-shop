# Project and Issue Content

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

Use [write-issues](../../write-issues/SKILL.md) for issue bodies, type-specific requirements, metadata, and findings
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
