from dataclasses import dataclass


@dataclass(frozen=True)
class Finding:
    title: str
    severity: int
    evidence_id: str


def main() -> None:
    print(Finding("synthetic event", 5, "evidence-1"))


if __name__ == "__main__":
    main()
