"""Validate and render the course's timestamp-aware YouTube resource catalog."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "video_resources.json"
MARKER_START = "<!-- video-resources:start -->"
MARKER_END = "<!-- video-resources:end -->"
VIDEO_ID = re.compile(r"^[A-Za-z0-9_-]{11}$")


def load_catalog() -> list[dict[str, object]]:
    payload = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    return payload["resources"]


def validate(resources: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    for resource in resources:
        video_id = str(resource["video_id"])
        if not VIDEO_ID.fullmatch(video_id):
            errors.append(f"invalid YouTube video ID: {video_id}")
        if f"watch?v={video_id}" not in str(resource["url"]):
            errors.append(f"canonical URL does not contain video ID: {video_id}")
        if resource["placement"] not in {"inline", "end_of_lesson", "phase_playlist"}:
            errors.append(f"invalid placement for {video_id}")
        if not resource.get("verified_on"):
            errors.append(f"missing verification date for {video_id}")
        for segment in resource["segments"]:
            start = int(segment["start"])
            end = int(segment["end"])
            if start < 0 or end <= start:
                errors.append(f"invalid segment for {video_id}: {start}-{end}")
    return errors


def timestamp(seconds: int) -> str:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return (
        f"{hours}:{minutes:02d}:{seconds:02d}"
        if hours
        else f"{minutes:02d}:{seconds:02d}"
    )


def link(resource: dict[str, object], segment: dict[str, object]) -> str:
    seconds = int(segment["start"])
    url = f"https://www.youtube.com/watch?v={resource['video_id']}&t={seconds}s"
    label = f"{timestamp(seconds)}–{timestamp(int(segment['end']))}: {segment['label']}"
    return f"[{label}]({url})"


def render_catalog(resources: list[dict[str, object]]) -> str:
    lines = [
        "# Timestamped Video Resources",
        "",
        (
            "Video is optional support. Read the lesson and run its starter first, "
            "then watch only the segment that answers the stated question. Return "
            "to the lesson and complete the practice without copying the video."
        ),
        "",
        (
            f"> Catalog last rendered: **{date.today().isoformat()}**. Always check "
            "the segment against the current video if a learner reports drift."
        ),
        "",
        "## How placement works",
        "",
        (
            "**Inline** references appear inside a lesson when a visual demonstration "
            "is immediately useful. **End-of-lesson** references are optional second "
            "explanations. **Phase playlists** are broader optional review routes. "
            "Every timestamp link starts at the recommended segment; the displayed "
            "end time is a stop point, not a technical playback limit."
        ),
        "",
        "## Catalog",
        "",
    ]
    for resource in resources:
        lines.extend(
            [
                f"### {resource['title']}",
                "",
                f"**Channel:** [{resource['channel']}]({resource['channel_url']})  ",
                f"**Placement:** `{resource['placement']}`  ",
                f"**Lessons:** {', '.join(str(day) for day in resource['lessons'])}  ",
                f"**Purpose:** {resource['purpose']}",
                "",
                "| Segment | Concept |",
                "| --- | --- |",
            ]
        )
        for segment in resource["segments"]:
            lines.append(f"| {link(resource, segment)} | {segment['concept']} |")
        lines.extend(
            [
                "",
                (
                    "**Written alternative:** "
                    f"[{resource['transcript_or_alternative']}]"
                    f"({resource['transcript_or_alternative']})  "
                ),
                f"**Safety note:** {resource['safety_note']}  ",
                f"**Verified:** {resource['verified_on']}  ",
                "",
            ]
        )
    lines.extend(
        [
            "## Learner video note template",
            "",
            (
                "After watching, record the exact segment, one observation, "
                "one question, and the local course command you ran to compare "
                "the idea. "
                "If the video "
                "is unavailable, use the written alternative and continue; never let a "
                "broken video block progress."
            ),
            "",
            "## Maintenance",
            "",
            (
                "The machine-readable source is "
                "[`video_resources.json`](video_resources.json). Maintainers should "
                "update the title, availability, timestamps, written "
                "alternative, and verification date together. Run "
                "`python scripts/video_catalog.py --check` before committing."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def block_for(day: int, resources: list[dict[str, object]]) -> str:
    lines = ["## Video support", ""]
    for resource in resources:
        placement = str(resource["placement"])
        prefix = (
            "**Inline recommendation:**"
            if placement == "inline"
            else "**Optional recommendation:**"
        )
        lines.append(
            f"{prefix} [{resource['title']}](https://www.youtube.com/watch?v={resource['video_id']})."
        )
        lines.append("")
        for segment in resource["segments"]:
            lines.append(
                f"- Watch {link(resource, segment)} for **{segment['concept']}**. "
                "Then return to this lesson and run the local starter."
            )
        lines.append("")
        lines.append(
            f"Written alternative: [{resource['transcript_or_alternative']}]"
            f"({resource['transcript_or_alternative']})."
        )
        lines.append("")
    return "\n".join(lines).rstrip()


def inject_into_lessons(resources: list[dict[str, object]]) -> None:
    by_day: dict[int, list[dict[str, object]]] = defaultdict(list)
    for resource in resources:
        for day in resource["lessons"]:
            by_day[int(day)].append(resource)
    for day, day_resources in by_day.items():
        matches = sorted(ROOT.glob(f"{day:03d}_day_*/*.md"))
        lesson_files = [
            path for path in matches if path.parent.name.startswith(f"{day:03d}_day_")
        ]
        if not lesson_files:
            continue
        path = lesson_files[0]
        text = path.read_text(encoding="utf-8")
        block = f"{MARKER_START}\n{block_for(day, day_resources)}\n{MARKER_END}"
        if MARKER_START in text:
            before, remainder = text.split(MARKER_START, 1)
            _, after = remainder.split(MARKER_END, 1)
            text = before + block + after
        else:
            anchor = "## Core lesson"
            if anchor in text:
                text = text.replace(anchor, f"{block}\n\n{anchor}", 1)
            else:
                text += f"\n\n{block}\n"
        path.write_text(text, encoding="utf-8")


def inject_into_specializations(resources: list[dict[str, object]]) -> None:
    track_resources = {
        "blue-team": ["ieqSi5Aicxc", "51W4Fhds7DQ"],
        "appsec": ["51W4Fhds7DQ"],
        "dfir": ["ieqSi5Aicxc"],
        "malware-analysis-foundations": ["51W4Fhds7DQ"],
        "cloud-devsecops": ["51W4Fhds7DQ"],
        "network-security": ["AYgXr1dynKU", "ueth6WvFVMU", "ieqSi5Aicxc"],
    }
    by_id = {str(resource["video_id"]): resource for resource in resources}
    for track, ids in track_resources.items():
        path = ROOT / "specializations" / track / "README.md"
        text = path.read_text(encoding="utf-8")
        selected = [by_id[video_id] for video_id in ids]
        block = (
            f"{MARKER_START}\n## Optional video route\n\n"
            "Use the [full timestamped catalog](../../VIDEO_RESOURCES.md) and "
            "watch these focused segments after completing the written track plan.\n\n"
        )
        for resource in selected:
            segment = resource["segments"][0]
            block += f"- {link(resource, segment)} — {resource['purpose']}\n"
        block += f"\n{MARKER_END}"
        if MARKER_START in text:
            before, remainder = text.split(MARKER_START, 1)
            _, after = remainder.split(MARKER_END, 1)
            text = before + block + after
        else:
            text += f"\n\n{block}\n"
        path.write_text(text, encoding="utf-8")


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    resources = load_catalog()
    errors = validate(resources)
    if errors:
        for error in errors:
            print(f"- {error}")
        return 1
    if args.check:
        print(f"Video catalog: OK ({len(resources)} resources)")
        return 0
    (ROOT / "VIDEO_RESOURCES.md").write_text(
        render_catalog(resources), encoding="utf-8"
    )
    inject_into_lessons(resources)
    inject_into_specializations(resources)
    print(
        f"Rendered {len(resources)} video resources and integrated lesson references."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
