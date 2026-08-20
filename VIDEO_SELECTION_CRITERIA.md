# Video Selection Criteria

The course will not select videos merely because they contain the word “cybersecurity” or have a large view count. A video enters the recommended path only when it earns a clear place in the learning sequence and can be checked against a written or primary source.

## Ranking model

| Criterion | Weight | What counts as strong evidence |
| --- | ---: | --- |
| Authority and subject expertise | 25% | Official project channel, university or recognized training provider, named subject-matter educator, or a creator with a sustained technical teaching record |
| Technical accuracy and currency | 20% | Correct terminology, current tools or standards, version/date context, and no claims that conflict with primary documentation |
| Teaching quality | 20% | Clear learning objectives, logical sequence, worked examples, explanations of why, and a pace suitable for the mapped learner level |
| Practical relevance | 15% | The video supports a specific course outcome and leads to a safe local exercise rather than passive watching |
| Evidence of learner value | 10% | Strong sustained learner feedback, meaningful comments, reputable course references, or broad adoption; view count alone is not sufficient |
| Accessibility and maintainability | 10% | Captions or transcript, chapters, stable canonical URL, written alternative, and timestamps that can be rechecked |

A video must meet minimum thresholds for authority, accuracy, and safety even if its total score is high. A popular but unsafe or outdated video will not be recommended as required learning.

## Source tiers

**Tier 1** sources are official project or standards channels, university channels, and recognized training providers. These are preferred for Python tooling, VS Code, Linux, networking concepts, OWASP, cloud, and defensive frameworks.

**Tier 2** sources are established educators with a consistent technical teaching record and transparent scope. These are useful for alternative explanations and demonstrations when the lesson is cross-checked against primary documentation.

**Tier 3** sources are community videos, conference recordings, interviews, and challenge walkthroughs. They may be included as optional context or critical-review material but are not used as the sole explanation of a security control.

## Required verification record

For every selected video, maintain the canonical URL, video ID, title, channel, publication date when available, duration, chapter or segment title, start and stop timestamps, mapped course outcome, source tier, written alternative, safety note, verification date, and status. Record what was actually checked; do not infer chapter timestamps from a search snippet.

## Disqualifiers

Exclude videos that encourage unauthorized scanning or access, expose real credentials or private data, rely on obsolete insecure defaults without warning, make unsupported claims, contain unexplained exploit instructions outside an authorized lab, hide the relevant content behind an account or paywall, or cannot be mapped to a concrete learner outcome.

## Learner feedback interpretation

Treat comments and ratings as signals rather than proof. Look for repeated comments describing clarity, correctness, pacing, and successful practice. Discount engagement that appears unrelated to teaching quality. A well-regarded video still requires technical review by the course maintainer.

## Placement decision

Use `inline` only when the video is the clearest next support for the current lesson. Use `end_of_lesson` for optional reinforcement. Use `phase_playlist` for a coherent route with several independent videos. Required course progress must never depend on YouTube availability.
