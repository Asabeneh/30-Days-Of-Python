"""Day 4 starter: make a policy expression visible."""


def needs_review(in_scope: bool, severity: int, repeated: bool) -> bool:
    return in_scope and (severity >= 7 or repeated)


def main() -> None:
    print(needs_review(True, 8, False))
    print(needs_review(False, 10, True))


if __name__ == "__main__":
    main()
