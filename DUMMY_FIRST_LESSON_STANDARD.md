# Dummy-First Lesson Standard

## Purpose

This standard replaces revision-note lessons with actual instruction for a learner who has never programmed before. A lesson is not successful because it contains keywords, five code blocks, or a security vocabulary list. It is successful when a new learner can read the explanation, run the examples, predict what will happen, make a mistake safely, repair it, and complete a small task without copying an unexplained solution.

The course may become more advanced as the days progress, but it must never assume that a learner has silently acquired missing foundations. Every new concept must be introduced before it is used, connected to an earlier idea, demonstrated in a small example, and then used in a meaningful cybersecurity context.

## What every lesson must teach

Each lesson must answer the following questions in ordinary language before asking the learner to work independently:

| Teaching question | Required evidence |
| --- | --- |
| What problem are we solving? | A concrete beginner-readable scenario before terminology. |
| What is the new word? | A definition, a non-example, and a connection to a familiar idea. |
| What does the smallest example do? | Code, expected output, and a line-by-line explanation. |
| What changes if one line changes? | At least one deliberate experiment with predicted and observed output. |
| What can go wrong? | A broken example, exact error or wrong output, diagnosis, and repair. |
| How does Python execute this? | A trace showing values, types, and control flow at each important step. |
| Why does cybersecurity care? | A bounded local or synthetic application, not a slogan. |
| What can the learner do alone? | Guided practice followed by independent numbered questions. |
| How do we know learning happened? | A finish line requiring explanation, output, code, and an edge case. |

## Required learner flow

A complete lesson follows this order unless the topic genuinely requires a different sequence:

1. **Welcome and orientation.** Tell the learner what they are about to learn, why it matters, how long the session may take, and what they should already know. Never open with unexplained jargon.
2. **The problem before the solution.** Show a small situation that is difficult or unclear without the new concept. Use a security example only after making the ordinary programming problem understandable.
3. **Vocabulary in plain English.** Define every new term. Use a short analogy only when it is accurate, and immediately connect the analogy back to Python.
4. **The smallest working example.** Start with the fewest lines possible. Show the exact file, the exact command, and the exact expected output.
5. **Line-by-line walkthrough.** Explain what Python reads, what value exists after each line, and what the learner would see. Explain punctuation when it is new.
6. **Second example with one change.** Change one line or one value. Ask the learner to predict the result before revealing it.
7. **Broken example and repair.** Show a realistic beginner mistake. Include the full useful part of the error, translate it into ordinary language, identify the faulty line, repair it, and rerun it.
8. **Guided practice.** Give a partially completed task with explicit steps and checkpoints. The learner should produce something before seeing independent questions.
9. **Cybersecurity application.** Apply the concept to a synthetic fixture, local file, or loopback service. Explain what the concept does and does not prove.
10. **Independent practice.** Use the original course’s numbered-question style. Questions should progress from prediction, to modification, to a small build, to an edge case, to explanation.
11. **Review and finish line.** Ask the learner to explain the mental model in their own words, show working evidence, name one failure mode, and state one safety boundary.

## Minimum content for a normal lesson

A normal lesson must contain enough prose to teach, not merely enough headings to look complete. The minimums below are floors, not targets.

| Component | Minimum |
| --- | ---: |
| Learner-facing explanatory prose | 1,500 words for foundation days; 1,200 words for advanced days, excluding code and navigation. |
| New concepts explicitly defined | 5 for a foundation day; 4 for an advanced day. |
| Fully walked-through code examples | 4, each with expected output and explanation. |
| Short experiments | 3, each with a prediction before execution. |
| Broken-and-repaired examples | 2, each with diagnosis and repair. |
| Execution traces | 2, including one boundary or failure path. |
| Guided practice steps | 1 complete exercise with checkpoints before independent work. |
| Cybersecurity application | 1 concrete bounded application with limitations. |
| Independent questions | 10 or more numbered questions, increasing in difficulty. |
| References | Official Python documentation plus relevant security documentation or a written alternative. |

Project days may use a different balance, but they must teach the project’s architecture, demonstrate each major component, explain the code line by line at least once, and provide a staged build sequence. A project description alone is not a lesson.

## How to explain code

A code block without an explanation is not teaching. Each important block must be followed by four things:

1. **What to type or save.** State the filename and command when relevant.
2. **What Python sees.** Explain literals, names, operators, calls, indentation, and return values that are new to the learner.
3. **What changes in memory or control flow.** Use a table when several values change.
4. **What appears on screen.** Show exact expected output, including the useful portion of an error for broken examples.

Do not explain every character mechanically when that would obscure the idea. Explain every character that a beginner could reasonably misread.

## Practice design

Practice must begin with a task the learner can complete using the immediately preceding explanation. It must not jump from “read this definition” to “build a security tool.” Each exercise file should contain numbered questions in this progression:

| Question group | Learner action |
| --- | --- |
| 1–3 | Predict output and identify values or types. |
| 4–6 | Modify a demonstrated example and explain the change. |
| 7–8 | Write a small program from a precise specification. |
| 9 | Add an invalid, missing, empty, or boundary input. |
| 10 | Apply the concept to a synthetic security fixture. |
| 11+ | Explain a design choice, limitation, or safety boundary. |

Hints should point to the relevant idea without giving the answer. Solutions should explain the reasoning, not merely paste code.

## Beginner language rules

Use short paragraphs and define technical terms at first use. Prefer “Python reads this line and stores the number 7 under the name `severity`” over “this initializes an integer variable.” The latter may be added after the first explanation, with the words defined.

Never write “simply,” “just,” or “obviously” around a step that could confuse a beginner. Never say “you already know” unless the earlier lesson explicitly taught and checked it. Avoid claiming that a security property is guaranteed when the example only demonstrates one small part of it.

## Human review gate

Automated checks can count words and headings, but a human reviewer must answer these questions before a lesson is marked complete:

- Could a learner who has never used the concept follow the first example without opening another page?
- Does every new word have an explanation before it appears in an exercise?
- Are the expected outputs exact and believable?
- Does the broken example teach debugging rather than merely display an error?
- Does the guided practice bridge the lesson to the independent questions?
- Is the cybersecurity application local, synthetic, authorized, and honest about limitations?
- Does the lesson build on the previous day and prepare the next day?
- Would a learner remember a mental model after closing the page?

A lesson that fails any of these questions is not teaching-worthy, regardless of its word count.
