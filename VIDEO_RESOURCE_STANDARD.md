# Video Resource Standard

Video is a **supporting learning mode**, not a replacement for the written lesson, runnable code, tests, or practice. Every learner must be able to complete the course without watching a video. Videos are included when a visual demonstration, terminal walkthrough, diagram, debugging session, or instructor explanation adds value that text alone does not provide.

## Placement rules

Use an **inline video reference** when the learner needs a visual demonstration to complete the immediate concept. The reference belongs directly after the relevant explanation and must identify the exact segment to watch before returning to the lesson.

Use an **optional end-of-lesson reference** when the video provides a second explanation, broader context, revision material, career perspective, or additional practice. End-of-lesson videos must not be required to satisfy the day's finish line.

Use a **phase playlist** when several videos form a coherent optional route. The playlist belongs in the phase resource guide and must still include individual video metadata and timestamps for the segments the course recommends.

## Timestamp format

Every recommended segment uses a timestamped URL and a human-readable time range:

```markdown
[Watch 04:12–07:30: virtual environments and interpreter selection](https://www.youtube.com/watch?v=VIDEO_ID&t=252s)
```

The `t` query parameter is the start time in seconds. If an end time is known, record it in the table and state “stop at” in the learner-facing text; YouTube links generally start at a time but do not reliably enforce an end time. The course should never pretend that a timestamp is exact if it has not been checked against the current video.

## Video metadata contract

Each video record must contain:

| Field | Requirement |
| --- | --- |
| `video_id` | The stable YouTube video identifier, not a shortened display URL alone. |
| `title` | The title observed at verification time. |
| `channel` | The publishing channel and its official channel URL when available. |
| `url` | The canonical watch URL. |
| `lesson` | The day, phase, or specialization where the video is used. |
| `placement` | One of `inline`, `end_of_lesson`, or `phase_playlist`. |
| `purpose` | The exact learner problem the video supports. |
| `segments` | One or more start times, optional end times, labels, and target concepts. |
| `verified_on` | The date the title, availability, and timestamps were checked. |
| `transcript_or_alternative` | A written alternative, transcript, captions note, or official documentation link where practical. |
| `safety_note` | Required for security content; state scope and distinguish demonstration from permission. |

## Selection rules

Prefer authoritative creators, official project channels, university lectures, established educators, and videos whose examples can be checked against primary documentation. Prefer stable, focused videos over sensational titles, unexplained tool demonstrations, or content that encourages testing systems without authorization. A video should support a course outcome, not merely contain related keywords.

Do not embed advertisements, affiliate promotions, unverified claims, leaked data, real credentials, or unsafe demonstrations in the learning path. If a video is useful but includes unsafe or outdated material, it may be listed only as a critical-review exercise with a warning, never as a required tutorial.

## Accessibility and learner control

Video recommendations must include captions information when available, a written alternative or related documentation link, and enough context that a learner knows what to watch for. Learners should be told the exact segment, the question to answer, and the action to perform after watching. Do not require autoplay, account creation, or public comments. Respect bandwidth, privacy, and learners who cannot use audio.

## Maintenance

YouTube videos can be edited, removed, age-restricted, region-limited, or retitled. The repository will run a URL check for canonical links, but link availability alone does not verify that the content or timestamp remains correct. Maintainers should rewatch each recommended segment when the video changes, when a learner reports drift, and at least once per course release. If a video breaks, the written lesson remains authoritative and the record should be marked `needs_review` rather than silently leaving a dead link.

## Learner workflow

Read the lesson explanation first. Watch only the listed segment. Write one observation or answer the question attached to the segment. Run the course starter and compare the video behavior with the local example. Then complete the practice task without copying the video. This keeps video in service of active learning rather than passive watching.
