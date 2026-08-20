"""Day 5 starter: classify one synthetic event."""


def classify(severity: int, in_scope: bool) -> tuple[str, str]:
    if not in_scope:
        return "ignore", "outside the lab scope"
    if severity >= 9:
        return "urgent_review", "high severity"
    if severity >= 5:
        return "review", "moderate severity"
    return "ignore", "low severity"


def main() -> None:
    print(classify(8, True))


if __name__ == "__main__":
    main()
