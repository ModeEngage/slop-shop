---
name: execute-issue
description: >-
  Classify an issue from its labels or an explicit type marker in its description, then execute it with the matching
  permanent implementation, prototype, research, or interview skill. Use when asked to execute an issue without
  selecting its execution skill; not to write issues, plan a project, or dispatch multiple issues.
---

# Execute an Issue

Route one assigned issue to its execution skill. Classification selects the workflow; the selected skill controls
execution, approval, verification, findings, and completion.

## Read and Classify

Resolve the target issue from the user's request and available context. Read its current labels and full description,
including the assignment and relevant linked context. Ask for the target if it cannot be identified.

Use an issue label or explicit label-shaped text in its description to select exactly one type:

| Type marker | Execution skill |
| --- | --- |
| `slop:implementation` | [execute-implementation-issue](../execute-implementation-issue/SKILL.md) |
| `slop:prototype` | [execute-prototype-issue](../execute-prototype-issue/SKILL.md) |
| `slop:research` | [execute-research-issue](../execute-research-issue/SKILL.md) |
| `slop:interview` | [execute-interview-issue](../execute-interview-issue/SKILL.md) |

Accept an exact lowercase marker as an issue label or as the full text of a standalone description line, with
surrounding whitespace ignored. Do not infer aliases or accept generic type names, `Issue type:` lines, bracketed
tags, or label fields as substitutes.

Read markers as declarations about the target issue. Do not classify from incidental words in prose, quoted examples,
code samples, linked issue titles, or labels for unrelated concerns such as priority or product area. An unknown
`slop:` marker needs clarification; unrelated labels do not affect routing.

Compare all applicable labels and description markers. Matching declarations select one type. If declarations conflict,
the marker is missing or unknown, or the assignment contradicts the declared type, explain the ambiguity and ask the
user which type applies. Do not guess from the title, default to permanent implementation, or silently prefer a label
over the description. A user's explicit resolution selects the route without requiring a metadata edit.

## Execute the Selected Workflow

State the selected type and the label or description marker that supports it, or the user's clarification. Load and
use only the selected execution skill from the table. Continue with its workflow; do not stop after recommending it.
If that skill is unavailable, report the missing skill and stop before execution.

Carry forward the complete assignment, scope, acceptance or completion criteria, constraints, dependencies, and
relevant decisions. Do not replace the assignment with a classification summary. Follow the selected skill's gates;
classification and a request to execute do not substitute for its required plan approval or human feedback.

Keep issue metadata unchanged unless the user requests a correction. Do not execute sibling issues, dispatch agents,
or close the issue merely because routing succeeded. Report the selected workflow's actual outcome and any pending
requirements under its completion rules.
