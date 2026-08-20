def diff(expected: dict[str, str], observed: dict[str, str]) -> dict[str, list[str]]:
    return {
        "added": sorted(set(observed) - set(expected)),
        "removed": sorted(set(expected) - set(observed)),
        "changed": sorted(
            key
            for key in expected.keys() & observed.keys()
            if expected[key] != observed[key]
        ),
    }


def main() -> None:
    print(diff({"mode": "safe"}, {"mode": "safe", "new": "value"}))


if __name__ == "__main__":
    main()
