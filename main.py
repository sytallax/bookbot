def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(get_string_word_count(file_contents))


def get_string_word_count(book: str) -> int:
    """Calculates the word count for a given string"""

    return len(book.split())


main()
