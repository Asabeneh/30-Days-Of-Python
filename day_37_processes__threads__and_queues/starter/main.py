from concurrent.futures import ThreadPoolExecutor


def ordered_upper(values: list[str]) -> list[str]:
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(str.upper, values))


def main() -> None:
    print(ordered_upper(["event-a", "event-b"]))


if __name__ == "__main__":
    main()
