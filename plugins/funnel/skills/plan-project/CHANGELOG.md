# Changelog

## 0.1.1 - 2026-09-17

- **What**: Move detailed content, dependency, replanning, verification, and handoff procedures into three linked
  references. Keep context setup, core planning rules, and reference loading instructions in SKILL.md.
- **Why**: Reduce the main skill prompt size without removing planning requirements.
- **Evidence**: The user reported that Codex truncated the plan-project main prompt. SKILL.md was 9,897 bytes.
- **Impact**: Detailed procedures load at the relevant planning stage. The main prompt retains scope, authorization,
  implementation readiness, and completion rules.
- **Reference**: This session's truncation report and the skill-creator guidance on progressive disclosure.

## 0.1.0 - 2026-09-15

- **What**: Add a draft recurring project planner for new, empty, and existing Linear projects. Define project context,
  issue selection, dependencies, replanning, cancellation records, planning exit criteria, and a planning handoff.
  Name the separate implementation breakdown skill and load it only for an actual breakdown task.
- **Why**: Develop vague ideas into decided implementation work as exploratory findings become available.
- **Evidence**: The user confirmed the design through an interview and requested explicit planning exit criteria.
  The user requested that implementation breakdown instructions stay out of project planning context.
- **Impact**: The planner maintains project-level issues without executing work or creating sub-issues. Unclear work
  remains in the project description until it can be assigned. Handoffs distinguish completed planning, planning that
  awaits findings, and project completion. Project planning does not load the implementation breakdown skill.
- **Reference**: This session's confirmed design; the user's `project-planner` and `linear-wayfinder` skills;
  the bundled `write-issues` and `interview` skills.
