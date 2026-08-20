# Exercise Standard

Every lesson ends with a question-driven `## Exercises` section. The exercise is an assignment the learner can start immediately, not a request to invent an assignment.

## Required shape

Each `practice/exercises.md` file contains a numbered sequence of questions and tasks in the same order as the lesson. The preferred sequence is:

1. **Try the examples.** Run the starter or the exact example from the lesson and record the output.
2. **Check understanding.** Answer one or two short questions about values, control flow, data shape, or the execution trace.
3. **Write code.** Implement a concrete function, command, parser, transformation, or test using supplied input.
4. **Apply to security.** Use synthetic events, local fixtures, or a resettable lab to make the concept useful for cybersecurity.
5. **Handle an edge case.** Add a boundary, malformed input, failure path, or negative test.
6. **Challenge yourself.** Extend the task only after the required questions are complete.

The sequence may be shorter or longer when the concept requires it, but every question must be specific enough that a beginner knows what to create and what evidence to produce.

## Question-writing rules

Use numbered Markdown questions such as “1. Run …”, “2. What does … return?”, “3. Write a function that …”, and “4. Test what happens when …”. Name the input, output, fixture, limit, or expected behavior. Ask for a printed value, return value, file, test, table, or explanation when that artifact matters.

Do not use vague instructions such as “explore this topic”, “build something useful”, or “be creative” without a concrete acceptance condition. Do not make the learner translate a level label into an assignment.

## Security exercise rules

Security tasks must identify the target as local, synthetic, authorized, and bounded. They must say what the learner may inspect or change, what evidence to save, and what the exercise cannot prove. Never use real credentials, private logs, public targets, university systems, or employer systems as practice input.

## Answer-key rules

`hints.md` should follow the exercise numbers and provide a small nudge without solving the task. `solutions.md` should follow the same numbers, show a reasonable implementation or reasoning path, and explain why the answer satisfies the acceptance condition. A solution is not required to use the same variable names as the learner.

## Assessment mapping

A lesson is complete when the learner can answer the understanding questions, produce the requested artifact, pass the relevant tests, and explain one edge case or limitation. The questions are the assessment surface; the starter and tests are supporting evidence.
