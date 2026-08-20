def review_checklist() -> list[str]:
    return ["read diff", "run tests", "check dependencies", "document security impact"]


def main() -> None:
    print("; ".join(review_checklist()))


if __name__ == "__main__":
    main()
