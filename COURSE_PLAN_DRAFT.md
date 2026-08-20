# Python for Cybersecurity Engineering: Curriculum Blueprint

**Status:** Revised draft for approval  
**Audience:** A complete programming beginner entering a university cybersecurity program, plus peers learning with them  
**Proposed scope:** 120-day core course with optional 30-day specialization tracks  
**Repository direction:** Keep the useful Python knowledge; remove the inherited 30 Days of Python presentation and clutter from the active course  
**Author:** Manus AI

## 1. Course promise and honest boundary

This repository should become a **Python-centered cybersecurity engineering pathway**, not merely a Python syntax challenge and not a claim that 120 days alone creates a professional security engineer. The course will take a learner from no programming experience to the point where they can write, test, secure, instrument, and explain useful security software; investigate controlled evidence; automate defensive workflows; assess deliberately vulnerable local applications; and choose a specialization for continued study.

The course will explicitly teach that cybersecurity is broader than one language. Python will be the primary instrument for automation, analysis, services, tooling, and labs, while the learner also develops the operating-system, networking, web, data, cryptography, systems, threat-modeling, and professional communication knowledge that makes Python useful in security work. This breadth is necessary because the NICE Framework describes cybersecurity work through distinct work roles and the knowledge and skills needed to perform them, rather than through one programming language or one job title [1].

The curriculum will not promise a job, a certification, or independent permission to test real systems. All offensive examples will run against local fixtures, intentionally vulnerable applications, synthetic data, or explicitly authorized training targets. Every security lab will state its scope, expected evidence, cleanup steps, and stop conditions.

## 2. Cleanup boundary: preserve knowledge, remove the inherited course shell

The active repository will be redesigned as a coherent Python cybersecurity course rather than presented as a fork of the original challenge. The goal is to preserve useful Python explanations, examples, exercises, and topic coverage as raw teaching knowledge while removing the old course shell, branding, translations, sponsor material, duplicated assets, and inconsistent navigation from the learner-facing experience.

| Preserve as source knowledge | Remove from the active course experience |
| --- | --- |
| Python fundamentals, collections, functions, modules, files, regular expressions, errors, packages, classes, APIs, data handling, and web foundations | The `30 Days Of Python` title, inherited sponsor blocks, sponsor referral links, old challenge badges, and motivational copy that makes unsupported completion or career promises |
| Useful explanations and examples after technical review | Translation directories and duplicated translated READMEs; the redesigned course will have one authoritative English source first, with translation support added deliberately later |
| Original license and attribution obligations where applicable | Legacy screenshots, duplicate image sets, obsolete setup instructions, unused web/database leftovers, stale test images, and files that do not support the new course |
| Git history for provenance and rollback | The old 30-day table of contents and navigation as the default entry point |

The clean repository will resemble the JavaScript/TypeScript course: a single polished curriculum, consistent numbered lesson directories, central setup and quality guides, per-day starters, practice routes, tests, projects, and an index that a new learner can follow from the root. Historical material will remain recoverable through Git history, but translations, sponsor material, legacy assets, and unrelated files will not be carried into the redesigned repository tree.

This cleanup will happen only after an inventory and a preservation check. Before deleting active files, the implementation will extract any useful concept, example, exercise, or attribution into the redesigned lessons or a migration note. The final repository audit will confirm that no old sponsor links, translation navigation, broken inherited paths, or unrelated assets remain in the learner-facing tree.

## 3. Complete first-run setup and learner ergonomics

The course will assume **zero prior programming experience and zero installed developer tools**. Day 1 and the root setup guide will walk through Windows, macOS, and Linux separately where commands differ. The learner will install Python, Git, and Visual Studio Code; verify each installation; clone the course; create a project-local virtual environment; install development dependencies; select the interpreter in VS Code; run the first Python program; run the first test; and use the course doctor command to confirm that the machine is ready.

The setup path will explain not only which command to type, but what the command did, where files were created, how to recover from a PATH problem, how to reopen the terminal after installation, how to update the repository, and how to ask for help with a useful error report. It will provide a no-Git ZIP fallback while teaching Git early enough that future project work is reproducible. Every setup command will have a visible verification step and a troubleshooting entry.

