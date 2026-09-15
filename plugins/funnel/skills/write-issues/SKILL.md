---
name: write-issues
description: Draft, revise, or create Linear issues for permanent implementations, prototypes, research, and interviews, with clear assignments and appropriate metadata.
---

# Writing Linear Issues

Write clear, actionable Linear issues. Use shared guidance here and load only the reference for the selected type.

## Workflow

1. Gather context from the conversation, repository, and relevant Linear work.
2. Select the issue type and read its reference. Default to permanent implementation unless the request indicates
   another type. Ask only when ambiguity would materially change the assignment.
3. Resolve gaps or conflicts that prevent a confident draft. Otherwise, state material assumptions with the draft.
4. Draft the issue and check it against shared and type-specific guidance.
5. Present the draft and incorporate feedback.
6. When asked to create the issue, create it with the supported title, description, and metadata. Return its identifier
   and link. Ask for confirmation only when unresolved content or metadata could materially change the issue.

Drafting an issue does not authorize execution of its assignment or changes to a linked project.
Before revising an issue in Linear, read [references/update-existing-issue.md](references/update-existing-issue.md).

## Issue Types

| Type | Use when the intended result is | Read |
| --- | --- | --- |
| Implementation: permanent | A decided product change that will complete the full software development life cycle | [Permanent implementation](references/permanent-implementation.md) |
| Implementation: prototype | A rough artifact used to collect feedback and refine a concept | [Prototype](references/prototype.md) |
| Research | Answers to questions investigated by an agent without a human in the loop, using facts from the environment or internet | [Research](references/research.md) |
| Interview | Refinement of a concept, design, or idea through dialogue using the interview skill | [Interview](references/interview.md) |

The type references define issue-writing guidance. Research, prototype, and interview assignments name the skill
that executes the work. Their output formats load only when writing or updating the selected issue type.

### Execution Markers

Select exactly one execution marker for the issue:

| Issue type | Marker |
| --- | --- |
| Implementation: permanent | `slop:implementation` |
| Implementation: prototype | `slop:prototype` |
| Research | `slop:research` |
| Interview | `slop:interview` |

Include the exact lowercase marker on a standalone line in the draft description. When creating or updating the
issue, use the matching existing issue label when available. The description line can be omitted when that label
is applied. If no matching label exists, keep the description marker; do not create labels without user direction.

The [execute-issue](../execute-issue/SKILL.md) skill routes from these exact labels or standalone description markers.
If both are present, they must agree. Resolve conflicting markers before saving the issue. Generic type names,
`Issue type:` lines, and attachments alone do not provide an execution marker. Preserve unrelated labels.

## Linear Context

Read [references/linear-context.md](references/linear-context.md) when the user references an existing Linear issue,
project, or initiative, provides an identifier or URL, or asks to find related work. Do not load it for drafts based
only on the conversation or repository.

## Issue Context and Scope

Use the available conversation, Linear context, and codebase before asking questions. If the issue can be drafted
confidently, proceed without clarification questions.

When a relevant repository is available, inspect code, tests, and documentation when they can confirm current behavior,
locate a defect, or reveal constraints and prior art. Include stable code links in the relevant context section when possible.

Draft at the scope of the meaningful deliverable, not the latest incidental change. Keep independently deliverable
prerequisites in separate, related issues.

If necessary, ask one focused question at a time for missing information needed to establish:

- The current problem or behavior
- The desired observable outcomes
- Scope boundaries and affected users or systems
- Relevant constraints, dependencies, and relationships
- Required metadata

Separate confirmed facts from assumptions. Resolve material conflicts before continuing; otherwise surface material
assumptions with the draft.

## Writing Guidelines

### Audience

Write the title, problem statement, and assignment so readers outside the domain can understand them. Define unfamiliar
domain terms when needed. Technical context may use domain-specific terminology for the people doing the work.

### Writing Style

- Prefer plain, precise language based on ASD-STE100 Simplified Technical English principles
- Use short, direct sentences and consistent terminology
- Prefer active voice and name the actor when it is relevant
- Avoid idioms, unnecessary jargon, and ambiguous wording
- Use a technical term only when replacing it with general language would make the requirement less precise, obscure the
  affected component, or change its meaning
- Define terms that engineers outside the domain may not recognize; definitions are not needed for code symbols, product
  names, or standard industry terms when their meaning is clear from context

### Section Guidelines

**Title:**

- Value-focused; include only technical names needed to identify the affected system or behavior
- Use simple action verbs appropriate to the type, such as "Add", "Compare", "Investigate", or "Refine"
- Use plain, precise language

**Problem Statement:**

- **Length**: 1-4 sentences
- **Content**: State the core problem and only the context or impact needed to understand it
- **What to exclude**: Proposed solutions and background that does not help explain the problem
- **Formatting**: Use backticks for code/tool names (e.g., `manifest-renderer`, `eks.amazonaws.com/role-arn`)
- **Tone**: Direct and factual
- Example: "`manifest-renderer` adds the IRSA annotation whenever there's an IAM role configured, but this is not needed for Pod Identity authentication."

**Intent (optional):**

Explain why the human requested the work, using their stated purpose or motivation. The Problem Statement describes
what the problem is; Intent adds meaningful context about why the human wants it addressed. Include Intent only when
it adds information not already covered by the Problem Statement. Do not invent motivation.

**Type-specific sections:**

Use the selected reference. Do not impose implementation Acceptance Criteria on exploratory issues. Include
Completion Criteria only for additional requirements not already implied by the assignment.

When the repository is known, append `[repo=owner/repository]` as the final description line.

## Metadata Guidelines

Use established team and project conventions when available. Inspect available metadata before applying defaults, and ask
the user when a material choice cannot be inferred.

**Labels**:

- Apply existing labels that identify the product area, repository, or issue type when their meaning is established
- Do not create or assume new labels without user direction

**Priority**:

- **Urgent (1)**: A critical bug that blocks users, operations, or committed work and needs immediate attention
- **High (2)**: High-impact bugs and committed work, including OKR-related work
- **Medium (3)**: Impactful but uncommitted work, including most new functionality
- **Low (4)**: Optional improvements, cleanup, or refactors with no near-term commitment

**Relationships**:

- Use a parent relationship when the issue is a scoped part of a larger deliverable
- Use `blocks` or `blocked by` only when one issue cannot proceed without the other
- Use `related` when issues share useful context but have no dependency
- Use `duplicate` when both issues describe the same required outcome

**Initial state**:

- Use the established state for the team and issue type
- If no convention can be inferred, suggest **Triage** for bugs or **Backlog** for new functionality only when that state
  exists; otherwise ask the user

## Findings

For prototype, research, and interview issues, read [references/findings.md](references/findings.md). Include its
recording requirements in the assignment so a later agent can discover them without this writing skill.

Interview assignments must explicitly require the execute-interview-issue skill, which uses the generic interview skill.
Research assignments must explicitly require the execute-research-issue skill.
Prototype assignments must explicitly require the execute-prototype-issue skill.

## Validation Checklist

Before finalizing, verify:

- The type is clear and its reference was used.
- Exactly one execution type is declared by a supported `slop:` label or standalone description marker; both agree
  when present.
- The Problem Statement describes the problem and necessary context, not a solution.
- Intent, when present, explains the human's reason for requesting the work without inventing motivation or repeating
  the Problem Statement.
- The assignment and any additional completion requirements are supported by the available context.
- Exploratory assignments include findings-recording requirements and any required execution skill.
- Metadata and relationships follow established conventions.
- The repository tag is the final description line when the repository is known.
