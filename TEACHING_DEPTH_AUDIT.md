# Teaching Depth Audit

## Measured comparison

| Material | Lines | Words | Code fences | Observation |
| --- | ---: | ---: | ---: | --- |
| Original root Days 1–3 material | 526 | 3,104 | 26 | Dense introduction with many examples and explanations |
| Original bundled Days 4–6 | 1,160 | 5,904 | 145 | Multiple concepts, demonstrations, and runnable snippets |
| Original bundled Days 10–12 | 901 | 4,379 | 116 | Functions, modules, and related examples with substantial code |
| Original bundled Days 13–15 | 890 | 4,181 | 80 | Higher-order functions, errors, and exercises |
| Original bundled Days 25–27 | 2,770 | 7,262 | 202 | Data and web material with extensive code and direct tasks |
| Redesigned Day 1 | 145 | 1,232 | 4 | More developed than later redesign pages but still needs richer teaching |
| Redesigned Day 11 | 81 | 611 | 2 | Outline-level explanation, not original-quality teaching |
| Redesigned Day 21 | 81 | 548 | 2 | Setup concept and security framing, but too few worked examples |
| Redesigned Day 31 | 89 | 631 | 2 | Concept summary and safety framing, but too few demonstrations |

## Qualitative findings

The original lessons explain terms in plain language, show multiple runnable examples, display expected outputs, introduce variations, and end with a long numbered exercise set. For example, the original Day 3 exercise section contains nineteen direct tasks involving variables, geometry, slopes, strings, membership, numeric conversion, and type comparison. The redesigned files currently provide a short conceptual explanation, one or two code blocks, a common-mistakes table, and a link to exercises, but many days do not contain enough worked teaching for a complete beginner to build understanding.

The rebuild must therefore increase the explanatory body of each lesson, not merely increase headings or exercise count. A dense day should teach the vocabulary, show the smallest example, trace the example, vary the input, demonstrate the failure case, connect the concept to a security use case, and then assign questions that reuse those exact examples.

## New target

The new minimum for a fully authored core lesson is a substantial explanatory body with at least five distinct worked examples or demonstrations where the concept warrants them, expected output for runnable examples, an execution trace, a common-mistakes table, a security application, a limitations section, and at least ten concrete questions or tasks. The target is pedagogical depth, not an arbitrary word count; complex topics may exceed the minimum and simple topics may use fewer examples when each is fully explained.
