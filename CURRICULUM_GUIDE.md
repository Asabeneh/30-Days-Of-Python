# Curriculum Guide

This course is a learning system rather than a playlist. Every day is paired with runnable code, numbered exercises, tests, and evidence of understanding. Read the concept, run the starter, change one line, rebuild a smaller version from a blank file, complete the exercises in order, run the checks, and explain the result.

## The 120-day progression

The sequence moves from programming and computing foundations toward systems, networks, secure software, defensive operations, investigations, authorized testing, delivery security, and engineering judgment. Python is present throughout, but the learner is never asked to use a security tool without first learning the underlying concept it automates.

| Days | Phase | Learner question |
| ---: | --- | --- |
| 1–10 | Start Here | How does a program run, and how do I practise cybersecurity safely? |
| 11–20 | Reliable Python | How do I turn Python syntax into tested, maintainable security utilities? |
| 21–30 | Engineering and data boundaries | How do I make scripts reproducible, typed, observable, and safe around untrusted data? |
| 31–40 | Systems automation | What is the host actually doing, and how can I inspect it without causing harm? |
| 41–50 | Networking | How do connections and protocols behave, and how can I monitor them responsibly? |
| 51–60 | Secure Python and cryptography | How do I protect integrity, secrets, and data boundaries without inventing cryptography? |
| 61–70 | Web and application security | How do I design and test a small service against common application risks? |
| 71–80 | Detection engineering | How do I turn telemetry into useful, explainable, low-noise findings? |
| 81–90 | Incident response and forensics | How do I preserve evidence, reconstruct events, and communicate confidence? |
| 91–100 | Authorized assessment | How do I plan, test, remediate, and retest within explicit scope? |
| 101–110 | DevSecOps and supply chain | How do I make secure engineering repeatable in delivery workflows? |
| 111–120 | Capstone | Can I build, review, explain, and improve a security tool as an engineer? |

## Ten-day phase rhythm

Days 1–8 introduce and practise concepts. Day 9 integrates the phase into a small design or implementation problem. Day 10 is a checkpoint or project day. A learner may take more than one calendar day to complete a lesson; the numbers are sequence markers, not a race.

At every checkpoint, submit a project folder containing a README, setup instructions, tests, sample input and output, threat model, limitations, and retrospective. The checkpoint is also a communication exercise: explain what the tool does, what it does not do, what assumptions it makes, and how you would improve it.

## Choosing specializations

After the core, choose the specialization that matches the type of questions you most enjoy. You do not need to choose a job title now. Spend ten days on one track, review the artifact, and then decide whether to deepen it or try another.

| If you enjoy… | Start with… |
| --- | --- |
| Building alerts, reducing noise, and understanding attacker behavior | [Blue Team](specializations/blue-team/README.md) |
| Finding and fixing flaws in services and APIs | [Application Security](specializations/appsec/README.md) |
| Reconstructing what happened from evidence | [Digital Forensics and Incident Response](specializations/dfir/README.md) |
| Understanding files and suspicious behavior in a safe sandbox | [Malware-Analysis Foundations](specializations/malware-analysis-foundations/README.md) |
| Identity, infrastructure, automation, and delivery pipelines | [Cloud DevSecOps](specializations/cloud-devsecops/README.md) |
| Protocols, traffic, services, and network behavior | [Network Security](specializations/network-security/README.md) |

## Proof before progress

Do not mark a day complete because the page loaded or because a command produced output. A day is banked when you can explain the data flow, pass the relevant checks, make the starter behave differently by changing a controlled input, answer the numbered exercises, and name at least one limitation or edge case.

## Full blueprint

The maintainer-facing rationale, phase tables, repository architecture, resource strategy, and migration decisions are in [COURSE_PLAN_DRAFT.md](COURSE_PLAN_DRAFT.md). The learner-facing files in this repository are the source of truth for the commands and exercises.
