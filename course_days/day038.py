import asyncio


async def read_label(label: str) -> str:
    await asyncio.sleep(0)
    return label


async def collect(labels: list[str]) -> list[str]:
    return await asyncio.gather(*(read_label(label) for label in labels))


def main() -> None:
    print(asyncio.run(collect(["a", "b"])))


if __name__ == "__main__":
    main()
