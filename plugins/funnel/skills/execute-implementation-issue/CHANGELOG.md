# Changelog

## 0.1.0 - 2026-09-15

- **What**: Add permanent implementation execution with agreed verification criteria, acceptance tests, explicit
  plan approval, red-green-refactor, and completion evidence. Include prerequisite and parent scope checks,
  rollback expectations, resumed-work evidence, Git skill handoffs, and delivery status requirements. Use the
  interview skill to establish the verification agreement, with one approval for the complete summary and plan.
  Enter harness plan mode when supported and permitted, and retain the approval gate when it is unavailable.
- **Why**: Establish how correctness will be proved before implementation begins.
- **Evidence**: The user requested an execution skill based on the supplied workslop guidance without direct tool
  references, then requested a review of the other repository skills, an explicit interview skill reference,
  and use of harness plan mode where applicable.
- **Impact**: The shared plugin can guide implementation execution across hosts. Implementation waits for user
  approval of the tests and plan, and completion requires the agreed evidence and delivery steps. The interview
  procedure is reused without a second approval of the same plan. Supported harnesses use plan mode until approval.
- **Reference**: User-provided workflow requirements and the repository's planning, breakdown, issue-writing,
  execution, interview, and Git skills reviewed in this session.
