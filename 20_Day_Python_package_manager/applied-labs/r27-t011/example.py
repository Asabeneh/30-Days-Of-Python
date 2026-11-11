def text_statistics(text: str) -> dict[str, int]:
    words = text.split()
    return {
        "word_count": len(words),
        "distinct_word_count": len(set(words)),
    }


if __name__ == "__main__":
    sample_text = "one two two"
    print(text_statistics(sample_text))
