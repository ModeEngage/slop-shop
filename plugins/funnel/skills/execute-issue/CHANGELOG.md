# Changelog

## 0.1.0 - 2026-09-15

- **What**: Add issue execution routing from exact `slop:` labels or standalone description markers to four execution skills.
  Require clarification for missing, unknown, conflicting, or inconsistent types.
- **Why**: Provide one entry point for executing a typed issue without duplicating execution workflows.
- **Evidence**: The user requested routing from labels or description text and confirmed four namespaced `slop:` markers.
- **Impact**: An agent selects and runs the matching skill while preserving its approval and completion requirements.
- **Reference**: This session's routing request and the repository's issue type conventions and execution skills.
