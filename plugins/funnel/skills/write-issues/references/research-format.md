# Research Issue Output Format

```markdown
Title: [Question or knowledge gap to investigate]

Description:

Issue type: Research

Use the `execute-research-issue` skill to investigate the questions below.

## Problem Statement

[1-4 sentences: The knowledge gap and the context needed to understand it]

## Intent

[Optional: why the human requested this research, based on their stated purpose or motivation]

## Research Questions

- [Specific question to answer]
- [Additional question, if needed]

## Constraints

- [Optional: known source, access, environment, or effort limit]

## Completion Criteria

- [Optional: additional requirement not implied by the research questions]

## Findings

Attach a Markdown document containing answers, supporting sources or observations, and material uncertainty to this
issue. For unresolved questions, include the evidence gap and what would be needed to answer them. Keep the assignment intact.
If this issue belongs to a project, check its description for an explicit reference to this issue. Update that entry
with a short outcome and a link to this issue; keep detailed findings in the attachment and preserve unrelated project content.

[repo=owner/repository]
```

Problem Statement, Research Questions, and the findings-recording instructions are required. Omit Intent, Constraints,
and Completion Criteria when they add no information. The Findings section states where results must be recorded;
do not invent results when drafting. Include a request for a recommendation only when the user asks for one.

Use an established type marker instead of the fallback line when available. Omit the repository tag when unknown;
otherwise, keep it as the final description line.
