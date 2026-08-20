def severity_label(severity: int) -> str:
    if not 0 <= severity <= 10:
        raise ValueError("severity must be between 0 and 10")
    return "high" if severity >= 7 else "normal"


def main() -> None:
    print(severity_label(8))


if __name__ == "__main__":
    main()
