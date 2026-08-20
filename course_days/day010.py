"""Day 10 starter: a small, explainable triage classifier."""


def classify_event(severity: int, in_scope: bool) -> tuple[str, str]:
    if not in_scope:
        return "ignore", "outside the lab scope"
    if severity >= 9:
        return "urgent_review", "high severity"
    if severity >= 5:
        return "review", "moderate severity"
    return "ignore", "low severity"


def main() -> None:
    cases = [(3, True), (5, True), (9, True), (10, False)]
    for case in cases:
        print(case, "->", classify_event(*case))


if __name__ == "__main__":
    main()
