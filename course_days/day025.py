from typing import TypedDict


class Event(TypedDict):
    source: str
    severity: int


def event_summary(event: Event) -> str:
    return f"{event['source']}: severity={event['severity']}"


def main() -> None:
    print(event_summary({"source": "fixture", "severity": 5}))


if __name__ == "__main__":
    main()
