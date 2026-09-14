---
name: interview
description: Interviews the user in rounds of questions to refine a plan, decision, or idea until no consequential question remains. Use when the user asks to be interviewed or questioned about a plan, or to work through a decision interactively. Not for written critique alone or job interview practice.
---

# Interview

Interview the user about a plan, decision, or idea until no answerable consequential question remains.

## Terminology

- **consequential question**: a question whose answer can materially change the result, such as by changing a
  decision, revealing a constraint, changing a risk assessment, or altering the scope or next action.
- **decision tree**: collection of interview questions with clear dependencies; each answer either clarifies and
  unblocks questions further into the tree or renders them inconsequential and thus not needing to be answered.
- **frontier**: all questions in the tree with settled prerequisites; no blockers remain to composing an informed answer
  for all questions at the frontier of the decision tree.

## Interview Mechanics

Map the problem space into a decision tree. Ask up to five questions from the frontier per round. Prioritize
questions that settle major decisions or remove dependent questions.

A question whose answer depends on another unanswered question belongs to a later round. Each question covers one
decision and gets a unique identifier across the interview. A question that you ask again keeps its identifier.
Only include consequential questions in the decision tree.

When a decision involves a material tradeoff, explain which goals or constraints compete and what the viable options
gain, give up, or put at risk. Use the user's stated priorities to frame the comparison. If those priorities do not
resolve the choice, ask the user which outcome matters more or which cost is acceptable. Apply priorities that the
user has already established without asking again. Distinguish known consequences from uncertain ones. Do not invent
tradeoffs or present options as equally suitable when the evidence favors one.

State the question without implying a preferred answer. If you recommend an answer, explain why it fits the user's
stated goals and constraints, and what the user would give up or accept by choosing it. Include a meaningful alternative
when it helps explain the tradeoff. You can omit a recommendation for any reason, including insufficient facts or
user preferences. Do not invent a recommendation that the available facts or user preferences do not support.

Write each round as text in the format below. Omit the ➡️ line when you do not recommend an answer.

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <recommended answer, why it fits, and the main tradeoff; include an alternative when useful>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <recommended answer, why it fits, and the main tradeoff; include an alternative when useful>

---

```

Each answer can settle a decision, unblock dependent questions, or remove questions that no longer apply. If the user
does not answer a question, keep it open; do not treat your recommendation as accepted. When the user changes an
answer, revisit dependent decisions and reassess questions that the previous answer removed. After each round,
recompute the frontier and ask the next round of questions.

## Fact-finding

The agent is responsible for finding facts. The user is responsible for decisions. Ask the user for facts that
you cannot obtain with available tools.

Prefer sub-agents for fact-finding so research can run while the interview continues. Use a direct lookup when it
can resolve the question faster than delegating it. If sub-agents are unavailable, investigate directly.

A question that depends on pending research is not part of the frontier. Continue with independent questions while
research is pending. When findings arrive, update the dependent questions and recompute the frontier. If a required
fact remains unavailable after asking the user, record the gap and its effect on the decision.

## Success Criteria

Continue the interview while an answerable consequential question remains. If a consequential question cannot be
answered, record the unknown and its effect. Treat it as a blocker only if it prevents the next action. Otherwise,
state the assumption under which work can proceed.

Before ending the interview, summarize the agreed result, decisions, accepted tradeoffs, constraints, assumptions,
and unresolved blockers. Do not act on the results of the interview until the user confirms the summary.
