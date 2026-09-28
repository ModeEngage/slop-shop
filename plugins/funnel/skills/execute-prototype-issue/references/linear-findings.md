# Prototype Issue Findings in Linear

Read the current issue, including relevant comments and assignment constraints, before building.

Make a code artifact durable in Linear, not in a branch. Attach a source bundle to the issue, for example a `git bundle`
of the local commits that names its required base commit. Also attach run instructions and output snapshots. The
artifact link in the findings points to these attachments.

Write the artifact link, collected human feedback, the human's iteration or completion decision, what was learned,
and unresolved questions in a Markdown document. Attach the document to the issue and keep the original assignment intact.

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
