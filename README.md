# Python for Cybersecurity Engineering

Welcome to a **beginner-first, Python-centered cybersecurity engineering course**. This repository is designed for a learner who has never written code before and wants to build the programming, systems, networking, secure-development, defensive, investigative, and professional skills needed for continued cybersecurity study.

This is not a 30-day challenge and it is not a promise that reading lessons alone creates a professional security engineer. It is a **120-day core pathway** with six optional specialization tracks. Each day asks you to read, run, change, practise, test, explain, and reflect. The course uses Python as the main instrument while teaching the broader foundations that make security automation useful.

> **Safety rule:** Only run security tests against systems, applications, data, and accounts that you own or have explicit permission to test. The default labs are local, synthetic, bounded, and resettable.

## Start here

If you have never programmed before, follow these files in order:

1. [Setup from zero](SETUP.md) — install Python, Git, VS Code, and the recommended extensions.
2. [VS Code setup](VS_CODE_SETUP.md) — configure the editor, interpreter, debugger, tests, and Markdown workflow.
3. [Safety and lab rules](SAFETY_AND_LAB_RULES.md) — learn authorization, scope, evidence handling, and cleanup.
4. [Day 1](day_1_setup_and_safe_practice/day_1_setup_and_safe_practice.md) — run your first Python program and your first safe cyber exercise.
5. [Curriculum guide](CURRICULUM_GUIDE.md) — understand the 120-day sequence and project checkpoints.
6. [Complete day index](DAY_INDEX.md) — jump directly to any of the 120 lessons.
7. [LeetCode guide](LEETCODE_GUIDE.md) — build problem-solving fluency without confusing puzzles with security engineering.
8. [Resources](RESOURCES.md) — use official documentation and authorized training labs effectively.
9. [Video resources](VIDEO_RESOURCES.md) — use inline and optional YouTube segments with exact timestamps.

## Contents

- [Start here](#start-here)
- [The daily learning loop](#the-daily-learning-loop)
- [Course map](#course-map)
- [Complete 120-day curriculum](DAY_INDEX.md)
- [What counts as progress](#what-counts-as-progress)
- [Repository standards](#repository-standards)
- [Specialization tracks](specializations/README.md)
- [Resources](RESOURCES.md)
- [Video resources](VIDEO_RESOURCES.md)
- [Safety and lab rules](SAFETY_AND_LAB_RULES.md)

The [complete day index](DAY_INDEX.md) remains the authoritative table of contents for all 120 lessons. Each lesson also contains its own **Table of contents** with links to every major topic, example, exercise, and reference section.

## The daily learning loop

Every day follows the same evidence-based loop. Read the prerequisites and outcomes. Run the starter without changing it. Trace what happened. Change one small thing and predict the result before running again. If the lesson includes a video, watch only the timestamped segment after attempting the local example, then return to the written practice. Answer the numbered exercises from a blank file where the question asks you to write code. Use hints only after a real attempt, and solutions only to compare decisions. Run the checks. Explain the mental model aloud or in writing. Record one edge case, failure mode, or security trade-off.

## Course map

| Phase | Days | Focus | Checkpoint |
| --- | ---: | --- | --- |
| 1 | 1–10 | Computing, Python, and safe cyber practice | Environment proof and triage classifier |
| 2 | 11–20 | Reliable Python security tools | Log Triage CLI |
| 3 | 21–30 | Professional engineering and data boundaries | Secure Evidence Journal |
| 4 | 31–40 | Operating systems and systems automation | Host Baseline Auditor |
| 5 | 41–50 | Networking and protocols | Local Network Service Monitor |
| 6 | 51–60 | Secure Python and applied cryptography | Tamper-Evident Case Bundle |
| 7 | 61–70 | Web services and application security | Secure Local Case Management API |
| 8 | 71–80 | Defensive automation and detection | Mini Detection Pipeline |
| 9 | 81–90 | Incident response and digital forensics | Synthetic Breach Investigation |
| 10 | 91–100 | Authorized security testing | Local Assessment Package |
| 11 | 101–110 | DevSecOps, cloud concepts, and supply chain | Secure Delivery Pipeline |
| 12 | 111–120 | Engineering judgment and capstone | Portfolio-ready capstone |

After Day 120, choose a specialization from the [specialization index](specializations/README.md): blue team, application security, digital forensics and incident response, malware-analysis foundations, cloud DevSecOps, or network security.

## What counts as progress

A day is complete when you can run its starter, pass its acceptance checks, explain its mental model, complete the core practice, and name an edge case. A project is complete when it includes working code, tests, setup instructions, a threat model, sample evidence, limitations, and a retrospective. The goal is not to collect completed pages. The goal is to build **reliable evidence of understanding**.

## Repository standards

The course quality contract is documented in [COURSE_QUALITY_STANDARD.md](COURSE_QUALITY_STANDARD.md), the actual teaching requirements are in [DENSE_LESSON_STANDARD.md](DENSE_LESSON_STANDARD.md), and the beginner-facing page structure is defined in [BEGINNER_TUTORIAL_STANDARD.md](BEGINNER_TUTORIAL_STANDARD.md). Use [TROUBLESHOOTING.md](TROUBLESHOOTING.md) when a command fails. Contributors should read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). The repository's course doctor checks structure, links, safety documents, and required learner files.

## License and provenance

This redesign keeps useful Python teaching knowledge while replacing the inherited course shell with a focused cybersecurity curriculum. The original repository history remains available through Git, while the working tree is intentionally limited to the redesigned course and its supporting materials. Attribution and license obligations are preserved in the repository history and in the migration notes where source material has been substantially rewritten.
