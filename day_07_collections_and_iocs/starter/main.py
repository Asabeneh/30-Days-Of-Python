"""Day 7 starter: keep indicators unique and retain context."""


def catalog(indicators: list[str]) -> dict[str, dict[str, str]]:
    return {
        value: {"kind": "ip", "source": "synthetic", "confidence": "low"}
        for value in sorted(set(indicators))
    }


def main() -> None:
    print(catalog(["203.0.113.8", "203.0.113.8", "198.51.100.7"]))


if __name__ == "__main__":
    main()
