# Prototype Issue Output Format

```markdown
Title: [Concept or behavior to prototype]

Description:

slop:prototype

Use the `execute-prototype-issue` skill to build the artifact and collect feedback.

## Problem Statement

[1-4 sentences: The problem or uncertainty and the context needed to understand it]

## Intent

[Optional: why the human requested this prototype, based on their stated purpose or motivation]

## Prototype and Feedback

[What people need to react to and what their feedback should clarify]
[Feedback audience, when known]

## Constraints

- [Optional: known scope, effort, fidelity, or iteration limit]

## Completion Criteria

- [Optional: additional requirement specific to this assignment]

## Findings

Attach a Markdown document containing the artifact link, collected feedback, the human's iteration or completion decision,
what was learned, and unresolved questions to this issue. Keep the assignment intact. If this issue belongs to a project,
check its description for an explicit reference to this issue. Update that entry with a short outcome and a link to this
issue; keep detailed findings in the attachment and preserve unrelated project content.

[repo=owner/repository]
```

Problem Statement, Prototype and Feedback, and the findings-recording instructions are required. Omit Intent,
Constraints, and Completion Criteria when they add no information. Do not invent feedback or findings when drafting.

Omit the marker line only when the matching `slop:prototype` issue label is applied. Omit the repository tag when unknown;
otherwise, keep it as the final description line.
