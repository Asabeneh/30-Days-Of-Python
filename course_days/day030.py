from dataclasses import dataclass


@dataclass(frozen=True)
class JournalEntry:
    timestamp: str
    source: str
    raw: str


def main() -> None:
    print(JournalEntry("2026-08-20T12:00:00Z", "fixture", "login_failed"))


if __name__ == "__main__":
    main()
