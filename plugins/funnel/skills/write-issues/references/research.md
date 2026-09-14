# Writing Research Issues

## Purpose

Write an assignment for autonomous investigation of questions. Require the executing agent to use the
`execute-research-issue` skill.
Include a request for a recommendation only when the user asks for one.

## Question Quality and Constraints

Write questions that are specific enough to investigate. During drafting, clarify scope and ambiguous terms when they
could change the answer, so execution can proceed without a live exchange. Do not assume an answer or phrase a question
to require a preferred conclusion.

Include known source, access, environment, or effort limits when they affect the investigation. State them alongside
the relevant question, or in a shared Constraints section when they apply to the whole assignment. These limits are
optional. Do not invent them or require the user to supply limits that are not needed for a clear assignment.

## Issue Output Format

Read [research-format.md](research-format.md) only when writing or updating a research issue.

## Validation

- Questions are specific enough to investigate, with material ambiguity resolved and no preferred conclusion assumed.
- The assignment requires the `execute-research-issue` skill and supports autonomous execution without a live human exchange.
- Relevant known limits are stated without invented constraints or repeated requirements.
- Recommendations are included in the assignment only when explicitly requested.
- The assignment requires direct answers, supporting sources or observations, and material uncertainty.
- Completion Criteria state only additional requirements specific to this assignment and allow documented evidence gaps.
- Findings-recording requirements specify a Markdown document attached to the issue and an update to any explicit entry
  in its linked project description.
