from typing import Counter, Dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(get_book_letter_count(file_contents))


def get_book_word_count(book: str) -> int:
    """Calculates the word count for a given book"""
    return len(book.split())


def get_book_letter_count(book: str) -> Dict[str, int]:
    """Calculates the count of each letter in a given book"""
    return Counter(book.lower())


main()
