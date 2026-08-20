# Course Quality Standard

A lesson is not complete because it names a Python feature or a security tool. It is complete when a learner can **explain, predict, practise, apply, test, and communicate** the idea safely.

## Every lesson must contain

1. A title, previous/next navigation, and a table of contents when the lesson has several sections.
2. Prerequisites written for a beginner, including the exact earlier day to revisit when needed.
3. Observable outcomes using verbs such as explain, trace, write, test, compare, or document.
4. The practical problem the concept solves before the syntax or tool appears.
5. A small runnable starter with expected output and an execution trace.
6. Plain-language terminology followed by precise technical vocabulary.
7. At least one common mistake, its symptom, and the smallest correction.
8. Three practice levels: mechanical, applied, and creative or investigative synthesis.
9. Separate `practice/hints.md` and `practice/solutions.md`; the reading flow must not reveal full answers.
10. A one-sentence mental model, a finish line, and a short proof section.

## Additional security requirements

Security-heavy lessons must also state the trust boundary, authorization and scope, threat or failure being studied, safe fixture or target, expected evidence, cleanup or reset procedure, and residual risk after the mitigation. Offensive demonstrations must be local, synthetic, bounded, and no more powerful than necessary to teach the defensive idea.

## Practice standard

Each exercise states the starting input or state, expected output or acceptance criterion, concepts already available, and a progressive hint route. A solution explains the decision, not only the final code. Level 1 practice builds fluency. Level 2 practice applies the concept to a security-relevant utility. Level 3 practice asks for design judgment, edge cases, evidence quality, or a stretch algorithm.

## Technical verification standard

Before a day is accepted:

- its starter runs with the documented command;
- its tests pass and include at least one meaningful negative or edge case;
- its links resolve or are marked as intentionally optional;
- its relative navigation is correct;
- its examples agree with its explanation;
- its security lab has a scope and reset instruction where applicable;
- no secret, private evidence, or destructive payload is included;
- its Markdown is readable and its code is formatted;
- its solution is not embedded in the practice prompt; and
- a beginner can identify what success looks like.

## Completion definition

The course is complete only when the root setup, all 120 days, all projects, specialization entry points, resource guide, LeetCode route, safety rules, and repository checks agree with one another. Completion does not mean professional mastery; it means the repository provides a coherent, testable, honest foundation for continued study and supervised practice.
