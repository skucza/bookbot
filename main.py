from stats import *

def main():
    book_path = "books/frankenstein.txt"

    with open(book_path, "r") as file:
        file_contents = file.read()
        word_count = number_of_words(file_contents)
        char_occurrence = character_occurrence(file_contents)
        characters_ranking = alphabet_character_ranking(char_occurrence)

        report(book_path, word_count, characters_ranking)

def report(filename: str, word_count: int, character_list: CharacterList):
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document")
    print()

    for entry in character_list:
        print(f"The '{entry['char']}' character was found {entry['count']}")

    print("--- End report ---")


if __name__ == "__main__":
    main()
