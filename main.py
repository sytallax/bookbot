def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(get_book_word_count(file_contents))


def get_book_word_count(book: str) -> int:
    """Calculates the word count for a given book"""

    return len(book.split())


main()
