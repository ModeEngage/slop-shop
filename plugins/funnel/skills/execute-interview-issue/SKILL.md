---
name: execute-interview-issue
description: Execute a Linear interview issue using the interview skill, then record the confirmed synthesis on the issue and update explicit project entries. Use when asked to work on an interview issue, not to draft one or conduct a general interview.
---

# Execute an Interview Issue

## Context and Interview

Read the current issue and relevant comments. Use its concept, scope, and constraints as the assignment context.

Load and use the `interview` skill for the dialogue, stopping rules, and final summary confirmation. That skill must
be available to execute the assignment. Do not duplicate its interview procedure here.

After the human confirms the final summary, record the synthesis. Do not report the assignment as complete while
confirmation or required recording remains pending.

## Record Findings

Write the confirmed result, decisions, accepted tradeoffs, constraints, assumptions, and unresolved questions in a
Markdown document. Attach the document to the issue and keep the original assignment intact.

If the issue belongs to a project, check the current project description for an explicit reference to the issue. When
one exists, update that entry with a short finding or outcome and a link to the issue. Keep detailed findings in the
attached document. Do not add an entry solely because the issue belongs to the project.

Before replacing an issue or project description, fetch its current content and preserve unrelated edits. Resolve
conflicting changes before writing. Inspect the updated content to confirm the findings were saved.

Verify that the Markdown document is attached to the issue and accessible. A local file alone does not complete this step.
If the document cannot be attached, return it with the reason and keep the issue open until attachment succeeds.

## Close the Issue

After the assignment's completion requirements are satisfied and all required issue and project findings are saved,
close the issue using the team's established completed state. Successful execution does not require a merge request.
Keep the issue open while required work, feedback, confirmation, or recording remains pending.

Verify the final state and return the issue link. If the status update fails, report that closure remains pending.
