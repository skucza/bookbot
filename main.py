from typing import TypedDict


class CharacterEntry(TypedDict):
    char: str
    count: int


CharacterList = list[CharacterEntry]
CharacterDict = dict[str, int]


def main():
    book_path = "books/frankenstein.txt"

    with open(book_path, "r") as file:
        file_contents = file.read()
        word_count = number_of_words(file_contents)
        char_occurrence = character_occurrence(file_contents)
        characters_ranking = alphabet_character_ranking(char_occurrence)

        report(book_path, word_count, characters_ranking)


def number_of_words(text: str) -> int:
    words = text.split()

    return len(words)


def character_occurrence(text: str) -> CharacterDict:
    characters: CharacterDict = {}

    for character in text.lower():
        characters[character] = characters.get(character, 0) + 1

    return characters


def alphabet_character_ranking(char_occurrence: CharacterDict) -> CharacterList:
    alphabet_list: CharacterList = [
        {"char": char, "count": count}
        for char, count in char_occurrence.items() if char.isalpha()
    ]

    alphabet_list.sort(reverse=True, key=lambda entry: entry["count"])

    return alphabet_list


def report(filename: str, word_count: int, character_list: CharacterList):
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document")
    print()

    for entry in character_list:
        print(f"The '{entry['char']}' character was found {entry['count']}")

    print("--- End report ---")


if __name__ == "__main__":
    main()
