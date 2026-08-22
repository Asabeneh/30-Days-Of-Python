from concurrent.futures import ThreadPoolExecutor


def bounded_identity(value: str, timeout: float = 2) -> str:
    with ThreadPoolExecutor(max_workers=1) as pool:
        return pool.submit(lambda: value).result(timeout=timeout)


def main() -> None:
    print(bounded_identity("completed"))


if __name__ == "__main__":
    main()
