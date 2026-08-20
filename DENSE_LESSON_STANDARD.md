# Dense Lesson Standard

A lesson is a teaching chapter, not a topic label. It must take a learner from “I have never seen this” to “I can explain it, run it, modify it, test it, and state its security limits.” The written lesson is authoritative; exercises measure whether the teaching worked.

## Required teaching sequence

1. **Orientation.** Explain why the idea matters in ordinary programming and why it appears in a cybersecurity engineering course.
2. **Vocabulary.** Define plain-language terms before using precise Python or security terminology.
3. **Problem first.** Show a small problem that the new idea solves. State the input, desired output, and assumptions.
4. **Smallest example.** Present the shortest runnable example and show its expected output.
5. **Syntax and semantics.** Explain each new token, the order Python evaluates it, the resulting values and types, and what changes when an input changes.
6. **Worked variations.** Add several examples that vary normal input, boundary input, and invalid input. Explain the output rather than only displaying code.
7. **Execution trace.** Walk through at least one example step by step using a table or annotated code.
8. **Common mistakes.** Show realistic beginner mistakes, the observed error or wrong output, and the smallest repair.
9. **Security application.** Apply the concept to synthetic logs, indicators, local files, a resettable service, or another bounded fixture. Distinguish observation from inference.
10. **Design judgment.** Discuss a trade-off, limitation, or alternative implementation. State what the example cannot prove.
11. **Exercises.** End with direct numbered questions and coding tasks that reuse the exact concepts and examples just taught.
12. **Finish line.** State the commands, tests, artifacts, and explanation that demonstrate completion.

## Example density

A fully authored lesson normally contains at least five distinct worked demonstrations when the concept warrants them: the smallest case, a variation, a boundary, an invalid case, and a cybersecurity application. Each runnable demonstration must show expected output or explain why output varies. A simple concept may use fewer examples when its behavior is fully traced; a complex concept should use more.

## Beginner-first rules

Never assume that a learner knows what a terminal, variable, argument, return value, exception, file path, package, process, socket, or trust boundary means. Introduce the term, show it in context, and connect it to something the learner can observe. Do not hide essential steps in a link or say “explore” when the learner needs a concrete action.

Use one new idea at a time. Reuse familiar values before introducing a new domain. Keep code snippets small enough to run and modify. Explain error messages as information about the program’s assumptions rather than as failures of intelligence.

## Security teaching rules

Every security example names its asset, input, trust boundary, authorization, fixture, expected evidence, cleanup, and residual risk. Demonstrations are local, synthetic, bounded, and resettable. The lesson explains the defensive mechanism before showing a failure mode. It never treats a string match, alert, scan, or test result as proof of attacker identity or compromise.

## Completion evidence

A dense lesson must provide a runnable starter, expected output, tests, direct exercises, hints, solutions, and a short proof task. The learner should be able to show a command transcript, test result, or small artifact and explain one edge case without copying the answer.
