from collections import defaultdict
from typing import Dict


def main():
    filepath = "books/frankenstein.txt"
    frankenstein = get_book_text(filepath)
    print_report(frankenstein, filepath)


def get_book_text(filepath: str) -> str:
    """Open a text file and return the file as a string."""
    with open(filepath) as f:
        return f.read()


def get_book_word_count(book: str) -> int:
    """Calculates the word count for a given book"""
    return len(book.split())


def get_book_letter_count(book: str) -> Dict[str, int]:
    """Calculates the count of each letter in a given book"""
    book_letter_count: Dict[str, int] = defaultdict(lambda: 0)
    for char in book.lower():
        book_letter_count[char] += 1
    return dict(book_letter_count)


def print_report(book: str, filepath: str) -> None:
    """Print a report of word count and letter occurances for a given
    book to the console.

    Args:
        book(str): The book represented as a string.
        filepath(str): The filepath of the book

    Returns:
        None. Report is printed to the console."""

    print(f"--- Begin report of {filepath} ---")
    print(f"{get_book_word_count(book)} words found in the document\n")

    book_letter_count = {
        k: v
        for k, v in sorted(
            get_book_letter_count(book).items(), key=lambda item: item[1], reverse=True
        )
        if k.isalpha()
    }

    for letter in book_letter_count:
        print(f"The '{letter}' character was found {book_letter_count[letter]} times")

    print("--- End of report ---")


main()
