import sys
from stats import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book_path = sys.argv[1]

    try:
        with open(book_path, "r") as file:
            file_contents = file.read()
            word_count = number_of_words(file_contents)
            char_occurrence = character_occurrence(file_contents)
            characters_ranking = alphabet_character_ranking(char_occurrence)

            report(book_path, word_count, characters_ranking)
    except FileNotFoundError as error:
        print("Could not find file: " + book_path)
        exit(1)

def report(filename: str, word_count: int, character_list: CharacterList):
    print(f"--- Begin report of {filename} ---")
    print(f"Found {word_count} total words")
    print()

    for entry in character_list:
        print(f"{entry['char']}: {entry['count']}")

    print("--- End report ---")


if __name__ == "__main__":
    main()
