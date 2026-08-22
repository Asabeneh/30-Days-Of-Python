# Safety and Lab Rules

Cybersecurity knowledge is powerful because it can protect systems and because it can cause harm when used without permission. This course teaches a professional habit before it teaches a security tool: **define authorization, scope, expected behavior, evidence, and cleanup before you run anything**.

## The authorization rule

You may test only systems, applications, accounts, networks, data, and services that you own or for which you have explicit permission. “It is public,” “I found it in a search result,” “I was curious,” and “the tool allowed me to do it” are not authorization. When a lab offers a target, use that target exactly as documented. When the scope is unclear, stop and ask an instructor or system owner.

## The default lab boundary

The default course labs use local fixtures, loopback addresses, synthetic logs, intentionally vulnerable applications supplied by the course, or explicitly authorized training platforms. They do not require scanning the public internet, testing university systems, guessing real credentials, bypassing access controls, deploying persistence, evading detection, disrupting availability, or collecting private data.

| Before a lab | During a lab | After a lab |
| --- | --- | --- |
| Read `lab/scope.md`; identify the owner, target, permitted actions, time window, data, and stop conditions. | Use the smallest test that answers the question. Rate-limit requests and keep a record of commands, timestamps, inputs, and outputs. | Reset fixtures, delete temporary credentials, remove collected data, preserve only approved evidence, and write what happened. |

## Security examples in this course

Some lessons show a vulnerable pattern so that the learner can recognize and fix it. Vulnerable examples must be isolated, clearly labeled, local, and non-destructive. The exploitation demonstration must be the minimum needed to prove the vulnerability. The preferred exercise is a regression test that fails before the fix and passes afterward.

The course will not provide instructions for credential theft, unauthorized access, persistence on real systems, destructive payloads, malware deployment, stealth or evasion, public-target scanning, or bypassing safety controls. Advanced topics such as malware analysis are taught with benign samples, static reasoning, and sandbox concepts.

## Evidence and privacy

Treat logs, packet captures, usernames, browser artifacts, and files as potentially sensitive even when they are synthetic. Do not upload private evidence to public websites or paste it into external assistants. Use hashes to record integrity, minimize collection, record provenance, and delete data according to the lab's retention instructions.

Separate an **observation** from an **inference**. “The fixture contains three failed logins” is an observation. “The user account was compromised” is an inference that requires more evidence. State confidence and limitations in every incident or assessment report.

## Stop conditions

Stop immediately if a target leaves the documented scope, a tool produces unexpected load, real personal data appears, credentials you do not own are exposed, a service becomes unstable, or you are unsure whether an action is permitted. Preserve the minimum safe evidence, clean up if it is safe to do so, and report the uncertainty. Do not continue merely because a command has already started.

## Reporting a safety concern

Open an issue using the safety template or contact the course owner privately. Include the lesson, the exact file or command, why it may be unsafe, and a safer replacement if you have one. Never include secrets or private evidence in the issue.

## Professional standard

A strong security engineer can explain not only **how** a technique works, but also when it is appropriate, who authorized it, what it might break, what evidence it produces, and how to undo it. That judgment is part of the curriculum, not an optional disclaimer.
