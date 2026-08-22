def matching_lines(lines, needle):
    for line in lines:
        if needle in line:
            yield line


def main() -> None:
    print(list(matching_lines(["ok", "login_failed", "ok"], "login")))


if __name__ == "__main__":
    main()
