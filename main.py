from typing import Counter, Dict


def main():
    filepath = "books/frankenstein.txt"
    frankenstein = get_book_text(filepath)
    print(get_book_letter_count(frankenstein))


def get_book_text(filepath: str) -> str:
    """Open a text file and return the file as a string."""
    with open(filepath) as f:
        return f.read()


def get_book_word_count(book: str) -> int:
    """Calculates the word count for a given book"""
    return len(book.split())


def get_book_letter_count(book: str) -> Dict[str, int]:
    """Calculates the count of each letter in a given book"""
    return Counter(book.lower())


main()
