# Beginner Tutorial Standard

The course is written for a learner who may have never programmed before. A lesson must be comfortable to read from top to bottom while remaining easy to scan through its persistent table of contents.

## Required page structure

Every lesson begins with a title, previous and next navigation, and a **Table of contents** linking to every major section and subsection on the page. The table of contents is not decorative: it lets a learner return to a definition, example, exercise, or summary without searching through the entire file.

Every lesson contains an orientation, prerequisites, outcomes, the problem, the security boundary, a **Keywords and terms** section, a separate **Topics** section, worked examples, an execution trace, common mistakes and repairs, guided practice, a bounded cybersecurity application, independent numbered exercises, a finish line, and references. Topics must be named questions or concepts, such as **What is a function?**, **Why are functions useful?**, **What are the parts of a function?**, and **What types of functions can we write?** Longer lessons must never hide all teaching inside one large block called Lesson.

## Required teaching behavior

Introduce one new idea at a time. Define every technical word before relying on it. Prefer ordinary language first, then show the Python term. Explain punctuation, indentation, names, operators, and function calls when they first appear. Show the complete code a learner can copy, the expected output, and a line-by-line explanation of what Python does.

Each major idea has a smallest example, a normal variation, a boundary case, and an intentionally broken example. Before each experiment, ask the learner to predict the output. After execution, explain any difference between the prediction and the result. Treat errors as information about an assumption and show the smallest repair.

## Required practice progression

Exercises progress through three levels without hiding the actual questions. First, the learner reproduces a demonstrated example with different values. Second, the learner modifies a guided example and must predict a changed result. Third, the learner solves a small independent problem using a local, synthetic, bounded cybersecurity fixture. Each lesson provides at least ten numbered questions, hints, solutions, and a proof task.

## Required cybersecurity boundary

A security application names the asset, input, trust boundary, authorization, fixture, expected evidence, cleanup, and residual risk. Examples use only invented values, local files, loopback services, `.invalid` domains, or repository fixtures. A string match, label, scan, or test result is described as an observation or rule outcome, never as proof of attacker identity or compromise.

## Required references

Reference material is included at the point where it helps the learner and repeated in a references section at the end. Official Python documentation is preferred for Python behavior. OWASP, NIST, MITRE, PortSwigger, and reputable educational resources are used for security context. External material supplements the lesson; it never replaces the explanation in the repository.
