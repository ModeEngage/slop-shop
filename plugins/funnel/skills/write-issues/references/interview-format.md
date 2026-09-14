# Interview Issue Output Format

```markdown
Title: [Concept, design, or idea to refine]

Description:

Issue type: Interview

Use the `execute-interview-issue` skill to conduct the interview and record its findings.

## Problem Statement

[1-4 sentences: The ambiguity or decision and the context needed to understand it]

## Intent

[Optional: why the human requested this interview, based on their stated purpose or motivation]

## Concept to Refine

[The concept, design, or idea and its known boundaries]
[Relevant settled decisions and open questions, when known]

## Constraints

- [Optional: known constraint affecting the discussion]

## Completion Criteria

- [Optional: additional requirement specific to this assignment]

## Findings

Attach a Markdown document containing the human-confirmed synthesis, including decisions, accepted tradeoffs, constraints,
assumptions, and unresolved questions, to this issue. Keep the assignment intact. If this issue belongs to a project,
check its description for an explicit reference to this issue. Update that entry with a short outcome and a link to
this issue; keep detailed findings in the attachment and preserve unrelated project content.

[repo=owner/repository]
```

Problem Statement, Concept to Refine, and the findings-recording instructions are required. Omit Intent, Constraints,
and Completion Criteria when they add no information. Do not invent decisions or a confirmed synthesis when drafting.

Use an established type marker instead of the fallback line when available. Omit the repository tag when unknown;
otherwise, keep it as the final description line.
