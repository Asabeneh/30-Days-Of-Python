import subprocess


def python_version() -> str:
    result = subprocess.run(
        ["python", "--version"], capture_output=True, text=True, timeout=3, check=True
    )
    return (result.stdout or result.stderr).strip()


def main() -> None:
    print(python_version())


if __name__ == "__main__":
    main()