| Tool | Required? | Learner-facing purpose | Recommended installation or use |
| --- | --- | --- | --- |
| Python 3.11–3.13 | Yes | The runtime that executes the course | Install from [python.org](https://www.python.org/downloads/); Windows learners must enable the PATH option |
| Git | Yes for the normal workflow | Clone, update, branch, and share work | Install from [git-scm.com](https://git-scm.com/downloads) and verify with `git --version` |
| VS Code | Strongly recommended | Read lessons, edit files, debug, and use the integrated terminal | Install from [code.visualstudio.com](https://code.visualstudio.com/) |
| A modern browser | Yes | Read linked references, view local documentation, and use permitted training platforms | Chrome, Firefox, Edge, or Safari |
| Project virtual environment | Yes | Keep course dependencies isolated and reproducible | Create with `python -m venv .venv` and activate using the platform-specific command |

The recommended VS Code profile will distinguish **required extensions** from optional quality-of-life extensions. The course will link to each official Marketplace page, state what the extension does, and provide a command-line-free installation path through the Extensions panel.

| Extension | Marketplace identifier | Status | Why it helps a beginner |
| --- | --- | --- | --- |
| Python | `ms-python.python` | Required | Interpreter selection, running files, environments, and test discovery |
| Pylance | `ms-python.vscode-pylance` | Required | Fast completion, readable diagnostics, navigation, and beginner-friendly type information |
| Python Debugger | `ms-python.debugpy` | Required | Breakpoints, step-through execution, variables, and call-stack inspection |
| Ruff | `charliermarsh.ruff` | Required | Fast formatting and lint feedback that teaches consistent Python habits; the setup guide will link to the current Marketplace page rather than hard-coding an installation command |
| Markdown All in One | `yzhang.markdown-all-in-one` | Required | Easier reading and navigation of the dense lesson material |
| Markdownlint | `DavidAnson.vscode-markdownlint` | Recommended | Keeps lessons and learner notes readable and consistent |
| GitLens | `eamodio.gitlens` | Recommended | Makes commits, blame, and history easier to understand visually |
| Rainbow CSV | `mechatroner.rainbow-csv` | Recommended | Makes security logs and tabular fixtures easier to inspect |
| SQLite Viewer | `qwtel.sqlite-viewer` | Recommended | Lets learners inspect local case databases without installing another GUI |

The course will explicitly warn learners not to install random “security” extensions, paste sensitive code into online tools, or enable extensions without checking the publisher and permissions. Extensions are conveniences, not prerequisites for understanding; every essential activity will remain runnable from the terminal.

## 4. Learning resources and the external-reference habit

Every major phase will contain a curated resource section that explains when to use a source, what to read, and what evidence to produce. The course will prefer official documentation, primary standards, and free hands-on platforms before adding optional books, videos, or commercial services. Links will be checked automatically, and lessons will record the relevant version or access date when a resource changes frequently.

| Resource family | Examples | How the course uses it |
| --- | --- | --- |
| Python language and tooling | [Python Tutorial](https://docs.python.org/3/tutorial/), [Python Standard Library](https://docs.python.org/3/library/), [Packaging User Guide](https://packaging.python.org/), [PEP 8](https://peps.python.org/pep-0008/), `pytest`, Ruff, and mypy documentation | Resolve syntax and tooling questions from primary sources; compare the course's simplified explanation with the full reference |
| Cybersecurity frameworks | NIST NICE, NIST CSF 2.0, CSEC2017 guidance, MITRE ATT&CK, and OWASP Top 10:2025 | Give names and structure to work roles, risk management, adversary behavior, and application risks [1] [2] [3] [4] [5] |
| Secure Python | OpenSSF Secure Coding Guide for Python and relevant CWE pages | Compare vulnerable and compliant examples, then write a regression test [6] |
| Web security practice | [PortSwigger Web Security Academy](https://portswigger.net/web-security) and OWASP Web Security Testing Guide | Use authorized, browser-based or local labs after web foundations; never treat public targets as practice targets |
| Beginner-friendly security labs | [picoCTF](https://picoctf.org/), [OverTheWire](https://overthewire.org/wargames/), and selected [TryHackMe](https://tryhackme.com/) rooms | Provide optional hands-on challenges with clear skill prerequisites and safe platform boundaries |
| Algorithms and problem solving | LeetCode, Python documentation, and course-built security utilities | Build general problem-solving fluency, then connect data structures and algorithms to logs, alerts, parsers, and detection pipelines |
| Professional practice | Git documentation, GitHub documentation, secure code review checklists, and incident-report examples | Teach collaboration, evidence, issue writing, and communication rather than only code production |

The resource guides will include a “read, run, record” pattern: read a narrowly chosen section, run a small example, and record one observation, edge case, or question. This prevents the resource list from becoming a link dump.

## 5. LeetCode and algorithmic problem-solving track

The course will add a dedicated `LEETCODE_GUIDE.md`, a problem index, and per-phase references from the daily lessons. LeetCode will be a **supporting practice strand**, not a substitute for security engineering. The learner should first understand Python control flow and data structures, then solve a small number of carefully selected problems, explain the complexity, write tests, and connect the pattern to a cybersecurity use case.

The recommended rhythm is two core problems and one stretch problem each week. A learner who is struggling may complete one core problem and write a clearer explanation instead of racing for volume. Every solution note will include the problem pattern, the invariant or decision rule, time and space complexity, one edge case, and one possible security application.

| Course period | Algorithm topics | Example problem themes | Security bridge |
| --- | --- | --- | --- |
| Days 11–20 | Arrays, strings, hash maps, sets, stacks | Two Sum, Contains Duplicate, Valid Anagram, Valid Parentheses, Valid Palindrome | IOC deduplication, frequency counts, balanced parser state |
| Days 21–30 | Two pointers, sliding windows, sorting, binary search | Best Time to Buy and Sell Stock, Longest Substring Without Repeating Characters, Binary Search | Time-window detection, ordered event search, threshold scans |
| Days 31–40 | Linked lists, queues, recursion, heaps | Merge Two Sorted Lists, Linked List Cycle, Kth Largest Element | Work queues, bounded processing, priority triage |
| Days 41–50 | Intervals, trees, graph traversal | Merge Intervals, Binary Tree Level Order Traversal, Number of Islands | Asset ranges, dependency graphs, network reachability in fixtures |
| Days 51–70 | Backtracking, dynamic programming, bit manipulation | Subsets, Combination Sum, House Robber, Counting Bits | Search-space reasoning, resource planning, bit flags and permissions |
| Days 71–90 | Practical pattern review | Mixed medium problems selected by the learner's weak areas | Translate a generic pattern into a parser or detection rule |
| Days 91–120 | Interview-style integration and explanation | One timed core problem per week plus project-specific design questions | Defend complexity, failure handling, and trade-offs in a security project |

The repository will not embed copyrighted problem statements or hidden platform solutions. It will link to the official problem pages, provide original course prompts and hints, and store learner-friendly solution explanations in a way that preserves the practice-first workflow. The LeetCode guide will also teach how to recognize when a security task is not a puzzle: correct authorization, evidence preservation, safe error handling, and threat modeling cannot be replaced by a clever algorithm.

## 6. Design principles borrowed from the JavaScript/TypeScript benchmark

The existing JavaScript/TypeScript course is the quality reference. Its strongest idea is that a lesson is not complete when a topic has been mentioned; it is complete when a learner can explain the behavior, predict it, practise it, apply it, and prove the result. The Python course will keep that standard while adapting the runtime and tooling to Python.

Every lesson will begin with a practical problem, state prerequisites and observable outcomes, show a small runnable example, trace the execution, name common mistakes, and end with a short mental model. Practice will be separated into progressive hints and explained solutions. Security lessons will add a sixth requirement: the learner must identify the trust boundary, threat, safe scope, expected defensive behavior, and evidence that the mitigation works.

| Benchmark expectation | Python-security adaptation |
| --- | --- |
| Problem-first teaching | Begin with a realistic defender, developer, analyst, or investigator problem before introducing syntax. |
| Dense concept coverage | Use multiple small examples, traces, diagrams, failure cases, and deliberate practice rather than one large unexplained script. |
| Runnable starters | Every day has a runnable `starter/main.py` or a clearly documented lab entry point. |
| Three practice levels | Level 1 builds fluency; Level 2 builds a security-relevant utility; Level 3 combines concepts and requires reasoning about failure or abuse. |
| Separate help | `practice/hints.md` gives progressive prompts; `practice/solutions.md` explains decisions and trade-offs. |
| Technical verification | Tests, linting, type checking where useful, link checks, and lab reset checks run from the repository root. |
| Portfolio progression | Every phase ends with a project that produces a README, tests, evidence, threat model, and retrospective. |

## 6. Outcome model

By the end of the 120-day core, a learner should be able to explain the Python execution model, write maintainable Python with tests and documentation, work safely with files and processes, reason about networks and protocols, validate and normalize untrusted input, use cryptographic APIs correctly without inventing cryptography, build and secure small web services, parse and enrich security telemetry, conduct a controlled incident investigation, and ship a security automation project with a documented threat model.

The outcome model is aligned to the broad academic areas represented in post-secondary cybersecurity curriculum guidance and to the practical work-role language of NICE [1] [2]. It also uses NIST CSF 2.0 as a management lens: **Govern, Identify, Protect, Detect, Respond, and Recover** [3]. Threat-informed labs use MITRE ATT&CK terminology to describe adversary goals and techniques without turning the course into uncontrolled attack instruction [4]. Application-security work uses the current OWASP Top 10:2025 categories as a reference for developer-facing risk [5]. Secure Python rules will be cross-checked against the OpenSSF Secure Coding Guide for Python, which provides framework-independent examples of vulnerable and compliant code [6].

| Capability family | Observable evidence by the end of the core |
| --- | --- |
| Programming foundations | The learner can design a small program from a written specification, trace it, test it, debug it, and explain its data flow without copying a solution. |
| Systems and automation | The learner can build safe command-line tools that handle paths, permissions, subprocesses, processes, configuration, and errors deliberately. |
| Networking | The learner can explain TCP/IP and HTTP behavior, write bounded clients and servers, parse protocol data, and handle timeouts, validation, and failure. |
| Secure development | The learner can identify trust boundaries, apply least privilege, avoid common injection and deserialization mistakes, manage secrets, and verify fixes with tests. |
| Application security | The learner can threat-model a local service, reproduce selected OWASP risks in a safe fixture, implement a mitigation, and document residual risk. |
| Defensive operations | The learner can normalize logs, extract indicators, write detection logic, map observations to ATT&CK concepts, and produce a useful alert with context. |
| Incident response and forensics | The learner can preserve synthetic evidence, calculate hashes, build a timeline, analyze artifacts, state confidence, and write an incident report. |
| Professional engineering | The learner can use Git, code review, documentation, issue tracking, CI checks, dependency hygiene, and reproducible environments. |
| Communication and ethics | The learner can define authorization, scope, rules of engagement, disclosure boundaries, and the difference between evidence, inference, and speculation. |

## 7. The 120-day core curriculum

The core is organized into twelve ten-day phases. Each phase has eight teaching days, one integration day, and one checkpoint or project day. The order intentionally delays advanced security tooling until the learner has enough Python, operating-system, networking, and web foundations to understand what the tool is doing.

### Phase 1 — Start Here: Computing, Python, and Safe Cyber Practice (Days 1–10)

This phase replaces the original 30 Days of Python introduction with a stronger first-run experience modeled on the benchmark's setup lesson. The learner installs Python, Git, and an editor; understands the interpreter and process model; runs a script and a test; learns the terminal; and receives the course's non-negotiable legal and ethical lab rules.

| Day | Focus | Security connection | Evidence |
| --- | --- | --- | --- |
| 1 | How code runs: interpreter, terminal, files, errors | Why tools act on a scope and why error output is evidence | A verified local environment and first script |
| 2 | Variables, values, names, and input/output | Treat external input as data, not truth | A small incident-note formatter |
| 3 | Numbers, strings, booleans, and conversions | Why parsing and type confusion create security problems | A validated indicator parser |
| 4 | Operators, comparisons, truthiness, and precedence | Correct authorization decisions depend on exact logic | A policy decision table |
| 5 | Branching and control flow | Triage logic and safe allow/deny paths | A file triage classifier |
| 6 | Loops and bounded repetition | Avoid infinite work and resource exhaustion | A bounded log scanner |
| 7 | Lists, tuples, sets, and dictionaries | Model alerts, indicators, and assets | An in-memory IOC catalog |
| 8 | Strings and text handling | Canonicalization, encoding, and log parsing | A robust line normalizer |
| 9 | Functions and decomposition | Make security checks testable and reviewable | A tested validation library |
| 10 | Checkpoint: terminal, Git, Python, and ethics | Demonstrate safe scope and reproducibility | Environment report plus oral explanation |

### Phase 2 — Core Python for Reliable Security Tools (Days 11–20)

The original Python topics are retained, but the learner now sees them through maintainability, correctness, and security boundaries. The phase introduces comprehensions only after explicit loops, and higher-order patterns only after functions are understood.

| Day | Focus | Security connection | Evidence |
| --- | --- | --- | --- |
| 11 | Function parameters, return contracts, and scope | Prevent hidden state in security decisions | A pure policy function suite |
| 12 | Modules, imports, and package boundaries | Reduce accidental coupling and import-time side effects | A small `security_utils` package |
| 13 | Exceptions and error taxonomy | Fail safely without hiding evidence | Error-aware file and parser pipeline |
| 14 | Files, paths, encodings, and safe cleanup | Path traversal, permissions, and resource handling | A safe evidence collector for synthetic files |
| 15 | Comprehensions, iterators, and generators | Stream large logs without unbounded memory | A lazy event pipeline |
| 16 | Regular expressions and structured parsing | Extract indicators while avoiding brittle matching | An IOC extraction tool with tests |
| 17 | Dates, time zones, and timestamps | Build defensible incident timelines | A timezone-aware timeline normalizer |
| 18 | Classes, dataclasses, and object design | Model assets, events, findings, and evidence | A typed finding model |
| 19 | Testing with `pytest` and test design | Prove detection and mitigation behavior | Unit and negative tests |
| 20 | Integration project: Log Triage CLI | Combine parsing, validation, testing, and reporting | Versioned CLI with README and test report |

### Phase 3 — Professional Python Engineering and Data Boundaries (Days 21–30)

This phase turns scripts into maintainable engineering artifacts. It introduces virtual environments, packaging, configuration, type hints, documentation, Git workflows, dependency review, and data serialization. The learner begins to understand software supply-chain risk rather than treating packages as magic downloads.

| Day | Focus | Security connection | Evidence |
| --- | --- | --- | --- |
| 21 | Virtual environments and reproducible installs | Isolation and dependency reproducibility | A clean rebuild from a lock or requirements file |
| 22 | CLI design with `argparse` | Safe interfaces and explicit options | A documented command-line tool |
| 23 | Configuration, environment variables, and secrets | Never commit credentials or rely on implicit defaults | A secret-free configuration system |
| 24 | JSON, CSV, SQLite, and serialization boundaries | Untrusted data and schema validation | A validated event store |
| 25 | Type hints, protocols, and static checking | Make security contracts visible to reviewers | A typed parser and policy layer |
| 26 | Logging, structured events, and redaction | Useful telemetry without leaking secrets | A redacting audit logger |
| 27 | Git, code review, and change history | Traceability and safe collaboration | A reviewed pull request simulation |
| 28 | Dependency hygiene, SBOM concepts, and scanning | Software supply-chain failures | A dependency inventory and risk note |
| 29 | Documentation, threat models, and abuse cases | Make assumptions and trust boundaries explicit | A threat model for the phase project |
| 30 | Project: Secure Evidence Journal | Combine storage, logging, typing, testing, and documentation | A reviewable local application |

### Phase 4 — Operating Systems, Linux, and Python Systems Automation (Days 31–40)

Cybersecurity engineering requires understanding the host. This phase teaches processes, permissions, users, services, environment variables, subprocesses, scheduling, and resource limits. Offensive examples are restricted to the learner's own local machine or provided sandbox fixtures.

| Day | Focus | Security connection | Evidence |
| --- | --- | --- | --- |
| 31 | Operating-system concepts and processes | What a security tool is actually observing | Process inventory explainer |
| 32 | Linux command line and filesystem permissions | Least privilege and defensive administration | Permission audit of a lab tree |
| 33 | `pathlib`, file metadata, and safe traversal | Prevent path confusion and unsafe collection | Bounded file inventory |
| 34 | `subprocess` without shell injection | Command injection and argument boundaries | Safe command runner with allowlist |
| 35 | Users, groups, permissions, and environment | Identity and privilege boundaries | Local permission report |
| 36 | Signals, timeouts, and resource limits | Stop runaway tools and handle failure | Timeout-controlled worker |
| 37 | Processes, threads, and queues | Concurrency, races, and evidence ordering | Parallel hash calculator with tests |
| 38 | Async I/O fundamentals | Efficient network and log collection | Bounded async collector |
| 39 | System inventories and configuration checks | Identify misconfiguration | Baseline comparison tool |
| 40 | Project: Host Baseline Auditor | Govern, identify, and protect a local lab host | JSON report, tests, and remediation guide |

### Phase 5 — Networking and Protocols with Python (Days 41–50)

This phase builds the network mental model before introducing scanners or packet tools. The learner writes bounded clients and servers, understands DNS and HTTP, reads packet captures supplied by the course, and handles timeouts, framing, validation, and privacy.

| Day | Focus | Security connection | Evidence |
| --- | --- | --- | --- |
| 41 | Network model, addresses, ports, and sockets | Understand exposure and attack surface | Network vocabulary map |
| 42 | TCP clients and servers | Connection lifecycle and timeouts | Local echo service with safeguards |
| 43 | UDP, framing, and reliability | Spoofing, loss, and validation limits | Bounded message protocol |
| 44 | DNS concepts and safe resolution | Name trust and resolution behavior | Resolver observation tool |
| 45 | HTTP requests, responses, headers, and cookies | Trust boundaries at web interfaces | HTTP inspection client for local fixtures |
| 46 | TLS concepts and certificate validation | Confidentiality is not the same as authentication | Certificate observation report |
| 47 | Network parsing and packet-capture basics | Evidence from traffic, not guesses | Parser for supplied PCAP-derived fixtures |
| 48 | Rate limits, retries, and backoff | Avoid self-inflicted denial of service | Polite client with tests |
| 49 | Network monitoring and connection baselines | Detect unusual behavior | Baseline comparison prototype |
| 50 | Project: Local Network Service Monitor | Detect availability and configuration drift safely | Local-only monitor with explicit scope |

### Phase 6 — Secure Python and Applied Cryptography (Days 51–60)

The learner studies secure defaults, encoding versus encryption, hashes, message authentication, password storage concepts, random number generation, key handling, and safe serialization. The course forbids implementing cryptographic primitives from scratch for production use. It demonstrates failure modes only in toy, local examples and emphasizes using reviewed libraries and documented APIs.

| Day | Focus | Security connection | Evidence |
| --- | --- | --- | --- |
| 51 | Trust boundaries, threat modeling, and attack surfaces | Security begins before code | Threat model of a small service |
| 52 | Encoding, canonicalization, and Unicode | Confusion at data boundaries | Canonicalization test suite |
| 53 | Hashes, integrity, and file fingerprints | Detect change; do not confuse with secrecy | Evidence hashing utility |
| 54 | HMAC and authenticity | Integrity with a shared secret | Signed event format |
| 55 | Randomness, tokens, and `secrets` | Predictability and session risk | Secure token service |
| 56 | Password storage and verification | Hashing passwords is not encryption | Local password-verifier fixture |
| 57 | Symmetric and asymmetric encryption concepts | Key management and threat assumptions | Design comparison, not homemade crypto |
| 58 | Secure serialization and deserialization | Code execution and data integrity risks | Safe schema-based loader |
| 59 | Secure error handling and logging | Avoid leaks while preserving useful evidence | Redacted error pipeline |
| 60 | Project: Tamper-Evident Case Bundle | Combine hashes, HMAC, metadata, and validation | Signed synthetic evidence bundle |

### Phase 7 — Web Services and Application Security (Days 61–70)

This phase uses a small local Python web service as a teaching laboratory. Each vulnerability fixture is isolated and intentionally incomplete. The learner first observes the failure, then writes a test that captures it, then implements a narrow mitigation, and finally documents residual risk. The sequence follows OWASP Top 10:2025 categories where they are relevant to Python services [5].

| Day | Focus | Security connection | Evidence |
| --- | --- | --- | --- |
| 61 | HTTP service architecture with Flask or FastAPI | Application trust boundaries | Local service skeleton |
| 62 | Routing, request parsing, and validation | Input is hostile until validated | Schema-validated endpoint |
| 63 | Authentication, sessions, and authorization | Identity is not permission | Role-aware access tests |
| 64 | Injection and parameterized queries | SQL, command, and template boundaries | Vulnerable fixture plus fixed tests |
| 65 | XSS, output encoding, and content types | Context-specific neutralization | Safe rendering tests |
| 66 | CSRF, cookies, CORS, and browser boundaries | Cross-origin trust decisions | Local browser-boundary demo |
| 67 | SSRF, URL validation, and outbound controls | Server-side network trust | Allowlisted fetcher against local targets |
| 68 | Security misconfiguration and secure defaults | Reduce dangerous deployment assumptions | Configuration audit |
| 69 | Supply-chain, integrity, and exceptional conditions | Fail safely under dependency and runtime failure | Dependency and error review |
| 70 | Project: Secure Local Case Management API | Design, implement, test, and threat-model a service | API, tests, threat model, and remediation report |

### Phase 8 — Defensive Automation, Detection, and Threat Intelligence (Days 71–80)

The learner now works as a junior defensive engineer. They ingest synthetic logs, normalize fields, enrich indicators, write detections, reduce noise, and explain a finding. MITRE ATT&CK is used as a common language for adversary goals and techniques, not as a checklist for uncontrolled attack execution [4].

| Day | Focus | Security connection | Evidence |
| --- | --- | --- | --- |
| 71 | Security telemetry and event schemas | Detection starts with usable data | Event schema and parser |
| 72 | Log normalization and timestamp handling | Correlation across sources | Normalized event stream |
| 73 | Indicators of compromise and enrichment | Context reduces false positives | Offline enrichment fixture |
| 74 | Detection logic and thresholds | Precision, recall, and analyst trust | Tested detection rules |
| 75 | MITRE ATT&CK mapping | Describe behavior consistently | ATT&CK-mapped finding |
| 76 | Alert triage and prioritization | Risk-based analyst workflow | Queue with severity rationale |
| 77 | Baselines, anomalies, and simple statistics | Detect deviation without magical AI claims | Explainable anomaly detector |
| 78 | Threat intelligence formats and provenance | Evidence quality and source confidence | Small STIX-like normalized dataset |
| 79 | Reporting, dashboards, and analyst communication | Turn code into decisions | Analyst-ready report |
| 80 | Project: Mini Detection Pipeline | Collect, normalize, detect, enrich, and report | Reproducible offline SOC pipeline |

### Phase 9 — Incident Response and Digital Forensics Foundations (Days 81–90)

This phase emphasizes evidence handling, repeatability, and humility. The learner works with synthetic disk images, logs, timelines, browser artifacts, and packet-derived records supplied by the course. The course distinguishes observation from inference and never encourages collecting or analyzing data without authorization.

| Day | Focus | Security connection | Evidence |
| --- | --- | --- | --- |
| 81 | Incident response lifecycle and case management | Prepare, detect, respond, recover | Case plan and decision log |
| 82 | Evidence integrity, hashing, and chain of custody | Preserve trust in findings | Evidence register |
| 83 | Filesystem metadata and timelines | Reconstruct activity | Timeline builder |
| 84 | SQLite and application artifacts | Query structured evidence | Artifact extractor |
| 85 | Browser and document metadata in synthetic cases | User activity clues and limits | Metadata report |
| 86 | Email and phishing analysis with fixtures | Headers, URLs, and social engineering indicators | Offline email triage tool |
| 87 | PCAP and network evidence analysis | Network observations in context | Flow summary from supplied capture data |
| 88 | Memory and process evidence concepts | Volatile data and uncertainty | Evidence interpretation worksheet |
| 89 | Incident report writing and confidence | Communicate impact and limitations | Executive and technical reports |
| 90 | Project: Synthetic Breach Investigation | Investigate a contained scenario end to end | Case bundle, timeline, findings, and lessons learned |

### Phase 10 — Authorized Security Testing and Vulnerability Analysis (Days 91–100)

This phase introduces the security tester's reasoning while keeping the practical work inside explicit lab boundaries. The learner learns asset discovery concepts, service enumeration against local fixtures, vulnerability validation, authentication testing in a toy application, and remediation verification. No public scanning, credential attacks, persistence, evasion, or exploitation of real systems is part of the default course path.

| Day | Focus | Security connection | Evidence |
| --- | --- | --- | --- |
| 91 | Rules of engagement and test scope | Authorization before action | Signed lab scope document |
| 92 | Asset inventory and attack-surface mapping | Identify what exists before testing | Local lab inventory |
| 93 | Safe service discovery and banners | Observe without causing harm | Bounded local enumerator |
| 94 | Vulnerability concepts, CVEs, and severity | Separate finding from impact claim | Vulnerability triage note |
| 95 | Web testing methodology with local fixtures | Reproduce and document controlled risk | Test plan |
| 96 | Authentication and authorization testing | Verify access-control assumptions | Negative authorization suite |
| 97 | Input validation and injection validation | Prove the narrow flaw and fix | Regression tests |
| 98 | Fuzzing concepts and resource controls | Discover edge cases without denial of service | In-process bounded fuzzer |
| 99 | Findings, remediation, and retesting | Security work ends with actionable fixes | Professional finding report |
| 100 | Project: Authorized Local Assessment | Plan, assess, report, remediate, retest | Complete assessment package |

### Phase 11 — DevSecOps, Cloud Concepts, and Supply-Chain Security (Days 101–110)

Python security engineering increasingly occurs in repositories and deployment pipelines. This phase covers secure development lifecycle practices, CI checks, dependency and secret scanning, SBOM concepts, container boundaries, cloud identity concepts, and configuration review. Cloud actions remain offline or mocked unless a learner independently provides an authorized sandbox.

| Day | Focus | Security connection | Evidence |
| --- | --- | --- | --- |
| 101 | Secure SDLC and threat modeling in delivery | Govern and identify risk early | Security backlog |
| 102 | CI quality gates and test automation | Make security repeatable | Local CI workflow |
| 103 | Static analysis, linting, and code review | Find patterns without outsourcing judgment | Annotated scan report |
| 104 | Dependency pinning, SBOM, and provenance | Software supply-chain failures | SBOM-like inventory |
| 105 | Secret detection and key rotation concepts | Reduce credential exposure | Secret-safe repository audit |
| 106 | Containers and isolation concepts | Boundaries, images, and runtime assumptions | Local container threat model |
| 107 | Cloud identity, roles, and least privilege | Permissions are policy, not convenience | Mock IAM policy analyzer |
| 108 | Infrastructure configuration and drift | Secure defaults at deployment | Configuration validator |
| 109 | Security metrics and risk communication | Measure outcomes rather than tool counts | Executive risk dashboard |
| 110 | Project: Secure Delivery Pipeline | Build, test, scan, report, and release a Python tool | Reproducible DevSecOps package |

### Phase 12 — Advanced Integration, Engineering Judgment, and Capstone (Days 111–120)

The final phase is not a collection of disconnected tricks. It asks the learner to select a problem, define the users and threat model, build a secure and observable solution, test it against failure and abuse cases, and defend the design in writing and conversation. The final project is an assessment of learning, not a promise of professional readiness.

| Day | Focus | Security connection | Evidence |
| --- | --- | --- | --- |
| 111 | Architecture for security tools | Separate collection, analysis, storage, and presentation | Architecture diagram |
| 112 | Performance, queues, caching, and backpressure | Availability and resource safety | Load-limited pipeline |
| 113 | Advanced async and concurrent design | Correctness under interleaving | Concurrency test suite |
| 114 | Robustness, graceful degradation, and recovery | Respond and recover | Failure-injection report |
| 115 | Privacy, data minimization, and retention | Security includes responsible handling | Data lifecycle policy |
| 116 | Research, documentation, and source evaluation | Avoid cargo-cult security | Annotated design references |
| 117 | Capstone planning and threat model review | Convert uncertainty into an executable plan | Approved project brief |
| 118 | Capstone implementation and verification | Build the secure core | Working project with tests |
| 119 | Capstone security review and incident exercise | Attack the design safely and fix it | Review findings and remediation |
| 120 | Final demonstration and portfolio packaging | Communicate engineering judgment | Demo, README, threat model, test evidence, retrospective |

## 8. Optional 30-day specialization tracks

After the core, learners should choose one 10-day track at a time rather than trying to become expert in every security role simultaneously. These tracks provide depth while preserving the shared Python foundation.

| Track | Days | Emphasis | Example final artifact |
| --- | --- | --- | --- |
| Blue Team and Detection Engineering | 121–130 | Detection-as-code, Sigma-like logic, alert quality, ATT&CK coverage, and response automation | Offline SOC automation kit |
| Application Security and Secure Backend Engineering | 131–140 | Advanced API security, secure architecture, testing, dependency risk, and remediation | Hardened service with security test suite |
| Digital Forensics and Incident Response | 141–150 | Evidence processing, timeline analysis, case management, and reporting | Reproducible forensic case notebook |
| Security Research and Malware Analysis Foundations | 151–160 | Static analysis, safe sandboxing concepts, file formats, YARA-like pattern reasoning, and reverse-engineering literacy | Benign sample-analysis report |
| Cloud and DevSecOps Security | 161–170 | Identity, CI/CD, containers, infrastructure policy, supply chain, and cloud monitoring | Policy-aware deployment pipeline |
| Network Security and Protocol Engineering | 171–180 | Protocol analysis, secure services, network telemetry, and resilient communication | Local protocol monitor and lab report |

These tracks are intentionally labeled **specialization tracks**, not promises of mastery. A learner should continue through supervised labs, university coursework, open-source contribution, internships, and professional feedback.

## 9. Standard lesson contract

Every numbered day will use the following structure. Security-specific sections are mandatory when the day touches systems, networks, data, applications, or adversary behavior.

```text
NNN_day_slug/
├── NNN_day_slug.md                 # Dense main lesson
├── starter/
│   ├── main.py                     # Runnable examples
│   ├── broken_example.py           # Optional, isolated failure case
│   └── README.md                   # Exact commands and expected output
├── practice/
│   ├── prompts.md                 # Level 1, Level 2, Level 3
│   ├── hints.md                    # Progressive help, not answers
│   └── solutions.md                # Explained decisions and trade-offs
├── tests/
│   └── test_main.py                # Learner-facing acceptance tests
├── lab/
│   ├── scope.md                   # Authorization, target, boundaries, stop conditions
│   ├── reset.sh / reset.ps1        # Safe cleanup where applicable
│   └── fixtures/                   # Synthetic or intentionally local data
└── diagrams/
    ├── execution-trace.svg
    ├── data-flow.svg
    └── threat-boundary.svg        # Required for security-heavy lessons
```

Each lesson must contain a table of contents, prerequisites, observable outcomes, the problem it solves, plain-language explanation, traced examples, common-mistake table, practice links, a one-sentence mental model, a finish line, and a short proof section. The benchmark's original Python content can be mined for examples, but it must be rewritten into this contract rather than copied into a longer page without scaffolding.

## 10. Repository architecture

The redesigned repository will keep the useful Python knowledge after review while removing the original translations and historical 30-day presentation from the repository tree. Git history preserves provenance and rollback; the working tree should be clean and intentional, like the JavaScript/TypeScript course.

```text
zero-to-hero-python-cybersecurity-/
├── README.md
├── CURRICULUM_GUIDE.md
├── COURSE_QUALITY_STANDARD.md
├── COURSE_PLAN_DRAFT.md
├── SAFETY_AND_LAB_RULES.md
├── SETUP.md
├── TROUBLESHOOTING.md
├── GLOSSARY.md
├── CONTRIBUTING.md
├── SECURITY.md
├── pyproject.toml
├── requirements-dev.txt
├── scripts/
│   ├── check_course.py
│   ├── check_links.py
│   ├── run_day.py
│   └── build_index.py
├── tests/
│   ├── test_course_structure.py
│   └── fixtures/
├── day_1_setup_and_safe_practice/
├── ...
├── day_117_capstone_planning/
├── specializations/
│   ├── blue-team/
│   ├── appsec/
│   ├── dfir/
│   ├── malware-analysis-foundations/
│   ├── cloud-devsecops/
│   └── network-security/
├── projects/
└── shared/
    ├── sample_data/
    ├── schemas/
    ├── lab_utils/
    └── diagrams/
```

The existing translation directories, sponsor blocks, duplicate screenshots, legacy web/database leftovers, and other unrelated files will be removed from the working tree after their useful technical content and license obligations have been reviewed. The redesigned root README will be the only default entry point; old links may be documented in a migration note, but the old setup will not remain part of the course.

## 11. Tooling and verification plan

The course should work on Windows, macOS, and Linux with Python 3.11–3.13 unless a later decision narrows support. The default setup should use a project-local virtual environment and commands of the form `python -m ...`, avoiding hidden global installations. A learner should be able to run one documented command for a lesson, one command for its tests, and one command for the whole-course structural audit.

The proposed development checks are `pytest` for behavior, `ruff` for style and selected static checks, `mypy` for the parts where annotations add real value, `bandit` for educational secure-coding checks, `pip-audit` for dependency review, and a custom course checker for links, required headings, starter files, scope documents, and expected practice files. Tool output will be explained in the lessons; automation is a guardrail, not a substitute for understanding.

Security-heavy exercises will follow a repeatable loop: read the scope, inspect the fixture, predict the behavior, run the smallest safe test, record evidence, implement a mitigation, rerun the test, and document residual risk. The repository will not include instructions that encourage scanning arbitrary public targets, stealing credentials, bypassing access controls on systems the learner does not own, deploying persistence, or evading detection.

## 12. Assessment and community model

A learner marks a day complete only when they can run the starter, pass the acceptance checks, explain the main mental model, finish at least the core Level 1 practice, complete one Level 2 application, and write a short reflection naming one edge case or security trade-off. Level 3 is stretch work; it should deepen reasoning rather than become a gate that discourages beginners.

Every ten-day phase ends with an integration project and a short oral or written defense. Every project must include a README, setup instructions, tests, sample input and output, threat model, security assumptions, limitations, and a retrospective. Peer study groups should review design and evidence, not share credentials or run tests against unapproved systems.

The course should add issue templates for broken examples, unclear explanations, safety concerns, accessibility issues, and translation updates. Contribution guidance should ask contributors to preserve beginner readability, keep labs bounded, and include tests for changed code.

## 13. Implementation sequence after approval

Implementation should proceed in vertical slices rather than attempting to write 120 lessons at once. First, establish the new root documentation, course quality standard, setup workflow, safety rules, test harness, and the first five days. Second, complete the first ten-day phase and verify that a complete beginner can clone, configure, run, practise, and recover from mistakes. Third, migrate the remaining phases in batches, keeping the same lesson contract and adding projects at every checkpoint. Fourth, run a repository-wide audit for links, code, tests, encoding, safety scope, and navigation.

The first implementation milestone should therefore be **Phase 1 plus the course infrastructure**, not an unreviewed bulk rewrite. Once the pattern is accepted by the learner and by the course owner, the remaining days can be produced consistently and reviewed in manageable batches.

## 14. References

[1]: https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center "NIST NICE Framework Resource Center"

[2]: https://niccs.cisa.gov/tools/nice-framework "CISA NICE Framework Work Roles"

[3]: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf "NIST Cybersecurity Framework 2.0"

[4]: https://attack.mitre.org/matrices/enterprise/ "MITRE ATT&CK Enterprise Matrix"

[5]: https://owasp.org/Top10/2025/en/ "OWASP Top 10:2025"

[6]: https://www.openssf.org/blog/2026/05/12/secure-coding-guide-for-python-pyscg-first-release/ "OpenSSF Secure Coding Guide for Python"

[7]: https://www.nist.gov/news-events/news/2018/02/new-guidelines-cybersecurity-curricula "NIST announcement of ACM/IEEE CSEC2017 curriculum guidance"
