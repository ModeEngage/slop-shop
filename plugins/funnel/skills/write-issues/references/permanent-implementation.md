# Permanent Implementation

Use for a decided unit of work intended to complete the full software development life cycle and become part of a
product. Establish valid Acceptance Criteria. Do not treat an unresolved concept as a decided implementation.

Treat a change as high-risk when failure could cause:

- Data loss or corruption
- A security or access-control failure
- A production outage or broad service degradation
- A difficult or irreversible migration

For high-risk changes, clarify rollback expectations when they are not already established.

## Section Guidelines

Use the shared Problem Statement and optional Intent guidance from SKILL.md.

**Acceptance Criteria:**

- **Structure**: Flat bullet lists by default
  - Use nested bullets when showing alternative behaviors or modes (e.g., "IRSA: does X" vs "Pod Identity: does Y")
  - Use nested bullets for complex technical validation steps with sub-checks
  - Don't nest for simple sub-points — integrate them into the parent bullet
- **Content**: Clear outcomes anyone can verify ("System supports X", "Service renders Y correctly")
- **Coverage**: Include relevant modes, defaults, exceptions, and runtime behavior
- **Clarity**: Apply the shared technical-term guidance in SKILL.md and define unfamiliar terms; put other technical detail in
  Implementation Details
- **No Repetition**: Don't repeat information already stated in Problem or Implementation Details
- **Formatting**: Use "backwards compatible" (not "backward compatible")
- Every criterion should be verifiable and outcome-focused, not task-based

**Implementation Details (when useful):**

- **Purpose**: High-level evidence, constraints, and pointers, not a prescribed solution
- **Structure**: Flat bullet lists — avoid creating subsections (no "References:", "Rollback plan:", etc.)
  - Exception: Complex migrations may benefit from labeled sections, but keep minimal
- **What to include**:
  - GitHub permalinks to relevant code (single line like L35 or range like L35-L36)
  - File paths that need changes (link to files for general references, specific lines for problematic code)
  - Prior art examples or reference implementations
  - Established testing or verification documentation
  - Relevant decision context or evidence, such as related issues, pull requests, design documents, or discussions
  - Known constraints and accepted tradeoffs
  - For a concrete bug, the exact location and a short code excerpt when it helps demonstrate the defect
  - An agreed rollback strategy for a high-risk change
- **What to exclude**:
  - Proposed implementations presented as requirements
  - Code blocks except for a short excerpt that demonstrates a concrete bug
  - Prescriptive "Modify this code to do X" instructions
  - Detailed step-by-step procedures
- **No Repetition**: Don't restate what's already clear from Acceptance Criteria
- Can be domain-specific and technical for experts who'll implement

## Issue Output Format

Use this structure:

```markdown
Title: [Desired value or behavior]

Description:

slop:implementation

## Problem Statement

[1-4 sentences: Direct explanation of what's broken or missing and only the context needed to understand it]

## Intent

[Optional: why the human requested this work, based on their stated purpose or motivation]

## Acceptance Criteria

- [Outcome 1 — system supports/renders/enables something]
- [Outcome 2 — conditional behavior with nested alternatives:]
  - [Mode A: specific behavior]
  - [Mode B: different behavior]
- [Outcome 3 — backwards compatible / tests verify correctness]

## Implementation Details

- [GitHub permalink to relevant code (single line or range L35-L36)]
- [File path that needs changes — high-level pointer]
- [Reference to tests that need updates — file-level link]

[repo=owner/repository]
```

Problem Statement and Acceptance Criteria are required. Include Implementation Details only when useful evidence,
constraints, or pointers are available. If known, append `[repo=owner/repository]` as the final description line.

Read [examples.md](examples.md) only when the user requests an example or the standard format is
difficult to apply to a concrete bug or high-risk migration.

Read [in-progress-work.md](in-progress-work.md) when the issue documents work that has already
started or been completed.

Omit the marker line only when the matching `slop:implementation` issue label is applied.
Omit Intent when it adds no context.

## Validation

- Acceptance Criteria are observable outcomes supported by the available context.
- Implementation Details provide useful evidence, constraints, or pointers without prescribing a solution.
- High-risk changes include an agreed rollback strategy.
